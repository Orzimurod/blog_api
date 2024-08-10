from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import CategoryViewSet,PostViewSet

router = DefaultRouter()
router.register(r'category',CategoryViewSet, basename='category')
router.register(r'posts',PostViewSet, basename='posts')

urlpatterns = [
    path('',include(router.urls))

    # path('category', CategoryViewSet.as_view(),name = 'category'),
    # path('posts', PostViewSet.as_view(),name = 'post')
]
