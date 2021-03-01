from django.shortcuts import render
import datetime
from .forms import CommentForm
# Create your views here.

def create_comment(request,post_id):
    comment_form= CommentForm(request.POST)
    if comment_form.is_valid():
        temp_form = comment_form.save(commit=False)
        temp_form.user = request.user
        temp_form.post = Post.objects.get(pk=post_id)
        temp_form.save()

        return redirect('post_detail', post_id)

def update_comment(request,comment_id,post_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if request.method == "POST":
        if request.user == my_comment.user:
            updated_form= CommentForm(request.POST, instance=my_comment)
            if updated_form.is_valid():
                updated_form.save()
                return redirect('post_detail', post_id)
            temp_form = comment_form.save(commit=False)
    return redirect('post_detail', post_id)

def delete_comment(request, post_id, comment_id):
    my_comment = Comment.objects.get(pk=comment_id)
    if request.user == my_comment.user:
        my_comment.delete()
        return redirect('post_detail', post_id)

    else:
        raise PermissionDenied