from django.shortcuts import render, redirect
import random, datetime


def root(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    activities = request.session['activities'][::-1]
    gold = request.session['gold']
    context = {
        'gold': gold,
        'activities': activities,
    }
    
    return render(request, 'index.html', context)


def process_money(request):
    building = request.POST['building']
    if building == 'farm':
        gold = random.randint(10, 20)
        request.session['gold'] += gold
    elif building == 'cave':
        gold = random.randint(5, 10)
        request.session['gold'] += gold
    elif building == 'house':
        gold = random.randint(2, 5)
        request.session['gold'] += gold
    elif building == 'casino':
        gold = random.randint(-50, 50)
        request.session['gold'] += gold
    if gold > 0:
        activity = f'Earned {gold} golds from the {building}! ({datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")})\n'
    else:
        activity = f'Entered a casino and lost {abs(gold)} golds... Ouch.. ({datetime.datetime.now().strftime("%Y/%m/%d %I:%M %p")})\n'
    request.session['activities'].append(activity)
    
    return redirect('/')


def restart(request):
    request.session['gold'] = 0
    request.session['activities'] = []
    return redirect('/')
