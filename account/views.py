from django.shortcuts import render

def account_list(request):
    accounts = [
        {'id': 1, 'email': 'helana.nabil.2@gmail.com', 'password': '112233'},
        {'id': 2, 'email': 'sara.nabil@hotmail.com', 'password': '332211'},
    ]
    context = {'accounts': accounts}
    return render(request, 'account/accountList.html', context)

def create_account(request):
    return render(request, 'account/createAccount.html')

def update_account(request, id):
    context = {'id': id}
    return render(request, 'account/updateAccount.html', context)

def delete_account(request, id):
    context = {'id': id}
    return render(request, 'account/deleteAccount.html', context)

def account_info(request, id):
    context = {'id': id}
    return render(request, 'account/accountInfo.html', context)
