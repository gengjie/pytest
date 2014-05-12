# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404
from models import Poll, Country
import hashlib


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
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