# Arrays - Missing Number

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)

**Companies:** `Amazon` `Microsoft` `Google` `Microsoft` `Meta` `Bloomberg` `Netflix` `Nvidia` `Goldman Sachs` `Arista Networks` `IBM`  	

## Problem Statement 📃

Write an algorithm that finds the **missing number** in an array containing `n` distinct integers taken from the range **0 to n**.

Example:  
If `nums = [4,0,3,1]`, the full range is `0, 1, 2, 3`, and the missing number is `2`.

## Theory Behind the Solution

Instead of searching for the missing value one by one, we use a mathematical property:  

**The sum of the first n integers (from 0 to n) is:**    
$$total=\frac{n(n+1)}{2}$$
This is the sum you would expect if no number was missing.  

Then:  
- Compute **the expected total sum**
- Compute the **actual sum** of the numbers in the array
- The difference between the two is the missing number
Exemple :
```Python
nums = [3, 0, 1]
n = 3

Expected sum = 0 + 1 + 2 + 3 = 6
Actual sum   = 3 + 0 + 1     = 4

Missing number = 6 - 4 = 2
```
This works because all numbers appear exactly once, except the missing one — so subtracting the sums isolates it.

## Technical Explanation of the Code
```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)
```
`n = len(nums)`

Gets the number of elements in the list.
If `nums` has 3 elements, we know the full range is from `0` to `3`.

`total = n * (n + 1) // 2`  
Computes the **expected** sum of the numbers `0` through `n`.  
We use `//` because it performs **integer division**, which is perfect for a sum of whole numbers.  
  

`sum(nums)`  

This built-in Python function returns the **actual** sum of the numbers present in the array.  

For example:
```Pyhton
sum([3, 0, 1]) == 4
```
`return total - sum(nums)`  
Subtracts the actual sum from the expected sum.  
The result is the **only number missing** from the array.

