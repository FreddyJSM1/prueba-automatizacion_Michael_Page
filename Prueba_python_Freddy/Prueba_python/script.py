import pandas as pd
import json
import os

#Lee el archivo CSV y retoma un DataFrame
def cargar_datos(ruta_archivo):
    try:
        df = pd.read_csv(ruta_archivo)
        print("Archivo cargado correctamente.")
        return df
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None

#Calcula estadísticas básicas del DataFrame, el conteototal de registros y el promedio de las columnas numéricas
def calcular_estadisticas(df):

    total_registros = len(df)

    columnas_numericas = df.select_dtypes(include=['number'])
    promedios = columnas_numericas.mean().to_dict()

    return {
        "total_registros": total_registros,
        "promedios_columnas_numericas": promedios
    }

#Filtra los datos según una columna y un umbral específico, validando que la columna exista y sea numérica
def filtrar_datos(df, columna, umbral):

    # Validar que la columna exista
    if columna not in df.columns:
        print(f"La columna '{columna}' no existe en el archivo.")
        return []

    # Validar que sea numérica
    if not pd.api.types.is_numeric_dtype(df[columna]):
        print(f"La columna '{columna}' no es numérica.")
        return []

    df_filtrado = df[df[columna] > umbral]

    print(f"Se encontraron {len(df_filtrado)} registros con '{columna}' > {umbral}.")

    return df_filtrado.to_dict(orient="records")

# Se exportan los resultados en formato JSON
def exportar_json(resultado, ruta_salida):
    try:
        with open(ruta_salida, "w", encoding="utf-8") as f:
            json.dump(resultado, f, indent=4, ensure_ascii=False)
        print("Archivo JSON generado correctamente.")
    except Exception as e:
        print(f"Error al exportar JSON: {e}")


def main():
    # Obtener ruta donde está el script
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Construir rutas dinámicas
    ruta_csv = os.path.join(base_dir, "Script de Procesamiento de Datos.csv")
    ruta_salida = os.path.join(base_dir, "resultado.json")

    # Cargar datos
    df = cargar_datos(ruta_csv)

    if df is not None:

        # Calcular estadísticas
        estadisticas = calcular_estadisticas(df)

        # Filtro específico solicitado
        columna_filtro = "Salary"
        umbral = 65000

        # Aplicar filtro
        datos_filtrados = filtrar_datos(df, columna_filtro, umbral)

        # Arma el archivo JSON con los resultados
        resultado_final = {
            "estadisticas": estadisticas,
            "filtro_aplicado": {
                "columna": columna_filtro,
                "umbral": umbral
            },
            "datos_filtrados": datos_filtrados
        }

        # Exporta el JSON
        exportar_json(resultado_final, ruta_salida)

        print("Proceso completado exitosamente.")


if __name__ == "__main__":
    main()