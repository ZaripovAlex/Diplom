from django import forms

from .models import User


# class RegForm(forms.Form):
#     username = forms.CharField(
#         max_length=50, label="Username", widget=forms.TextInput(
#             attrs={'class': 'form_user_registration_not_necessary',}))
#     first_name = forms.CharField(
#         required=False, min_length=1, max_length=50, label='firstname', widget=forms.TextInput(
#             attrs={'class': 'form_user_registration_not_necessary',}))
#     last_name = forms.CharField(
#         required=False, min_length=1, max_length=50, label='Lastname', widget=forms.TextInput(
#             attrs={'class': 'form_user_registration_not_necessary',}))
#
#     email = forms.EmailField(
#         required=True, label='email', widget=forms.EmailInput(
#             attrs={'class': 'form_user_registration_necessary'}),
#     )
#     password1 = forms.CharField(
#         required=True, label="Password", widget=forms.PasswordInput(attrs={'class': 'form_user_registration_necessary',}))
#     password2 = forms.CharField(required=True, label="Confirm password", widget=forms.PasswordInput(
#         attrs={'class': 'form_user_registration_necessary'}))
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         user = User.objects.filter(email=email).first()
#         if user:
#             raise ValueError('Пользователь с таким адресом существует!')
#         else:
#             return email
#
#     def clean_password(self):
#         pas1 = self.cleaned_data.get('password1')
#         pas2 = self.cleaned_data.get('password2')
#         if pas1 != pas2:
#             raise ValueError('Пароли не совпадают!')
#         else:
#             return pas2
#
#     class Meta:
#         Model = User
#         fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class RegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password',]


class UploadPhotoForm(forms.Form):
    image = forms.ImageField(required=False,
                             widget=forms.FileInput(attrs={'class': 'form_user_personal_account_upload_user_photo'}))


class Authorization(forms.Form):
    email = \
        forms.EmailField(required=True, label='Электронная почта', widget=forms.EmailInput(
            attrs={'class': 'form_user_log_in_personal_account', 'placeholder': 'Адрес электронной почты'}))
    password = forms.CharField(required=True, label="Пароль", widget=forms.PasswordInput(
        attrs={'class': 'form_user_log_in_personal_account', 'placeholder': 'Пароль'}))


class LoginUserForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
