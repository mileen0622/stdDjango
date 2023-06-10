from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),#전달받으면 뷰로 연결
]