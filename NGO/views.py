from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth import logout
from django.db.models import Q
from django.contrib.auth.forms import PasswordChangeForm
from NGO.models import NGO, Events, Children, Staff, Donor, Certificate, Photos
from superadmin.models import Invoice
from .forms import EventForm, ChildrenForm, CertificateForm, NGOForm


@login_required
def home(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        ngo = NGO.objects.filter(user=request.user)
        ch = Children.objects.filter(ngo=ngo)
        return render(request, 'ngo/index.html', {'ngo': ngo, 'ch': ch})


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
    ph = Photos.objects.filter()
    don = Donor.objects.all()
    return render(request,
                  'ngo/children_detail.html',
                  {'child': child, 'photos': ph, 'donor': don})


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
def notification(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        try:
            noti_ids = []
            for ngo in NGO.objects.filter(user=request.user):
                for noti in ngo.children_set.all():
                    noti_ids.append(noti.pk)
            user_cert = Certificate.objects.filter(pk__in=noti_ids)
        except NGO.DoesNotExist:
            user_cert = []
        return render(request, 'ngo/notification.html', {
            'notification': user_cert,
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
        return render(request, 'ngo/certificate.html', {'ngo': ngo})
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
def staff(request):
    staffs = Staff.objects.all()
    return render(request, 'ngo/staff_all.html', {'staff': staffs})


@login_required
def staff_detail(request, id):
    staff = get_object_or_404(Staff, id=id)
    return render(request,
                  'ngo/staff_detail.html',
                  {'staff': staff})


@login_required
def donor_list(request):
    form = Donor.objects.all()
    return render(request, 'ngo/donor.html', {'form': form})


@login_required
def donor_detail(request, id):
    form = get_object_or_404(Donor, id=id)
    return render(request, 'ngo/donor_detail.html', {'form': form})


@login_required
def notification_list(request):
    form = Invoice.objects.all()
    return render(request, 'ngo/notification.html', {'form': form})


@login_required
def notification_detail(request, id):
    form = get_object_or_404(Invoice, id=id)
    return render(request, 'ngo/notification_detail.html', {'form': form})


@login_required
def transaction(request):
    return render(request, 'ngo/transaction.html')


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


def photos(request):
    images = Photos.objects.all()
    return render(request, 'ngo/children_detail.html', {'photos': images})
