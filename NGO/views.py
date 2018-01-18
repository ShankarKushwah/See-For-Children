from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from NGO.models import NGO, Events, Children, Staff, Donor
from .forms import EventForm, EditChildrenForm, ChildrenForm


@login_required
def home(request):
    return render(request, 'ngo/index.html')

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
    child = Children.objects.all()
    return render(request, 'ngo/children_all.html', {'child': child})

@login_required
def children_detail(request, id):
    child = get_object_or_404(Children, id=id)
    return render(request,
                  'ngo/children_detail.html',
                  {'child': child})

@login_required
def children_add(request):
    if request.method == 'POST':
        form = ChildrenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/children_list/')
    else:
        form = ChildrenForm()
        return render(request, 'ngo/children_add.html', {'form': form})

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
