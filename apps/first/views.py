from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import *

def index(req):
    return render(req, 'index.html', {'users': User.objects.all()})

def registration(req):
    print('check1')

    if req.method == 'POST':
        errors = User.objects.validate(req.POST)
        if not errors:                        
            user = User.objects.create_user(req.POST)            
            req.session['user_id'] = user.id
            username = User.objects.get(email = req.POST['email']).first_name
            user_id = User.objects.get(email = req.POST['email']).id
            req.session['user'] = username
            return redirect('/dashboard')
        if errors:
            for key, value in errors.items():
                print(messages.error(req,value))
                print(errors.items)
            return redirect('/')
            
def login(req):
    errors = User.objects.validateLogin(req.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(req, value)
        return redirect('/')
    else:
        username = User.objects.get(email = req.POST['email']).first_name
        user_id = User.objects.get(email = req.POST['email']).id
        req.session['user_id'] = user_id
        req.session['user'] = username
        return redirect('/dashboard')

def logout(req):
    req.session.clear()
    return redirect('/')

def dashboard(req):
    print("check")
    if 'user_id' not in req.session:
        return redirect('/')
    context = {
        'user': user,
        'likes': Quote.objects.all().order_by('-created_at'),
        'quotes': Quote.objects.all()
    }
    return render(req, 'dashboard.html', context)

def create(req):
    req.session['user_id']
    return render(req, )

def quote(req):
    if req.method == 'POST':
        errors = Quote.objects.validateQuote(req.POST)
        if not errors:
            req.session['user_id']
            oneT = User.objects.get(id = req.session['user_id'])
            quotes = Quote.objects.create(content = req.POST['liveQuote'], author = req.POST['author'], one = oneT)
            oneT.manyT.add(quotes)            
            return redirect('/dashboard')
        if errors:
            for key, value in errors.items():
                print(messages.error(req,value))
                print(errors.items)
            return redirect('/dashboard')

def editAccount(req):
    if req.method == 'POST':
        errors = User.objects.validateEdit(req.POST)
        if not errors:
            change = User.objects.get(id = req.session['user_id']),
            User.first_name = req.POST['first'],
            User.last_name = req.POST['last'],
            User.email = req.POST['email'],
            return redirect('/update')
        if errors:
            for key, value in errors.items():
                print(messages.error(req,value))
                print(errors.items)
            return redirect('/edit')

def edit(req):
    return render(req, 'edit.html')

def user(req,id):
    print("check")
    Users=User.objects.get(id = id)
    context = {
        'users': User.objects.get(id = id),
        'added': Users.manyT.all()
    }
    return render(req,'user.html', context)

def liked(req):
	user = User.objects.get(id=id)
	quote = Quote.objects.get(id=id)	
	user.likesT.add(quote)
	likes = quote.likes.all()

	return redirect('/dashboard')

def delete(req):
    quoteDelete = Quote.objects.get(id = req.POST['del'])
    quoteDelete.delete()
    return redirect('/dashboard')

def update(req):
    return render(req, 'update.html')

