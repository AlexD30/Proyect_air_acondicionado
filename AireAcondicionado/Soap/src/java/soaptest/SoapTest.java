/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/WebServices/WebService.java to edit this template
 */
package soaptest;

import javax.jws.WebService;
import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebResult;
import modelo.Persona;

/**
 *
 * @author isanchezcigna
 */
@WebService(serviceName = "SoapTest")
public class SoapTest {

    /**
     * This is a sample web service operation
     */
    @WebMethod(operationName = "hello")
    public String hello(@WebParam(name = "name") String txt) {
        return "Hello " + txt + " !";
    }
    
    @WebMethod(operationName = "sumar") /* Nombre Mascara/Ruta */
    @WebResult(name = "sumaNumero") /* Cambiar el nombre a la etiqueta de resultado */
    public int sumar(
        @WebParam(name = "numero1") int num1,
        @WebParam(name = "numero2") int num2){
            int sum;
            sum = num1+num2;
            return sum;
    } 
    
    @WebMethod(operationName = "mostrarPersona")
    @WebResult(name="persona")
    public Persona mostrarPersona() {
        Persona objPer = new Persona();
        objPer.setNombre("Sandra Olea");
        objPer.setEdad(50);
        
        return objPer;
    }
    
}
