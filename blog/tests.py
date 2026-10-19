from django.test import TestCase
from django.urls import reverse

from blog.models import Post


class PostViewsTests(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title='Birinchi post', text='Salom dunyo')

    def test_list_page(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Birinchi post')

    def test_detail_page(self):
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        self.assertContains(response, 'Salom dunyo')

    def test_create_post(self):
        response = self.client.post(reverse('post_create'), {'title': 'Yangi', 'text': 'Matn'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title='Yangi').exists())

    def test_update_post(self):
        self.client.post(reverse('post_update', args=[self.post.pk]), {'title': "O'zgardi", 'text': 'Matn'})
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "O'zgardi")

    def test_delete_post(self):
        self.client.post(reverse('post_delete', args=[self.post.pk]))
        self.assertFalse(Post.objects.exists())
