from django.shortcuts import render, redirect
from .forms import UsersCreationForm

# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UsersCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')

    else:
        form = UsersCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def user_login_in(request, *args, **kwargs):
    return render(request, 'logged_in.html', {})
