from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from rest_framework import views, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import parsers, renderers, exceptions, status

from rest_accounts.api.serializers import *
from rest_accounts.models import UserProfile


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserCreateAPIView(views.APIView):
    serializer_class = UserSerializer

    permission_classes = ()

    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TokenAPIView(views.APIView):
    serializer_class = UserSerializer

    permission_classes = ()

    parser_classes = (
        parsers.FormParser,
        parsers.MultiPartParser,
        parsers.JSONParser,
    )

    renderer_classes = (renderers.JSONRenderer,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if request.data.get("username") and request.data.get("password"):
            user = get_object_or_404(UserProfile, username=request.data.get("username"))
            is_authenticated_api = authenticate(
                username=user.username,
                password=request.data["password"]
            )
            if is_authenticated_api:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise exceptions.ValidationError(msg)
                else:
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({
                        "token": token.key
                    })
            else:
                msg = 'Unable to log in with provided credentials.'
                raise exceptions.ValidationError(msg)

        else:
            msg = "Username and Password are required!"
            raise exceptions.ValidationError(msg)
