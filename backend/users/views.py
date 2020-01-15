from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Profile
from .serializers import ProfileSerializer


class DetailUserView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            user = request.user
            username = user.username
            group_names = [group.name for group in user.groups.all()]
            avatar = Profile.objects.filter(user=user).first().avatar.url
            data = {}
            if user:
                data = {
                    'username': username,
                    'groups': group_names,
                    'avatar': avatar
                }
        else:
            data = {}

        return Response(data)


class UpdateProfileAvatar(APIView):
    permission_classes = (IsAuthenticated, )
    parser_classes = (MultiPartParser, )

    @action(detail=True, methods=['put'])
    def put(self, request, id=None, format=None):
        user = request.user
        profile = user.profile
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response("Bad Request", status=400)
