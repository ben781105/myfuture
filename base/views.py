from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import login,authenticate
from django.http import HttpResponse
from django.db.models import Sum
from datetime import datetime
from .models import Member,MonthlyObligation,Deposit,DepositHistory
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_user(request):
   if request.method =='POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username,password=password)
      if user is not None:
         login(request,user)
         return redirect('home')
      else:
         messages.error(request, "Invalid username or password")
         return redirect('login')  

   return render(request, 'registration/login.html',{})


@login_required(login_url="login")
def home_view(request):
   user =request.user
   member = Member.objects.get(user=user)
   total_funds = Deposit.objects.filter(confirmed = True).aggregate(total= Sum('amount'))['total'] or 0
   total_funds = int(total_funds)
   members_no = Member.objects.all().count()
   obligations = MonthlyObligation.objects.order_by('-month').first()
   obligation_amount = obligations.amount if obligations else 50000
   
   
     
   total_deposits = Deposit.objects.filter(member=member, confirmed = True).aggregate(total = Sum('amount'))['total'] or 0
     
   context = {
     
     'obligations': str(obligation_amount),
     'total_funds': int(total_funds),
     'user': request.user,
     'members_no':members_no,
     'total_deposits':total_deposits
    
     
   }
   return render(request, 'home.html',context)


@login_required(login_url="login")
def members_view(request):
   members = Member.objects.all()
   for member in members:
     position = member.leadership_position
   return render(request, 'members.html',{'members':members,'position':position})
   
@login_required(login_url="login")
def deposits_view(request):
  members =Member.objects.all()
  total_funds = Deposit.objects.filter(confirmed = True).aggregate(total= Sum('amount'))['total'] or 0
  total_funds = int(total_funds)
  latest_obligation = MonthlyObligation.objects.order_by('-month').first()
  obligation_amount = int(latest_obligation.amount) if latest_obligation else 50000
  
  
  current_month = datetime.now().strftime('%Y-%m')
  member_data =[]
  for member in members:
     total_deposits = Deposit.objects.filter(member=member, confirmed = True).aggregate(total = Sum('amount'))['total'] or 0
     deposits = Deposit.objects.filter(member=member, confirmed=True).order_by('-date')
     
     this_month_deposits = deposits.filter(date__startswith =current_month).aggregate(total=Sum('amount'))['total']
     this_month_deposits = int(this_month_deposits) if this_month_deposits is not None else 0
    
     amount_due = obligation_amount - this_month_deposits if this_month_deposits < obligation_amount else 0
     
     
     member_data.append({
      'username': member.user.username,
      'total_deposits': int(total_deposits),
      'this_month_deposits': this_month_deposits,
      'amount_due': amount_due,
      'deposit_history': deposits.values('amount','date'),
     })
       
  return render(request, 'deposits.html',{'member_data':member_data,})

@login_required(login_url="login")
def deposit_history(request):
   members = Member.objects.all()
   member_data =[]
   for member in members:
      history = DepositHistory.objects.filter(member=member).order_by('-month')[:2]

      member_data.append({
         'username':member.user.username ,
         'leadership_position':member.leadership_position if member.leadership_position else 'Member',
         'deposit_history':history,
         
      })
   for member in members:
      history = DepositHistory.objects.filter(member=member).order_by('-month')[:2]
   
      context ={
   'user':(request.user),
   'member_data': member_data
   }
      return render(request,'deposit_history.html',context)
   

