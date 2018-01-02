/* TwoSum

 Created by Bill Li on 1/2/2018.
 */

package easy;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i ++) {
            for (int j = 0; j < nums.length; j ++) {
                if ((i != j) && (nums[i] + nums[j] == target)) {
                    int[] result = {i, j};
                    return result;
                }
            }
        }
        return null;
    }
}
