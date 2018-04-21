from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate

from rest_framework import views, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import parsers, renderers, exceptions, status

from rest_accounts.api.serializers import *
from rest_accounts.models import *

from rest_accounts.utils import *


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

     # def list(self, request):


     # def retrieve(self, request, pk=None):


     # def perform_create(self, serializer):


     # def perform_update(self, serializer):


     # def perform_destroy(self, instance):



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
            print(user.username,request.data.get("password"))
            is_authenticated_api = authenticate(
                request,
                username=str(user.username),
                password=str(request.data.get("password"))
            )
            if is_authenticated_api is not None:
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



class MpesaB2Cviewset(viewsets.ModelViewSet):
    serializer_class = MpesaB2CSerializer
    queryset = MpesaB2C.objects.all()


class MpesaC2Bviewset(viewsets.ModelViewSet):
    serializer_class = MpesaC2BSerializer
    queryset = MpesaC2B.objects.all()


class MpesaAccountBalanceviewset(viewsets.ModelViewSet):
    serializer_class = MpesaAccountBalanceSerializer
    queryset = MpesaAccountBalance.objects.all()


class TransactionStatusviewset(viewsets.ModelViewSet):
    serializer_class = TransactionStatusSerializer
    queryset = TransactionStatus.objects.all()


class MpesaReversalsviewset(viewsets.ModelViewSet):
    serializer_class = MpesaReversals
    queryset = MpesaReversals.objects.all()


class HomeAPIView(views.APIView):
    # renderer_classes = (renderers.JSONRenderer,)

    def get(self,request):
        return Response({
            "status": "success",
            "message": "Welcome to Viraja Pay API."
        })
