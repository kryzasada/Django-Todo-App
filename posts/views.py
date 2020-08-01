from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import UserPostForms
from .models import UserPost

# Create your views here.


def user_login_in(request, *args, **kwargs):
    current_user = request.user

    if request.method == "POST":
        form = UserPostForms(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('logged')
        
    else:
        form = UserPostForms()

    obj = UserPost.objects.filter(users=current_user.id)

    context = {
        'form': form,
        'user_id': current_user.id,
        'obj': obj,
    }
    return render(request, 'logged.html', context)

def post_remove(request, user_id):
    print("\n\n\n\n\n\n")
    print(UserPost.objects)
    post = UserPost.objects.get(id=user_id)
    post.delete()
    return redirect('logged')