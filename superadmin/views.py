from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect

from NGO.models import NGO, Events, Children
from superadmin.models import Donor
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from superadmin.forms import InvoiceForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from messenger.models import Message
from See4Children2.decorators import ajax_required


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
    form = Donor.objects.all()
    return render(request, 'super_admin/donor_list.html', {'form': form})


@staff_member_required
def donor_detail(request, id):
    form = get_object_or_404(Donor, id=id)
    return render(request, 'super_admin/donor_detail.html', {'form': form})


@staff_member_required
def ngo_list(request):
    form = NGO.objects.all()
    return render(request, 'super_admin/ngo_list.html', {'form': form})


@staff_member_required
def ngo_detail(request, id):
    form = get_object_or_404(NGO, id=id)
    events = Events.objects.filter(ngo=form)
    child = Children.objects.filter(ngo=form)
    return render(request,
                  'super_admin/ngo_detail.html',
                  {'form': form, 'events': events, 'child': child})


@staff_member_required
def send_detail(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/superadmin/send_detail/')
    else:
        form = InvoiceForm()
        return render(request, 'super_admin/send_detail.html', {'form': form})


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
def notification_detail(request):
    return render(request, 'super_admin/notification_detail.html')


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


@login_required
def inbox(request):
    conversations = Message.get_conversations(user=request.user)
    users_list = User.objects.filter(
        is_active=True).exclude(username=request.user).order_by('username')
    active_conversations = None
    messages = None
    if conversations:
        conversation = conversations[0]
        active_conversations = conversation['user'].username
        messages = Message.objects.filter(user=request.user, conversation=conversation['user'])
        messages.update(is_read=True)
        for conversation in conversations:
            if conversation in conversations:
                if conversation['user'].username == active_conversations:
                    conversation['unread'] = 0
    return render(request, 'super_admin/messenger/inbox.html', {
        'messages': messages,
        'conversations': conversations,
        'users_list': users_list,
        'active': active_conversations
    })


@login_required
def messages(request, username):
    conversations = Message.get_conversations(user=request.user)
    users_list = User.objects.filter(
        is_active=True).exclude(username=request.user).order_by('username')
    active_conversation = username
    messages = Message.objects.filter(user=request.user, conversation__username=username)
    messages.update(is_read=True)
    for conversation in conversations:
        if conversation['user'].username == username:
            conversation['unread'] = 0

    return render(request, 'super_admin/messenger/inbox.html', {
        'messages': messages,
        'conversations': conversations,
        'users_list': users_list,
        'active': active_conversation
    })


@login_required
@ajax_required
def delete(request):
    return HttpResponse()


@login_required
@ajax_required
def send(request):
    if request.method == 'POST':
        from_user = request.user
        to_user_username = request.POST.get('to')
        to_user = User.objects.get(username=to_user_username)
        message = request.POST.get('message')
        if len(message.strip()) == 0:
            return HttpResponse()

        if from_user != to_user:
            msg = Message.send_message(from_user, to_user, message)
            return render(request, 'super_admin/messenger/includes/partial_conversations.html', {'message': msg})

        return HttpResponse()

    else:
        return HttpResponseBadRequest()


@login_required
@ajax_required
def check(request):
    count = Message.objects.filter(user=request.user, is_read=False).count()
    return HttpResponse(count)
