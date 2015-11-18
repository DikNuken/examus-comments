from comments.models import Comment
# Create your views here.
from comments.serializers import CommentHTMLSerializer, CommentSerializer
from django.db.models import Count
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CommentsListApiView(ListCreateAPIView):
    serializer_class = CommentHTMLSerializer

    def get_queryset(self):
        return Comment.objects.annotate(childrens=Count('comment')).filter(
            reply_to__pk=self.kwargs.get('comment_pk'))


@permission_classes((IsAuthenticated,))
class CommentApiView(CreateAPIView):
    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.dict()
        data['user'] = request.user.pk
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        serializer = CommentHTMLSerializer(instance=serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
