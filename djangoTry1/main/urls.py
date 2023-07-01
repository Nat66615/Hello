from django.urls import path
from . import views as main_views
from multiply import views as multiply_views
from programmers_day import views as proggsday_views

urlpatterns = [
    path('', main_views.index),
    path('multiply/', multiply_views.get_table_of_multiply),
    path('proggsday/', proggsday_views.get_programmers_day)
]
