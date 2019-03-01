from django.urls import path
from ferien import views

urlpatterns = [
    path('', views.index, name='index'),
    path('company/<int:year>', views.company_calendar, name='company'),
    path('<slug:location>/<int:year>', views.country_calendar, name='country'),
]
