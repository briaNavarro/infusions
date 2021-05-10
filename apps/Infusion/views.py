from django.shortcuts import render, redirect


from apps.login_app.models import User
from .models import InfuseLog, MessageBoard, Comment
# Create your views here.

# RENDER PAGES


def index(request):
    # data is sent here to be displayed by creating_user functions
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        # why doesnt Profile.objects.all() work?, it doesnt appear on the DOM
        'infusions': InfuseLog.objects.all().order_by('-kreator_id'),
    }
    return render(request, 'html/dashboard.html', context)


def profiler(request, user_id):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'html/profilePage.html', context)


def myprofile(request, user_id):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'html/myprofile.html', context)


# CREATING/REDIRECTING


def infusion(request):
    maker = User.objects.get(id=request.session['user_id'])
    newInfusion = InfuseLog.objects.create(date=request.POST['infDate'], time=request.POST['infTime'], desc=request.POST['desc'],
                                           bleed=request.POST['yes_no'], dose_amount=request.POST['doseAmount'], dose_onHand=request.POST['onHand'], kreator=maker)

    print(newInfusion)

    return redirect('/royalblood/')

# DELETE 


def delete(request, infuser_id):
    infuse_log = InfuseLog.objects.get(id=infuser_id)

    infuse_log.delete()
    return redirect('/royalblood/')
