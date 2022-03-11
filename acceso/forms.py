
from django import forms

from acceso.models import Usuario


class UsuarioForm(forms.ModelForm):

    confirmar_password = forms.CharField(label="Confirmar Contraseña", widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

        if cleaned_data.get('password') != cleaned_data.get('confirmar_password'):
            raise forms.ValidationError(
                    "Las contraseñas no coinciden"
                )

    class Meta:
        model = Usuario
        fields  = ['nombre','apellido','email','password']

        labels = {
            'nombre':'Nombre: ',
            'apellido':'Apellido: ',
            'email':'Correo: ',
            'password':'Contraseña: ',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'type':'email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
