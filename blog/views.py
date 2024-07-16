import os
import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post2, Comment, Topic, PostComment
from .forms import RegistrationForm, PostForm, TopicForm, CommentForm, CustomAuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.utils import timezone
from django.db.models import Count



def index(request):
    posts = Post2.objects.all()
    latest_posts = Post2.objects.order_by('-pub_date')[:4]
    latest_topics = Topic.objects.order_by('-pub_date')[:10]
    post_with_highest_likes = Post2.objects.annotate(num_likes=Count('likes')).order_by('-num_likes').first()

    context = {'list_of_posts': posts, 'latest_posts': latest_posts, 'latest_topics': latest_topics,
               'post_with_highest_likes': post_with_highest_likes}
    return render(request, 'blog/index.html', context=context)



class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'blog/login.html'

    def form_valid(self, form):
        """Override the default form_valid method to perform custom actions."""
        response = super().form_valid(form)
        # Your custom logic here (if needed)
        return response

    def form_invalid(self, form):
        """Override the default form_invalid method to perform custom actions."""
        response = super().form_invalid(form)
        # Your custom logic here (if needed)
        return response

    def get(self, request, *args, **kwargs):
        """Handle GET requests."""
        response = super().get(request, *args, **kwargs)
        # Your custom logic here (if needed)
        return response

    def post(self, request, *args, **kwargs):
        """Handle POST requests."""
        response = super().post(request, *args, **kwargs)
        # Your custom logic here (if needed)
        return response


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Change 'home' to your home URL name
    else:
        form = RegistrationForm()

    return render(request, 'blog/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Assign the current user as the author
            post.save()
            return redirect('index')  # Change 'home' to your home URL name
    else:
        form = PostForm()

    return render(request, 'blog/new_post.html', {'form': form})


@login_required
def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.author = request.user
            topic.save()
            return redirect('index')  # Change 'home' to your home URL name
    else:
        form = TopicForm()

    return render(request, 'blog/new_topic.html', {'form': form})


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    comments = Comment.objects.filter(topic=topic).order_by('pub_date')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = Comment(topic=topic,
                        author=request.user,
                        content=form.cleaned_data["comment"],
                        pub_date=timezone.now())
            c.save()
            return HttpResponseRedirect(f'/blog/topics/{topic.id}')
    else:
        form = CommentForm()

    context = {'topic': topic,
               'comments': comments,
               'form': form}

    return render(request, 'blog/topic.html', context=context)


def post(request, post_id):
    post = Post2.objects.get(id=post_id)
    comments = PostComment.objects.filter(post=post).order_by('pub_date')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            c = PostComment(post=post,
                        author=request.user,
                        content=form.cleaned_data["comment"],
                        pub_date=timezone.now())
            c.save()
            return HttpResponseRedirect(f'/blog/posts/{post.id}')
    else:
        form = CommentForm()

    context = {'post': post,
               'comments': comments,
               'form': form}

    return render(request, 'blog/post.html', context=context)


# @login_required
def like_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')  # Change 'home' to your home URL name
    try:
        post = get_object_or_404(Post2, pk=post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        likes_count = post.likes.count()
        likes = list(post.likes.values_list('id', flat=True))
        return JsonResponse({'likes_count': likes_count, 'likes': likes, 'currentUserId': request.user.id})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def check_like_post(request, post_id):
    post = get_object_or_404(Post2, pk=post_id)
    likes = list(post.likes.values_list('id', flat=True))
    return JsonResponse({'likes': likes})


def all_posts(request):
    posts = Post2.objects.all().order_by('-pub_date')
    context = {'list_of_posts': posts}
    return render(request, 'blog/all_posts.html', context=context)


def all_topics(request):
    topics = Topic.objects.all().order_by('-pub_date')
    context = {'list_of_topics': topics}
    return render(request, 'blog/all_topics.html', context=context)
