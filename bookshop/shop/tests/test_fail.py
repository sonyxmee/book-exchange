import unittest
from unittest import TestCase

from ..forms import RegisterForm


# to run -> python manage.py test shop.tests.test_fail


class TestRegisterForm(TestCase):
    def test_invalid_email_is_too_long(self):
        form = RegisterForm(data={"first_name": "Bob",
                                  "last_name": "Big",
                                  "username": "BigBob123",
                                  "email": "1233444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444",
                                  "password1": "ytrewq4321",
                                  "password2": "ytrewq4321"})
        self.assertTrue(
            form.is_valid()
        )