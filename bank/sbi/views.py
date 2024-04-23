from django.shortcuts import render
from django.http import HttpResponse
from .models import Registration

def sbilogin(request):
    return render(request, 'sbilogin.html')

def reg(request):
    if request.method == 'POST':
        account_number = request.POST['accountnumber']
        name = request.POST['name']
        amount = request.POST['amount']
        phone = request.POST['phone']
        data = Registration.objects.create(account_number=account_number, name=name, amount=amount, phone=phone)
        return render(request, 'page2.html')
    else:
        return render(request, 'sbilogin.html')

def balance(request):
    if request.method == 'POST':
        account_number = request.POST['accountnumber']
        try:
            data = Registration.objects.get(account_number=account_number)
            return render(request, 'page2.html', {'data': data})
        except Registration.DoesNotExist:
            return HttpResponse("error")
    else:
        return render(request, 'sbilogin.html')
def depositt(request):
    if request.method == "POST":
        account_number = request.POST.get('account_number')
        deposit_amount = int(request.POST.get('deposit_amount'))

        if deposit_amount % 1000 != 0:
            return render(request, "page2.html",{"return": "Invalid amount. Deposit amount should be a multiple of 1000."})
        try:
            data = Registration.objects.get(account_number=account_number)
            data.amount += deposit_amount
            data.save()
            return render(request, 'page2.html', {'return': f'Your amount of {deposit_amount} has been deposited.'})
        except Registration.DoesNotExist:
            return render(request, "page2.html", {"return": "Account not found."})
        except Exception as e:
            return HttpResponse("Error: {}".format(str(e)))

def withdraw(request):
    if request.method == "POST":
        account_number = request.POST.get("account_number")
        withdraw_amount = int(request.POST.get("withdraw_amount"))
        if withdraw_amount % 100 != 0 and withdraw_amount % 200 != 0 and withdraw_amount % 500 != 0:
            return render(request, "page2.html", {"return": "Invalid amount. Withdraw amount should be multiple of 100, 200, or 500."})
        try:
            data = Registration.objects.get(account_number=account_number)
            if data.amount < withdraw_amount:
                return render(request, "page2.html", {"return": "Insufficient balance."})
            data.amount -= withdraw_amount
            data.save()
            return render(request, "page2.html", {"return": "Your amount "+str(withdraw_amount)+" has been withdrawn."})
        except Registration.DoesNotExist:
            return render(request, "page2.html", {"return": "Account not found."})
        except Exception as e:
            return HttpResponse("Error: {}".format(str(e)))
