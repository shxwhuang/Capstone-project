from django.contrib import admin 
from django.urls import path, include
#from .views import sayHello 
from . import views
from rest_framework import routers

from .views import UserViewSet, MenuItemsView, SingleMenuItemView
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tables', views.BookingViewSet)
  
urlpatterns = [
#    path('', sayHello, name='sayHello'), 
#    path('', views.index, name='index'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]