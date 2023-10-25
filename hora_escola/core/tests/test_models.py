
from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Client, USER_TYPE_CHOICES

class UserCreationTest(TestCase):

    def test_create_user(self):
        user = User.objects.create_user(username="teste@gmail.com", 
                                        password="2345678senha",
                                        email="teste@gmail.com",
                                        first_name="Fulano",
                                        last_name="de Tal")
        
        self.assertEqual(user.email, "teste@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_client(self):
        user = User.objects.create_user(username="teste@gmail.com", 
                                        password="2345678senha",
                                        email="teste@gmail.com",
                                        first_name="Fulano",
                                        last_name="de Tal")
        
        profile = Client(user=user, phone='21969372663', type=USER_TYPE_CHOICES[(0)])
        self.assertEqual(profile.user.email, "teste@gmail.com")
        self.assertNotEqual(profile.user, user.username)
        #True porque a variavel herda o object User e não somente um atributo.
        self.assertEqual(profile.type, ('aluno', 'Aluno(a)'))
        