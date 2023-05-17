from django.contrib import admin 
from django.urls import path, include
#from .views import sayHello 
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserViewSet, MenuView, SingleMenuItemsView, MenuItemsView
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)
  
urlpatterns = [
#    path('', sayHello, name='sayHello'), 
#    path('', views.index, name='index'),
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemsView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('message/', views.msg),
]