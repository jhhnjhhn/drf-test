from django.conf.urls import url, include
from api import views

from rest_framework.routers import DefaultRouter
from api.views import ProductViewSet

router = DefaultRouter()
router.register(r'product', views.ProductViewSet)

# api url 配置
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^test/$', views.GetMessageView.as_view()),
]