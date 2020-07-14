from django.shortcuts import render, redirect
from .forms import UsersCreationForm

# Create your views here.


def user_register(request):
    if request.method == 'POST':
        form = UsersCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print("123")
            return redirect('zalogowany')
    else:
        form = UsersCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'logged_out.html', context)


def user_login(request):
    form = UsersCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'logged_out.html', context)


def user_login_in(request, *args, **kwargs):
    return render(request, 'logged_in.html', {})
