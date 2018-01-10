/* 4. Median of Two Sorted Arrays

 Created by Bill Li on 1/4/2018.
 */

package hard;

import java.util.ArrayList;

public class MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int len1 = nums1.length;
        int len2 = nums2.length;
        int med1, med2;
        boolean even1, even2;

        if (len1 % 2 == 1) {
            even1 = false;
            med1 = nums1[len1 / 2];
        } else {
            even1 = true;
            med1 = (nums1[len1 / 2 - 1] + nums1[len1 / 2]) / 2;
        }
        if (len2 % 2 == 1) {
            even2 = false;
            med2 = nums2[len2 / 2];
        } else {
            even2 = true;
            med2 = (nums2[len2 / 2 - 1] + nums1[len2 / 2]) / 2;
        }

        if (med1 == med2) {
            return med1;
        } else {
            ArrayList between = new ArrayList();
            if (med1 > med2) {
                if (len1 / 2 - 1 >= 0) {
                    System.out.println("oops");
                }
            }
        }
        return 9;
    }
}
