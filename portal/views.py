from rest_framework import generics, permissions
from . serializers import commentSerilizers
from . models import comment

class commentList(generics.ListCreateAPIView):
    queryset = comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = commentSerilizers

class commentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = comment.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = commentSerilizers
   


