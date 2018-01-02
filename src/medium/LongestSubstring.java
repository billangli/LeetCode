/* 3. Longest Substring Without Repeating Characters

 Created by Bill Li on 1/2/2018.
 */

package medium;

import java.util.ArrayList;

public class LongestSubstring {
    public int lengthOfLongestSubstring(String s) {
        ArrayList used = new ArrayList();
        int i = 0;
        int j = 0;
        int n = s.length();
        int max = 0;

        while ((i < n) && (j < n)) {
            if (!used.contains(s.charAt(j))) {
                used.add(s.charAt(j));
                j++;
                max = Math.max(max, j - i);
            } else {
                used.remove(used.indexOf(s.charAt(i)));
                i++;
            }
        }
        return max;
    }

    public static void main(String[] args){
        LongestSubstring l = new LongestSubstring();
        System.out.println(l.lengthOfLongestSubstring("abcabcbb"));
    }
}
