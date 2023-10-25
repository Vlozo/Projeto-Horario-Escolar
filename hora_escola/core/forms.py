from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Client
from .validators import validate_password, validate_fullname, validate_phone, only_numbers_validate

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
        validators = [validate_password],
        min_length = 8,
        widget=forms.PasswordInput(attrs={'placeholder':'Senha*', 'id':'password1'}))
    
    password2 = forms.CharField(
        validators = [validate_password],
        min_length = 8,
        widget = forms.PasswordInput(attrs={'placeholder':'Confirmar senha*', 'id':'password2'}))

    fullname = forms.CharField(
        validators = [validate_fullname],
        max_length = 50,
        required = False,
        widget = forms.TextInput(attrs={'placeholder':'Nome Completo*', 'id': 'fullname', 'class': 'hidden'}))

    type = forms.ChoiceField(
        choices = USER_TYPE_CHOICES,
        widget = forms.Select(attrs={'id': 'user_type'})
    )

    phone = forms.CharField(
        max_length = 14,
        required = False,
        validators = [validate_phone],
        widget = forms.TextInput(attrs={'placeholder': 'Telefone/Celular', 'id': 'phone'})
    )

    student_id = forms.CharField(
        max_length= 24,
        required = False,
        validators = [only_numbers_validate],
        widget = forms.TextInput(attrs={'placeholder':'Matrícula*', 'id':'id_number'}),
    )

    class Meta:
        model = Client
        fields = ['phone', 'student_id', 'type', 'birthdate', 'dependent']
        
        widgets = {'birthdate':forms.DateInput(attrs={'type':'date'})}
    
    def save(self, commit=True):
        fullname = self.cleaned_data['fullname']
        usertype = self.cleaned_data['type']
        student_id = self.cleaned_data['student_id']
        
        if fullname and usertype == 'responsavel':
            firstname, lastname = fullname.split(" ",1)
            user = User.objects.create_user(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password1'],
                email = self.cleaned_data['username'],
                first_name = firstname,
                last_name = lastname
            )
            dependent = Client.objects.get(type = 'aluno', student_id = student_id)
            user_dependent = dependent.user
            client = super(RegistrationForm, self).save(commit=False)
            client.user = user
            
            if commit:
                client.save()
                client.dependent.add(user_dependent)
            return client
        else:
            save_user(self, commit=True)
    
    def clean(self):
        cleaned_data = super().clean()
        user_type = cleaned_data.get('type')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        email = cleaned_data.get('username')
        
        if User.objects.filter(username = email).exists():
            raise ValidationError('O email inserido já está sendo utilizado.')
        
        if password2 != password1:
            raise ValidationError("As senhas inseridas devem ser compatíveis")
        
        if user_type == 'aluno' or user_type == 'responsavel':
            student_id = cleaned_data.get('student_id')
            if not student_id:
                raise ValidationError("O número de matrícula é obrigatório para alunos e responsáveis.")
            
        if user_type == 'responsavel':
            fullname = cleaned_data.get('fullname')
            if not fullname:
                raise ValidationError("O nome completo é obrigatório para responsáveis")
            if not Client.objects.filter(type = 'aluno', student_id = student_id).exists():
                raise ValidationError("Não há nenhum aluno registrado com a matrícula endereçada.")
                
        if user_type == 'aluno':
            if Client.objects.filter(type = 'aluno', student_id = student_id).exists():
                raise forms.ValidationError('O registro referente a matrícula endereçada já está sendo utilizado.')


def save_user(self, commit = True):
    user = User.objects.create_user(
        username=self.cleaned_data['username'],
        password=self.cleaned_data['password1'],
        email = self.cleaned_data['username'],
    )
    client = super(RegistrationForm, self).save(commit=False)
    client.user = user
    if commit:
        client.save()
    return client


