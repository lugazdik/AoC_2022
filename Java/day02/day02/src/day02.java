// link to source problem: https://adventofcode.com/2022/day/2
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashMap;

public class day02 {
    // lose = 0, draw = 3, win = 6
    // A,X = rock = 1, B,Y = paper = 2, C,Z = scissors = 3
    static HashMap<String, Integer> mapOfPointsTask1   = new HashMap<>() {{
        put("A X", 4); put("A Y", 8); put("A Z", 3);
        put("B X", 1); put("B Y", 5); put("B Z", 9);
        put("C X", 7); put("C Y", 2); put("C Z", 6);
    }};

    // X = lose = 0, Y = draw = 3, Z = win = 6
    // A= rock = 1, B = paper = 2, C = scissors = 3
    static HashMap<String, Integer> mapOfPointsTask2   = new HashMap<>() {{
        put("A X", 3); put("A Y", 4); put("A Z", 8);
        put("B X", 1); put("B Y", 5); put("B Z", 9);
        put("C X", 2); put("C Y", 6); put("C Z", 7);
    }};

    public static void main(String[] args) {
        Path filePath = Path.of("src/day02.txt");
        try {
            String content = Files.readString(filePath);
            String[] lines = content.split("\r\n");
            int sumOfPointsTask1 = 0;
            int sumOfPointsTask2 = 0;
            for (String item : lines) {
                sumOfPointsTask1 += mapOfPointsTask1.get(item);
                sumOfPointsTask2 += mapOfPointsTask2.get(item);
            }
            System.out.println("Task 1: " + sumOfPointsTask1);
            System.out.println("Task 2: " + sumOfPointsTask2);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}