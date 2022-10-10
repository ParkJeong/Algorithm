import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String str = " a";

        String[] words = str.split(" ");

        for(String temp: words) {
            if (temp.equals("")){
                System.out.print("True");
            }
            else{
                System.out.print("");
            }
            System.out.println(temp);
        }
    }
}
