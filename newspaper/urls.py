from django.urls import path
from .views import PostsList, PostList


urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('<int:pk>', PostList.as_view(), name='post')
]
