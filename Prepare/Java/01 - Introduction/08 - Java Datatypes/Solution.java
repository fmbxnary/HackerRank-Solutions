import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        scanner.next();
        long number;
        
        while (scanner.hasNext()) {
            try {
                number = scanner.nextLong();
                System.out.println(number + " can be fitted in:");
                if (number >= -128 && number <= 127) System.out.println("* byte");
                if (number >= -32768 && number <= 32767) System.out.println("* short");
                if (number >= (-Math.pow(2, 31)) && number <= (Math.pow(2, 31) - 1)) System.out.println("* int");
                if (number >= (-Math.pow(2, 63)) && number <= (Math.pow(2, 63) - 1)) System.out.println("* long");
            } catch (Exception e) {
                System.out.println(scanner.next() + " can't be fitted anywhere.");
            }
        }
    }
}
