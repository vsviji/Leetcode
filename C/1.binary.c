#include <stdio.h>

int searchInsert(int nums[], int numsSize, int target) {
    int left = 0;
    int right = numsSize - 1;
    while (left <= right) {
        int mid = (left + right) >> 1;
        if (nums[mid] == target) {
            return mid;
        } else if (target < nums[mid]) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return left;
}

int main() {
    int nums[] = {1, 3, 5, 6};
    int target = 5;
    int result = searchInsert(nums, 4, target);
    printf("The target should be inserted at index: %d\n", result);
    return 0;
}
