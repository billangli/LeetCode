/* 7. ReverseInteger

 Created by Bill Li on 1/3/2018.
 */

package easy;

public class ReverseInteger {
    public int reverse(int x) {
        int result = 0;
        while (x != 0) {
            if (Math.abs(result) > (Math.pow(2, 31) - 1) / 10) {
                return 0;
            }
            result *= 10;
            result += x % 10;
            x /= 10;
        }
        if (Math.abs(result) > Math.pow(2, 31) - 1) {
            return 0;
        }
        return result;
    }

    public static void main(String[] args){
        ReverseInteger r = new ReverseInteger();
        System.out.println(r.reverse(1534236469));
    }
}
