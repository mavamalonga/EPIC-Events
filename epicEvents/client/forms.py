from django import forms
from api.models import User


class ClientForm(forms.Form):

    first_name = forms.CharField(max_length=25)
    last_name = forms.CharField(max_length=25)
    email = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=20)
    mobile = forms.CharField(max_length=20)
    company_name = forms.CharField(max_length=250)
    sales_contact_id = forms.IntegerField()
    #authors = forms.ModelMultipleChoiceField(queryset=User.objects.all())