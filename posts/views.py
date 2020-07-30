from django.shortcuts import render
from .forms import UserPostForms

# Create your views here.


def user_login_in(request, *args, **kwargs):
    current_user = request.user

    if request.method == "POST":
        form = UserPostForms(request.POST)

        if form.is_valid():
             post = form.save(commit=True)

    else:
        form = UserPostForms()

    context = {
        'form': form,
        'user_id': current_user.id,
    }
    return render(request, 'logged.html', context)
