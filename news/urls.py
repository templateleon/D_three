from django.urls import path, include
from .views import *

urlpatterns = [
    path('', PostList.as_view(), name='news'),
    path('<int:pk>', PostDetail.as_view(), name='new_s'),
]