from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.conf import settings

from .forms import *
from .models import *

User = get_user_model()

@login_required
def home(request):

    posts = Post.objects.all()

    if request.POST:
        
        req = Request.objects.get(id=request.POST['request_id'])

        if request.POST['submit'] == 'accept':
            req.status = 'accepted'
            req.save()
        elif request.POST['submit'] == 'reject':
            req.delete()

    elif request.GET.get('search'):
        text = request.GET['search']
        posts = posts.filter(commodity_name__icontains=text) \
            | posts.filter(description__icontains=text)
    
    return render(request, 'home.html', context={'posts': posts, 'categories': Post.CATEGORIES})

@login_required
def edit_profile(request):

    if request.POST:
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'edit_profile.html', context={'form': EditProfileForm(instance=request.user)})

@login_required
def create_post(request):

    if request.POST:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = request.user
            post.save()
            return redirect('home')
            
    return render(request, 'post.html', context={'post': Post(), 'is_create': True})

@login_required
def edit_post(request, id):

    if request.POST:
        post = Post.objects.get(id=id)
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        try:
            post = Post.objects.get(id=id)
            return render(request, 'post.html', context={'post': post, 'is_create': False})
        except:
            return redirect('home')

@login_required
def delete_post(request, id):

    try:
        post = Post.objects.get(id=id)
        post.delete()
    except:
        pass

    return redirect('home')

@login_required
def others_profile(request, username):

    try:
        user = User.objects.get(username=username)

        if user.username == request.user.username:
            return redirect('edit_profile')

        return render(request, 'others_profile.html', context={'other': user, 'categories': Post.CATEGORIES})
    except:

        return redirect('home')

def send_request(request, post1, post2):
    
    post = Post.objects.get(id=post1)
    offered = Post.objects.get(id=post2)

    request = Request()

    request.post = post
    request.receiver = post.poster

    request.offered = offered
    request.sender = offered.poster

    request.save()

def post_detail(request, id):
    return render(request, 'home.html')

    



    


