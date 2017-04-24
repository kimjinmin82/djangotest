from django.shortcuts import render

# Create your views here.
from main.models import Post


def index(request):
    post_list = Post.objects.all()
    return render(request, 'index.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {
        'post': post,
    })