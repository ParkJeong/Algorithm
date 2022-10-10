import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args){

    }
    public static int solution(String s){
        int answer = s.length();

        for(int group = 1; group <= s.length()/2; group++){
            StringBuilder tempStr = new StringBuilder();
            for(int idx = 0; idx < s.length(); idx++){
                int endIdx = idx + group;
                String groupStr = s.substring(idx, endIdx);
                String nextStr = s.substring(endIdx, endIdx + group);
                if (groupStr.equals(nextStr)){

                }
            }
        }


        return answer;
    }
}
