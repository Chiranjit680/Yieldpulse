from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from .models import *
from rest_framework.views import APIView
from .serializers import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework import status
# Create your views here.

class dashboard(APIView):
    def get(self,request,pk):
         budget= get_object_or_404(Budget, pk=pk)
         budget_serializer = BudgetSerializer(budget)
         
         
         expense=get_object_or_404(Expense, pk=pk)
         expense_serializer = ExpenseSerializer(expense)
         
         income=get_object_or_404(Income, pk=pk)
         income_serializer = IncomeSerializer(income)
         
         portfolio=get_object_or_404(Portfolio, pk=pk)
         portfolio_serializer = PortfolioSerializer(portfolio)
         return Response({
             'budget': budget_serializer.data,
             'expense': expense_serializer.data,
             'income': income_serializer.data,
             'portfolio': portfolio_serializer.data,
         })
class UserDetails(generics.CreateAPIView):
    queryset = User_details.objects.all()
    serializer_class = User_detail_serializer
    
    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        user=User.objects.get(pk=pk)
        user_queryset=User_details.objects.filter(user=user)
        if user_queryset.exists():
            raise ValidationError('User already has a details')
        serializer.save(user=user)


class UpdateUserDetail(generics.UpdateAPIView):
    queryset = User_details.objects.all()
    serializer_class = User_detail_serializer
    
    def perform_update(self, serializer):
        pk = self.kwargs.get('pk')
        user_details = get_object_or_404(User_details, pk=pk)
        user = user_details.user
        user_queryset = User_details.objects.filter(user=user).exclude(pk=pk)
        
        if user_queryset.exists():
            serializer.save(user=user)
        else:
            raise ValidationError('User detail with this user does not exist.')
class investmentDetailsAV(APIView):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        investments=get_object_or_404(Portfolio, pk=pk)
        investment_serializer = PortfolioSerializer(investments)
        return Response(request,{'investments':investment_serializer.data})

class ExpenseCreateAPIView(APIView):
    def post(self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)