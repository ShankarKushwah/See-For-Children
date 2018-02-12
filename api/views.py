from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from django.db.models import Q
from rest_framework import viewsets, filters
from rest_framework.authentication import SessionAuthentication
from rest_framework.reverse import reverse as api_reverse
from NGO.models import NGO, Children, Events
from superadmin.models import Donor
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, NGOSerializer, NGODetailSerializer, ChildrenSerializer, \
    ChildrenDetailSerializer, EventSerializer, EventDetailSerializer, DonorSerializer, DonorDetailSerializer, DonorDetailUpdateSerializer, EventDetailUpdateSerializer
from rest_framework import generics
from .pagination import ChildrenPagination


class HomeAPIView(APIView):
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = {
            "auth": {
                "login_url": api_reverse("auth_login_api", request=request),
                "refresh_url": api_reverse("refresh_token_api", request=request),
            },
            "ngo": {
                "count": NGO.objects.all().count(),
                "url": api_reverse("ngo_api", request=request)
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
    model = NGO
    queryset = NGO.objects.all()
    serializer_class = NGOSerializer

    def get_queryset(self):
        qs = super(NGOListAPIView, self).get_queryset()
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(name__icontains=query)
            )
        return qs


class NGORetrieveAPIView(generics.RetrieveAPIView):
    queryset = NGO.objects.all()
    serializer_class = NGODetailSerializer


class ChildrenListAPIView(generics.ListAPIView):
    model = Children
    queryset = Children.objects.all()
    serializer_class = ChildrenSerializer
    pagination_class = ChildrenPagination

    def get_queryset(self, *args, **kwargs):
        qs = super(ChildrenListAPIView, self).get_queryset(*args, **kwargs)
        query = self.request.GET.get("q")
        if query:
            qs = self.model.objects.filter(
                Q(name__icontains=query)
            )
        return qs


class ChildrenRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Children.objects.all()
    serializer_class = ChildrenDetailSerializer


class EventListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Events.objects.all()
    serializer_class = EventSerializer


class EventRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Events.objects.all()
    serializer_class = EventDetailSerializer


class EventCreateView(generics.CreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventDetailUpdateSerializer


class DonorRudAPIView(generics.ListAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorSerializer


class DonorRetrieveRudAPIView(generics.RetrieveAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorDetailSerializer


class DonorCreateView(generics.CreateAPIView):
    queryset = Donor.objects.all()
    serializer_class = DonorDetailUpdateSerializer
