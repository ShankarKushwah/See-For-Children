from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from NGO.models import NGO, Events, Children, Donor, Certificate, Photos, Photo
from superadmin.models import Invoice
from .forms import EventForm, ChildrenForm, CertificateForm, NGOForm, PhotoForm
import datetime

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

@login_required
def home(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        ngo = NGO.objects.filter(user=request.user)
        ch = Children.objects.filter(ngo=ngo)
        eve = Events.objects.filter(ngo=ngo)
        query = request.GET.get("q")
        if query:
            ch = ch.filter(
                Q(name__icontains=query)
            ).distinct()
            eve = eve.filter(
                Q(name__icontains=query)
            ).distinct()
            return render(request, 'ngo/index.html', {'ngo': ngo, 'ch': ch, 'eve': eve})
        else:
            return render(request, 'ngo/index.html')


@login_required
def children(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        try:
            child_ids = []
            for ngo in NGO.objects.filter(user=request.user):
                for child in ngo.children_set.all():
                    child_ids.append(child.pk)
            user_child = Children.objects.filter(pk__in=child_ids).order_by('-name')
        except NGO.DoesNotExist:
            user_child = []
        return render(request, 'ngo/children_all.html', {
            'child': user_child,
        })


@login_required
def children_detail(request, id):
    child = get_object_or_404(Children, id=id)
    don = Donor.objects.all()
    return render(request,
                  'ngo/children_detail.html',
                  {'child': child, 'donor': don})


@login_required
def children_add(request):
        form = ChildrenForm(request.POST, request.FILES)
        ngo = get_object_or_404(NGO, user=request.user)
        if form.is_valid():
            ngo_child = ngo.children_set.all()
            for c in ngo_child:
                if c.id == form.cleaned_data.get("name"):
                    context = {
                        'ngo': ngo,
                        'form': form
                    }
                    return render(request, 'ngo/children_add.html', context)
            child = form.save(commit=False)
            child.ngo = ngo
            child.save()
            return redirect('/children_list/')
        context = {
            'ngo': ngo,
            'form': form,
        }
        return render(request, 'ngo/children_add.html', context)


# @login_required
# def ngo_register(request):
#     if not request.user.is_authenticated():
#         return render(request, 'accounts/login.html')
#     else:
#         form = NGOForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             ngo = form.save(commit=False)
#             ngo.user = request.user
#             ngo.save()
#             return render(request, 'accounts/registration.html', {'ngo': ngo})
#         context = {
#             'form': form
#         }
#         return render(request, 'accounts/registration.html', context)


@login_required
def children_edit(request, id):
    instance = get_object_or_404(Children, id=id)
    form = ChildrenForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/children_detail/%d/' % int(id))

    context = {
        "instance": instance,
        "form": form,
    }
    return render(request, "ngo/edit_children.html", context)


@login_required
def event_list(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        try:
            event_ids = []
            for ngo in NGO.objects.filter(user=request.user):
                for event in ngo.events_set.all():
                    event_ids.append(event.pk)
            user_event = Events.objects.filter(pk__in=event_ids)
        except NGO.DoesNotExist:
            user_event = []
        return render(request, 'ngo/upcoming_event.html', {
                'event_list': user_event,
            })


@login_required
def event_details(request, id):
    form = get_object_or_404(Events, id=id)
    return render(request,
                  'ngo/event_details.html',
                  {'form': form})


@login_required
def events_add(request):
    form = EventForm(request.POST or None, request.FILES or None)
    ngo = get_object_or_404(NGO, user=request.user)
    if form.is_valid():
        ngo_event = ngo.events_set.all()
        for e in ngo_event:
            if e.id == form.cleaned_data.get("name"):
                context = {
                    'ngo': ngo,
                    'form': form
                }
                return render(request, 'ngo/events.html', context)
        event = form.save(commit=False)
        event.ngo = ngo
        event.save()
        return redirect('/event_list/')
    context = {
        'ngo': ngo,
        'form': form,
    }
    return render(request, 'ngo/events.html', context)


@login_required
def certificate(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        try:
            cert_ids = []
            for ngo in NGO.objects.filter(user=request.user):
                for cert in ngo.certificate_set.all():
                    cert_ids.append(cert.pk)
            user_cert = Certificate.objects.filter(pk__in=cert_ids)
        except NGO.DoesNotExist:
            user_cert = []
        return render(request, 'ngo/certificate.html', {
            'certificate': user_cert,
        })


@login_required
def certificate_detail(request, id):
    certificate = get_object_or_404(Certificate, id=id)
    return render(request, 'ngo/certificate_detail.html', {'form': certificate})


@login_required
def certificate_add(request):
    form = CertificateForm(request.POST or None)
    ngo = get_object_or_404(NGO, user=request.user)
    if form.is_valid():
        ngo_cert = ngo.certificate_set.all()
        for c in ngo_cert:
            if c.id == form.cleaned_data.get("donor_name"):
                context = {
                    'ngo': ngo,
                    'form': form
                }
                return render(request, 'ngo/certificate_add.html', context)
        certificate = form.save(commit=False)
        certificate.ngo = ngo
        certificate.save()
        return redirect('/certificate/')
    context = {
        'ngo': ngo,
        'form': form
    }
    return render(request, 'ngo/certificate_add.html', context)


@login_required
def certificate_sent(request, id=id):
    form = get_object_or_404(Certificate, id=id)
    return render(request, 'ngo/sent_certificate.html', {'form': form})


@login_required
def donor_list(request):
    form = Donor.objects.all()
    return render(request, 'ngo/donor.html', {'form': form})


@login_required
def donor_detail(request, id):
    form = get_object_or_404(Donor, id=id)
    return render(request, 'ngo/donor_detail.html', {'form': form})


# @login_required
# def notification(request):
#     if not request.user.is_authenticated():
#         return render(request, 'accounts/login.html')
#     else:
#         try:
#             noti_ids = []
#             for ngo in NGO.objects.filter(user=request.user):
#                 for noti in ngo.children_set.all():
#                     noti_ids.append(noti.pk)
#             user_cert = Certificate.objects.filter(pk__in=noti_ids)
#         except NGO.DoesNotExist:
#             user_cert = []
#         return render(request, 'ngo/notification.html', {
#             'notification': user_cert,
#         })


@login_required
def notification_list(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        try:
            noti_ids = []
            for ngo in NGO.objects.filter(user=request.user):
                for noti in ngo.invoice_set.all():
                    noti_ids.append(noti.pk)
            user_noti = Invoice.objects.filter(pk__in=noti_ids).order_by('-time_stamp')
        except NGO.DoesNotExist:
            user_noti = []
        return render(request, 'ngo/notification.html', {'form': user_noti})


@login_required
def notification_detail(request, id):
    form = get_object_or_404(Invoice, id=id)
    return render(request, 'ngo/notification_detail.html', {'form': form})


@login_required
def profile(request):
    ngo = NGO.objects.filter(user=request.user)
    return render(request, 'ngo/profile.html', {'form': ngo})


@login_required
def profile_edit(request, id):
    instance = get_object_or_404(NGO, id=id)
    form = NGOForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/profile/')

    context = {
        "name": instance.name,
        "ngo": instance,
        "form": form,
    }
    return render(request, 'ngo/profile_edit.html', context)


@login_required
def chat(request):
    return render(request, 'ngo/chat.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'ngo/change_password.html', {
        'form': form
    })


# @login_required
# def photos(request):
#     images = Photos.objects.all()
#     return render(request, 'ngo/children_detail.html', {'photos': images})


# @login_required
# class BasicUploadView(View):
#     def get(self, request):
#         photo_list = Photo.objects.all()
#         return render(self.request, 'ngo/gallery.html', {'photos': photo_list})
#
#     def post(self, request):
#         form = PhotoForm(self.request.POST, self.request.FILES)
#         if form.is_valid():
#             photo = form.save()
#             data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
#         else:
#             data = {'is_valid': False}
#         return JsonResponse(data)


@login_required
def report_demo(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        error = False
        try:
            rep_ids = []
            for ngo in NGO.objects.filter(user=request.user):
                for rep in ngo.invoice_set.all():
                    rep_ids.append(rep.pk)
            user_rep = Invoice.objects.filter(pk__in=rep_ids).order_by('-time_stamp')
            if 'q1' and 'q2' in request.GET:
                date_from = datetime.datetime.strptime(request.GET['q1'], '%Y-%m-%d')
                date_to = datetime.datetime.strptime(request.GET['q2'], '%Y-%m-%d')
                report = Invoice.objects.filter(date__range=(date_from, date_to))
                return render(request, 'ngo/search_results.html', {'report': report})
        except NGO.DoesNotExist:
            user_rep = []
    return render(request, 'ngo/reports.html', {'form': user_rep, 'error': error})


# @login_required
# def report(request):
#     form = Invoice.objects.filter().order_by('-time_stamp')
#     error = False
#     if 'q1' and 'q2' in request.GET:
#         date_from = datetime.datetime.strptime(request.GET['q1'], '%Y-%m-%d')
#         date_to = datetime.datetime.strptime(request.GET['q2'], '%Y-%m-%d')
#         report = Invoice.objects.filter(date__range=(date_from, date_to))
#         return render(request, 'ngo/search_results.html', {'report': report})
#
#     return render(request, 'ngo/reports.html', {'form': form, 'error': error})


@login_required
def report_detail(request, id):
    form = get_object_or_404(Invoice, id=id)
    return render(request, 'ngo/report_detail.html', {'form': form})


@login_required
def report_print(request, id):
    form = get_object_or_404(Invoice, id=id)
    return render(request,
                  'ngo/print_document.html',
                  {'form': form})
