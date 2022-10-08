from django.urls import path
from .views import Home,AddStudent,Delete_Student,EditStudent
urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('add/',AddStudent.as_view(),name='add'),
    path('delete/',Delete_Student.as_view(),name='delete'),
    path('edit/<int:id>/',EditStudent.as_view(),name="edit")
]
