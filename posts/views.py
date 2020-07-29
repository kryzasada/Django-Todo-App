from django.shortcuts import render
from .forms import UserPostForms

# Create your views here.


def user_login_in(request, *args, **kwargs):
    form = UserPostForms(request.POST or None)

    if form.is_valid():
        form.save(commit=True)
        form = UserPostForms()

    context = {
        'form': form,
    }
    return render(request, 'logged.html', context)
