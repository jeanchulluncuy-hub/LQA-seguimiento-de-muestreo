import plotly.graph_objects as go
from analisis import procesar_datos

colores = ["#3B82F6", "#10B981", "#F59E0B", "#8B5CF6", "#EC4899", "#6366F1"]

# 1. BARRAS: TIPO DE CLIENTE
def grafico_barras(df):
    if df is None or "Tipo de Cliente" not in df.columns:
        return go.Figure()

    conteo = df["Tipo de Cliente"].value_counts()
    fig = go.Figure(go.Bar(
        x=list(conteo.index),
        y=list(conteo.values),
        marker_color=[colores[i % len(colores)] for i in range(len(conteo))],
        text=list(conteo.values),
        textposition="auto"
    ))
    fig.update_layout(title="1. Cantidad por Tipo de Cliente", template="plotly_white", height=380, showlegend=False)
    return fig

# 2. DONA: TIPO DE CLIENTE
def grafico_dona(df):
    if df is None or "Tipo de Cliente" not in df.columns:
        return go.Figure()

    conteo = df["Tipo de Cliente"].value_counts()
    fig = go.Figure(go.Pie(
        labels=list(conteo.index),
        values=list(conteo.values),
        hole=0.60,
        marker=dict(colors=colores)
    ))
    fig.update_layout(title="2. Distribución % Por Tipo", template="plotly_white", height=380, showlegend=False)
    return fig

# 3. BARRAS: PERSONAS FRECUENTES
def grafico_vendedores(df):
    if df is None or "Nombres Completos" not in df.columns:
        return go.Figure()

    df_personas = df[df["Nombres Completos"].str.strip() != ""]
    conteo = df_personas["Nombres Completos"].value_counts().head(8)

    fig = go.Figure(go.Bar(
        x=list(conteo.index),
        y=list(conteo.values),
        marker_color="#10B981",
        text=list(conteo.values),
        textposition="auto"
    ))
    fig.update_layout(title="3. Registros por Nombre de Persona", template="plotly_white", height=380, showlegend=False)
    return fig

# 4. DONA: EMPRESAS
def grafico_categorias(df):
    if df is None or "Nombre de la Empresa" not in df.columns:
        return go.Figure()

    df_empresas = df[df["Nombre de la Empresa"].str.strip() != ""]
    conteo = df_empresas["Nombre de la Empresa"].value_counts().head(5)

    fig = go.Figure(go.Pie(
        labels=list(conteo.index),
        values=list(conteo.values),
        hole=0.50,
        marker=dict(colors=colores)
    ))
    fig.update_layout(title="4. Distribución por Nombre de Empresa", template="plotly_white", height=380, showlegend=False)
    return fig

# 5. BARRAS: DNI VS RUC
def grafico_documentos(df):
    if df is None:
        return go.Figure()

    con_dni = (df["Número de DNI"].str.strip() != "").sum() if "Número de DNI" in df.columns else 0
    con_ruc = (df["Número de RUC"].str.strip() != "").sum() if "Número de RUC" in df.columns else 0

    fig = go.Figure(go.Bar(
        x=["Con DNI (Persona)", "Con RUC (Empresa)"],
        y=[con_dni, con_ruc],
        marker_color=["#3B82F6", "#F59E0B"],
        text=[con_dni, con_ruc],
        textposition="auto"
    ))
    fig.update_layout(title="5. Tipo de Documento Ingresado (DNI vs RUC)", template="plotly_white", height=380, showlegend=False)
    return fig

# 6. BARRAS: DOMINIOS DE CORREO
def grafico_dominios(df):
    if df is None or "Correo Electrónico" not in df.columns:
        return go.Figure()

    correos = df["Correo Electrónico"].str.strip()
    correos = correos[correos != ""]
    dominios = correos.apply(lambda x: x.split("@")[-1] if "@" in x else "Sin Correo")
    conteo = dominios.value_counts().head(5)

    fig = go.Figure(go.Bar(
        x=list(conteo.index),
        y=list(conteo.values),
        marker_color="#8B5CF6",
        text=list(conteo.values),
        textposition="auto"
    ))
    fig.update_layout(title="6. Top Proveedores de Correo Electrónico", template="plotly_white", height=380, showlegend=False)
    return fig

if __name__ == "__main__":
    df, resumen = procesar_datos()
    grafico_barras(df).show()
    grafico_dona(df).show()
    grafico_vendedores(df).show()
    grafico_categorias(df).show()
    grafico_documentos(df).show()
    grafico_dominios(df).show()