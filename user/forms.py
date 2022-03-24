from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from .models import UserModel


class RegistrationForm(forms.ModelForm):
    first_name = forms.CharField(
        label="First Name",
        min_length=4,
        max_length=50,
        help_text="Required"
    )
    Last_name = forms.CharField(
        label="Last Name",
        min_length=0,
        max_length=50,
        help_text="Required"
    )
    email = forms.EmailField(
        label='Email',
        help_text="Required",
        error_messages={'required': 'Sorry, you will need an email'}
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Repeat Password",
        widget=forms.PasswordInput
    )
    is_tutor = forms.BooleanField(
        label="Are you a Tutor? "
    )

    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'email', 'phone', 'is_tutor')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Last Name'}
        )
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['phone'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': '9999999999'}
        )

        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})


class UserLoginForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.EmailInput(
        {'class': 'form-control mb-3', 'placeholder': 'abc@example.com', 'id': 'login-email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        {'class': 'form-control mb-3', 'placeholder': 'Password', 'id': 'login-pwd'}))


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    phone_number = forms.CharField(label='Phone Number', min_length=10, max_length=10, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': '9900990099', 'id': 'form-phone'}))



    class Meta:
        model = UserModel
        fields = ( 'email', 'phone_number',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True



class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = UserModel.objects.filter(email=email)
        if not user:
            raise forms.ValidationError('This email address is invalid!')
        return email


class UserPasswordConfirmForm(SetPasswordForm):
    newpassword1 = forms.CharField(widget=forms.PasswordInput(
        {'class': 'form-control mb-3', 'placeholder': 'Enter New Password', 'id': 'form-new-pwd1'}))
    newpassword2 = forms.CharField(widget=forms.PasswordInput(
        {'class': 'form-control mb-3', 'placeholder': 'Repeat Password', 'id': 'form-new-pwd2'}))