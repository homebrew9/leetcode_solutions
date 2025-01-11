#include <stdio.h>
#define MAX 9

int maxSubArray(int* nums, int numsSize){
    // Kadane's algorithm.
    // If the running total upto an element is less than that element, then
    // set running total to that element. maxSum gets refreshed to the higher
    // of maxSum and running total at each iteration. Here's a run:
    //   { -2, 1, -3, 4, -1, 2, 1, -5, 4 }
    // c = -2  1  -2  4   3  5  6   1  5
    // m = -2  1   1  4   4  5  6   6  6
    // There are other slight variations, but the underlying logic is essentially the same.
    // Keep checking the current Sum, and discard is if current element is higher than it.
    int currSum = 0;
    int maxSum = nums[0];
    for (int i = 0; i < numsSize; i++) {
        currSum += nums[i];
        if (nums[i] > currSum) {
            currSum = nums[i];
        }
        if (currSum > maxSum) {
            maxSum = currSum;
        }
    }
    return maxSum;
}

void displayArray(int *nums, int numsSize) {
    for (int i = 0; i < numsSize; i++) {
        if (i == 0) {
            printf("arr = { %d", *nums);
        } else {
            printf(", %d", *nums);
        }
        nums++;
    }
    printf(" }\n");
}

int main() {
    int row0[9] = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int row1[5] = {1, 2, 3, 4, 5};
    int row2[5] = {-1, -2, -3, -4, -5};
    int row3[5] = {5, 4, -1, 7, 8};
    int row4[6] = {1, -1, 1, -1, 1, -1};
    int row5[2] = {1, -1};
    int row6[1] = {1};
    int row7[6] = {1, 2, 3, -1, -2, -3};
    int row8[7] = {1, 1, 1, 1, 1, 1, 1};

    int *jagged[MAX] = {row0, row1, row2, row3, row4, row5, row6, row7, row8};

    int size[MAX] = {9, 5, 5, 5, 6, 2, 1, 6, 7};
    int k = 0;

    for (int i = 0; i < MAX; i++) {
        int *ptr = jagged[i];
        displayArray(ptr, size[k]);

        int ret = maxSubArray(ptr, size[k]);
        printf("ret = %d\n", ret);
        printf("=========\n");

        k++;
        jagged[i]++;
    }
    return 0;
}

