from rest_framework import serializers
from core_app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
    def validate_username(self, value):
        if User.objects.filter(name=value).exists():
            raise serializers.ValidationError("Username already exists")
        return value
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be greater than zero")
        return value
class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'

    def validate(self, data):
        total = data.get('stock', 0) + data.get('bond', 0) + data.get('mf', 0) + data.get('gold', 0) + data.get('crypto', 0)
        if total != 100:
            raise serializers.ValidationError("Portfolio must add up to 100%")
        return data
    
class User_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = User_details
        fields = '__all__'