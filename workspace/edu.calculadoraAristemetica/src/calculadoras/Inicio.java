package calculadoras;

import java.util.Scanner;

/**
 * Clase controladora de la aplicacion
 * 270924
 * @author frank
 */

public class Inicio {
	/**
	 * Puerta de entrada a la aplicacion
	 * 270924
	 * @param args parametro de configuracion 
	 */


	public static void main(String[] args) {
		// TODO Auto-generated method stub
		boolean esCerrado = false; 
		Scanner scanner = new Scanner (System.in);
        byte opcionUsuario;
        float operador1, operador2, resultado;
        
        //La primera vez siempre se ejecuta lo que hay en el do
        do {
        	
        	System.out.println("-----MENU-----");
        	System.out.println("0. Cerrar menu");
        	System.out.println("1. Suma");
        	System.out.println("2. Resta");
        	System.out.println("3. Divisiòn");
        	System.out.println("4. Producto");
        	System.out.println("5. Modulo");
        	System.out.println("---------------");
        	System.out.println("Escriba la opcion deseada: "); 
			opcionUsuario = scanner.nextByte();
        	switch (opcionUsuario) {
        	case 0: {
        		System.out.println("se ha seleccionado la opcion 0");
        	    esCerrado = true;
        	    break; 
        	}
        	
        	case 1:{
        		System.out.println("Operacion suma");
        		System.out.println("Indique el primer operando: ");
        		operador1 = scanner.nextFloat();
        		System.out.println("Indique el segundo operador: ");
        		operador2 = scanner.nextFloat();
        		resultado = operador1 + operador2;
        		System.out.println("el resultado de la suma es: " + resultado);
    
        		break;
        		
        	}
        	
        	case 2:{
        		System.out.println("Operacion resta");
    
        		break;
        		
        	}
        	
        	case 3:{
        		System.out.println("Operacion division");
    
        		break;
        		
        	}
        	
        	case 4:{
        		System.out.println("Operacion producto");
    
        		break;
        		
        	}
        	
        	case 5:{
        		System.out.println("Operacion mòdulo");
    
        		break;
        		
        	}
      
        	default:
        		
        		System.out.println("la opcion seleccionada no existe");
        		break;
        		
        	} 
        	
        } while (!esCerrado); //vuelve al do si la condicion de evalua como true	

        scanner.close();
     }
}		