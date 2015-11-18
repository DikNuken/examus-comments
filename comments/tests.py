# Create your tests here.

from comments.models import Comment
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase, APIClient


class CommentCreateTest(APITestCase):
    user = None

    def setUp(self):
        super().setUp()
        self.user = get_user_model().objects.create_user("test", 'test@test.ru', 'test')
        self.client.force_authenticate(user=self.user)

    def test_simple_comment_create(self):
        page_url = '/'
        text = 'text'

        response = self.client.post(reverse('comments'), {'page_url': page_url,
                                                          'text': text})
        self.assertEqual(response.status_code, 201)

        comment = Comment.objects.first()
        self.assertTrue(comment)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.page_url, page_url)
        self.assertEqual(comment.text, text)

    def test_reply_comment_create(self):
        page_url = '/'
        text = 'text'
        base_comment = Comment.objects.create(user=self.user, page_url=page_url, text=text)
        response = self.client.post(reverse('comments'), {'page_url': page_url,
                                                          'text': text, 'reply_to': base_comment.pk})
        self.assertEqual(response.status_code, 201)

        comment = Comment.objects.last()
        self.assertTrue(comment)
        self.assertEqual(comment.user, self.user)
        self.assertEqual(comment.page_url, page_url)
        self.assertEqual(comment.text, text)
        self.assertEqual(comment.reply_to, base_comment)

    def test_bad_reply_comment_create(self):
        page_url = '/'
        text = 'text'
        base_comment = Comment.objects.create(user=self.user, page_url=page_url, text=text)
        response = self.client.post(reverse('comments'), {'page_url': 'blog/',
                                                          'text': text, 'reply_to': base_comment.pk})
        self.assertEqual(response.status_code, 400)

    def test_comment_create_anonymous(self):
        page_url = '/'
        text = 'text'
        client = APIClient()
        response = client.post(reverse('comments'), {'page_url': page_url,
                                                     'text': text})
        self.assertEqual(response.status_code, 403)


class CommentsListTest(APITestCase):
    def setUp(self):
        super().setUp()
        self.user = get_user_model().objects.create_user("test", 'test@test.ru', 'test')
        page_url = '/'
        text = 'text'
        self.comment = Comment.objects.create(user=self.user, page_url=page_url, text=text)
        Comment.objects.create(user=self.user, page_url=page_url, text=text, reply_to=self.comment)
        Comment.objects.create(user=self.user, page_url=page_url, text=text, reply_to=self.comment, deleted=True)

    def test(self):
        response = self.client.get(reverse('comments', kwargs={'comment_pk': self.comment.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
