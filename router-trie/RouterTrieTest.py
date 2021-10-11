import unittest

from RouterTrie import Router

class RouterTrieTest(unittest.TestCase):

    def setUp(self):
        self.router = Router("root handler", "not found handler")
        self.router.add_handler("/home/about", "about handler")

    def test_should_return_root_handler(self):
        handler = self.router.lookup("/")

        self.assertEqual("root handler", handler)

    def test_should_return_about_handler(self):
        handler = self.router.lookup("/home/about")

        self.assertEqual("about handler", handler)

    def test_should_return_about_handler_also_with_trailing_slash(self):
        handler = self.router.lookup("/home/about/")

        self.assertEqual("about handler", handler)

    def test_should_return_not_found_handler(self):
        handler_one = self.router.lookup("/home")
        handler_two = self.router.lookup("/home/about/me")

        self.assertEqual("not found handler", handler_one)
        self.assertEqual("not found handler", handler_two)

