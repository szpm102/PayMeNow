from django.shortcuts import render
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.core.files.storage import FileSystemStorage
import requests, json
from django.utils import timezone
from datetime import timedelta
from datetime import datetime
from dateutil import parser
from django.conf import settings
from .forms import PaymentListForm
from base64 import b64encode
import pyperclip
# Create your views here.

USER_ID = 18

def get_token():
    while True:
        body = {
            "username":settings.API_UNAME,
            "password":settings.API_PW
        }
        headers = {'content-type': 'application/json'}

        response = requests.post(f"{settings.API_LINK}/token/", headers=headers, data=json.dumps(body))
        if response.status_code == 200:
            j = json.loads(response.text)
            return j['token'], j['token_create']
            break


def get_list_transactions(user_id):
    token, token_created_date = get_token()
    date = parser.parse(token_created_date)
    while True:
        if date > timezone.now() - timedelta(
                seconds=900):
            headers = {'content-type': 'application/json', 'Authorization': f"Token {token}"}
            response = requests.get(f"{settings.API_LINK}/outstanding_transactions?user={user_id}", headers=headers)
            data = json.loads(response.text)
            if response.status_code == 401:
                token, token_created_date = get_token()
            else:
                result = {
                    "status_code": response.status_code,
                    "message": response.reason,
                    "data": data
                }
                break
    return result

def get_transaction_by_id(trn_pk):
    token, token_created_date = get_token()
    date = parser.parse(token_created_date)
    while True:
        if date > timezone.now() - timedelta(
                seconds=900):
            headers = {'content-type': 'application/json', 'Authorization': f"Token {token}"}
            response = requests.get(f"{settings.API_LINK}/outstanding_transactions/{trn_pk}", headers=headers)
            data = json.loads(response.text)
            if response.status_code == 401:
                token, token_created_date = get_token()
            else:
                result = {
                    "status_code": response.status_code,
                    "message": response.reason,
                    "data": {
                        "Section": data['section'],
                        "Receipt_Date": data['post_date'],
                        "Title": data['title'],
                        "Receipt_Amount": data['expense_amt'],
                        "Request_Amount": data['requested_amt'],
                        "Receipt_Attachment": data['attachment'],
                        "Note": data['description'],
                    }
                }
                break
    return result


def post_create_payments(section, title, description, postdate, attachment, exp_amt, req_amt, user_id, date_created):
    token, token_created_date = get_token()
    date = parser.parse(token_created_date)
    data = {
        "section": int(section),
        "title": f"{title}",
        "description": f"{description}",
        # "description": f"{form['Note'].value()}",
        "post_date": f"{postdate}",
        "attachment": attachment,
        "expense_amt": f"{exp_amt}",
        "requested_amt": f"{req_amt}",
        "user": user_id,
        "date_created": f"{date_created}",

    }
    pyperclip.copy(json.dumps(data))
    while True:
        if date > timezone.now() - timedelta(
                seconds=900):
            headers = {'content-type': 'application/json', 'Authorization': f"Token {token}"}
            response = requests.post(f"{settings.API_LINK}/outstanding_transactions/", headers=headers, data=json.dumps(data))
            try:
                data = json.loads(response.text)
            except:
                data = response.text
            if response.status_code == 401:
                token, token_created_date = get_token()
            else:
                result = {
                    "status_code": response.status_code,
                    "message": response.reason,
                    "data": data
                }
                break
    return result


def all_payments(request):
    j = get_list_transactions(USER_ID)
    return render(request,'paymentlist/viewpayments.html', {'list': j['data']})

def create_payments(request):
    if request.method =='GET':
        form = PaymentListForm()
        return render(request, 'paymentlist/createeditpayments.html', {'form': form})
    else:
        form = PaymentListForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['Receipt_Attachment']
            Section = request.POST['Section']
            post_date = request.POST['Receipt_Date']
            data = file.read()
            b64image = b64encode(data).decode()
            data = post_create_payments(Section, form['Title'].value(), form['Note'].value(), post_date, f"data:image/jpeg;base64,{b64image}",
                                 form['Receipt_Amount'].value(), form['Request_Amount'].value(), USER_ID, datetime.now().replace(microsecond=0).isoformat())
            if data['status_code'] == 201:
                j = get_list_transactions(USER_ID)
                return redirect ('all_payments')
            else:
                return render(request, 'paymentlist/createeditpayments.html', {'form': form, 'error': data['data']})
        else:
            return render(request, 'paymentlist/createeditpayments.html', {'form': form, 'error': form.errors})

def edit_payments(request, trn_pk):
    trns = get_transaction_by_id(trn_pk)
    data = trns['data']
    if request.method == 'GET':
        form = PaymentListForm(initial=data)
        return render(request, 'paymentlist/createeditpayments.html', {'form': form})




