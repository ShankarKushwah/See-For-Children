from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
from NGO.models import NGO, Events
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


@staff_member_required
def index(request):
    return render(request, 'super_admin/index.html')


@staff_member_required
def event_list(request):
    event_ids = []
    for ngo in NGO.objects.filter(user=request.user):
        for event in ngo.events_set.all():
            event_ids.append(event.pk)
    ngo_event = Events.objects.filter(pk__in=event_ids)
    return render(request, 'ngo/event_list.html', {
        'event_list': ngo_event,
    })


@staff_member_required
def donor_list(request):
    return render(request, 'super_admin/donor_list.html')


@staff_member_required
def donor_detail(request):
    return render(request, 'super_admin/donor_detail.html')


@staff_member_required
def ngo_list(request):
    form = NGO.objects.all()
    return render(request, 'super_admin/ngo_list.html', {'form': form})


@staff_member_required
def ngo_detail(request, id):
    form = get_object_or_404(NGO, id=id)
    events = Events.objects.filter()
    return render(request,
                  'super_admin/ngo_detail.html',
                  {'form': form, 'events': events})


@staff_member_required
def send_detail(request):
    return render(request, 'super_admin/send_detail.html')


@staff_member_required
def transaction_list(request):
    return render(request, 'super_admin/transaction_list.html')


@staff_member_required
def transaction_detail(request):
    return render(request, 'super_admin/transaction_detail.html')


@staff_member_required
def notification(request):
    return render(request, 'super_admin/notification.html')


@staff_member_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'super_admin/change_password.html', {
        'form': form
    })
