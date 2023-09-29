from users.models import User
from notes.models import Note
from taggit.models import Tag
from rest_framework.test import APITestCase


URL = "http://127.0.0.1:8000/api/note"

class NoteCreationTestCase(APITestCase):
    def setUp(self):
        # Create test user accounts
        self.user1 = User.objects.create_user(
            first_name = 'usertest1', 
            last_name = 'usertest1', 
            email = 'testuser1@oal.com',
            username='user1', 
            password='password1'
        )
        self.user2 = User.objects.create_user(
            first_name = 'usertest2', 
            last_name = 'usertest2', 
            email = 'testuser2@oal.com',
            username='user2', 
            password='password2'
        )

        # Create test tags
        self.tag1 = Tag.objects.create(name='tag1')
        self.tag2 = Tag.objects.create(name='tag2')

    def test_create_note_with_tags(self):
        # Log in as user1
        self.client.login(email='testuser1@oal.com', password='password1')

        # Create a note with tags
        response = self.client.post(URL + '/lists-create/', {
            'title': 'Test Note',
            'body': 'This is a test note.',
            'tags': [self.tag1.id, self.tag2.id],  # Use tag IDs
        })


        self.assertEqual(response.status_code, 200) 
        self.assertTrue(Note.objects.filter(title='Test Note').exists())

    def test_edit_own_note(self):
        # Create a note owned by user1
        note = Note.objects.create(title='User1 Note', body='This note belongs to user1', user=self.user1)
        note.tags.set([self.tag1])

        # Log in as user1
        self.client.login(username='user1', password='password1')

        # Edit user1's own note
        response = self.client.post(URL + f'/note/{note.id}/', {
            'title': 'Updated Note',
            'body': 'This is an update by user1.',
            'tags': [self.tag2.id],  # Use a different tag
        })

        # Check if the edit was successful
        self.assertEqual(response.status_code, 200) 
        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated Note')
        self.assertEqual(note.body, 'This is an update by user1.')
        self.assertTrue(self.tag2 in note.tags.all())

    def test_edit_other_users_note(self):
        # Create a note owned by user1
        note = Note.objects.create(title='User1 Note', body='This note belongs to user1', user=self.user1)
        note.tags.set([self.tag1])

        # Log in as user2
        self.client.login(email='testuser2@oal.com', password='password2')

        # Attempt to edit user1's note
        response = self.client.post(URL + f'/edit-note/{note.id}/', {
            'title': 'Updated Note',
            'body': 'This is an update by user2.',
            'tags': [self.tag2.id],  # Use a different tag
        })

        # Check if the edit request is denied due to object-level permissions
        self.assertEqual(response.status_code, 403) 

    def test_delete_own_note(self):
        # Create a note owned by user1
        note = Note.objects.create(title='User1 Note', body='This note belongs to user1', user=self.user1)
        note.tags.set([self.tag1])

        # Log in as user1
        self.client.login(email='testuser1@oal.com', password='password1')

        # Delete user1's own note
        response = self.client.post(URL + f'/delete-note/{note.id}/')

        # Check if the note was deleted successfully
        self.assertEqual(response.status_code, 200) 
        self.assertFalse(Note.objects.filter(title='User1 Note').exists())

    def test_delete_other_users_note(self):
        # Create a note owned by user1
        note = Note.objects.create(title='User1 Note', body='This note belongs to user1', user=self.user1)
        note.tags.set([self.tag1])

        # Log in as user2
        self.client.login(email='testuser2@oal.com', password='password2')

        # Attempt to delete user1's note
        response = self.client.post(URL + f'/delete-note/{note.id}/')

        # Check if the delete request is denied due to object-level permissions
        self.assertEqual(response.status_code, 403) 
