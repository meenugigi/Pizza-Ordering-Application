from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add/<str:category>/<str:name>/<str:cost>", views.add, name="add"),
    path("delete/<str:category>/<str:name>/<str:cost>", views.delete, name="delete"),
    path("confirmorder/", views.confirmorder, name="confirmorder"),
    path("viewmyorders", views.viewmyorders, name="viewmyorders"),
  #  path("get_more_tables", views.get_more_tables, name="get_more_tables"),
    path('payment', views.HomePageView.as_view(), name='payment'),
]
