from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic import ListView
from .forms import NewPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User



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
	context = {
	'post' : post
	}

	return render(request, 'blog/post_detail.html', context)