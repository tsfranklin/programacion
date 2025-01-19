package boletin;

import java.util.Scanner;
public class ejer2 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
       
		Scanner scanner = new Scanner(System.in);
		System.out.println("Introduce tu peso: ");
		float peso = Float.valueOf(scanner.nextLine());
		System.out.println("Introduce tu altura: ");
		float altura = Float.valueOf(scanner.nextLine());
		double IMC=peso/Math.pow((altura), 2);
		/*
		 18,5       Peso insuficiente
		 18,5-25,9  Normopeso
		 25-26,9    Sobrepeso grado I
		 27-29,9    sobrepeso grado II (preobesidad)
		 30-34,9    Obesidad de tipo I
		 35-39,9    Obesidad tipo II
		 40-49,9    Obesidad de tipo III (morbida)
		 >=50       Obesidad de tipo IV (extrema)
		 */
		
		System.out.println(IMC);
		if (IMC < 18.5) {
			System.out.println("Peso insuficiente");
		}else if (peso<25) {
			System.out.println("Normopeso");
		}else if (peso<27) {
			System.out.println("Sobre peso grado I");	
		}else if (peso<30) {
			System.out.println("sobrepeso grado II (preobesidad)");
		}else if (peso<35) {
			System.out.println(" Obesidad de tipo I");
		}else if (peso<40) {
			System.out.println("Obesidad tipo II");
		}else if(peso<50) {
			System.out.println("Obesidad de tipo III (morbida)");
		}else {
			System.out.println("Obesidad de tipo IV (extrema)");
		}
	}

}
