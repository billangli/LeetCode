package medium;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class StringToInteger {
    static int myAtoi(String str) {

        if (str.length() == 0) {
            return 0;
        }

        boolean converting = false;
        boolean done = false;
        boolean isNegative = false;
        int num = 0;
        String digit = "^\\d$";
        String sign = "^-|\\+$";
        String whiteSpace = "^\\s$";

        for (int i = 0; i < str.length() && !done; i++) {
            String currentLetter = str.substring(i, i + 1);

            if (currentLetter.matches(digit)) {

                // Digit
                int currentDigit = Integer.parseInt(currentLetter);

                if (converting) {
                    if (num > 214748364 || (num == 214748364 && ((currentDigit > 8 && isNegative) || (currentDigit > 7 && !isNegative)))) {
                        if (isNegative) {
                            return Integer.MIN_VALUE;
                        } else {
                            return Integer.MAX_VALUE;
                        }
                    } else {
                        num = num * 10 + currentDigit;
                    }
                } else {
                    num = currentDigit;
                    converting = true;
                }

            } else if (currentLetter.matches(sign)) {

                // Sign
                if (converting) {
                    done = true;
                } else {
                    converting = true;
                    if (currentLetter.equals("-")) {
                        isNegative = true;
                    }
                }

            } else {

                // Word
                if (converting || (!converting && !currentLetter.matches(whiteSpace))) {
                    done = true;
                }

            }
        }

        if (isNegative && converting) {
            num = -1 * num;
        }

        return num;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        System.out.println(myAtoi(s));
    }
}
