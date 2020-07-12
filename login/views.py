from django.shortcuts import render
from .forms import userLoginForm

# Create your views here.


def user_login_out(request):
    form = userLoginForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }
    return render(request, 'logged_out.html', context)


def user_login_in(request, *args, **kwargs):
    return render(request, 'logged_in.html', {})
