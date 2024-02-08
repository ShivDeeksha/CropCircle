from django import forms
from django.core.exceptions import ValidationError
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken.")
        return username

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return confirm_password

    def clean(self):
        cleaned_data = super().clean()

        # Implement your custom validation logic here
        user_type = cleaned_data.get('user_type')
        adharcard = cleaned_data.get('adharcard')
        document = cleaned_data.get('document')
        merchant_license = cleaned_data.get('merchant_license')
        driving_license = cleaned_data.get('driving_license')

        if user_type not in ['customer', 'cropexpert','cropbankowner'] and not (adharcard or document or merchant_license or driving_license):
            raise forms.ValidationError("At least one document is required for verification.")

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)