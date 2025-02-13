from django.db import models
from datetime import date
from django.contrib.auth.models import User
# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    leadership_position =models.CharField(max_length=100,blank=True,null=True)

    
    def __str__(self):
        return self.user.username
    
    

class Deposit(models.Model):
    member = models.ForeignKey(Member, on_delete= models.CASCADE)
    amount = models.IntegerField()
    date = models.DateField(default=date.today)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.member.user.username} - {self.amount}'

class MonthlyObligation(models.Model):
    amount = models.IntegerField()
    month = models.DateField()

    def __str__(self):
        return f"obligation for {self.month.strftime('%d %Y')}"
    

class DepositHistory(models.Model):
    member =models.ForeignKey(Member,on_delete=models.CASCADE)
    month = models.CharField(max_length=7)
    total_deposit = models.PositiveBigIntegerField(default=0)

    class Meta:
        unique_together = ('member','month')

    def __str__(self):
        return f'{self.member.user.username}-{self.month}-{self.total_deposit}'    

