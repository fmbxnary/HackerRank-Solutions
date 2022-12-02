import java.io.*;
import java.util.*;

public class Solution {
    static int B, H;
    static boolean flag;
    static int area = 0;
    static {
        Scanner scanner = new Scanner(System.in);
        try {
            B = scanner.nextInt();
            H = scanner.nextInt();
            
            if (B <= 0 || H <= 0) {
                throw new IllegalArgumentException("java.lang.Exception: Breadth and height must be positive");

            } else {
                area = B * H;
                flag = true;
            }
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }
    }
    public static void main(String[] args) {
        if (flag) {
            System.out.println(area);
        }
    }
}
