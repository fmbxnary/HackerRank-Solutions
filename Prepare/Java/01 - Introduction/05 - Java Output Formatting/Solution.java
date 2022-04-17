import java.io.*;
import java.util.*;

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("=".repeat(32));
        while (scanner.hasNext()) {
            String[] parts = scanner.nextLine().split(" ");
            System.out.println(String.format("%-15s%03d", parts[0], Integer.parseInt(parts[1])));
        }
        System.out.println("=".repeat(32));
    }
}
