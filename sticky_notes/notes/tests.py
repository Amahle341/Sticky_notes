from django.test import TestCase
from .forms import NoteForm
from .models import Notes
from django.urls import reverse

# Create your tests here.


# Testing for Models
class NotesModelTest(TestCase):
    def test_create_note(self):
        note = Notes.objects.create(title="Test", text="Content")
        self.assertEqual(note.title, "Test")
        self.assertIn("Content", note.text)
        self.assertIsNotNone(note.pk)


# Testing for Forms
class NotesFormTest(TestCase):
    def test_valid_form(self):
        data = {'title': 'T', 'text': 'something'}
        form = NoteForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = NoteForm(data={'title': ''})
        self.assertFalse(form.is_valid())


# Testing for Views
class NotesViewsTest(TestCase):
    def setUp(self):
        self.note = Notes.objects.create(title="V", text="vvv")

    def test_notes_list_view(self):
        url = reverse('notes.list')  # ensure this name matches your urls
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.note.title)

    def test_notes_detail_view(self):
        url = reverse('notes.detail', kwargs={'pk': self.note.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.note.text)

    def test_create_view_redirects(self):
        url = reverse('notes.new')
        resp = self.client.post(
            url, {'title': 'new', 'text': 'hi'}, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'new')