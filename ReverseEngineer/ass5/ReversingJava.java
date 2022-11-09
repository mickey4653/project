public class ReversingJava {
	public double convertTemp(double fahrenheit) {
		double celsius = 0;
		double freezingPoint = 32;
		double converRate = 5.0 / 9.0;

		celsius = (fahrenheit - freezingPoint) * converRate;

		return celsius;
	}

	
	public static void main(String[] args) {
		ReversingJava reversing = new ReversingJava();

		for (int fahrenheit = 0; fahrenheit < 100; fahrenheit++) {
			System.out.println(fahrenheit + "\t" + reversing.convertTemp(fahrenheit));
		}
	}
}
