from django.test import TestCase
from django.urls import reverse


class EmailSentViewTests(TestCase):
    def test_email_sent_page_renders(self):
        response = self.client.get(reverse('email-sent'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Message envoyé')
