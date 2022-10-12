## What is Big O

- A way to categorize your algorithm's time or memory requirements
- Not meant to be an exact measurement
- Will not tell you how many CPU cycles it takes
- Meant to generalize the growth of your algorithm

Example

- O(N): Your algorithm will grow linearly based on input

### Why Do We Use It?

- To make decisions about what data structures and algorithms to use
- Knowing how they perform can greatly help create the best possible program out there

### Important Concepts

- Growth is with respect to the input
- Constants are dropped
  - O(2N) becomes O(N)
  - Big O is meant to describe the upper bound of the algorithm(the growth of the algorithm)
  - The constant eventually becomes irrelevant

Example
- N = 1: O(10N) = 10, O(N^2) = 1
- N = 5: O(10N) = 50, O(N^2) = 25
- N = 100: O(10N) = 1,000, O(N^2) = 10,000 // 10x bigger
- N = 1000: O(10N) = 10,000, O(N^2) = 1,000,000 // 100x bigger
- N = 10000: O(10N) = 100,000, O(N^2) = 100,000,000 // 1000x bigger