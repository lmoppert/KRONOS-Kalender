from django.urls import path
from ferien import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:location>/<int:year>', views.country_calendar, name='country'),
]
