import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    // c=
    // c-
    // dz=
    // d-
    // lj
    // nj
    // s=
    // z=
    // ljes=njak 6
//    ddz=z=    3
//      nljj    3
//    c=c=  2
//    dz=ak 3
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line = br.readLine();

        int len = 0;
        if (line.length() == 0) {
        }
        else {
            char prevCh = line.charAt(0);
            for (int idx = 1; idx < line.length(); idx++) {
                len++;

                if (idx + 1 >= line.length()){
                    break;
                }

                char nextCh = line.charAt(idx);

                if (prevCh == 'c') {
                    if (nextCh == '=' || nextCh == '-'){
                        idx++;
                    }
                }
                else if (prevCh == 'd') {
                    if (nextCh == 'z' || nextCh == '-') {
                        idx++;
                    }
                }
                else if (prevCh == 'l') {
                    if (nextCh == 'j') {
                        idx++;
                    }
                }
                else if (prevCh == 'n') {
                    if (nextCh == 'j') {
                        idx++;
                    }
                }
                else if (prevCh == 's') {
                    if (nextCh == '=') {
                        idx++;
                    }
                }
                else if (prevCh == 'z') {
                    if (nextCh == '=') {
                        idx++;
                    }
                }
                prevCh = nextCh;
            }
        }
        System.out.println(len);
    }
}
