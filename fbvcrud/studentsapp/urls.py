from django.urls import path
from .views import *

urlpatterns={
    path("home/", home, name="home"),
    path("form/", studentform, name="form"),
    path("stu/", studentdata, name="stu"),
    path("delete/<int:id>/", delete, name="dlt"),
    path("upd/<int:oid>/", update, name="updt")
}