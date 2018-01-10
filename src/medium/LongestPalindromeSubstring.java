/* 5. LongestPalindromeSubstring

 Created by Bill Li on 1/4/2018.
 */

package medium;

import java.util.ArrayList;
import java.util.Iterator;

public class LongestPalindromeSubstring {
    public String longestPalindrome(String s) {
        // Creating a reversed string
        StringBuilder sb = new StringBuilder(s);
        String r = sb.reverse().toString();

        if (s.equals(r)) {
            return s;
        }

        boolean condition = false;
        ArrayList listCommon = new ArrayList();
        String common = "";

        while (!condition) {
            common = longestCommonSubstring(s, r, listCommon);
            int si = s.indexOf(common);
            int ri = r.indexOf(common);
            int length = s.length();
            int checker = common.length();

            if (si < ri) {
                if (si == length - (ri + common.length())) {
                    condition = true;
                }
            } else if (si > ri) {
                if (ri == length - (si + common.length())) {
                    condition = true;
                }
            } else {
                if ((si * 2 + common.length() == length)) {
                    condition = true;
                }
            }
            listCommon.add(common);
        }

        return common;
    }

    public String longestCommonSubstring(String s, String r, ArrayList listCommon) {
        int l = s.length();
        int[][] lc = new int[l][l];
        int longest = 0;
        String longestString = s.substring(0, 1);

        for (int i = 0; i < l; i++) {
            for (int j = 0; j < l; j++) {
                int temp = 0;
                if (s.substring(i, i + 1).equals(r.substring(j, j + 1))) {
                    temp = 1;
                    lc[i][j] = 1;

                    if ((i > 0) && (j > 0)) {
                        lc[i][j] = temp + lc[i - 1][j - 1];
                    }
                }



                if (lc[i][j] > longest) {
                    // Check if this is already used
                    String potentialLongest = s.substring(i - lc[i][j] + 1, i + 1);

                    boolean alreadyUsed = false;
                    for (Object aListCommon : listCommon) {
                        if (potentialLongest.equals(aListCommon)) {
                            alreadyUsed = true;
                        }
                    }

                    if (!alreadyUsed) {
                        longest = lc[i][j];
                        longestString = potentialLongest;
                    }
                }
            }
        }

        if (longest == 0) {
            return s.substring(0, 1);
        }
        return longestString;
    }

    public String bruteForceLongestPalindrome(String s) {
        int length = s.length();
        while (length > 0) {
            int start = 0;

            while (start + length <= s.length()) {
                String original = s.substring(start, start + length);
                String reversed = new StringBuilder(original).reverse().toString();
                if (original.equals(reversed)) {
                    return original;
                }
                start++;
            }
            length--;
        }
        return s.substring(0, 1);
    }

    private String oldLongestPalindrome(String s) {
        String longest = s.substring(0, 1);
        String mirrored = "";
        String temp;
        int counter = 0;

        while (counter < s.length()) {
            mirrored = s.substring(counter, counter + 1) + mirrored;
            temp = s.substring(0, counter + 1);
            temp += mirrored;
            longest = palindromeChecker(temp, s, longest);


            if (counter + 2 < s.length()) {
                mirrored = s.substring(counter + 1, counter + 2) + mirrored;
                temp = s.substring(0, counter + 1);
                temp += mirrored;
                longest = palindromeChecker(temp, s, longest);
                mirrored = mirrored.substring(1);
            }

            counter++;
        }

        return longest;
    }

    private String palindromeChecker(String temp, String s, String longest) {
        // Check for palindrome
        boolean isPalindrome = true;
        int tempLength = temp.length();
        int halfLength = tempLength / 2;
        int distFromHalf = 1;
        String tempLongest = "";

        if (tempLength % 2 == 1) {
            if (!temp.substring(halfLength, halfLength + 1).equals(s.substring(halfLength, halfLength + 1))) {
                isPalindrome = false;
            } else {
                tempLongest = s.substring(halfLength, halfLength + 1);
            }
            while ((isPalindrome) && (distFromHalf <= halfLength) &&
                    (halfLength + distFromHalf + 1 <= s.length())) {
                if ((!temp.substring(halfLength - distFromHalf, halfLength - distFromHalf + 1).equals(s.substring(halfLength - distFromHalf, halfLength - distFromHalf + 1))) ||
                        (!temp.substring(halfLength + distFromHalf, halfLength + distFromHalf + 1).equals(s.substring(halfLength + distFromHalf, halfLength + distFromHalf + 1)))) {
                    isPalindrome = false;
                } else {
                    tempLongest = s.substring(halfLength - distFromHalf, halfLength + distFromHalf + 1);
                }
                distFromHalf++;
            }
        } else {
            if (halfLength + 1 <= s.length()) {
                if (!temp.substring(halfLength - 1, halfLength + 1).equals(s.substring(halfLength - 1, halfLength + 1))) {
                    isPalindrome = false;
                } else {
                    tempLongest = s.substring(halfLength - 1, halfLength + 1);
                }
                while ((isPalindrome) && (distFromHalf < halfLength) &&
                        (halfLength + distFromHalf + 1 <= s.length())) {
                    if ((!temp.substring(halfLength - distFromHalf - 1, halfLength - distFromHalf).equals(s.substring(halfLength - distFromHalf - 1, halfLength - distFromHalf))) ||
                            (!temp.substring(halfLength + distFromHalf, halfLength + distFromHalf + 1).equals(s.substring(halfLength + distFromHalf, halfLength + distFromHalf + 1)))) {
                        isPalindrome = false;
                    } else {
                        tempLongest = s.substring(halfLength - distFromHalf - 1, halfLength + distFromHalf + 1);
                    }
                    distFromHalf++;
                }
            }
        }

        if (tempLongest.length() > longest.length()) {
            longest = tempLongest;
        }
        return longest;
    }

    public static void main(String[] args) {
        LongestPalindromeSubstring lps = new LongestPalindromeSubstring();
        System.out.println(lps.longestPalindrome("ccc"));
    }
}
