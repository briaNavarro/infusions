from django.shortcuts import render, redirect
from apps.login_app.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    # main page to look out
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'logInPage.html')


def create_user(request):
    errors = User.objects.validate(request.POST)

    if errors:
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errorscopy
        return redirect('/')
    else:

        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id

        return redirect('/royalblood/')


def login(request):
    results = User.objects.authenticate(
        request.POST['email'], request.POST['password'])
    if results == False:
        messages.error(request, "Invalid Information")
    else:
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id

        return redirect('/royalblood/')
    return redirect('/')


def logout(request):
    request.session.clear()
    return redirect('/')
