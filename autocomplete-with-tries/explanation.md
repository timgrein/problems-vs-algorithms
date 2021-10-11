### Design Choices

The basic design was already provided by the starter code. For this problem you use a Trie and a TrieNode.
The TrieNode contains the information, wether it's a word end. It also contains a dicitonary of children, which are also 
of type TrieNode.

### Time Complexity

- TrieNode:
  - insert:
    - time complexity: O(1) (could also be O(n) in the worst case due to collisions, but this is very unlikely)
    - space complexity: O(1)
  - suffixes:
    - time complexity: O(m * n), where m is the number of children per Node and n is the depth of the Trie tree
    - space complexity: O(m * n) where m is the length of a word and n the number of words in the trie tree
- Trie:
  - insert:
    - time complexity: O(n)
    - space complexity: O(n)
  - find:
    - time complexity: O(n), where n is the length of the prefix
    - space complexity: O(1)