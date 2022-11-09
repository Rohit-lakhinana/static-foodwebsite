from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib.staticfiles.urls  import staticfiles_urlpatterns

urlpatterns = [

   path('', views.hot, name="hot"),
   path('pink/', views.spunk, name="pink"),
   path('next/', views.one, name="next"),
   path('help/', views.hh, name="help"),
   path('suc/', views.suc, name="suc")
]
   

urlpatterns += staticfiles_urlpatterns()

