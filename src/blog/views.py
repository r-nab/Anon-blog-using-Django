from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger, InvalidPage
# from django.core.exceptions.ObjectDoesNotExist import DoesNotExist
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from .forms import NewPostForm
import random
from urllib.parse import quote_plus


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
    search_q = request.GET.get("q")
    if search_q:
        qry_list = qry_list.filter(
            Q(title__icontains=search_q) |
            Q(content__icontains=search_q)
            )

    paginator = Paginator(qry_list, 5)
    page = request.GET.get('page')
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
    if request.GET:
        search_q = request.GET.get("q")
        return HttpResponseRedirect('/blog/?q='+search_q)
    qry = get_object_or_404(Post, myurl=post_myurl)
    # qry = Post.objects.get(pk=post_uid)
    share_str = quote_plus(qry.content)
    context = {'qry':qry, 'share_str':share_str}
    return render(request, 'details.html', context)


def create_post(request):
    if request.GET:
        search_q = request.GET.get("q")
        return HttpResponseRedirect('/blog/?q='+search_q)
    form = NewPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.uid = randomuid()
        instance.save()
        print(form.cleaned_data.get("title"))
        messages.success(request, 'successfully created new POST !!')
        return HttpResponseRedirect('/blog/')
    elif request.POST and not form.is_valid():
        if not form.cleaned_data.get("title"):
            # print("title_error")
            messages.error(request, 'title_error')
        elif not form.cleaned_data.get("content"):
            # print("content_error")    
            messages.error(request, 'content_error')
    # print(form)
    context = {"form":form}
    return render(request,'create_post.html', context)
