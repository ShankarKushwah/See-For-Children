from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.reverse import reverse as api_reverse
from NGO.models import NGO
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, NGOSerializer, NGODetailSerializer
from rest_framework import generics


class APIView(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = {
            "auth": {
                "login_url": api_reverse("auth_login_api", request=request),
                "refresh_url": api_reverse("refresh_token_api", request=request),
            }
        }
        return Response(data)


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


class CreateUserView(CreateAPIView):
    model = get_user_model()

    serializer_class = UserSerializer


class NGOListAPIView(generics.ListAPIView):
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer


class NGORetrieveAPIView(generics.RetrieveAPIView):
    queryset = NGO.objects.all()
    serializer_class = NGODetailSerializer
