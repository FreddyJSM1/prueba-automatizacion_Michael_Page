using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;

namespace ValidadorCadenas
{
    class Program
    {
        static void Main(string[] args)
        {
            List<string> cadenas = new List<string>
            {
                "Hola",
                "Software",
                "ABC123",
                "Prueba",
                "Desarrollo"
            };

            char caracterABuscar = 'a';

            foreach (var cadena in cadenas)
            {
                Console.WriteLine("=================================");
                Console.WriteLine($"Validando cadena: {cadena}");

                Validador.ValidarCadena(cadena, 5, 10, caracterABuscar);
            }

            Console.WriteLine("Proceso finalizado.");
            Console.ReadLine();
        }
    }
}