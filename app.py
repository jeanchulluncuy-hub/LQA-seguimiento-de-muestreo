from flask import Flask, render_template
from analisis import procesar_datos
from graficos import (
    grafico_barras,
    grafico_dona,
    grafico_vendedores,
    grafico_categorias,
    grafico_documentos,
    grafico_dominios
)

app = Flask(__name__)

@app.route("/")
def dashboard():
    df, resumen = procesar_datos()

    total_registros = resumen.get("total_registros", 0)
    total_personas = resumen.get("total_personas", 0)
    total_empresas = resumen.get("total_empresas", 0)
    porcentaje_empresas = resumen.get("porcentaje_empresas", 0)

    g1 = grafico_barras(df).to_html(full_html=False, include_plotlyjs=False)
    g2 = grafico_dona(df).to_html(full_html=False, include_plotlyjs=False)
    g3 = grafico_vendedores(df).to_html(full_html=False, include_plotlyjs=False)
    g4 = grafico_categorias(df).to_html(full_html=False, include_plotlyjs=False)
    g5 = grafico_documentos(df).to_html(full_html=False, include_plotlyjs=False)
    g6 = grafico_dominios(df).to_html(full_html=False, include_plotlyjs=False)

    columnas = list(df.columns) if df is not None else []
    filas = df.fillna("").values.tolist() if df is not None else []

    return render_template(
        "dashboard.html",
        total_registros=total_registros,
        total_personas=total_personas,
        total_empresas=total_empresas,
        porcentaje_empresas=porcentaje_empresas,
        g1=g1, g2=g2, g3=g3, g4=g4, g5=g5, g6=g6,
        columnas=columnas,
        filas=filas
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)