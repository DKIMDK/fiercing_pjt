from django.urls import path
from . import views

urlpatterns = [
    # path('df/', views.get_recommended_products),
    path('<str:saving_pk>/databaseSaving/', views.databaseSaving),
    path('savingsend/', views.savingsend),
    path('depositsned/', views.depositsend),
    path('<str:deposit_pk>/databaseDeposit/', views.databaseDeposit),
    path('deposit/', views.get_recommended_deposit_products),
    path('saving/', views.get_recommended_saving_products),
    # path('<int:deposit_pk>/databaseDeposit/', views.databaseDeposit),
]