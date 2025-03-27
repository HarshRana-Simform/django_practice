from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('all_post/', views.all_post, name='all_post'),
    # Dynamic urls
    path('<slug:slug>/', views.post, name='post'),
    # path('to_post/<int:id>/', views.to_post),
    path('add_post/', views.add_post_form, name='add_post'),
    path('success/', views.post_success, name='post_success'),
    path('delete/<int:id>/', views.delete_post, name='delete'),
    path('update/<int:id>/', views.update_post, name='update'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('ban_user/<int:uid>', views.ban_user, name='ban_user'),
]
