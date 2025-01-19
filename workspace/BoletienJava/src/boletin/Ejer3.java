package boletin;

import java.util.Scanner;

public class Ejer3 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		Scanner scanner = new Scanner (System.in);
		System.out.println("introduce el año: ");
		int año = Integer.valueOf(scanner.nextLine());
		System.out.println("introduce el mes: ");
		int mes = Integer.valueOf(scanner.nextLine());
		
        int dias; // Variable para guardar los días del mes
        
        // Determinar los días del mes
        if (mes == 2) { // Si es febrero
            if ((año % 4 == 0 && año % 100 != 0) || (año % 400 == 0)) {
                dias = 29; // Año bisiesto
            } else {
                dias = 28; // Año no bisiesto
            }
        } else if (mes == 4 || mes == 6 || mes == 9 || mes == 11) {
            dias = 30; // Meses con 30 días
        } else {
            dias = 31; // Meses con 31 días
        }
        
        // Mostrar el resultado
        System.out.println("El mes " + mes + " del año " + año + " tiene " + dias + " días.");
        
		

	}

}
