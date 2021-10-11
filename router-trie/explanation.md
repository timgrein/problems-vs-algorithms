### Design Choices

The basic design was already provided by the starter code. For this problem you use a RouteTrie and a RouteTrieNode.
The RouteTrieNode contains a handler and children routes.

### Time Complexity

- RouteTrieNode:
  - insert:
    - time complexity: O(1) (could also be O(n) in the worst case due to collisions, but this is very unlikely)
    - space complexity: O(1)
  - find:
    - time complexity: O(m * n), where m is the depth of the route and n is the of the part of the route
    - space complexity: O(1)
- Router:
  - add_handler:
    - time complexity: O(n)
    - space complexity: O(n)
  - lookup (= find of RouteTrie)
  - split_path:
    - time complexity: O(n), where n is the length of the path
    - space complexity: O(n), where n is the length of the path