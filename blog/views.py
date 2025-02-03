from django.shortcuts import render
from django.views import generic
from .models import Post

#from django.http import HttpResponse

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "post_list.html"
    #model = Post
#def my_blog(request):
    #return HttpResponse("Hello, Blog!")
