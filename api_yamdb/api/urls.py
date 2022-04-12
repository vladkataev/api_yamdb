from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, ReviewViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'^titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet,
                basename='review')
router.register(
    r'^titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
]