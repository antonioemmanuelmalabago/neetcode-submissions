class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        List<Integer> studentList = Arrays.stream(students)
                                          .boxed()
                                          .collect(Collectors.toCollection(ArrayList::new));
        List<Integer> sandwichList = Arrays.stream(sandwiches)
                                           .boxed()
                                           .collect(Collectors.toCollection(ArrayList::new));
        
        int rechecks = 0;
        int iteration = 0;
        while (rechecks < studentList.size()) {
            if (studentList.get(0) == sandwichList.get(0)) {
                studentList.remove(0);
                sandwichList.remove(0);
                rechecks = 0;
            } else {
                studentList.add(studentList.get(0));
                studentList.remove(0);
                rechecks++;
            }
            System.out.println("Iteration #" + iteration);
            System.out.println(studentList);
            System.out.println(sandwichList);
            iteration++;
        }

        return studentList.size();
    }
}