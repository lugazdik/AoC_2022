// link to source problem: https://adventofcode.com/2022/day/1

import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class day01 {

    public static ArrayList<ArrayList<Integer>> read_file(String path) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        try{
            File myInput = new File(path);
            Scanner myReader = new Scanner(myInput);
            ArrayList<Integer> elfCalories = new ArrayList<>();
            while (myReader.hasNextLine()) {
                String line = myReader.nextLine();
                if (line.equals("")) {
                    result.add(elfCalories);
                    elfCalories = new ArrayList<>();
                } else {
                    elfCalories.add(Integer.parseInt(line));
                }
            }
        } catch (FileNotFoundException e) {
            System.out.println("File does not exist.");
            e.printStackTrace();
        }
        return result;
    }

    public static void main(String[] args) {
        ArrayList<ArrayList<Integer>> parsed_file = read_file("src/day01.txt");
        ArrayList<Long> caloriesSums = new ArrayList<>();
        for (ArrayList<Integer> integers : parsed_file) {
            long calSum = 0L;
            for (Integer integer : integers) {
                calSum += integer;
            }
            caloriesSums.add(calSum);
        }
        caloriesSums.sort(Collections.reverseOrder());
        System.out.format("Maximum calories: %d\n", caloriesSums.get(0));
        System.out.format("Top three: %d\n", caloriesSums.get(0) + caloriesSums.get(1) + caloriesSums.get(2));
    }
}