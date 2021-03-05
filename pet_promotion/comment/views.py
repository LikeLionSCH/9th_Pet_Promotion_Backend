from django.shortcuts import render
from rest_framework import viewsets

from .serializers import CommentSerializer
from .models import Comment

@api_view(['POST'])
def comment_create(request, post_id):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(post=post_id)#post필드 값으로 post_id입력(어떤 게시물의 댓글인지 알기위함)
        return Response(serializer.data)

@api_view(['PUT','DELETE']) #PUT : 데이터 수정할 때, DELETE : 데이터 삭제 할 때
def comment_update_and_delete(request, post_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'PUT':
        serializer = CommentSerializer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'update'})
    else:
        comment.delete()
        return Response({'message':'delete'})