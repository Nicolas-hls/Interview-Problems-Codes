# Arrays - Duplicate Check

![Difficulty: Easy](https://img.shields.io/badge/Difficulty-Easy-brightgreen?style=for-the-badge)

**Companies:** `Google` `Amazon` `Meta` `Microsoft` `Bloomberg` `TCS` `Netflix` `IBM` `Visa`  

## Problem Statement 📃

Write a function that takes a list of integers and returns **True** if there is at least one duplicate number in the list.  
Return **False** if all elements are unique.

## Exemple :

### **First scenario :**  

**Input:** `nums = [1, 2, 3, 3]`  
**Output:** `True`  
**Explanation:** The number 1 appears twice.

### Second scenario :
**Input:** `nums = [1, 2, 3, 4]`  
**Output:** `False`  
**Explanation:** All numbers are unique.

### Third scenario :  
**Input:** `nums = [1, 2, 2, 1, 8, 9, 6, 7, 1]`  
**Output:** `True`  
**Explanation:** Multiple numbers appear more than once.

## Solutions :  
# Solution1 :  
```Python
class Solution1:
```
- This line defines a **class** called `Solution1`
- In Python, classes are often used to group related methods (functions) together.

  
```Python
 def duplicate_check(self, nums: List[int]) -> bool:
```
- This defines a **method** of the class called `duplicate_check`.
- It takes two parameters:  
  1. `self`: a reference to the instance of the class (required in Python class methods).  
  2. `nums: List[int]`: a list of integers to check.
- `-> bool` indicates that the function **returns a boolean** (`True` or `False`).
```Python
return len(nums) != len(set(nums))
```
- `set(nums)` converts the list `nums` into a **set**:
  - A set cannot contain **duplicate elements**, so all duplicates are automatically removed.
- `len(nums)` gives the **number of elements in the original list**.
- `len(set(nums))` gives the **number of unique elements**.
- `!=` checks if these two lengths are **different**:
  - If the lengths differ → there are duplicates → return `True`.
  - Otherwise → no duplicates → return `False`.

**Execution Stats**  
| Metric  | Value                |
|:-------|:-------------------:|
| Runtime | 5 ms | Beats 95.13%   |
| Memory  | 31.55 MB | Beats 53.78%  |
# Solution2 :
```Python
class Solution2:
    def duplicate_check(self, nums: List[int]) -> bool:
```
Defines another class called Solution2.
Same function signature as Solution 1.
```Python
return len(nums) > len(set(nums))
```
- Here, `>` is used instead of `!=`.
- Logic:
  - If the length of the original list is **greater** than the length of the set → there must be duplicates.
  - Otherwise → no duplicates.
**Note:** Both solutions do exactly the same thing. This is just a slightly different way to write the condition.
**Execution Stats**
| Metric  | Value                |
|:-------|:-------------------:|
| Runtime | 14 ms | Beats 58.45%   |
| Memory  | 31.57 MB | Beats 53.78%  |

# Simple summary:
- `set()` → removes duplicates.
- `len(nums) != len(set(nums))` or `len(nums) > len(set(nums))` → checks if the list contains duplicates.
- Solution 1 is more “generic” (`!=`), Solution 2 is more “intuitive” (`>`).
