using System;
using System.Linq;

namespace ValidadorCadenas
{
    public static class Validador
    {
        // Método principal que ejecuta todas las validaciones
        public static void ValidarCadena(string cadena, int longitudMin, int longitudMax, char caracter)
        {
            Console.WriteLine($"Solo alfabética: {EsSoloAlfabetica(cadena)}");
            Console.WriteLine($"Longitud válida ({longitudMin}-{longitudMax}): {LongitudValida(cadena, longitudMin, longitudMax)}");
            Console.WriteLine($"Cantidad de '{caracter}': {ContarCaracter(cadena, caracter)}");
        }

        // Validar si contiene solo letras
        public static bool EsSoloAlfabetica(string cadena)
        {
            return cadena.All(char.IsLetter);
        }

        // Validar longitud
        public static bool LongitudValida(string cadena, int min, int max)
        {
            return cadena.Length >= min && cadena.Length <= max;
        }

        // Contar ocurrencias de un carácter
        public static int ContarCaracter(string cadena, char caracter)
        {
            return cadena.Count(c => char.ToLower(c) == char.ToLower(caracter));
        }
    }
}