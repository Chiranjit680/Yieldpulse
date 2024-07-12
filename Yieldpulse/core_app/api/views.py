from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError

from core_app.models import *
from .serializers import *

# Helper function to get user details
def get_user_detail(pk):
    return get_object_or_404(User_details, pk=pk)

class DashboardAPIView(APIView):
    def get(self, request, pk):
        user=get_object_or_404(User, pk=pk)
        budget = get_object_or_404(Budget, user=user)
        budget_serializer = BudgetSerializer(budget)
        
        expense = get_object_or_404(Expense, user=user)
        expense_serializer = ExpenseSerializer(expense)
        
        income = get_object_or_404(Income, user=user)
        income_serializer = IncomeSerializer(income)
        
        portfolio = get_object_or_404(Portfolio, user=user)
        portfolio_serializer = PortfolioSerializer(portfolio)
        
        return Response({
            'budget': budget_serializer.data,
            'expense': expense_serializer.data,
            'income': income_serializer.data,
            'portfolio': portfolio_serializer.data,
        },status=status.HTTP_200_OK)

class UserDetailsCreateAPIView(generics.CreateAPIView):
    queryset = User_details.objects.all()
    serializer_class = User_detail_serializer
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(User, pk=pk)
        user_queryset = User_details.objects.filter(user=user)
        
        if user_queryset.exists():
            raise ValidationError('User already has details.')
        
        serializer.save(user=user)

class UserDetailsUpdateAPIView(generics.UpdateAPIView):
    queryset = User_details.objects.all()
    serializer_class = User_detail_serializer
    
    def perform_update(self, serializer):
        pk = self.kwargs.get('pk')
        user_details = get_user_detail(pk)
        user = user_details.user
        user_queryset = User_details.objects.filter(user=user).exclude(pk=pk)
        
        if user_queryset.exists():
            raise ValidationError('Another user detail with this user already exists.')
        
        serializer.save(user=user)

class InvestmentDetailsAPIView(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        investments = get_object_or_404(Portfolio, user=user)
        investment_serializer = PortfolioSerializer(investments)
        
        return Response({'investments': investment_serializer.data})

class ExpenseCreateAPIView(APIView):
    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        data = request.data.copy()
        data['user'] = user.pk
        serializer = ExpenseSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

