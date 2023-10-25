from django.test import TestCase
from ..forms import RegistrationForm

class UserRegistrationTest(TestCase):
    def test_form_is_valid(self):
        form_data = {
            'username':'teste26@gmail.com', #EmailField
            'password1':'12345678Teste#', #CharField. PasswordInput, 8 digítos
            'password2':'12345678Teste#', #CharField, PasswordInput, 8 digítos
            'type': 'aluno', #Obrigatório, se chamado pela constante recebe dois valores e o teste retorna Falso
            'fullname':'Lee U',
            'phone':'(21)97943-6905',
            'student_id':'123456789'
        }
        form = RegistrationForm(form_data)
        self.assertTrue(form.is_valid())
    
    def test_email_invalid(self):
        form_data = {
            'username':'teste',
            'password1':'12345678Teste#',
            'password2':'12345678Teste#', 
            'type': 'aluno',
            'student_id':'123456789'
        }
        form = RegistrationForm(form_data)
        self.assertFalse(form.is_valid())
    
    def test_password_invalid(self):
        form_data = {
            'username':'teste26@gmail.com',
            'password1':'12345678',
            'password2':'12345678',
            'type': 'aluno',
            'student_id':'123456789'
        }
        form = RegistrationForm(form_data)
        self.assertFalse(form.is_valid())
    
    def test_fullname_invalid(self):
        form_data = {
            'username':'teste26@gmail.com',
            'password1':'12345678Teste#', 
            'password2':'12345678Teste#', 
            'type': 'aluno',
            'student_id':'123456789',
            'fullname':'Lee'
        }
        form = RegistrationForm(form_data)
        self.assertFalse(form.is_valid())

        # Nomes inválidos: "L33 U", "123 456", "Lee", "L$$ U", "Lee   "
    
    def test_phone_invalid(self):
        form_data = {
            'username':'teste26@gmail.com',
            'password1':'12345678Teste#', 
            'password2':'12345678Teste#', 
            'type': 'aluno',
            'student_id':'123456789',
            'phone': '(02)99744-3238' #Requer DDD válido no brasil
        }
        form = RegistrationForm(form_data)
        self.assertFalse(form.is_valid())

        # Telefones inválidos: "0000-0000", "2345","(21)12345-6789"
        # Observação: números como "212121-2121" passam pois estão dentro da formatação adequada
    
    def test_student_id(self):
        form_data = {
            'username':'teste26@gmail.com',
            'password1':'12345678Teste#', 
            'password2':'12345678Teste#', 
            'type': 'aluno',
            'student_id':'123matriculaaa' #inválido se tiver letras ou caracteres especias
        }
        form = RegistrationForm(form_data)
        self.assertFalse(form.is_valid())
    
    def test_student_type_invalid(self):
        form_data = {
            'username':'teste26@gmail.com',
            'password1':'12345678Teste#', 
            'password2':'12345678Teste#', 
            'type': 'aluno',
            # Não há matricula, então o formulário é inválido
        }
        form = RegistrationForm(form_data)
        self.assertFalse(form.is_valid())
    
    def test_responsable_type_invalid(self):
        form_data = {
            'username':'teste26@gmail.com',
            'password1':'12345678Teste#', 
            'password2':'12345678Teste#', 
            'type': 'responsavel',
            'fullname':'Mohammed Lee', #Campo obrigatório para responsáveis
            # Falta o campo de matricula, obrigatório para responsáveis logo o formulário é inválido
            # Para um responsável ser criado é necessário que já exista uma conta aluno com a matricula referente a que ele inserir como dependente.
        }

        form = RegistrationForm(form_data)
        self.assertFalse(form.is_valid())
    
    def test_password_are_different(self):
        form_data = {
            'username':'teste26@gmail.com',
            'password1':'12345678Teste#', 
            'password2':'Teste#12345678', 
            'type': 'aluno',
            'student_id':'123456789'
        }

        form = RegistrationForm(form_data)
        self.assertFalse(form.is_valid())

    


