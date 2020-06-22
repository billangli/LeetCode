#include <stdbool.h>
#include <stdio.h>

bool checkPossibility(int *nums, int numsSize)
{
    // Locate the index i where nums[i] > nums[i + 1]
    int problemIndex = -1;
    for (int i = 0; i < numsSize - 1; ++i)
    {
        if (nums[i] > nums[i + 1])
        {
            if (problemIndex != -1)
                return false;
            problemIndex = i;
        }
    }

    return ((problemIndex == -1) || (problemIndex == 0) ||
            (problemIndex == numsSize - 2) ||
            (nums[problemIndex - 1] <= nums[problemIndex + 1]) ||
            (nums[problemIndex] <= nums[problemIndex + 2]));
}

int main(int argc, char *argv[])
{
    int nums0[] = {3, 4, 2, 3};
    printf("Answer: %d, solution: 0\n", checkPossibility(nums0, sizeof(nums0) / sizeof(nums0[0])));
    int nums1[] = {4, 2, 3};
    printf("Answer: %d, solution: 1\n", checkPossibility(nums1, sizeof(nums1) / sizeof(nums1[0])));
    int nums2[] = {4, 2, 1};
    printf("Answer: %d, solution: 0\n", checkPossibility(nums2, sizeof(nums2) / sizeof(nums2[0])));
    int nums3[] = {2, 3, 3, 2, 4};
    printf("Answer: %d, solution: 1\n", checkPossibility(nums3, sizeof(nums3) / sizeof(nums3[0])));
    int nums4[] = {5, 4, 3, 2, 1};
    printf("Answer: %d, solution: 0\n", checkPossibility(nums4, sizeof(nums4) / sizeof(nums4[0])));
    int nums5[] = {2, 1, 3, 5, 4};
    printf("Answer: %d, solution: 0\n", checkPossibility(nums5, sizeof(nums5) / sizeof(nums5[0])));
    return 0;
}