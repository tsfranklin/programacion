package controladores;
import java.util.Scanner;
public class Inicio {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

	/**Este es un comentario para el JAVADOC del proyecto
	 * author Franklin Torres Santos
	 * param  para facilitar los datos del metodo
	 * return indica que valores va devolver el metodo*/
		
	String mensaje;
	mensaje = "Bienvenido a gestion de blibliotecas";
	System.out.println(mensaje);
	
	
	Scanner sc = new Scanner(System.in);
	int edad;
	System.out.println("Escriba su edad");
	edad = sc.nextInt();
	System.out.println("la edad es: " + edad);
	
	System.out.println("lasdjfvdfjdfjvdafjk\n"
			+ "jajdjdjsddjjsddsj\n");
	
	 // Creamos un objeto Scanner para leer datos desde la consola
    Scanner scanner = new Scanner(System.in);
    
    // Solicitar al usuario el número de vehículos
    System.out.print("Por favor, ingresa el número de vehículos en tu casa: ");
    
    // Leer la entrada como un valor de tipo byte
    byte numeroDeVehiculos = scanner.nextByte();
    
    // Mostrar el número de vehículos
    System.out.println("El número de vehículos en tu casa es: " + numeroDeVehiculos);
    
    // Cerramos el objeto Scanner
    scanner.close();
    
    final char A = 'a';

    final int primerCodigo = (int) 'r';

    System.out.print("Las letras minúsculas con sus códigos ASCII son: \n");

    System.out.println("Caracter: " + (char) primerCodigo + " Valor: " + A + primerCodigo);
	}

}
