from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect



def home(request):

	qs = Post.objects.all().order_by('-date_posted')
	context = {
	'posts' : qs
	}
	return render(request, 'blog/home.html', context)

@login_required
def new_post(request):
	if request.method == "POST":
		form = NewPostForm(request.POST)
		if form.is_valid():
			current_user = User.objects.get(id=request.user.id)
			instance = form.save(commit=False)
			instance.author = current_user
			instance.save()
			title = form.cleaned_data.get('title')
			return redirect('home')
	else:	
		form = NewPostForm()
	return render(request, 'blog/new_post.html', {'form':form})

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)

	# Bookmark logic
	is_bookmark = False
	if post.bookmark.filter(id=request.user.id).exists():
		is_bookmark = True

	context = {
	'post' : post,
	'is_bookmark' : is_bookmark
	}

	return render(request, 'blog/post_detail.html', context)

def bookmark_post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if post.bookmark.filter(id=request.user.id).exists():
		post.bookmark.remove(request.user)
	else:
		post.bookmark.add(request.user)
	return HttpResponseRedirect(post.get_absolute_url())