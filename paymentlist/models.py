# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
import uuid
import os
from datetime import datetime
from django.contrib.auth.models import User

def transaction_image_file_path(instance, filename):
    """ Generate file path for new image """
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    currentYear = datetime.now().year
    return os.path.join(f'financial_transactions/{currentYear}/', filename)


class FinancerecordsAccountinggrouping(models.Model):
    title = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=150)
    donation_group = models.BooleanField(db_column='Donation_Group')  # Field name made lowercase.
    hide_field = models.BooleanField(db_column='Hide_field')  # Field name made lowercase.
    membership_group = models.BooleanField(db_column='Membership_Group')  # Field name made lowercase.
    merchandise_group = models.BooleanField(db_column='Merchandise_Group')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'financerecords_accountinggrouping'


class FinancerecordsNormalfestagrouping(models.Model):
    title = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=150)
    section = models.ForeignKey('HomepageSection', models.DO_NOTHING)
    donation_group = models.BooleanField(db_column='Donation_Group')  # Field name made lowercase.
    hide_field = models.BooleanField(db_column='Hide_field')  # Field name made lowercase.
    membership_group = models.BooleanField(db_column='Membership_Group')  # Field name made lowercase.
    merchandise_group = models.BooleanField(db_column='Merchandise_Group')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'financerecords_normalfestagrouping'


class FinancerecordsNormalfestayear(models.Model):
    title = models.CharField(unique=True, max_length=50)
    description = models.CharField(max_length=150)
    datefrom = models.DateField(db_column='dateFrom')  # Field name made lowercase.
    dateto = models.DateField(db_column='dateTo')  # Field name made lowercase.
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'financerecords_normalfestayear'


class HomepageSection(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    short = models.CharField(max_length=50)
    rimage = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'homepage_section'



class SzpmApiMobileUser(models.Model):
    fb_id = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.CharField(max_length=254, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    device_token = models.CharField(max_length=100)
    login_type = models.CharField(max_length=50)
    picture = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'szpm_api_mobile_user'


class SzpmApiOutstandingTransaction(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=50)
    note = models.CharField(max_length=100, blank=True, null=True)
    receipt_date = models.DateField()
    receipt_attachment = models.ImageField(upload_to =transaction_image_file_path,null=True, blank=True)
    receipt_amount = models.DecimalField(max_digits=8, decimal_places=2)
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateField(blank=True, null=True)
    section = models.ForeignKey(HomepageSection, models.DO_NOTHING)
    requested_amount = models.DecimalField(max_digits=8, decimal_places=2)
    account_group = models.ForeignKey(FinancerecordsAccountinggrouping, models.DO_NOTHING, blank=True, null=True)
    feast_group = models.ForeignKey(FinancerecordsNormalfestagrouping, models.DO_NOTHING, blank=True, null=True)
    feast_year = models.ForeignKey(FinancerecordsNormalfestayear, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'szpm_api_outstanding_transaction'
