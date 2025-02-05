from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post

#from django.http import HttpResponse


# Create your views here.
class PostList(generic.ListView):
    #queryset = Post.objects.all()
    #queryset = Post.objects.filter(author=2)
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

    #model = Post
    #def my_blog(request):
    #return HttpResponse("Hello, Blog!")


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/post_detail.html",
        {"post": post},
    )
