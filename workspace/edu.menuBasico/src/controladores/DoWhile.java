package controladores;

import java.util.Scanner;

/**
 * Clase controladora de la aplicacion
 * 270924
 * @author frank
 */

public class DoWhile {
	
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
        
        //La primera vez siempre se ejecuta lo que hay en el do
        do {
        	
        	System.out.println("-----MENU-----");
        	System.out.println("0. Cerrar menu");
        	System.out.println("1. Alta Usuario");
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
        		System.out.println("se ha seleccionado la opcion 1");
    
        		break;
        		
        	}
      
        	default:
        		
        		System.out.println("la opcion seleccionada no existe");
        		break;
        		
        	} 
        	
        } while (!esCerrado); //vuelve al do si la condicion de evalua como true	

     }
}		
