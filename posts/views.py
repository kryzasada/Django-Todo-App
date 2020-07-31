from django.shortcuts import render
from .forms import UserPostForms
from .models import UserPost
from django.db.models import Q


# Create your views here.


def user_login_in(request, *args, **kwargs):
    current_user = request.user

    if request.method == "POST":
        form = UserPostForms(request.POST)

        if form.is_valid():
            form.save(commit=True)
            form = UserPostForms()

    else:
        form = UserPostForms()

    obj = UserPost.objects.filter(users=current_user.id)

    context = {
        'form': form,
        'user_id': current_user.id,
        #'obj': obj.values('text'),
        'obj': obj,
    }
    return render(request, 'logged.html', context)
