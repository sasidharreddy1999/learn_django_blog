

from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required

def post_list(request):
	posts=Post.objects.filter(published_date__lte=timezone.now())
	return render(request,'blog/post_list.html',{ 'posts':posts })

def post_detail(request,num):
	post=get_object_or_404(Post,pk=num)
	return render(request,'blog/post_detail.html',{ 'post':post })

@login_required
def post_new(request):
	if request.method=="POST":
		form=PostForm(request.POST)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.save()
			return redirect('post_detail',num=post.pk)
	else:
		form=PostForm()
	return render(request,'blog/post_edit.html',{ 'form':form })

@login_required
def post_edit(request,num):
	post=get_object_or_404(Post,pk=num)
	if request.method=="POST":
		form=PostForm(request.POST,instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.save()
			return redirect('post_detail',num)
	else:
		form=PostForm(instance=post)
		return render(request,'blog/post_edit.html',{ 'form':form })

@login_required
def post_draft_list(request):
	posts=Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request,'blog/post_draft_list.html',{ 'posts':posts })

@login_required
def post_publish(request,num):
	post=get_object_or_404(Post,pk=num)
	post.publish()
	return redirect('post_detail',num)

@login_required
def post_remove(request,num):
	post=get_object_or_404(Post,pk=num)
	post.delete()
	return redirect('post_list')

def add_comment_to_post(request,num):
	post=get_object_or_404(Post,pk=num)
	if request.method=="POST":
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.post=post
			comment.save()
			return redirect('post_detail',num)
	else:
		form=CommentForm()
	return render(request,'blog/add_comment_to_post.html',{ 'form':form })

def comment_approve(request,num):
	comment=get_object_or_404(Comment,pk=num)
	comment.approve()
	return redirect('post_detail',(comment.post).pk)

def comment_remove(request,num):
	comment=get_object_or_404(Comment,pk=num)
	comment.delete()
	return redirect('post_detail',comment.post.pk)
