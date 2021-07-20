from django.urls import path
from .import views

urlpatterns = [
    path('create/',views.create,name = "create_public"),
    path('report_list/',views.report_list,name='report_list'),
    path('create_form/',views.create_form,name='create_form'),

]


