int compare_ints(const void *a, const void *b) {
    if (*(const int*)a < *(const int*)b) return -1;
    if (*(const int*)a > *(const int*)b) return 1;
    return 0;
}

bool containsDuplicate(int* nums, int numsSize) {
    if (numsSize <= 1) {
        return false;
    }

    qsort(nums, numsSize, sizeof(int), compare_ints);

    for (int i = 0; i < numsSize - 1; i++) {
        if (nums[i] == nums[i+1]) {
            return true;
        }
    }
    return false;
}
