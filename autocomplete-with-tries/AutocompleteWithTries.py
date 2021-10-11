class TrieNode:
    def __init__(self):
        self.children = {}
        self.word_end = False

    def insert(self, character):
        if character not in self.children:
            self.children[character] = TrieNode()

    def suffixes(self, suffix=''):
        suffixes = []

        for key in self.children:
            if self.children[key].word_end:
                suffixes.append(suffix + key)
            suffixes += self.children[key].suffixes(suffix + key)

        return suffixes


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr_node = self.root

        for character in word:
            curr_node.insert(character)
            curr_node = curr_node.children[character]

        curr_node.word_end = True

    def find(self, prefix):
        current_node = self.root

        for character in prefix:
            if character in current_node.children:
                current_node = current_node.children[character]
            else:
                return None

        return current_node
