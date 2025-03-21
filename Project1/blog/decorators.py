from django.http import HttpResponse
from django.shortcuts import render
from django.core.exceptions import PermissionDenied


def is_super_user(view_function):
    def wrapper_function(request, *args, **kwargs):
        if request.user.is_superuser:
            return view_function(request, *args, **kwargs)
        else:
            print('NOT A SUPER USER')
            raise PermissionDenied
    return wrapper_function


def allowed_groups(allowed=[]):
    def decorator(view_fun):
        def wrapper_function(request, *args, **kwargs):

            if request.user.is_superuser:
                return view_fun(request, *args, **kwargs)

            group_set = set(group.name for group in request.user.groups.all())

            if group_set & set(allowed):
                return view_fun(request, *args, **kwargs)
            else:
                print('NOT in the allowed groups.')
                raise PermissionDenied

        return wrapper_function
    return decorator
