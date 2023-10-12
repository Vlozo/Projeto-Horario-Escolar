from django import forms
from .models import Usuario, Aluno
from django.forms.widgets import NumberInput


USER_TYPE_CHOICES = [
    ('aluno', 'Aluno(a)'),
    ('professor', 'Professor(a)'),
    ('responsavel', 'Responsável'),
]

class CadastroForm(forms.ModelForm):

    nome = forms.CharField(
        max_length = 45, 
        min_length = 8, 
        required= False, 
        widget=forms.TextInput(attrs={'placeholder':'Nome Completo*', 'id': 'nome', 'class': 'hidden'}))
    
    tipo = forms.ChoiceField(
        choices = USER_TYPE_CHOICES, 
        widget=forms.Select(attrs={'id': 'select_id'}))
    
    confirmar_senha = forms.CharField(
        min_length= 8,
        widget = forms.PasswordInput(attrs={'placeholder':'Confirmar senha*', 'id':'confirmar_senha'}))
    
    class Meta:
        model = Usuario
        fields = ['matricula', 'data_nascimento', 'email', 'telefone', 'senha']
        widgets = {
            'matricula':forms.TextInput(attrs={'placeholder':'Matrícula*', 'id':'matricula'}),
            'data_nascimento':NumberInput(attrs={'type': 'date'}),
            'email':forms.EmailInput(attrs={'placeholder':'Email*', 'id':'email'}),
            'telefone':forms.TextInput(attrs={'placeholder':'Telefone/Celular', 'id':'telefone'}),
            'senha':forms.PasswordInput(attrs={'placeholder':'Senha*', 'id':'senha'})
        }
    
    
    def clean(self):
        cleaned_data = super().clean()
        matricula = cleaned_data.get('matricula')
        email = cleaned_data.get('email')
        data_nascimento = cleaned_data.get('data_nascimento')
        tipo_usuario = cleaned_data.get('tipo')

        if tipo_usuario == 'aluno':
            if not Aluno.objects.filter(matricula=matricula, data_nascimento = data_nascimento).exists():
                raise forms.ValidationError('O registro referente a matrícula não existe, é inválido ou já está sendo utilizado.')
            if Usuario.objects.filter(matricula = matricula).exists():
                raise forms.ValidationError('O registro referente a matrícula não existe, é inválido ou já está sendo utilizado.')
            if Usuario.objects.filter(email = email).exists():
                raise forms.ValidationError('O email inserido já está em uso.')

        elif tipo_usuario == 'professor':
            #Validar professor
            pass
        elif tipo_usuario == 'responsavel':
            #Validar responsável
            pass
        
        return cleaned_data


