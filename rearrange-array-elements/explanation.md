### Design Choices

I've created an array, which holds the frequencies of the numbers occuring in the input list. Then I loop through the
array starting from the greatest element and create the two numbers alternating.

### Time Complexity

The time complexity is O(n), since I loop through the input list array one time (creating the frequency list). The iteration 
through the frequency array is O(1) (at most ten elements, constant upper bound). Per iteration we loop make at most n iterations.

### Space Complexity

Space Complexity is constant:
- one array of size 10
- 2 tuple to return
