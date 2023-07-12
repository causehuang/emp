from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("<int:questions_id>/",views.detail,name="detail"),
    path("<int:questions_id>/results",views.results,name="results"),
    path("<int:questions_id>/vote",views.vote,name="vote"),

]