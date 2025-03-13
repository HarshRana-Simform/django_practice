from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from blog.models import Posts_db
from blog.forms import add_post, RegisterForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def all_post(request):
    blogs = Posts_db.objects.all()
    return render(request, 'blog/posts.html', {'blogs': blogs})


def post(request, id):

    try:
        selected_post = Posts_db.objects.get(id=id)
        return render(request, 'blog/single_post.html', {'post': selected_post})
    except Posts_db.DoesNotExist:
        return render(request, '404.html', status=404)


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
            print(form.cleaned_data())
            form.save()
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

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})

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
