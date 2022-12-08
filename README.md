# DSA-SHEET

-----Check if a pair exists with given sum in given array

Naive Approach :- Time complexity in worset case is o(n)2 and space is constant o(1)

Two Sum using Sorting and Two-Pointers technique:- O(N) for traversel and N(LogN) for sort function which we have used , sorting time can be decreased can bed done (LOGN)

Logic = The idea is to use the two-pointer technique. But for using the two-pointer technique, the array must be sorted. Once the array is sorted the two pointers can be taken which mark the beginning and end of the array respectively. If the sum is greater than the sum of those two elements, shift the right pointer to decrease the value of the required sum and if the sum is lesser than the required value, shift the left pointer to increase the value of the required sum.

Two Sum using Hashing :- The insert and pop take O(1) time complexity in hashmap and loop in the code takes O(n) . Total time complexity is O(n)and space complexity is also O(n)--> the values are taken dynaically at run time

This problem can be solved efficiently by using the technique of hashing. Use a hash_map to check for the current array value x(let), if there exists a value target_sum-x which on adding to the former gives target_sum. This can be done in constant time.

----Majority Element

Naive Approach:- It can be easily done by using concept of indexing like arr[a[i]]++ and you will get the frequency of each element . this method takes O(N) time and space depends on the size of the array of which we are creating frequency 
or can this can be also and approach 
The basic solution is to have two loops and keep track of the maximum count for all different elements. If the maximum count becomes greater than n/2 then break the loops and return the element having the maximum count. If the maximum count doesn’t become more than n/2 then the majority element doesn’t exist.

 Moore’s Voting Algorithm:- I didnt had a good understanding but it insure to return the maximum repeated element in O(n) time complexity.
 
 Hashing :- n Hashtable(key-value pair), at value, maintain a count for each element(key), and whenever the count is greater than half of the array length, return that key(majority element). Time complexity is O(n).
