from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('fire-alarm/', views.fire_alarm, name='fire_alarm'),
    path('burglar-alarm/', views.burglar_alarm, name='burglar_alarm'),
]
