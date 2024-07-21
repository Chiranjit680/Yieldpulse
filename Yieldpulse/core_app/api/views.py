from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from .permissions import UserOrAdmin

from core_app.models import *
from .serializers import *

# General dashboard views
class DashboardAPIView(APIView):
    permission_classes = [UserOrAdmin]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        budget = get_object_or_404(Budget, user=user)
        expense = get_object_or_404(Expense, user=user)
        income = get_object_or_404(Income, user=user)
        portfolio = get_object_or_404(Portfolio, user=user)

        budget_serializer = BudgetSerializer(budget)
        expense_serializer = ExpenseSerializer(expense)
        income_serializer = IncomeSerializer(income)
        portfolio_serializer = PortfolioSerializer(portfolio)

        return Response({
            'budget': budget_serializer.data,
            'expense': expense_serializer.data,
            'income': income_serializer.data,
            'portfolio': portfolio_serializer.data,
        }, status=status.HTTP_200_OK)

# User details views
class UserDetailsCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [UserOrAdmin]
    serializer_class = User_detail_serializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        return User_details.objects.filter(user=user)

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        user = get_object_or_404(User, pk=pk)
        user_queryset = User_details.objects.filter(user=user)

        if user_queryset.exists():
            raise ValidationError('User already has details.')

        serializer.save(user=user)

class UserDetailsUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [UserOrAdmin]
    serializer_class = User_detail_serializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        return User_details.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.save()

# Portfolio views
class PortfolioDetailsAPIView(APIView):
    permission_classes = [UserOrAdmin]

    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        investments = get_object_or_404(Portfolio, user=user)
        investment_serializer = PortfolioSerializer(investments)

        return Response({'investments': investment_serializer.data})

    def post(self, request):
        serializer = PortfolioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        investments = get_object_or_404(Portfolio, user=user)
        serializer = PortfolioSerializer(investments, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvestmentView(generics.ListCreateAPIView):
    permission_classes = [UserOrAdmin]
    serializer_class = InvestmentSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        return InvestmentAdvisoy.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save()

# Expense views
class ExpenseCreateAPIView(APIView):
    permission_classes = [UserOrAdmin]

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        data = request.data.copy()
        data['user'] = user.pk
        serializer = ExpenseSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Budget views
class BudgetCreate(generics.ListCreateAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [UserOrAdmin]

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        return Budget.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BudgetUpdate(generics.UpdateAPIView):
    serializer_class = BudgetSerializer
    permission_classes = [UserOrAdmin]

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        return Budget.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.save()

# Income views
class IncomeCreate(generics.ListCreateAPIView):
    serializer_class = IncomeSerializer
    permission_classes = [UserOrAdmin]

    def get_queryset(self):
        pk = self.kwargs['pk']
        user = get_object_or_404(User, pk=pk)
        return Income.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save()
