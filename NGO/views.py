from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Q

from NGO.models import NGO, Events, Children, Staff, Donor, Certificate
from .forms import EventForm, ChildrenForm, CertificateForm


@login_required
def home(request):
    if not request.user.is_authenticated():
        return render(request, 'accounts/login.html')
    else:
        ngo = NGO.objects.filter(user=request.user)
        ch = Children.objects.filter(ngo=ngo)
        return render(request, 'ngo/index.html', {'ngo': ngo, 'ch': ch})


@login_required
def event_all(request):
    event = Events.objects.all()
    return render(request, 'ngo/upcoming_event.html', {'form': event})


@login_required
def event_list(request):
    event_ids = []
    for ngo in NGO.objects.filter():
        for event in ngo.events_set.all():
            event_ids.append(event.pk)
    ngo_event = Events.objects.filter(pk__in=event_ids)
    return render(request, 'ngo/event_list.html', {
        'event_list': ngo_event,
    })


@login_required
def events_add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/event_list/')
    else:
        form = EventForm()
    return render(request, 'ngo/events.html', {'form': form})


@login_required
def event_details(request, id):
    form = get_object_or_404(Events, id=id)
    return render(request,
                  'ngo/event_details.html',
                  {'form': form})


@login_required
def chat(request):
    return render(request, 'ngo/chat.html')


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
            user_child = Children.objects.filter(pk__in=child_ids)
        except NGO.DoesNotExist:
            user_child = []
        return render(request, 'ngo/children_all.html', {
            'child': user_child,
        })


@login_required
def children_detail(request, id):
    child = get_object_or_404(Children, id=id)
    return render(request,
                  'ngo/children_detail.html',
                  {'child': child})


@login_required
def children_add(request):
        form = ChildrenForm(request.POST or None)
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
            return render(request, 'ngo/children_detail.html', {'ngo': ngo})
        context = {
            'ngo': ngo,
            'form': form,
        }
        return render(request, 'ngo/children_add.html', context)


@login_required
def children_edit(request, id):
    instance = get_object_or_404(Children, id=id)
    form = ChildrenForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('/children_list')

    context = {
        "name": instance.name,
        "instance": instance,
        "form": form,
    }
    return render(request, "ngo/edit_children.html", context)


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
    return render(request, 'ngo/notification.html')


@login_required
def transaction(request):
    return render(request, 'ngo/transaction.html')


@login_required
def profile(request):
    return render(request, 'ngo/profile.html')


@login_required
def certificate(request):
    certificate = Certificate.objects.filter()
    return render(request, 'ngo/certificate.html', {'form': certificate})


@login_required
def certificate_detail(request, id):
    certificate = get_object_or_404(Certificate, id=id)
    return render(request, 'ngo/certificate_detail.html', {'form': certificate})


@login_required
def certificate_add(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/certificate/')
    else:
        form = CertificateForm()
        return render(request, 'ngo/certificate_add.html', {'form': form})
