from django.forms import ModelForm,DateInput,DateField, forms
from bootstrap_datepicker_plus import DatePickerInput
# from django.core.validators import EMPTY_VALUES
# from django.conf import settings
# from django.utils import timezone
# from datetime import timedelta
# from dateutil import parser
# import requests, json
from django import forms
from .models import SzpmApiOutstandingTransaction
from django.core.exceptions import ValidationError


class PaymentListForm(forms.ModelForm):
    receipt_date = DateField(widget=DatePickerInput(format='%d/%m/%Y').start_of('event active days'),
                               input_formats=('%d/%m/%Y',),
                               required=False)

    class Meta:
        model = SzpmApiOutstandingTransaction
        fields = ['section', 'receipt_date', 'title', 'receipt_amount', 'requested_amount', 'receipt_attachment', 'note']

    def __init__(self, *args, **kwargs):
        super(PaymentListForm, self).__init__(*args, **kwargs)
        self.user = kwargs.pop('user', None)

    def clean(self):
        receipt_amount = self.cleaned_data.get('receipt_amount', False)
        requested_amount = self.cleaned_data.get('requested_amount', False)
        if requested_amount > receipt_amount:
            raise ValidationError('Requested Amount cannot be greater then Receipt amount')
        attachment = self.cleaned_data.get('receipt_attachment', False)
        if attachment == None and receipt_amount>=50:
            raise ValidationError('Attachment Required for Receipts greater than €50')

# def get_token():
#     while True:
#         body = {
#             "username": settings.API_UNAME,
#             "password": settings.API_PW
#         }
#         headers = {'content-type': 'application/json'}
#
#         response = requests.post(f"{settings.API_LINK}/token/", headers=headers, data=json.dumps(body))
#         if response.status_code == 200:
#             j = json.loads(response.text)
#             return j['token'], j['token_create']
#             break
#
# def get_section():
#     token, token_created_date = get_token()
#     date = parser.parse(token_created_date)
#     while True:
#         if date > timezone.now() - timedelta(
#                 seconds=900):
#             headers = {'content-type': 'application/json', 'Authorization': f"Token {token}"}
#             response = requests.get(f"{settings.API_LINK}/section", headers=headers)
#             if response.status_code == 200:
#                 j = json.loads(response.text)
#                 break
#         else:
#             token, token_created_date = get_token()
#     for i in j:
#         del i['title']
#     return { d['id'] : d['short'] for d in j }
#
#
# SECTION_CHOICES = [(k, v) for k, v in get_section().items()]
#
# class PaymentListForm(forms.Form):
#     Section = forms.ChoiceField(choices=SECTION_CHOICES)
#     Receipt_Date = forms.DateField(widget=DatePickerInput(format="%Y-%m-%d").start_of('event active days'),
#                                input_formats=("%Y-%m-%d",),
#                                required=True)
#     Title = forms.CharField(max_length=50)
#     Receipt_Amount = forms.DecimalField(max_digits=8, decimal_places=2)
#     Request_Amount = forms.DecimalField(max_digits=8, decimal_places=2)
#     Receipt_Attachment = forms.FileField()
#     Note = forms.CharField(max_length=100, required=False)
#     # Post_Date = forms.DateTimeField(auto_now_add=True)
#     #
#
#     def __init__(self, *args, **kwargs):
#         super(PaymentListForm, self).__init__(*args, **kwargs)


