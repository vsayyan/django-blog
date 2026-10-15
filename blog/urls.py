from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("about/", views.about, name="about"),
    path("hello/<str:name>/", views.hello, name="hello"),
    path("api/status/", views.status , name="status"),
    path("contact/", views.contact, name="contact"),
    path("api/add/<int:a>/<int:b>/", views.add , name="add")
]
