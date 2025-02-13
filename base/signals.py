from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Deposit,DepositHistory
from datetime import datetime
from django.db.models import Sum


@receiver(post_save, sender = Deposit)
def update_deposit_histort(sender,instance, **kwargs):
    if instance.confirmed:
        month = instance.date.strftime('%Y-%m')

        history, created = DepositHistory.objects.get_or_create(
            member = instance.member,
            month=month
        )
        history.total_deposits= Deposit.objects.filter(
            member=instance.member,
            date__startswith=month,
            confirmed =True
        ).aggregate(total=Sum('amount'))['total'] or 50000
        history.save()