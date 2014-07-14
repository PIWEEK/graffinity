from unittest import TestCase

import graffinity

class TestFoo(TestCase):
    def test_foo(self):
        s = graffinity.foo()
        self.assertTrue(isinstance(s, str))
