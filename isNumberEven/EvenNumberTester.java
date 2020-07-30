public class EvenNumberTester {

    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            System.out.println(i + ": " + isEven(i))
        }
    }

    public boolean isEven(int number) {
        if (number == 0) {
            return true
        }

        return !isEven(number-1)
    }
}