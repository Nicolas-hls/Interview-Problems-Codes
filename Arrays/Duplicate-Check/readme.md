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
# Python - Solutions

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

#  C - Solution
The code implements a solution to check for the existence of duplicates in an array by using the **sorting method**.
### 1. The Comparison Function: `compare_ints`
```C
int compare_ints(const void *a, const void *b) {
    if (*(const int*)a < *(const int*)b) return -1;
    if (*(const int*)a > *(const int*)b) return 1;
    return 0;
}
```
This function is an **essential prerequisite** for using the standard C sorting function, `qsort`.
- **Role:** It tells `qsort` how to compare two elements of the array in order to sort them.
- **Parameters (`const void *a`, `const void b`)**: `qsort` is a generic function and doesn't know what data type it's sorting. It passes the addresses (pointers) of the two elements to be compared as **generic pointers** (`void *`).
- **The Cast (`*(const int*)a`):** To compare the values, you must tell the compiler that these generic pointers actually point to integers (`int`).
  1. `(const int*)a` : Converts the generic pointer `a` into a constant integer pointer.
  2. `*(...) `: **Dereferences** the pointer to get the **integer value** stored at that address.
- **Return Values:** C has strict conventions for comparison functions:
  - **Negative (-1)**: If `a` should come **before** `b` (i.e., `a < b`).
  - **Zero (0):** If `a` and `b` are **equal**.
### 2. The Main Function: `containsDuplicate`
```C
bool containsDuplicate(int* nums, int numsSize) {
    if (numsSize <= 1) {
        return false;
    }
```
This function is the one that solves the problem.  
**Signateur and Arguments**
- `bool containsDuplicate(int* nums, int numsSize)`:
  - `bool`: Indicates that the function returns a boolean (`true` or `false`).
  - `int* nums`: A **pointer** to the first element of the integer array. This is how arrays are passed in C.
  - `int numsSize`: The size of the array. In C, arrays **do not know their own size**, so it must be passed separately.

### Step 1: Sorting  
```C
qsort(nums, numsSize, sizeof(int), compare_ints);
```
This is where the sorting happens.
- `qsort`: Standard C library function (from `stdlib.h`) for performing a quick sort ("Quicksort").
- `nums`: The array to be sorted (passed by its starting pointer).
- `numsSize`: The number of elements to sort.
- `sizeof(int)`: The size, in bytes, of a single element in the array (so `qsort` knows where the next element begins).
- `compare_ints`: The comparison function we defined previously.
**Result**: After this line, if the array was `[1, 2, 2, 1, 8]`, it becomes `[1, 1, 2, 2, 8]`. All duplicates are now **adjacent**.
### Step 2: Duplicate Detection  
```C
    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] == nums[i+1]) {
            return true;
        }
    }
    return false;
```
This is the fastest and simplest part of the code logic.
- `for (int i = 0; i < numsSize - 1; i++)`: The loop stops at `numsSize - 1` because in each iteration, it compares `nums[i]` with the next element, `nums[i+1]`. If it went up to `numsSize`, accessing `nums[i+1]` would go beyond the end of the array (a classic C error called **"buffer overflow"**).
- `if (nums[i] == nums[i+1]`): If two consecutive elements are equal, it means a duplicate has been found. The function **stops immediately** and returns `true`.
- `return false;`: If the loop finishes without ever finding an equal adjacent pair, it means all elements are unique. The function returns `false`.


**Execution Stats**  
| Metric  | Value                |
|:-------|:-------------------:|
| Runtime | 46 ms | Beats 55.66%   |
| Memory  | 17.33 MB | Beats 56.35%  |
