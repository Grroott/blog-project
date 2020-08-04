from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.db.models import Count



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

	# Like logic
	is_like = False
	if post.like.filter(id=request.user.id).exists():
		is_like = True

	context = {
	'post' : post,
	'is_bookmark' : is_bookmark,
	'is_like' : is_like
	}

	return render(request, 'blog/post_detail.html', context)

@login_required
def delete_post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if post.author == request.user:
		post.delete()
		return redirect('home')
	else:
		return HttpResponseRedirect(post.get_absolute_url())


@login_required
def bookmark_post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if post.bookmark.filter(id=request.user.id).exists():
		post.bookmark.remove(request.user)
	else:
		post.bookmark.add(request.user)
	return HttpResponseRedirect(post.get_absolute_url())

@login_required
def like_post(request, slug):
	post = get_object_or_404(Post, slug=slug)

	if post.author != request.user:

		if post.like.filter(id=request.user.id).exists():
			post.like.remove(request.user)
		else:
			post.like.add(request.user)
		return HttpResponseRedirect(post.get_absolute_url())

	else:

		return HttpResponseRedirect(post.get_absolute_url())

def top_posts(request):
	posts = Post.objects.annotate(num_likes=Count('like')).order_by('-num_likes')[:5]

	context = {
	'posts' : posts
	}

	return render(request, 'blog/top_posts.html', context)