public class Math {
	public double multiple(double i1,double i2) {
		double sum=0;

		sum=i1*i2;

		return sum;
	}

	
	public static void main(String[] args) {
		Math math=new Math();
		for (int i = 1; i < 11; i++) {
			for (int j = 1; j < 11; j++) {
			System.out.println(i+"*"+j+ "=\t" + times.multiple(i,j));
			}
		}
	}
}
