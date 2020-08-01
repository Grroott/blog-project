from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm
from .models import Profile
from django.contrib.auth.models import User

def register(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)

		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			return redirect('home')
	else:
		form = UserRegisterForm()

	return render(request, 'users/register.html', {'form': form})

def profiles(request, username):
	p_user = get_object_or_404(User, username=username)
	profile = get_object_or_404(Profile, user=p_user)

	context ={
	'profile' : profile
	}

	return render (request, 'users/profile.html', context)