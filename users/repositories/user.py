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
        # getting the only data that we need from the dictionary.
        print(kwargs)
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
        # This can be implemented if we don't care.
        # I care.. 
        # if user:
        #     for key, value in kwargs.items():
        #         setattr(user, key, value)
        #     user.save()
        return user

    def delete_user(self, user_id):
        user = self.get_user_by_id(user_id)
        if user:
            user.delete()

    def get_all_users(self):
        return User.objects.all()
    

    def send_password_reset_email(self, email):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return False  # User with this email does not exist

        # Generate and save a reset token (you need to add a field for this in your model)
        reset_token = generate_reset_token()  # Implement your token generation logic
        user.reset_token = reset_token
        user.save()

        # Send the password reset email here, including the reset token

        return True  # Password reset email sent successfully
