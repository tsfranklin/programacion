package boletin;
import java.util.Scanner;
public class Ejer1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
      
		Scanner scanner = new Scanner(System.in);
		System.out.println("Introduce tu edad: ");
		int edad=Integer.valueOf(scanner.nextLine());
		if (edad<=0 || edad>120) {
			
			System.out.println("Edad Incorrecta");
		}else if (edad<18) {
			System.out.println("Es niñ@");
		}else if (edad<65) {
			System.out.println("Es un/a adult@");
		}else {
			System.out.println("Es un/a ancian@");
		}
		
	 
	}

}
