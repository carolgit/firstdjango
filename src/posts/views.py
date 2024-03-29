# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    context = {
        'post_list': posts
    }
    return render(request, "posts/post_list.html", context)