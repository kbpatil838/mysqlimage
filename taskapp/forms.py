from django import forms
from django.forms.widgets import RadioSelect
from django.contrib.auth import get_user_model
from taskapp import models
from .models import Employee

User = get_user_model()

# STATUS_CHOICES = [
#     ('Enable','ENABLE'),
#     ('Disable','DISABLE'),
# ]


class EmpForm(forms.ModelForm):
    # status = forms.ChoiceField(choices=STATUS_CHOICES,
    #                            widget=forms.RadioSelect)
    class Meta:
        model = Employee
        fields = "__all__"

    # def clean_email(self):
    #     mail = self.cleaned_data
    #     email = mail['email']
    #
    #     # object is exists and email is not modified, so don't start validation flow
    #     if self.instance.pk is not None and self.instance.email == email:
    #         return mail
    #
    #     # check email is unique or not
    #     if User.objects.filter(email=email).exists():
    #         raise forms.ValidationError("Email address {} already exists!".format(value))
    #     return mail

    # empname = forms.CharField(
    #     label='Employee Name',
    #     widget=forms.TextInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Employee Name'
    #         }
    #     )
    # )
    #
    # email = forms.EmailField(
    #     label='Email ID',
    #     widget=forms.EmailInput(
    #         attrs={
    #             'class': 'form-control',
    #             'placeholder': 'Email_ID'
    #         }
    #     )
    # )
    # STATUS_CHOICES = (
    #     ('Enable', 'Enable'),
    #     ('Disable', 'Disable')
    # )
    # status = forms.ChoiceField(
    #     widget=forms.RadioSelect(
    #     ), choices=STATUS_CHOICES)
    # GENDER = [
    #     ('Male', 'Male'),
    #     ('Female', 'Female')
    # ]
    # gender = forms.CharField(label='Gender', widget=forms.Select(choices=GENDER))
    #
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     qs = User.objects.filter(email=email)
    #     if qs.exists():
    #         raise forms.ValidationError("Email-ID Is Already Exists.")
    #     elif not '@gmail.com' in email:
    #         raise forms.ValidationError("Email has to be @gmail.com")
    #     return email
    #
    # def clean_empname(self):
    #     empname = self.cleaned_data.get('empname')
    #     for character in empname:
    #         if not character.isalpha():
    #             raise forms.ValidationError("Employee Name should be Only letters!")
    #         else:
    #             return empname
    #
