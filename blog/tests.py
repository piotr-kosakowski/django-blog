from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post2, Topic, Comment

class BlogViewsTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create some test data (replace this with your actual data creation logic)
        self.post = Post2.objects.create(title='Test Post', author=self.user)
        self.topic = Topic.objects.create(title='Test Topic', author=self.user)
        self.comment = Comment.objects.create(content='Test Comment', author=self.user, topic=self.topic)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your view logic

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your view logic

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your view logic

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # 302 is the HTTP status code for redirection
        # Add more assertions based on your view logic

    def test_new_post_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('new_post'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your view logic

    def test_new_topic_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('new_topic'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your view logic

    def test_topic_view(self):
        response = self.client.get(reverse('topic', args=[self.topic.id]))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your view logic

    def test_post_view(self):
        response = self.client.get(reverse('post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your view logic

    def test_like_post_view(self):
        response = self.client.get(reverse('like_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to login page
        # Add more assertions based on your view logic

    def test_check_like_post_view(self):
        response = self.client.get(reverse('check_like_post', args=[self.post.id]))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your view logic

    def test_all_posts_view(self):
        response = self.client.get(reverse('all_posts'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your view logic

    def test_all_topics_view(self):
        response = self.client.get(reverse('all_topics'))
        self.assertEqual(response.status_code, 200)
        # Add more assertions based on your view logic
