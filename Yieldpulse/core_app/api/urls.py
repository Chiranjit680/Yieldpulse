from django.urls import path
from .views import (
    DashboardAPIView,
    UserDetailsCreateAPIView,
    UserDetailsUpdateAPIView,
    InvestmentDetailsAPIView,
    ExpenseCreateAPIView
)

urlpatterns = [
    path('dashboard/<int:pk>/', DashboardAPIView.as_view(), name='dashboard'),
    path('user_details/create/<int:pk>/', UserDetailsCreateAPIView.as_view(), name='user_details_create'),
    path('user_details/update/<int:pk>/', UserDetailsUpdateAPIView.as_view(), name='user_details_update'),
    path('investments/<int:pk>/', InvestmentDetailsAPIView.as_view(), name='investment_details'),
    path('expenses/create/<int:pk>/', ExpenseCreateAPIView.as_view(), name='expense_create'),
]
