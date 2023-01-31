from django.test import TestCase
from django.contrib.auth.models import User

# to run -> python manage.py test shop.tests.test_client_model


class TestClientModel(TestCase):

    def setUp(self) -> None:
        user = User.objects.create_user(username='BigBob123',
                                        email='bigbob123@gmail.com',
                                        first_name='Bob',
                                        last_name='Big')
        self.first_name = 'Bob'
        self.last_name = 'Big'
        self.user_pw = 'ytrewq4321'
        user.set_password(self.user_pw)
        user.vk_link = "https://vk.com/bigbob"
        user.save()
        self.user = user

    def test_user_exists(self):
        user_count = User.objects.all().count()
        print(user_count)
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        user = User.objects.get(username=self.user.username)
        self.assertTrue(self.user.check_password('ytrewq4321'))

    def test_user_username(self):
        user = User.objects.get(username=self.user.username)
        self.assertEqual(user.username, 'BigBob123')

    def test_user_first_name(self):
        user = User.objects.get(username=self.user.username)
        self.assertEqual(user.first_name, self.first_name)

    def test_user_last_name(self):
        user = User.objects.get(username=self.user.username)
        self.assertEqual(user.last_name, self.last_name)

    def test_login_url(self):
        login_url = ''
        data = {"username": "BigBob123"}
        response = self.client.post(login_url, data, follow=True)
        # print(dir(response))
        redirect_path = response.request.get("PATH_INFO")
        self.assertEqual(redirect_path, "")

    def test_invalid_request(self):
        self.client.login(username=self.user.username,
                          password=self.user_pw)
        response = self.client.post("/products/create/", {"title": "this is invalid test"})
        self.assertTrue(response.status_code != 200)

    def tearDown(self) -> None:
        self.user.delete()
