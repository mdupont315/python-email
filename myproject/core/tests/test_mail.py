from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class EmailTest(TestCase):

    def setUp(self):
        data = dict(
            name='Regis Santos',
            email='regis@example.com',
        )
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_email_sent(self):
        expect = 'Teste de envio de email'
        self.assertEqual(expect, self.email.subject)

    def test_no_email_sent(self):
        self.response = self.client.get(reverse('send'))
        self.assertEqual(len(mail.outbox), 0)

    def test_email_sent(self):
        self.response = self.client.get(
            reverse('send'),
            {'email': 'test@example.com'}
        )
        self.assertEqual(len(mail.outbox), 1)
        msg = 'This is a test message sent to regis@example.com.'
        self.assertEqual(mail.outbox[0].body, msg)

    def test_subscription_email_body(self):
        contents = [
            'Regis Santos',
            'regis@example.com',
            'lorem ipsum dollor',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
