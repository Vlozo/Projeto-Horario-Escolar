from django import forms
from .models import Client
from django.forms.widgets import NumberInput
from django.contrib.auth.models import User



USER_TYPE_CHOICES = [
    ('aluno', 'Aluno(a)'),
    ('professor', 'Professor(a)'),
    ('responsavel', 'Responsável'),
]

class RegistrationForm(forms.ModelForm):

    username = forms.EmailField(
        max_length = 60,
        widget = forms.EmailInput(attrs={'placeholder':'Email*', 'id':'email'}))
    
    password1 = forms.CharField(
        min_length= 8,
        widget=forms.PasswordInput(attrs={'placeholder':'Senha*', 'id':'password1'}))
    
    password2 = forms.CharField(
        min_length= 8,
        widget = forms.PasswordInput(attrs={'placeholder':'Confirmar senha*', 'id':'password2'}))

    fullname = forms.CharField(
        max_length = 45,
        min_length = 8,
        required = False,
        widget = forms.TextInput(attrs={'placeholder':'Nome Completo*', 'id': 'fullname', 'class': 'hidden'}))

    type = forms.ChoiceField(
        choices = USER_TYPE_CHOICES,
        widget = forms.Select(attrs={'id': 'user_type'})
    )

    class Meta:
        model = Client
        fields = ['phone', 'student_id', 'type', 'birthdate']
        widgets = {
            'phone':forms.TextInput(attrs={'placeholder':'Telefone/Celular', 'id':'phone'}),
            'student_id':forms.TextInput(attrs={'placeholder':'Matrícula*', 'id':'id_number'}),
            'birthdate':forms.NumberInput(attrs={'type':'date'})
        }
    
    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1']
        )
        client = super(RegistrationForm, self).save(commit=False)
        client.user = user
        if commit:
            client.save()
        return client


#     def clean(self):
#         cleaned_data = super().clean()
#         matricula = cleaned_data.get('matricula')
#         email = cleaned_data.get('email')
#         data_nascimento = cleaned_data.get('data_nascimento')
#         tipo_usuario = cleaned_data.get('tipo')
#
#         if tipo_usuario == 'aluno':
#             if not Aluno.objects.filter(matricula=matricula, data_nascimento = data_nascimento).exists():
#                 raise forms.ValidationError('O registro referente a matrícula não existe, é inválido ou já está sendo utilizado.')
#             if Usuario.objects.filter(matricula = matricula).exists():
#                 raise forms.ValidationError('O registro referente a matrícula não existe, é inválido ou já está sendo utilizado.')
#             if Usuario.objects.filter(email = email).exists():
#                 raise forms.ValidationError('O email inserido já está em uso.')
#
#         elif tipo_usuario == 'professor':
#             #Validar professor
#             pass
#         elif tipo_usuario == 'responsavel':
#             #Validar responsável
#             pass
#
#         return cleaned_data


