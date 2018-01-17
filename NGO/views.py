from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

from NGO.models import NGO, Events, Children, Staff


@login_required
def home(request):
    return render(request, 'ngo/index.html')


def event_all(request):
    event = Events.objects.all()
    return render(request, 'ngo/upcoming_event.html', {'form': event})


def event_list(request):
    event_ids = []
    for ngo in NGO.objects.filter():
        for event in ngo.events_set.all():
            event_ids.append(event.pk)
    ngo_event = Events.objects.filter(pk__in=event_ids)
    return render(request, 'ngo/event_list.html', {
        'event_list': ngo_event,
    })


def chat(request):
    return render(request, 'ngo/chat.html')


def children(request):
    child = Children.objects.all()
    return render(request, 'ngo/children_all.html', {'child': child})


def children_detail(request, id):
    child = get_object_or_404(Children, id=id)
    return render(request,
                  'ngo/children_detail.html',
                  {'child': child})


def staff(request):
    staffs = Staff.objects.all()
    return render(request, 'ngo/staff_all.html', {'staff': staffs})


def staff_detail(request, id):
    staff = get_object_or_404(Staff, id=id)
    return render(request,
                  'ngo/staff_detail.html',
                  {'staff': staff})


def donor_list(request):
    return render(request, 'ngo/donor.html')


def notification_list(request):
    return render(request, 'ngo/notification.html')


def transaction(request):
    return render(request, 'ngo/transaction.html')
