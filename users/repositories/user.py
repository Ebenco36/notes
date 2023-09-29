# user_management/repositories.py
from users.models import User
from users.utils.helpers import generate_reset_token
from django.core.exceptions import ValidationError

class UserRepository:
    def get_user_by_id(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def get_user_by_email(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    def create_user(self, **kwargs):
        try:
            username = kwargs['username']
            email = kwargs['email']
            password = kwargs['password']
        except KeyError:
            raise ValidationError("Email and password are required fields.")

        user = User.objects.create_user(
            email=email,
            username=username,
            password=password,
            first_name=kwargs.get('first_name', ''),
            last_name=kwargs.get('last_name', ''),
        )
        return user

    def update_user(self, user_id, email, first_name='', last_name=''):
        user = self.get_user_by_id(user_id)
        
        if user:
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        return user

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            user.delete()

    def get_all_users(self):
        return User.objects.all()