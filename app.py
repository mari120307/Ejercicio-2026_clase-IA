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

# Título principal con frase motivadora
if pagina == "Título":
    st.title("El impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje")
    st.markdown("<p style='text-align:right; font-style:italic;'>La inteligencia artificial no reemplaza al docente, lo potencia: abre caminos para que cada estudiante alcance su máximo potencial.</p>", unsafe_allow_html=True)

elif pagina == "Introducción":
    st.header("Introducción")
    st.markdown("""
    La inteligencia artificial (IA) está transformando la detección temprana de trastornos del aprendizaje.  
    Mediante el análisis de datos académicos y patrones de comportamiento, la IA permite identificar señales de dislexia, problemas de atención y dificultades lectoras.  
    Esto facilita intervenciones más rápidas y personalizadas, promoviendo una educación inclusiva.  
    """)

elif pagina == "Trastornos del aprendizaje":
    st.header("Trastornos del aprendizaje")
    st.markdown("""
    Son dificultades específicas en lectura, escritura, atención o procesamiento de información que afectan el rendimiento académico.  
    Ejemplos: dislexia, discalculia, TDAH.  
    """)

elif pagina == "Detección temprana":
    st.header("Detección temprana")
    st.markdown("""
    Se refiere a la identificación de señales iniciales de dificultades para intervenir antes de que se agraven.  
    La IA permite reconocer patrones complejos en datos educativos, mejorando la precisión diagnóstica.  
    """)

elif pagina == "Educación inclusiva":
    st.header("Educación inclusiva")
    st.markdown("""
    Modelo educativo que busca atender las necesidades de todos los estudiantes, respetando la diversidad.  
    La IA puede apoyar este modelo al personalizar el aprendizaje y reducir sesgos humanos.  
    """)

elif pagina == "Ética en IA":
    st.header("Ética en IA")
    st.markdown("""
    Principios que garantizan privacidad, transparencia y uso responsable de los datos educativos.  
    Es fundamental que la IA complemente al docente y no lo sustituya, evitando la deshumanización del proceso educativo.  
    """)

elif pagina == "Conceptos clave":
    st.header("Conceptos clave")
    conceptos = {
        "Trastornos del aprendizaje": "Dificultades específicas en lectura, escritura, atención o procesamiento de información.",
        "Detección temprana": "Identificación de señales iniciales para intervenir antes de que se agraven.",
        "Educación inclusiva": "Modelo que atiende la diversidad de estudiantes.",
        "Ética en IA": "Privacidad, transparencia y uso responsable de datos educativos."
    }
    df = pd.DataFrame(list(conceptos.items()), columns=["Concepto", "Definición"])
    st.table(df)

elif pagina == "Conclusiones":
    st.header("Conclusiones")
    st.markdown("""
    La IA mejora la detección temprana de trastornos del aprendizaje y promueve la educación inclusiva.  
    Sin embargo, requiere un equilibrio entre innovación tecnológica y valores humanos, garantizando ética, transparencia y respeto a la diversidad.  
    """)

elif pagina == "Referencias":
    st.header("Referencias bibliográficas")
    st.markdown("Haz clic en cada referencia para desplegar su información.")
    with st.expander("Sphaera E (2024)"):
        st.write("Modelo basado en IA para detección temprana de dificultades lectoras en primaria. Mejora la precisión diagnóstica frente a métodos tradicionales.")
    with st.expander("Alejandra P, Cevallos E (2024)"):
        st.write("Ensayo sobre el impacto de la IA en la detección temprana de trastornos del aprendizaje. Revisión sistemática de 15 fuentes académicas.")
    with st.expander("Espinosa P (2024)"):
        st.write("Revisión sistemática sobre IA en la detección de dislexia, discalculia y TDAH. Señala beneficios y limitaciones éticas y metodológicas.")
    with st.expander("García M (2025)"):
        st.write("Uso de machine learning para predecir estudiantes en riesgo de bajo rendimiento académico. Alta precisión en modelos supervisados.")
    with st.expander("NeurekaLAB (2023)"):
        st.write("Plataforma gamificada con IA para detectar dislexia y TDAH mediante minijuegos interactivos. Precisión superior al 90%.")
    with st.expander("Verzosi et al. (2025)"):
        st.write("Revisión sobre IA en educación infantil. Oportunidades y riesgos como dependencia tecnológica y problemas de privacidad.")
    with st.expander("Vargas G (2024)"):
        st.write("Aplicación de IA en enseñanza-aprendizaje. Beneficios en personalización y retos como brecha digital y necesidad de marcos regulatorios.")
    with st.expander("Gómez A et al. (2024)"):
        st.write("Explora desafíos éticos de la IA en la personalización del aprendizaje: equidad, protección de datos y diversidad educativa.")
    with st.expander("Martínez B (2025)"):
        st.write("Impacto de la IA generativa en enseñanza-aprendizaje. Beneficios y riesgos, necesidad de normativas claras y formación docente.")

