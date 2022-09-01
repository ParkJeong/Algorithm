import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        int year;
        int parsed_year;
        int YEAR_DIFFERENCE = 543;

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        year = Integer.parseInt(br.readLine());
        parsed_year = year - YEAR_DIFFERENCE;
        System.out.println(parsed_year);
    }
}
