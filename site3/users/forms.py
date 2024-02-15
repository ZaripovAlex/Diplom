from django import forms

from site3.users.models import User


class RegForm(forms.Form):
    first_name = forms.CharField(
            required=False, min_length=1, max_length=50, label='Имя', widget=forms.TextInput(
                attrs={'class': 'form_user_registration_not_necessary', 'placeholder': 'Введите Ваше имя'}))
    last_name = forms.CharField(
            required=False, min_length=1, max_length=50, label='Фамилия', widget=forms.TextInput(
                attrs={'class': 'form_user_registration_not_necessary', 'placeholder': 'Введите Вашу фамилию'}))

    email = forms.EmailField(
            required=True, label='Электронная почта', widget=forms.EmailInput(
            attrs={'class': 'form_user_registration_necessary', 'placeholder': 'Введите Вашу почту'}),
        )
    password1 = forms.CharField(
        required=True, label="Пароль", widget=forms.PasswordInput( attrs={'class': 'form_user_registration_necessary',
                   'placeholder': 'Пароль'}))
    password2 = forms.CharField(required=True, label="Подтверждение пароля", widget=forms.PasswordInput(
            attrs={'class': 'form_user_registration_necessary', 'placeholder': 'Подтверждение пароля'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            raise ValueError('Пользователь с таким адресом существует!')
        else:
            return email

    def clean_password(self):
        pas1 = self.cleaned_data.get('password1')
        pas2 = self.cleaned_data.get('password2')
        if pas1 != pas2:
            raise ValueError('Пароли не совпадают!')
        else:
            return pas2

    class Meta:
        Model = User
        fields = ['first_name','last_name','email','password1', 'password2']

class UploadPhotoForm(forms.Form):
    image = forms.ImageField(required=False,
                             widget=forms.FileInput(attrs={'class': 'form_user_personal_account_upload_user_photo'}))

class Authorization(forms.Form):
    email = \
        forms.EmailField(required=True, label='Электронная почта', widget=forms.EmailInput(
                attrs={'class': 'form_user_log_in_personal_account','placeholder': 'Адрес электронной почты'}))
    password = forms.CharField(required=True, label="Пароль", widget=forms.PasswordInput(
                attrs={'class': 'form_user_log_in_personal_account', 'placeholder': 'Пароль'}))

