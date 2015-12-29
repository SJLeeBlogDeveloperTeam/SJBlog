# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Article
from datetime import datetime
from django.http import Http404


# Create your views here.
def home(request):
    post_list = Article.objects.all()  # 获取Article全部对象
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    """post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
           % (post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)"""
    '''return HttpResponse("my_arts:%s." % my_args)'''
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'detail.html', {'post': post})


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})


def markdown(request):
    """
    :param request:
    :return:
    """
    return render(request,'markdownDemo.html',{'viewBag':42})