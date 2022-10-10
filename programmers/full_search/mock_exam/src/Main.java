import java.util.*;

public class Main {
    public static void main(String[] args){
        int[] answers = {1,2,3,4,5};
        int[] result = solution(answers);

        System.out.println(result);
    }
    public static int[] solution(int[] answers) {
        int[] answer = new int[3];

        int studentLen = 3;
        int[][] studentsAnswers = {
                {1, 2, 3, 4, 5},
                {2, 1, 2, 3, 2, 4, 2, 5},
                {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        Map<Integer, Integer> studentsScore = new HashMap<Integer, Integer>();

        for (int idx = 0; idx < studentLen; idx++){
            studentsScore.put(idx + 1, getStudentScore(answers, studentsAnswers[idx]));
        }
        List<Integer> keySet = new ArrayList<>(studentsScore.keySet());

        keySet.sort(new Comparator<Integer>(){
            @Override
            public int compare(Integer o1, Integer o2){
                return studentsScore.get(o1).compareTo(studentsScore.get(o2));
            }
        }
        );

        int idx = 0;
        for (Integer key: keySet){
            answer[idx] = studentsScore.get(key);
            idx++;
        }

        return answer;
    }

    public static int getStudentScore(int[] examAnswers, int[] studentAnswers){
        int score = 0;
        for(int idx = 0; idx < examAnswers.length; idx++){
            int studentIdx = idx % studentAnswers.length;
            if (examAnswers[idx] == studentAnswers[studentIdx]){
                score++;
            }
        }
        return score;
    }
}
