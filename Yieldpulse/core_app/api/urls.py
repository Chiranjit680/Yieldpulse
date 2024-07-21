from django.urls import path
from .views import (
    DashboardAPIView,
    UserDetailsCreateAPIView,
    UserDetailsUpdateAPIView,
    PortfolioDetailsAPIView,
    InvestmentView,
    ExpenseCreateAPIView,
    BudgetCreate,
    BudgetUpdate,
    IncomeCreate,
)

urlpatterns = [
    path('dashboard/<int:pk>/', DashboardAPIView.as_view(), name='dashboard'),
    path('userdetails/create/<int:pk>/', UserDetailsCreateAPIView.as_view(), name='user-details-create'),
    path('userdetails/update/<int:pk>/', UserDetailsUpdateAPIView.as_view(), name='user-details-update'),
    path('portfolio/<int:pk>/', PortfolioDetailsAPIView.as_view(), name='portfolio-details'),
    path('investments/<int:pk>/', InvestmentView.as_view(), name='investment-view'),
    path('expenses/create/<int:pk>/', ExpenseCreateAPIView.as_view(), name='expense-create'),
    path('budgets/create/<int:pk>/', BudgetCreate.as_view(), name='budget-create'),
    path('budgets/update/<int:pk>/', BudgetUpdate.as_view(), name='budget-update'),
    path('incomes/create/<int:pk>/', IncomeCreate.as_view(), name='income-create'),
]
