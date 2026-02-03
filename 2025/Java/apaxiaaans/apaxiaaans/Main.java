import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String tj = sc.nextLine();

        String newWord = Character.toString(tj.charAt(0));

        for (int i = 1; i < tj.length(); i++)
        {
            if (tj.charAt(i) != tj.charAt(i-1))
            {
                newWord += Character.toString(tj.charAt(i));
            }
        }
        System.out.println(newWord);

        sc.close();
    }
}
