from django.urls import path
from . import views

urlpatterns = [
    # path('database/', views.deposits),
    # path('savings/', views.savings),
    path('dview/', views.deposit),
    path('doview/', views.filteredOptions),
    path('sview/', views.saving),
    path('soview/', views.filteredSavingOption),
    path('ddd/', views.ddd),
    path('dddd/', views.dddd),
    # path('hocheol/', views.hocheol),
    # path('hocheol2/', views.hocheol2)
]