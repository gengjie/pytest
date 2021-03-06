# _*coding=utf-8_*_
# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from models import Poll, Country, MyUser
import hashlib


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:1000]
    # template = loader.get_template('polls/index.html')
    # context = Context({
    #     'latest_poll_list': latest_poll_list,
    # })
    context = {'latest_poll_list': latest_poll_list}
    # outputstr = ','.join([p.question for p in latest_poll_list])
    # return HttpResponse(template.render(context))
    response = render(request, 'polls/index.html', context)
    response.set_cookie('username', 'tom')
    m = hashlib.md5()
    m.update('abc1234')
    response.set_cookie('password', m.hexdigest())
    return response


def detail(request, poll_id):
    # try:
    #     poll = Poll.objects.get(pk=poll_id)
    # except:
    #     raise Http404
    # # return HttpResponse('Hello World!!! This is %s parameter...' % poll_id)
    poll = get_object_or_404(Poll, pk=poll_id)
    print '--->', request.COOKIES['username']
    return render(request, 'polls/detail.html',
                  {'poll': poll, 'username': request.COOKIES['username'], 'password': request.COOKIES['password']})


def result(request, poll_id):
    return HttpResponse('Hello World!!! This is %s result...' % poll_id)

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        select_choice = p.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request,
               'polls/detail.html', {
                    'poll': p,
                    'error_message': 'You do not select the right choice...'
                })
    else:
        select_choice.votes += 1
        select_choice.save()
    return render(request, 'polls/vote.html', {'select_choice': select_choice, 'poll': p})

def test(request, p_a, p_b):
    print p_a, p_b

    country = Country()
    choices = {1: 'UN', 2: 'USA'}
    # return HttpResponse('%s, %s' % (p_a, p_b))
    return render(request, 'polls/test.html', {'country': country, 'choices': choices})

@login_required
def main(request):
    u = MyUser(username='Jie', password='123456')
    u.save()
    # if request.method != 'POST':
    #     raise Http404('Only POSTs are allowed')
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print user
        # return HttpResponseRedirect('/you-are-logged-in/')
        return render(request, 'polls/main.html', {'project_name': 'Jet\'s Blog'})
    except User.DoesNotExist:
        return Http404('')

def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        # return HttpResponseRedirect('/you-are-logged-in/')
        return render(request, 'polls/main.html', {'project_name': 'Jet\'s Blog'})
    except User.DoesNotExist:
        return Http404('')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')
