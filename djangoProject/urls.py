"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import routers

from oAuth.views import UserInfoViewSet, UserViewSet,  UserCreateViewSet

router_V1 = routers.DefaultRouter()
router_V1.register('info', UserInfoViewSet)
router_V1.register('users/create/activate', UserCreateViewSet)
router_V1.register('users/create', UserCreateViewSet)
router_V1.register('users', UserViewSet)
# router_V1.register('books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router_V1.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
