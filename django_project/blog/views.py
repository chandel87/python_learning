from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse


# Create your views here.
def blog_home(request):
    context = {
        'posts': Post.objects.all()
    }
    # return HttpResponse('<h1>My blog home page</h1>')
    return render(request, 'blog/home.html', context)


def blog_about(request):
    # return HttpResponse('<h1>This is about page for Blog app</h1>')
    return render(request, 'blog/about.html', {'title' : 'About'})