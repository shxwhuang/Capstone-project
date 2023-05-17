from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from rest_framework import viewsets, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import UserSerializer, MenuSerializer, BookingSerializer, MenuItemSerializer
from .models import Menu, Booking, MenuItem

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class UserViewSet (viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated] 

class MenuView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class BookingViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    def get(self, request):
        return Response({'message': "list of MenuItem"}, status.HTTP_200_OK)
    def post(self, request):
        return Response({'message': "new MenuItem"}, status.HTTP_200_OK)

# @api_view()
# @permission_classes([IsAuthenticated])
# def securedview(request):
#     print("This is securedview")
#     return Response({'message': 'needs authentication'})

@api_view()
@permission_classes([IsAuthenticated])
#@authentication_classes([TokenAuthentication])
def msg(request):
    print("This is msg")
    return Response({"message":"This view is protected"})