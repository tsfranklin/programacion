package controladores;

public class OperadoresIncrementale {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		
		
		int a = 10;

		a = (a==10) ? (a+10) : a;

		int b = (a>20) ? (a*2) : a;
		
		System.out.println("a: " + a + ", b: " + b);
		System.out.printf("a: %d, b: %d\n", a, b);

	}

}
