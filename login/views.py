from django.shortcuts import render


# Create your views here.


def user_login_out(request, *args, **kwargs):
    return render(request, 'logged_out.html', {})


def user_login_in(request, *args, **kwargs):
    return render(request, 'logged_in.html', {})
