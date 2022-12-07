# DSA-SHEET


Naive Approach :- Time complexity in worset case is o(n)2 and space is constant o(1)

Two Sum using Sorting and Two-Pointers technique:- O(N) for traversel and N(LogN) for sort function which we have used , sorting time can be decreased can bed done (LOGN)

Logic = The idea is to use the two-pointer technique. But for using the two-pointer technique, the array must be sorted. Once the array is sorted the two pointers can be taken which mark the beginning and end of the array respectively. If the sum is greater than the sum of those two elements, shift the right pointer to decrease the value of the required sum and if the sum is lesser than the required value, shift the left pointer to increase the value of the required sum.

Two Sum using Hashing :- The insert and pop take O(1) time complexity in hashmap and loop in the code takes O(n) . Total time complexity is O(n)and space complexity is also O(n)--> the values are taken dynaically at run time

This problem can be solved efficiently by using the technique of hashing. Use a hash_map to check for the current array value x(let), if there exists a value target_sum-x which on adding to the former gives target_sum. This can be done in constant time.
