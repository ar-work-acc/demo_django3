from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from snippets.models import Snippet


class CreateAndListSnippetsTestCase(TestCase):
    def setUp(self) -> None:
        self.user_data = {
            'username': 'archvile',
            'email': 'meowfish.org@gmail.com',
            'password': 'pw20220618',
            'first_name': 'Louis',
            'last_name': 'Huang',
        }

        self.user = User.objects.create_superuser(**self.user_data)
        # self.client.login(**self.user_data)

    def test_list_snippets_after_creation(self):
        # initially, there should be no snippet:
        response = self.client.get(
            # note: the ending / matters
            '/snippets/',
        )
        data = response.json()
        self.assertEqual(data['count'], 0)

        # create 5 snippets, check API if you can see 5:
        for n in range(5):
            Snippet.objects.create(
                title=f'code title {n}',
                owner=self.user,
                code='console.log("Hi!")',
                language='javascript',
            )
        response = self.client.get(
            '/snippets/'
        )
        data = response.json()
        self.assertEqual(data['count'], 5)
