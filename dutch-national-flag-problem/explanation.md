### Design Choices

There are only three different possible values in the array. So if we sort two of them, the third one has to be in the correct place.
In this case I sort the zeros to the beginning and the twos to the end.

### Time Complexity

The time complexity is O(n), since we only have to iterate once through the array.

### Space Complexity

The space complexity is O(1), since all operations (primarily swapping) is done inplace.