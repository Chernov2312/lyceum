from django.core import mail
from django.test import TestCase
from django.urls import reverse

__all__ = ['FeedbackEmailTest']


class FeedbackEmailTest(TestCase):
    def setUp(self):
        self.url = reverse('feedback:feedback')
        self.valid_data = {
            'name': 'Иван Петров',
            'mail': 'ivan@example.com',
            'text': 'Хочу купить абонемент',
        }

    def test_email_sent_successfully(self):
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.subject, self.valid_data['name'])
        self.assertEqual(email.body, self.valid_data['text'])
        self.assertIn(self.valid_data['mail'], email.to)
        self.assertEqual(response.status_code, 302)
