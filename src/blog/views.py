from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import NewPostForm

def all_posts(request):
    qry = Post.objects.all() #.order_by('-timestamp')
    context = {'qry':qry}
    return render(request,'all_post.html', context)
def details(request, post_id):
    qry = Post.objects.get(pk=post_id)
    context = {'title':qry.title, 'content':qry.content, 'timestamp':qry.timestamp, 'tag':qry.tag}
    return render(request, 'details.html', context)

def create_post(request):
    form = NewPostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        # messages.success(request, 'successfully posted!!')
        return HttpResponseRedirect('/blog/')
    # else:
        # messages.error(request, 'Error!! Post Not Created!!')
    context = {"form":form}
    return render(request,'create_post.html', context)
