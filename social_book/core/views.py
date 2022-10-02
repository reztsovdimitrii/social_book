from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

from .models import LikePost, Profile, Post


@login_required(login_url='signin')
def index(request):
    user_profile = Profile.objects.get(user=request.user)

    posts = Post.objects.all()
    context = {
        'user_profile': user_profile,
        'posts': posts
    }
    return render(request, 'index.html', context)


@login_required(login_url='signin')
def upload(request):
    if request.method == 'POST':
        user = Profile.objects.get(user=request.user)
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()
        return redirect('/')
    else:
        return redirect('/')


@login_required(login_url='signin')
def like_post(request):
    username = get_object_or_404(Profile, user=request.user.id)
    post_id = request.GET.get('post_id')
    post = Post.objects.get(id=post_id)
    like_filter = LikePost.objects.filter(post_id=post, username=username).first()
    print(like_filter)
    if like_filter is None:
        new_like = LikePost.objects.create(post_id=post, username=username)
        new_like.save()
        post.no_of_likes = post.no_of_likes+1
        post.save()
        return redirect('/')
    else:
        like_filter.delete()
        post.no_of_likes = post.no_of_likes-1
        post.save()
        return redirect('/')

    print(post_id)
    pass


@login_required(login_url='signin')
def settings(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        if request.FILES.get('image') is None:
            image = user_profile.profileimg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        if request.FILES.get('image') is not None:
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileimg = image
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        return redirect('settings')

    return render(request, 'setting.html', {'user_profile': user_profile})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password
                )
                user.save()
                user_login = auth.authenticate(
                    username=username,
                    password=password
                )
                auth.login(request, user_login)
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model,
                    id_user=user_model.id
                )
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('signin')

    return render(request, 'signin.html')


@login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')
