import unittest
from unittest import TestCase

from ..forms import RegisterForm


# to run -> python manage.py test shop.tests.test_register_form


class TestRegisterForm(TestCase):
    def test_valid_form(self):
        form = RegisterForm(data={"first_name": "Bob",
                                  "last_name": "Big",
                                  "username": "BigBob123",
                                  "email": "bigbob123@gmail.com",
                                  "password1": "ytrewq4321",
                                  "password2": "ytrewq4321"})
        self.assertTrue(form.is_valid())

    def test_invalid_email(self):
        form = RegisterForm(data={"first_name": "Bob",
                                  "last_name": "Big",
                                  "username": "BigBob123",
                                  "email": "12334",
                                  "password1": "ytrewq4321",
                                  "password2": "ytrewq4321"})
        self.assertEqual(
            form.errors["email"], ["Введите правильный адрес электронной почты."]
        )

    def test_invalid_email_is_too_long(self):
        form = RegisterForm(data={"first_name": "Bob",
                                  "last_name": "Big",
                                  "username": "BigBob123",
                                  "email": "1233444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444",
                                  "password1": "ytrewq4321",
                                  "password2": "ytrewq4321"})
        self.assertFalse(
            form.is_valid()
        )

    def test_passwords_do_not_match(self):
        form = RegisterForm(data={"first_name": "Bob",
                                  "last_name": "Big",
                                  "username": "BigBob123",
                                  "email": "bigbob123@gmail.com",
                                  "password1": "ytrewq4321",
                                  "password2": "ytrewq54321"})
        self.assertFalse(form.is_valid())

    def test_password_is_only_digits(self):
        form = RegisterForm(data={"first_name": "Bob",
                                  "last_name": "Big",
                                  "username": "BigBob123",
                                  "email": "bigbob123@gmail.com",
                                  "password1": "4321",
                                  "password2": "4321"})
        self.assertFalse(form.is_valid())

    def test_password_is_like_username(self):
        form = RegisterForm(data={"first_name": "Bob",
                                  "last_name": "Big",
                                  "username": "BigBob123",
                                  "email": "bigbob123@gmail.com",
                                  "password1": "BigBob12345",
                                  "password2": "BigBob12345"})
        self.assertFalse(form.is_valid())


if __name__ == '__main__':
    unittest.main()
