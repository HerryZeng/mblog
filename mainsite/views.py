from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import redirect
from django.template.loader import get_template
from datetime import datetime

# Create your views here.


# def homepage(request):
#     posts = Post.objects.all()
#     post_list = []
#
#     post_list.append("<title>发布信息</title>")
#
#     for count,post in enumerate(posts):
#         post_list.append("No.{}:".format(str(count + 1)) + "&nbsp;&nbsp;&nbsp;&nbsp;<b>" +str(post) + "</b>" + "<hr />")
#         post_list.append("<small>" + str(post.body) + "</small><br /><br />")
#
#     return HttpResponse(post_list)


def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request,slug):
    template = get_template("post.html")
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('index')