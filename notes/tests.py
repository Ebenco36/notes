from users.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Note

class NoteAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # Create a sample note for the test user
        self.note = Note.objects.create(
            owner=self.user,
            title='Test Note',
            content='This is a test note'
        )

        # Obtain a JWT token for authentication
        response = self.client.post(
            reverse('token_obtain_pair'),
            {'username': 'testuser', 'password': 'testpassword'},
            format='json'
        )
        self.token = response.data['access']

        # Set the Authorization header for future requests
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_note(self):
        url = reverse('note-list-create')
        data = {'title': 'New Note', 'content': 'This is a new note'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 2)  # Check that the note was created

    def test_retrieve_note(self):
        url = reverse('note-retrieve-update-destroy', args=[self.note.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Note')

    def test_update_note(self):
        url = reverse('note-retrieve-update-destroy', args=[self.note.id])
        data = {'title': 'Updated Note', 'content': 'This is an updated note'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.note.refresh_from_db()  # Refresh the object from the database
        self.assertEqual(self.note.title, 'Updated Note')

    def test_delete_note(self):
        url = reverse('note-retrieve-update-destroy', args=[self.note.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Note.objects.count(), 0)  # Check that the note was deleted
