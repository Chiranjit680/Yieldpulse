from typing import Collection
from django.core.validators import MinValueValidator, EmailValidator
from django.db import models
from django.contrib.auth.models import User


class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expense = models.CharField(max_length=100)
    amount = models.IntegerField(validators=[MinValueValidator(0)])
    date = models.DateField()
    category = models.CharField(max_length=100)
    
    def __str__(self):  
        return self.expense

class Income(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    income = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    date = models.DateField()
    
    def __str__(self):
        return self.income

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_income = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    housing = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    food = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    transportation = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    entertainment = models.DecimalField(max_digits
=10, decimal_places=2, validators=[MinValueValidator(0)])
    def __str__(self):
        return str(self.user)

class Portfolio(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    bond = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    mf = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    gold=models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    crypto=models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    def validate_portfolio(self):
        if self.stock+self.bond+self.mf+self.gold+self.crypto != 100:
            raise ValueError("Portfolio must add up to 100%")
        
    def __str__(self):
        return str(self.user)
class InvestmentAdvisoy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    bond = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    mf = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    gold=models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    crypto=models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    
    def validate_portfolio(self):
        if self.stock+self.bond+self.mf+self.gold+self.crypto != 100:
            raise ValueError("Portfolio must add up to 100%")
        
    def __str__(self):
        return str(self.user)

class User_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    age = models.IntegerField(validators=[MinValueValidator(0)])
    income = models.IntegerField(validators=[MinValueValidator(0)])
    type_income=models.CharField(max_length=10)
    no_of_dependents=models.IntegerField(validators=[MinValueValidator(0)])
    savings=models.IntegerField(validators=[MinValueValidator(0)])
    invested=models.IntegerField(validators=[MinValueValidator(0)])
    loan=models.IntegerField(validators=[MinValueValidator(0)])
    
    def __str__(self):
        return self.name
    
    