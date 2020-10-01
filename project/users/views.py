from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.response import Response

from .serializers import UserSerializer


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register(request):
    user = UserSerializer(data=request.data)

    if user.is_valid():
        user.save()
        return Response(status=status.HTTP_201_CREATED)

    return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
