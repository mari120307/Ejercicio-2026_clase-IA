import streamlit as st
import pandas as pd

# Configuración general
st.set_page_config(page_title="IA en la detección temprana", layout="wide")

# Sidebar de navegación
st.sidebar.title("Navegación")
pagina = st.sidebar.radio(
    "Selecciona una sección:",
    [
        "Título",
        "Introducción",
        "Trastornos del aprendizaje",
        "Detección temprana",
        "Educación inclusiva",
        "Ética en IA",
        "Conceptos clave",
        "Conclusiones",
        "Referencias"
    ]
)

# 1.1 TÍTULO
if pagina == "Título":
    st.title("El impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje")

    st.markdown(
        """
        <p style='text-align:right; font-style:italic; font-size:18px;'>
        "La inteligencia artificial no reemplaza al docente, lo potencia: abre caminos para que cada estudiante alcance su máximo potencial."
        </p>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.write("""
    La inteligencia artificial está revolucionando múltiples áreas del conocimiento, y la educación es una de las más beneficiadas.
    En particular, su aplicación en la detección temprana de trastornos del aprendizaje abre nuevas oportunidades para mejorar
    la inclusión educativa y ofrecer apoyo oportuno a los estudiantes.
    """)

# 1.2 INTRODUCCIÓN
elif pagina == "Introducción":
    st.header("Introducción")

    st.write("""
    La inteligencia artificial (IA) se ha convertido en una herramienta clave para transformar la educación.
    Su capacidad de analizar grandes volúmenes de datos académicos y patrones de comportamiento permite identificar
    señales tempranas de dificultades como la dislexia, el TDAH o problemas de lectura.
    """)

    st.write("""
    Esto representa un cambio frente a los métodos tradicionales, que suelen ser más lentos y menos precisos.
    El objetivo es promover una educación inclusiva, donde cada estudiante reciba apoyo personalizado.
    """)

    st.write("""
    Sin embargo, este avance tecnológico debe ser acompañado de principios éticos claros que garanticen
    la privacidad y la transparencia en el uso de algoritmos.
    """)

# 1.3 TRASTORNOS DEL APRENDIZAJE
elif pagina == "Trastornos del aprendizaje":
    st.header("Trastornos del aprendizaje")

    st.write("""
    Los trastornos del aprendizaje son dificultades específicas en lectura, escritura, atención o procesamiento
    de información que afectan el rendimiento académico.
    """)

    st.markdown("### Principales trastornos:")

    st.markdown("""
    - **Dislexia:** problemas en la decodificación de palabras y comprensión lectora.  
    - **Discalculia:** dificultades en el razonamiento matemático y cálculo.  
    - **TDAH:** déficit de atención e hiperactividad que impacta la concentración y el desempeño escolar.
    """)

    st.info("La detección temprana es fundamental para evitar que estas dificultades se conviertan en barreras educativas permanentes.")

# 1.4 DETECCIÓN TEMPRANA
elif pagina == "Detección temprana":
    st.header("Detección temprana")

    st.write("""
    La detección temprana consiste en identificar señales iniciales de dificultades de aprendizaje antes
    de que los problemas se agraven o afecten significativamente el desarrollo académico del estudiante.
    """)

    st.write("""
    La inteligencia artificial permite analizar patrones complejos en el desempeño escolar,
    identificando errores recurrentes, tiempos de respuesta y comportamiento cognitivo.
    """)

    st.success("""
    Por ejemplo, plataformas como **NeurekaLAB** utilizan gamificación e inteligencia artificial
    para analizar patrones de lectura y respuesta, logrando una precisión superior al 90 %
    en la identificación de perfiles de riesgo.
    """)

# 1.5 EDUCACIÓN INCLUSIVA
elif pagina == "Educación inclusiva":
    st.header("Educación inclusiva")

    st.write("""
    La educación inclusiva busca garantizar que todos los estudiantes tengan acceso a oportunidades
    de aprendizaje equitativas, respetando sus diferencias cognitivas, sociales y culturales.
    """)

    st.write("""
    La integración de IA permite desarrollar herramientas de aprendizaje adaptativo que ajustan
    los contenidos educativos según las necesidades de cada estudiante.
    """)

    st.info("""
    Según García (2025), los algoritmos de aprendizaje automático permiten predecir qué estudiantes
    presentan riesgo de bajo rendimiento académico, facilitando intervenciones pedagógicas tempranas.
    """)

# 1.6 ÉTICA EN IA
elif pagina == "Ética en IA":
    st.header("Ética en Inteligencia Artificial")

    st.write("""
    El uso de inteligencia artificial en educación debe estar guiado por principios éticos
    que aseguren un uso responsable de la tecnología.
    """)

    st.markdown("### Principios éticos fundamentales")

    st.markdown("""
    - **Privacidad de datos:** proteger la información personal de los estudiantes.  
    - **Transparencia:** explicar cómo funcionan los algoritmos utilizados.  
    - **Equidad:** evitar sesgos algorítmicos que puedan generar discriminación.  
    - **Complementariedad:** la IA debe apoyar al docente, no sustituirlo.
    """)

    st.warning("""
    Autores como Vargas (2024) destacan que la IA debe ser vista como una herramienta de apoyo pedagógico
    y no como un reemplazo de la interacción humana en el proceso educativo.
    """)

# 1.7 CONCEPTOS CLAVE
elif pagina == "Conceptos clave":
    st.header("Conceptos clave")

    conceptos = {
        "Inteligencia Artificial (IA)": "Tecnología que simula procesos de razonamiento humano mediante algoritmos y aprendizaje automático.",
        "Detección temprana": "Identificación de señales iniciales para intervenir antes de que las dificultades se agraven.",
        "Educación inclusiva": "Modelo educativo que atiende la diversidad y necesidades de todos los estudiantes.",
        "Ética en IA": "Principios que garantizan privacidad, transparencia y uso responsable de los datos educativos."
    }

    df = pd.DataFrame(list(conceptos.items()), columns=["Concepto", "Definición"])

    st.table(df)

# 1.8 CONCLUSIONES
elif pagina == "Conclusiones":
    st.header("Conclusiones")

    st.write("""
    La inteligencia artificial tiene un enorme potencial para transformar la educación,
    especialmente en la detección temprana de trastornos del aprendizaje.
    """)

    st.write("""
    Gracias a su capacidad de analizar grandes volúmenes de información, la IA permite
    mejorar la precisión diagnóstica, identificar estudiantes en riesgo y ofrecer
    intervenciones educativas personalizadas.
    """)

    st.write("""
    No obstante, su implementación también plantea desafíos importantes, como la necesidad
    de capacitar a los docentes, garantizar la privacidad de los datos y establecer
    marcos regulatorios claros.
    """)

    st.success("""
    El futuro de la educación inclusiva dependerá de lograr un equilibrio entre innovación tecnológica
    y valores humanos, donde la IA funcione como una herramienta que fortalezca la labor docente.
    """)

# 1.9 REFERENCIAS
elif pagina == "Referencias":
    st.header("Referencias bibliográficas")

    with st.expander("Espinosa P (2024)"):
        st.write("Impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje.")

    with st.expander("NeurekaLAB (2023)"):
        st.write("Plataforma gamificada que utiliza IA para detectar dislexia y TDAH mediante minijuegos interactivos.")

    with st.expander("García M (2025)"):
        st.write("Uso de inteligencia artificial para predecir estudiantes en riesgo de bajo rendimiento académico.")

    with st.expander("Vargas G (2024)"):
        st.write("Aplicación de IA en estrategias de enseñanza-aprendizaje y sus implicaciones pedagógicas.")

    with st.expander("Gómez A., Yecid O., Gallego M. (2024)"):
        st.write("Desafíos éticos de la inteligencia artificial en la personalización del aprendizaje.")
        
