from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("hello/<str:name>/", views.hello, name="hello"),
    path("api/status/", views.status , name="status")
]
