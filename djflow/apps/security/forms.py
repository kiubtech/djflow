from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):

    email = forms.CharField(widget=forms.EmailInput(attrs=({'class': 'validate'})), required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False, attrs=({'class': 'validate'})), required=True)
    my_user = None  # Si se logea un usuario correctamente entonces se almacena aquí la sesión.

    def clean_password(self):
        from django.contrib.auth import authenticate
        try:
            user = User.objects.get(email=self.cleaned_data['email'])
        except:
            user = None
        if user:
            user_auth = authenticate(username=user.username, password=self.cleaned_data['password'])
        else:
            user_auth = None
        if user_auth is not None:
            if user.is_active:
                self.my_user = user_auth
                pass
            else:
                raise forms.ValidationError("Lo lamentamos, el usuario se encuentra deshabilitado")
        else:
            raise forms.ValidationError("Email y/o contraseña incorrecta")


class RecoverPasswordForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs=({'class': 'validate form-control',
                                                            'placeholder': 'ingresa tu mail'})),
                            required=True, label="")


class ChangePasswordForm(forms.Form):
    password_one = forms.CharField(widget=forms.PasswordInput(attrs=({'class': 'validate form-control',
                                                                      'placeholder': 'Nueva contraseña',
                                                                      'required': 'required'})),
                                   required=True, label="")
    password_two = forms.CharField(widget=forms.PasswordInput(attrs=({'class': 'validate form-control',
                                                                      'placeholder': 'Repite tu nueva contraseña',
                                                                      'required': 'required'})),
                                   required=True, label="")

    def clean_password_two(self):
        if self.cleaned_data['password_one'] == self.cleaned_data['password_two']:
            pass
        else:
            raise forms.ValidationError("Contraseñas no coinciden, intente de nuevo.")


class NewTokenForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs=({'class': 'validate form-control',
                                                            'placeholder': 'ingresa tu mail'})),
                            required=True, label="")


class RegisterForm(forms.Form):

    first_name = forms.CharField(widget=forms.TextInput(attrs=({'class': 'form-control',
                                                                 'placeholder': 'Nombre','required':'required','autofocus':'autofocus'})),
                                 required=True, label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs=({'class': 'form-control',
                                                                'placeholder': 'Apellido','required':'required'})),
                                required=True, label="")
    email = forms.EmailField(widget=forms.EmailInput(attrs=({'class': 'form-control', 'required': 'true',
                                                            'placeholder': 'Email','required':'required'})),
                             required=True, label="")
    password_one = forms.CharField(widget=forms.PasswordInput(render_value=False,
                                                              attrs=({'class': 'form-control',
                                                                      'placeholder': 'Contraseña','required':'required'})),
                                   required=True, label="")
    password_two = forms.CharField(widget=forms.PasswordInput(render_value=False,
                                                              attrs=({'class': 'form-control',
                                                                      'placeholder': 'Repite de nuevo tu contraseña ','required':'required'})),
                                   required=True, label="")

    def clean_email(self):
        try:
            User.objects.get(email=self.cleaned_data['email'])
            raise forms.ValidationError("Este email ya se encuentra registrado, ¿has perdido tu contraseña?")
        except User.DoesNotExist:
            return self.cleaned_data['email']

    def clean_password_two(self):
        if self.cleaned_data['password_one'] == self.cleaned_data['password_two']:
            pass
        else:
            raise forms.ValidationError("Password no coincide, intente de nuevo")

