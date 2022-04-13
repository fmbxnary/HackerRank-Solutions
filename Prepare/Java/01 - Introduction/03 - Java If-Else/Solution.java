import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int myInt = scanner.nextInt();
        if (myInt % 2 != 0)
            System.out.println("Weird");
        else if (myInt >= 2 && myInt <= 5)
            System.out.println("Not Weird");
        else if (myInt >= 6 && myInt <= 20)
            System.out.println("Weird");
        else if (myInt > 20)
            System.out.println("Not Weird");
    }
}
