from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from blog.models import Posts_db
from django.contrib.auth.models import User, Group
from blog.forms import add_post, RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from blog.decorators import is_super_user, allowed_groups
from django.db import connection
from django.utils.text import slugify
# Create your views here.


@login_required(login_url='login')
def home(request):
    return render(request, 'blog/home.html')


def all_post(request):
    blogs = Posts_db.objects.all()
    print(request.user)
    return render(request, 'blog/posts.html', {'blogs': blogs})


def post(request, slug):

    try:
        print(slug)
        selected_post = Posts_db.objects.get(slug=slug)
        return render(request, 'blog/single_post.html', {'post': selected_post})
    except Posts_db.DoesNotExist:
        return render(request, '404.html', status=404)


# @permission_required('blog.add_posts_db', login_url='login', raise_exception=True)
@allowed_groups(allowed=['default', 'moderator'])
def add_post_form(request, id=None):

    if id:
        post = get_object_or_404(Posts_db, id=id)
    else:
        post = None

    if request.method == 'POST':
        form = add_post(request.POST, request.FILES, instance=post)
        if form.is_valid():
            # ti = form.cleaned_data['title']
            # au = form.cleaned_data['author']
            # co = form.cleaned_data['content']
            # post = Posts_db(title=ti, author=au, content=co)
            # post.save()
            print(form.cleaned_data)
            p = form.save(commit=False)
            p.author = request.user
            print(request.user)
            p.save()

            return HttpResponseRedirect(reverse('post_success'))
        else:
            # Form is not valid, render the template with errors
            return render(request, 'blog/add_post.html', {'form': form})

    else:
        form = add_post(instance=post)
    context = {
        'form': form
    }
    return render(request, 'blog/add_post.html', context)


def post_success(request):
    return render(request, 'blog/success.html')


def delete_post(request, id):
    post = Posts_db(id=id)
    post.delete()
    return HttpResponseRedirect(reverse('all_post'))


def update_post(request, id):
    return add_post_form(request, id=id)


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')

    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})


@is_super_user
def ban_user(request, uid):

    user = User.objects.filter(id=uid).first()
    try:
        group = Group.objects.get(name='default')
        group.user_set.remove(user)
    except:
        pass
    try:
        group = Group.objects.get(name='moderator')
        group.user_set.remove(user)
    except:
        pass

    return HttpResponseRedirect(reverse('all_post'))

# def add_post_form(request):

#     if request.method == 'GET':
#         form = add_post(request.POST)
#         print(request.POST)
#         form = add_post()
#     else:
#         form = add_post()
#     context = {
#         'form': form
#     }
#     return render(request, 'blog/add_post.html', context)


# def to_post(request, id):
#     url = reverse('post', args=[id])
#     print(url)
#     return HttpResponseRedirect(url)
