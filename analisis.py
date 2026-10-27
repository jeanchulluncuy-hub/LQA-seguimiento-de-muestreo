import pandas as pd
from conexion_sheets import obtener_datos

def contar_registros(df):
    return len(df) if df is not None else 0

def contar_estado(df, columna, valor_buscado):
    if df is not None and columna in df.columns:
        return (df[columna] == valor_buscado).sum()
    return 0

def agrupar_por_tipo(df):
    if df is not None and "Tipo de Cliente" in df.columns:
        return df["Tipo de Cliente"].value_counts().to_dict()
    return {}

def agrupar_por_dominio_correo(df):
    if df is None or "Correo Electrónico" not in df.columns:
        return {}
    
    correos = df["Correo Electrónico"].dropna().astype(str)
    dominios = correos.apply(lambda x: x.split("@")[-1] if "@" in x else "Sin Correo")
    return dominios.value_counts().head(5).to_dict()

def conteo_documentos(df):
    if df is None:
        return {"Con DNI": 0, "Con RUC": 0}
    
    con_dni = (df["Número de DNI"].str.strip() != "").sum() if "Número de DNI" in df.columns else 0
    con_ruc = (df["Número de RUC"].str.strip() != "").sum() if "Número de RUC" in df.columns else 0
    
    return {"Con DNI": int(con_dni), "Con RUC": int(con_ruc)}

def procesar_datos():
    datos = obtener_datos()

    if not datos or len(datos) < 2:
        return None, {
            "total_registros": 0,
            "total_personas": 0,
            "total_empresas": 0,
            "porcentaje_empresas": 0,
            "por_tipo": {},
            "dominios_correo": {},
            "documentos": {}
        }

    encabezados = datos[0]
    filas = datos[1:]
    df = pd.DataFrame(filas, columns=encabezados)

    total = contar_registros(df)
    total_personas = contar_estado(df, "Tipo de Cliente", "Persona")
    total_empresas = contar_estado(df, "Tipo de Cliente", "Empresa")
    
    porcentaje_empresas = round((total_empresas / total) * 100, 1) if total > 0 else 0

    resumen = {
        "total_registros": total,
        "total_personas": total_personas,
        "total_empresas": total_empresas,
        "porcentaje_empresas": porcentaje_empresas,
        "por_tipo": agrupar_por_tipo(df),
        "dominios_correo": agrupar_por_dominio_correo(df),
        "documentos": conteo_documentos(df),
        "columnas": list(df.columns)
    }

    return df, resumen

if __name__ == "__main__":
    df, resumen = procesar_datos()
    
    print("==========================================")
    print("      REPORTE DE ANÁLISIS DE DATOS        ")
    print("==========================================")
    print(f"📌 Total de Registros: {resumen['total_registros']}")
    print(f"👤 Total de Personas:  {resumen['total_personas']}")
    print(f"🏢 Total de Empresas:  {resumen['total_empresas']}")
    print(f"📈 % Corporativo:     {resumen['porcentaje_empresas']}%")
    print("------------------------------------------")
    print("📊 Distribución por Tipo de Cliente:")
    for tipo, cantidad in resumen['por_tipo'].items():
        print(f"   - {tipo}: {cantidad}")
    print("------------------------------------------")
    print("🆔 Documentos Ingresados:")
    for doc, cantidad in resumen['documentos'].items():
        print(f"   - {doc}: {cantidad}")
    print("==========================================")
    
    print("\n==========================================")
    print("        VISTA PREVIA DE LA TABLA          ")
    print("==========================================")
    if df is not None:
        print(df.head())
    print("==========================================")