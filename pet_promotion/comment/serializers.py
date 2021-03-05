from rest_framework import serializers

from .models import Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id','comment', 'user','create_date','update_date','post')