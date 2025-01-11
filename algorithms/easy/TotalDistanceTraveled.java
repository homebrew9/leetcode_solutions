public class TotalDistanceTraveled {
    public static int distanceTraveled(int mainTank, int additionalTank) {
        int result = 0;
        for (int i = 1; i <= mainTank; i++){
            //System.out.println(i + ", " + mainTank + ", " + additionalTank + ", " + result);
            if (additionalTank != 0 && i % 5 == 0){
                additionalTank -= 1;
                result += 10;
                mainTank += 1;
            } else {
                result += 10;
            }
        }
        return result;
        // Note that the value of the target "x" keeps changing inside the loop
        // so the following is essentially an infinite loop in Java.
        // In Python, if "range" is used in the "for" loop, then its target is
        // fixed, so it will loop through only 5 times, even if x is incremented
        // inside the loop!!! Check the Python program for this problem.
        //
        //int x = 5;
        //for (int i = 0; i < x; i++) {
        //    x += 1;
        //    System.out.println(i);
        //}
        //return -999;
    }

    public static void main(String[] args) {
        int[][] data;
        data = new int[6][2];
        data[0][0] = 5; data[0][1] = 10;
        data[1][0] = 1; data[1][1] = 2;
        data[2][0] = 9; data[2][1] = 1;
        data[3][0] = 9; data[3][1] = 2;
        data[4][0] = 9; data[4][1] = 3;
        data[5][0] = 13; data[5][1] = 3;

        int mainTank, additionalTank;
        for (int i = 0; i < data.length; i++) {
            mainTank = data[i][0];
            additionalTank = data[i][1];
            int result = distanceTraveled(mainTank, additionalTank);
            System.out.println("mainTank, additionalTank = " + mainTank + ", " + additionalTank);
            System.out.println("r = " + result);
            System.out.println("==================");
        }

    }
}

