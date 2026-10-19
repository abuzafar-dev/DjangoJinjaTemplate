from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from blog.forms import PostForm
from blog.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save()
        messages.success(request, "Post qo'shildi")
        return redirect('post_detail', pk=post.pk)
    return render(request, 'post_form.html', {'form': form, 'title': 'Yangi post'})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Post yangilandi')
        return redirect('post_detail', pk=post.pk)
    return render(request, 'post_form.html', {'form': form, 'title': 'Postni tahrirlash'})


@require_POST
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, "Post o'chirildi")
    return redirect('post_list')
