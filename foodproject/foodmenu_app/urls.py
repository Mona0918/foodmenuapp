from django.urls import path
from . import views

urlpatterns=[
    path("index/",views.index,name="index"),
    path("itemview/",views.itemview,name="itemview"),
    path("<int:item_id>/",views.detailview,name="detailview"),
    path("additem/",views.additemview,name="additem"),
    path("updateitem/<int:pk>/",views.updateitemview,name="updateitem"),
    path("deleteitem/<int:pk>/",views.deleteitemview,name="deleteitem")
]