from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
# from django.core.exceptions.ObjectDoesNotExist import DoesNotExist
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from .forms import NewPostForm
import random

def randomuid():
    s = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res=''
    for _ in range(7):
        res = res + random.choice(s)
    try:
        check = Post.objects.get(pk=res)
        randomuid()
    except :
        return res    




def all_posts(request):
    qry_list = Post.objects.all() #.order_by('-timestamp')
    paginator = Paginator(qry_list, 5)
    page = request.GET.get('page')
    # qry = paginator.page(page)
    try:
        qry = paginator.page(page)
    except PageNotAnInteger:
        qry = paginator.page(1)
    except InvalidPage:
        qry = paginator.page(1)
    except TypeError:
        qry = paginator.page(1)        
    except EmptyPage:
        qry = paginator.page(paginator.num_pages)    
    

    context = {'qry':qry}
    return render(request,'all_post.html', context)


def details(request, post_myurl):
    qry = get_object_or_404(Post, myurl=post_myurl)
    # qry = Post.objects.get(pk=post_uid)
    context = {'qry':qry}
    return render(request, 'details.html', context)


def create_post(request):
    form = NewPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.uid = randomuid()
        instance.save()
        # messages.success(request, 'successfully posted!!')
        return HttpResponseRedirect('/blog/')
    # else:
        # messages.error(request, 'Error!! Post Not Created!!')
    print(form)
    context = {"form":form}
    return render(request,'create_post.html', context)
