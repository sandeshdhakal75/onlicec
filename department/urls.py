from django.urls import path
from .import views

urlpatterns = [
    path('create/',views.create_department,name='create_department'),
    path('create/',views.create,name = "create_public"),
    path('report_create/',views.report_create,name='report_create'),
]
