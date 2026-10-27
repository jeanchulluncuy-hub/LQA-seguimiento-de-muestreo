import os
import gspread

# 1. RUTA ABSOLUTA DEL ARCHIVO DE CREDENCIALES
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CREDENTIALS_PATH = os.path.join(BASE_DIR, "credenciales.json")

# 2. ID DE LA HOJA DE GOOGLE SHEETS
SPREADSHEET_ID = "1YVxma65TsdnAhKuGHIm9tZBi8b7qD0fJ91n9r87NDHw"


def obtener_datos():
    """Conecta con Google Sheets usando la cuenta de servicio

    y retorna las filas en una lista de listas.
    """
    cliente = gspread.service_account(filename=CREDENTIALS_PATH)
    archivo = cliente.open_by_key(SPREADSHEET_ID)
    hoja = archivo.sheet1

    # Obtener todas las filas de la hoja como lista de listas
    datos = hoja.get_all_values()
    return datos


if __name__ == "__main__":
    # Prueba rápida de conexión al ejecutar este archivo directamente
    try:
        cliente_prueba = gspread.service_account(filename=CREDENTIALS_PATH)
        archivo_prueba = cliente_prueba.open_by_key(SPREADSHEET_ID)

        print("==========================================")
        print("¡Conexión a Google Sheets exitosa! 🎉")
        print("==========================================")
        print(f"📄 Título de la hoja: {archivo_prueba.title}")

        datos = obtener_datos()
        print(
            f"📊 Total de filas recuperadas (incluyendo encabezados): {len(datos)}"
        )
        print("==========================================")
    except Exception as e:
        print("==========================================")
        print(f"❌ Error al conectar con Google Sheets: {e}")
        print("==========================================")