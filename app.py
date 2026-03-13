import streamlit as st
import pandas as pd

# ---------------- CONFIGURACIÓN GENERAL ----------------

st.set_page_config(
    page_title="IA y detección temprana de trastornos del aprendizaje",
    layout="wide"
)

# ---------------- ESTILOS CSS ----------------

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

.modal {
background: rgba(0,0,0,0.4);
backdrop-filter: blur(6px);
position: fixed;
top:0;
left:0;
width:100%;
height:100%;
display:flex;
align-items:center;
justify-content:center;
z-index:1000;
}

.modal-content{
background:#e8f2e8;
border-radius:20px;
padding:30px;
max-width:700px;
box-shadow:0 10px 25px rgba(0,0,0,0.2);
border:2px solid #4a7c4a;
}

.close-btn{
float:right;
font-weight:bold;
font-size:20px;
cursor:pointer;
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

# ---------------- TITULO ----------------

st.markdown("<h1><i>El impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje</i></h1>", unsafe_allow_html=True)

st.markdown("""
<p class="frase">
"La inteligencia artificial no reemplaza al docente, lo potencia: abre caminos para que cada estudiante alcance su máximo potencial."
</p>
""", unsafe_allow_html=True)

# ---------------- INICIO ----------------

if pagina == "Inicio":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
La inteligencia artificial (IA) está transformando profundamente la educación y especialmente los procesos de evaluación y detección temprana de dificultades de aprendizaje.

Tradicionalmente, la identificación de trastornos del aprendizaje dependía de la observación docente y de pruebas estandarizadas. Aunque útiles, estos métodos pueden ser lentos y a veces no detectan señales tempranas.

La IA permite analizar grandes volúmenes de datos educativos, identificar patrones complejos y facilitar intervenciones pedagógicas más tempranas y personalizadas.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- INTRODUCCION ----------------

elif pagina == "Introducción":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
Los trastornos del aprendizaje representan uno de los principales desafíos en los sistemas educativos. Muchas veces las dificultades en lectura, escritura o atención no se identifican a tiempo.

La inteligencia artificial permite analizar patrones de comportamiento académico y detectar señales tempranas que podrían pasar desapercibidas mediante métodos tradicionales.

Esto permite implementar intervenciones educativas tempranas que favorecen el desarrollo académico y emocional de los estudiantes.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- TRASTORNOS ----------------

elif pagina == "Trastornos del aprendizaje":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
Los trastornos del aprendizaje son dificultades específicas en procesos cognitivos relacionados con la adquisición del conocimiento.

Ejemplos principales:

• **Dislexia:** dificultades en lectura y decodificación de palabras.  
• **Discalculia:** problemas en el razonamiento matemático.  
• **TDAH:** déficit de atención e hiperactividad.

Consecuencias frecuentes:

- Bajo rendimiento escolar  
- Problemas de autoestima  
- Riesgo de abandono académico
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- DETECCIÓN TEMPRANA ----------------

elif pagina == "Detección temprana":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
La detección temprana consiste en identificar señales iniciales de dificultades de aprendizaje antes de que se conviertan en problemas académicos graves.

La inteligencia artificial puede:

- Analizar datos de tareas y evaluaciones
- Detectar patrones de error
- Evaluar comportamiento en plataformas digitales

Esto permite intervenciones educativas más rápidas y eficaces.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- EDUCACIÓN INCLUSIVA ----------------

elif pagina == "Educación inclusiva":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
La educación inclusiva busca garantizar que todos los estudiantes tengan oportunidades de aprendizaje independientemente de sus capacidades o contextos.

La IA contribuye mediante:

- Personalización del aprendizaje
- Identificación de necesidades educativas específicas
- Reducción de sesgos humanos en evaluación
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- ETICA ----------------

elif pagina == "Ética en IA":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
El uso de inteligencia artificial en educación plantea importantes desafíos éticos.

Principios fundamentales:

- Privacidad de datos
- Transparencia en algoritmos
- Uso responsable de información educativa

La IA debe ser utilizada como **herramienta complementaria del docente**, nunca como reemplazo.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- BENEFICIOS ----------------

elif pagina == "Beneficios de la IA":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
Beneficios principales de la IA en educación:

• Mayor precisión en la detección de dificultades.  
• Intervenciones educativas tempranas.  
• Personalización del aprendizaje.  
• Reducción de sesgos humanos.  
• Evaluación continua del desempeño académico.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- DESAFIOS ----------------

elif pagina == "Desafíos":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
Principales desafíos:

- Sesgos algorítmicos
- Privacidad de datos
- Falta de regulación clara
- Necesidad de capacitación docente
- Dependencia tecnológica excesiva
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PERSPECTIVAS ----------------

elif pagina == "Perspectivas futuras":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
Las investigaciones futuras se enfocan en:

- Evaluar la efectividad a largo plazo de sistemas de IA
- Adaptar herramientas a distintos contextos culturales
- Integrar IA con neurociencia y gamificación
- Mejorar marcos éticos y regulatorios
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PERCEPCIÓN DOCENTE ----------------

elif pagina == "Percepción docente":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
Los docentes desempeñan un papel fundamental en la integración de la inteligencia artificial.

Su rol incluye:

- Interpretar los datos generados por sistemas de IA
- Diseñar estrategias pedagógicas personalizadas
- Garantizar el uso ético de la tecnología

La IA debe fortalecer el trabajo docente, no sustituirlo.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONCEPTOS CLAVE ----------------

elif pagina == "Conceptos clave":

    data = {
    "Concepto":[
    "Trastornos del aprendizaje",
    "Detección temprana",
    "Educación inclusiva",
    "Ética en IA"
    ],

    "Definición":[
    "Dificultades específicas en lectura, escritura o atención",
    "Identificación temprana de señales de dificultades",
    "Modelo educativo que atiende la diversidad",
    "Privacidad, transparencia y uso responsable de datos"
    ]
    }

    df = pd.DataFrame(data)

    st.table(df)

# ---------------- CONCLUSIONES ----------------

elif pagina == "Conclusiones":

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.write("""
La inteligencia artificial representa una herramienta poderosa para mejorar la detección temprana de trastornos del aprendizaje.

Su capacidad para analizar grandes volúmenes de datos permite identificar patrones que facilitan intervenciones educativas tempranas.

Sin embargo, su implementación debe realizarse de manera ética y responsable, garantizando siempre el papel central del docente en el proceso educativo.
""")

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- REFERENCIAS ----------------

elif pagina == "Referencias":

    st.markdown("### Artículos relacionados")

    articulo = st.selectbox(
    "Selecciona un artículo:",
    [
    "Impacto de la IA en la detección temprana",
    "IA y aprendizaje personalizado",
    "Gamificación y detección temprana",
    "Desafíos éticos de la IA en educación"
    ]
    )

    if articulo == "Impacto de la IA en la detección temprana":

        st.info("""
El artículo analiza cómo los algoritmos de machine learning permiten identificar dificultades de aprendizaje a partir del análisis de datos académicos.
""")

    if articulo == "IA y aprendizaje personalizado":

        st.info("""
Se explora cómo los sistemas inteligentes pueden adaptar contenidos educativos según las necesidades del estudiante.
""")

    if articulo == "Gamificación y detección temprana":

        st.info("""
Describe el uso de plataformas basadas en juegos para evaluar habilidades cognitivas y detectar dificultades de aprendizaje.
""")

    if articulo == "Desafíos éticos de la IA en educación":

        st.info("""
Analiza los riesgos relacionados con privacidad de datos, sesgos algorítmicos y dependencia tecnológica.
""")
