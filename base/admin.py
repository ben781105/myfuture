from django.contrib import admin
from .models import Deposit,MonthlyObligation,Member
# Register your models here.
admin.site.register(Member)
admin.site.register(Deposit)
admin.site.register(MonthlyObligation)

