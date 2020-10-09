var searchHelper = function(nums, target, start, end) {
    if (start > end) {
        return -1;
    } else if (start + 1 == end) {
        return nums[start] == target ? start : -1;
    }
    
    const mid = start + Math.floor((end - start) / 2);
    if (target == nums[mid]) {
        return mid;
    } else if (target < nums[mid]) {
        return searchHelper(nums, target, start, mid);
    } else {
        return searchHelper(nums, target, mid + 1, end);
    }
}

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    return searchHelper(nums, target, 0, nums.length);
};
