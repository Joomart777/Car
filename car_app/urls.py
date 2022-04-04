from django.urls import path

from car_app.views import *

urlpatterns = [
path('car/', CarListView.as_view()),
path('car_create/', CarCreateView.as_view()),
path('car_update/<int:pk>/', CarUpdateView.as_view()),
path('car_detail/<int:pk>/', CarDetailView.as_view()),
path('car_delete/<int:pk>/', CarDeleteView.as_view()),

    ]