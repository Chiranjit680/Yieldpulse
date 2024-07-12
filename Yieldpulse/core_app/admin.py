from django.contrib import admin
from .models import Expense, Income, Budget, Portfolio, User_details

# Register your models here
admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Budget)
admin.site.register(Portfolio)
admin.site.register(User_details)
