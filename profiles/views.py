from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer
from drf_api_micah.permissions import IsOwnerOrReadOnly


class ProfileList(ListCreateAPIView):
    """
    List all profiles
    No Create view (post method), as profile creation handled by django signals
    """
    serializer = ProfileSerializer
    queryser = Profile.objects.all()


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    serializer_class = ProfileSerializer
    permission_classes =[IsOwnerOrReadOnly]
    queryset = Post.objects.all()