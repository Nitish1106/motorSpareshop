

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('', views.signin, name='signin'),
      path('', views.signup, name='signup'),
    
]
