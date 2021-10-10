### Design Choices

I've also used the binary search algorithm for this problem (slightly changed, because the array is rotated and the start
and end indezes have to be set in another way in some special cases)

### Time Complexity

The time complexity is O (log n), because the binary search algorithm is used, which halves the problem with every iteration

### Space Complexity

The Space Complexity is O (log n), because every iteration has O(1) space complexity and we iterate log (n) times.