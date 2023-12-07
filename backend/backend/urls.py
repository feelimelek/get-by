"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
1. Add an import: from my_app import views
2. Add a URL to urlpatterns: path('', views.home, name='home')
Class-based views
1. Add an import: from other_app.views import Home
2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')
Including another URLconf
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from core.views import AddressViewSet
from core.views import EmotionViewSet
from core.views import TipViewSet
from core.views import CommentViewSet
from core.views import EmotionTipViewSet
from core.views import PersonViewSet
from core.views import PersonEmotionViewSet
from core.views import SelectionViewSet
from core.views import TaskViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'address', AddressViewSet, basename="address")
router.register(r'emotion', EmotionViewSet)
router.register(r'tip', TipViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'emotion-tip', EmotionTipViewSet)
router.register(r'person', PersonViewSet)
router.register(r'person-emotion', PersonEmotionViewSet)
router.register(r'selection', SelectionViewSet)
router.register(r'task', TaskViewSet)

urlpatterns = [
path('', include(router.urls)),
path('admin/', admin.site.urls)
]
