from django.test import TestCase
from .models import Posts_db
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.


class Posts_dbTestCase(TestCase):
    def setUp(self):
        # Set up any initial data for your tests
        self.user = User.objects.create_user(
            username='harsh',
            password='Test@123',
            email='testuser@example.com'
        )
        Posts_db.objects.create(
            title='value1', content='value2', author=User.objects.get(username='harsh'))

    def test_field1_content(self):
        # Test specific functionality
        obj = Posts_db.objects.get(id=1)
        self.assertEqual(obj.title, 'value1')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/all_post/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('all_post'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/posts.html')
