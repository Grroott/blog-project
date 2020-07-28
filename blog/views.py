from django.shortcuts import render, redirect
from .models import Post
from django.views.generic import ListView
from .forms import NewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



def home(request):

	qs = Post.objects.all().order_by('-date_posted')
	context = {
	'objects' : qs
	}
	return render(request, 'blog/home.html', context)


def new_post(request):
	if request.method == "POST":
		form = NewForm(request.POST)
		if form.is_valid():
			u = User.objects.get(id=1)
			instance = form.save(commit=False)
			instance.author = u
			instance.save()
			title = form.cleaned_data.get('title')
			return redirect('home')
	else:	
		form = NewForm()
	return render(request, 'blog/new_post.html', {'form':form})