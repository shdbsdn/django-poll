from django.urls import include,path
from django.contib import admin
from . import views

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]