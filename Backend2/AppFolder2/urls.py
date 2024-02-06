from django.urls import path,include
from . import views
urlpatterns = [
    path('viewDB2/', views.ViewDB, name='glance at the database')

]