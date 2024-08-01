from django.urls import path

from .views import *

urlpatterns=[
    path("av/",addview),
    path("sv/",showview),
    path("uv/<int:ud>/",updateview),
    path("dv/<int:id>/",deleteview)
]