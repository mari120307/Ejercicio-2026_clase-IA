import streamlit as st
import pandas as pd

# ---------------- CONFIGURACIÓN GENERAL ----------------

st.set_page_config(
    page_title="IA y detección temprana de trastornos del aprendizaje",
    layout="wide"
)

# ---------------- ESTILOS ----------------

st.markdown("""
<style>

body {
background-color: #f7f9f7;
}

.block-container{
padding-top:2rem;
}

.card {
background-color:white;
padding:25px;
border-radius:18px;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
margin-bottom:20px;
}

.frase {
text-align:right;
font-style:italic;
color:#3b6f3b;
}

</style>
""", unsafe_allow_html=True)

# ---------------- MENÚ LATERAL ----------------

st.sidebar.title("📚 Navegación")

pagina = st.sidebar.radio(
"Selecciona un apartado:",
[
"Inicio",
"Introducción",
"Trastornos del aprendizaje",
"Detección temprana",
"Educación inclusiva",
"Ética en IA",
"Beneficios de la IA",
"Desafíos",
"Perspectivas futuras",
"Percepción docente",
"Conceptos clave",
"Conclusiones",
"Referencias"
]
)

# ---------------- INICIO ----------------

if pagina == "Inicio":

    st.title("El impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje")

    st.markdown("""
<p class="frase">
"La inteligencia artificial no reemplaza al docente, lo potencia: abre caminos para que cada estudiante alcance su máximo potencial."
</p>
""", unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
La inteligencia artificial (IA) está transformando profundamente la educación y especialmente los procesos de evaluación y detección temprana de dificultades de aprendizaje.

Tradicionalmente, la identificación de trastornos del aprendizaje dependía de la observación docente y de pruebas estandarizadas.

La IA permite analizar grandes volúmenes de datos educativos, identificar patrones complejos y facilitar intervenciones pedagógicas más tempranas y personalizadas.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- INTRODUCCIÓN ----------------

elif pagina == "Introducción":

    st.header("Introducción")

    st.write("""
Los trastornos del aprendizaje representan uno de los principales desafíos en los sistemas educativos.

Muchas veces las dificultades en lectura, escritura o atención no se identifican a tiempo.

La inteligencia artificial permite analizar patrones de comportamiento académico y detectar señales tempranas que podrían pasar desapercibidas mediante métodos tradicionales.
""")

# ---------------- TRASTORNOS ----------------

elif pagina == "Trastornos del aprendizaje":

    st.header("Trastornos del aprendizaje")

    st.write("""
Los trastornos del aprendizaje son dificultades específicas en procesos cognitivos relacionados con la adquisición del conocimiento.

Ejemplos:

• **Dislexia:** dificultades en lectura.  
• **Discalculia:** problemas en razonamiento matemático.  
• **TDAH:** déficit de atención e hiperactividad.

Consecuencias:

- Bajo rendimiento escolar  
- Problemas de autoestima  
- Riesgo de abandono académico
""")

# ---------------- DETECCIÓN TEMPRANA ----------------

elif pagina == "Detección temprana":

    st.header("Detección temprana")

    st.write("""
La detección temprana consiste en identificar señales iniciales de dificultades antes de que se conviertan en problemas académicos graves.

La inteligencia artificial puede:

- Analizar datos de tareas
- Detectar patrones de error
- Evaluar comportamiento digital

Esto permite intervenciones educativas más rápidas.
""")

# ---------------- EDUCACIÓN INCLUSIVA ----------------

elif pagina == "Educación inclusiva":

    st.header("Educación inclusiva")

    st.write("""
La educación inclusiva busca garantizar que todos los estudiantes tengan oportunidades de aprendizaje.

La IA contribuye mediante:

- Personalización del aprendizaje
- Identificación de necesidades educativas
- Reducción de sesgos humanos
""")

# ---------------- ÉTICA ----------------

elif pagina == "Ética en IA":

    st.header("Ética en Inteligencia Artificial")

    st.write("""
El uso de inteligencia artificial en educación plantea desafíos éticos importantes.

Principios fundamentales:

- Privacidad de datos
- Transparencia en algoritmos
- Uso responsable de información educativa

La IA debe ser complemento del docente, no reemplazo.
""")

# ---------------- BENEFICIOS ----------------

elif pagina == "Beneficios de la IA":

    st.header("Beneficios de la Inteligencia Artificial")

    st.write("""
Beneficios principales:

• Mayor precisión diagnóstica  
• Intervenciones tempranas  
• Personalización del aprendizaje  
• Evaluación continua del desempeño
""")

# ---------------- DESAFÍOS ----------------

elif pagina == "Desafíos":

    st.header("Desafíos del uso de IA")

    st.write("""
Principales desafíos:

- Sesgos algorítmicos
- Privacidad de datos
- Dependencia tecnológica
- Necesidad de capacitación docente
""")

# ---------------- PERSPECTIVAS ----------------

elif pagina == "Perspectivas futuras":

    st.header("Perspectivas futuras")

    st.write("""
Las investigaciones futuras se centran en:

- Evaluar efectividad a largo plazo
- Adaptar herramientas a distintos contextos
- Integrar IA con neurociencia y gamificación
""")

# ---------------- PERCEPCIÓN DOCENTE ----------------

elif pagina == "Percepción docente":

    st.header("Percepción y rol de los docentes")

    st.write("""
Los docentes son clave en la integración de IA.

Funciones principales:

- Interpretar datos generados por IA
- Diseñar estrategias pedagógicas
- Garantizar uso ético de la tecnología
""")

# ---------------- CONCEPTOS CLAVE ----------------

elif pagina == "Conceptos clave":

    st.header("Conceptos clave")

    data = {
    "Concepto":[
    "Trastornos del aprendizaje",
    "Detección temprana",
    "Educación inclusiva",
    "Ética en IA"
    ],

    "Definición":[
    "Dificultades específicas en lectura, escritura o atención",
    "Identificación temprana de señales",
    "Modelo educativo que atiende diversidad",
    "Privacidad y transparencia en datos"
    ]
    }

    df = pd.DataFrame(data)

    st.table(df)

# ---------------- CONCLUSIONES ----------------

elif pagina == "Conclusiones":

    st.header("Conclusiones")

    st.write("""
La inteligencia artificial mejora la detección temprana de trastornos del aprendizaje.

Permite intervenciones más rápidas y contribuye a una educación inclusiva.

Sin embargo, su uso debe mantener un equilibrio entre innovación tecnológica y valores humanos.
""")

# ---------------- REFERENCIAS ----------------

elif pagina == "Referencias":

    st.header("Referencias")

    articulo = st.selectbox(
    "Selecciona un artículo:",
    [
    "Impacto de la IA en la detección temprana",
    "IA y aprendizaje personalizado",
    "Gamificación y detección temprana",
    "Desafíos éticos de la IA"
    ]
    )

    if articulo == "Impacto de la IA en la detección temprana":

        st.info("Uso de machine learning para identificar dificultades de aprendizaje.")

    if articulo == "IA y aprendizaje personalizado":

        st.info("Los sistemas inteligentes adaptan el contenido al ritmo del estudiante.")

    if articulo == "Gamificación y detección temprana":

        st.info("Plataformas educativas utilizan juegos para evaluar habilidades cognitivas.")

    if articulo == "Desafíos éticos de la IA":

        st.info("Privacidad de datos y sesgos algorítmicos son retos importantes.")
   
    
