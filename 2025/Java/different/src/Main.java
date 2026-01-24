
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();

        while(line != null) {
            String[] tokens = line.split(" ");

            // TODO actual problem

            Long diff = Math.abs(Long.parseLong(tokens[0]) - Long.parseLong(tokens[1]));

            System.out.println(diff);

            line = br.readLine();
        }
    }
}
