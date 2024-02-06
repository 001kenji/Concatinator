from django.urls import path,include
from . import views
urlpatterns = [
    path('viewDB/', views.ViewDB, name='glance at the database')

]