from rest_framework.test import APITestCase
from users.models import User

URL = "http://127.0.0.1:8000/api/auth"
class LoginTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name = 'ebenezertestuser', 
            last_name = 'olatestuser', 
            email = 'testuser@oal.com',
            username = 'testuser', 
            password = 'testpassword'
        )

    def test_login_valid_user(self):
        response = self.client.post(URL+"/login/", {
            'email': 'testuser@oal.com', 
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200) 

    def test_login_invalid_user(self):
        response = self.client.post(URL+'/login/', {
            'username': 'invaliduser', 
            'password': 'invalidpassword'
        })
        self.assertEqual(response.status_code, 401)



class RegisterTestCase(APITestCase):
    def test_register_valid_user(self):
        response = self.client.post(URL+'/register/', {
            'first_name': 'ebenezertestuser', 
            'last_name': 'olatestuser', 
            'email': 'testuser@oal.com',
            'username': 'testuser', 
            'password': 'testpassword',
            'confirm_password': 'testpassword'
        })
        
        self.assertEqual(response.status_code, 201)
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_invalid_user(self):
        # Test for duplicate username or other validation errors
        response = self.client.post(URL+'/register/', {
            'username': 'testuser', 
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 400) 


class LogoutTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            first_name = 'ebenezertestuser', 
            last_name = 'olatestuser', 
            email = 'testuser@oal.com',
            username = 'testuser', 
            password = 'testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_logout_user(self):
        # logout without auth token should fail
        response = self.client.post(URL+'/logout/')
        self.assertEqual(response.status_code, 401)
