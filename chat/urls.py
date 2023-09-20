from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('chat/<str:username>', views.chatPage , name='chat'),
    path('login/' , views.Login , name="login"),
    path('register/' , views.register , name="register"),
]
