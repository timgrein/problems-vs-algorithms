import unittest

from AutocompleteWithTries import Trie


class AutocompelteWithTriesTest(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()

        word_list = [
            "ant", "anthology", "antagonist", "antonym",
            "fun", "function", "factory",
            "trie", "trigger", "trigonometry", "tripod"
        ]

        for word in word_list:
            self.trie.insert(word)

    def test_should_return_all_suffixes(self):
        suffixes = self.trie.find("").suffixes()

        self.assertEqual([
            'ant', 'anthology', 'antagonist',
            'antonym', 'fun', 'function',
            'factory', 'trie', 'trigger',
            'trigonometry', 'tripod'], suffixes)

    def test_should_return_suffixes_for_f(self):
        suffixes = self.trie.find("f").suffixes()

        self.assertEqual(['un', 'unction', 'actory'], suffixes)

    def test_edge_case_returning_nothing(self):
        suffixes = self.trie.find("tripod").suffixes()

        self.assertEqual([], suffixes)
