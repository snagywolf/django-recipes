from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..forms import RegisterForm


@login_required
def logout_view(request):

    if request.method == 'POST':
        logout(request)
        return redirect('home')

    return redirect('home')

def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            user.save()

            return redirect('login')

    else:
        form = RegisterForm()

    return render(
        request,
        'recipes/page/register.html',
        {
            'form': form
        }
    )