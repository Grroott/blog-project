from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, ProfileUpdateForm
from .models import Profile
from django.contrib.auth.models import User
from blog.models import Post
from django.contrib.auth.decorators import login_required

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

	posts = Post.objects.filter(author=p_user)

	context ={
	'profile' : profile,
	'posts' : posts
	}

	return render (request, 'users/profile.html', context)

@login_required
def edit_profile(request):

	p_user = get_object_or_404(User, username=request.user)
	profile = get_object_or_404(Profile, user=p_user)

	if request.method == "POST":
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

		if p_form.is_valid():
			p_form.save()
			return redirect('edit-profile')
	else:
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context = {		
		'p_form' : p_form,
		'profile' : profile
	}

	return render(request, 'users/edit_profile.html', context)