import streamlit as st
import pandas as pd

# Configuración general
st.set_page_config(page_title="IA en la detección temprana", layout="wide")

# Sidebar de navegación
st.sidebar.title("Navegación")
pagina = st.sidebar.radio(
    "Selecciona una sección:",
    ["Resumen", "Conceptos clave", "Beneficios", "Desafíos", "Conclusiones", "Artículos relacionados", "Referencias"]
)

# Título principal
st.title("El impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje")
st.markdown("<p style='text-align:right; font-style:italic;'>La inteligencia artificial no reemplaza al docente, lo potencia: abre caminos para que cada estudiante alcance su máximo potencial.</p>", unsafe_allow_html=True)

# Contenido según la página seleccionada
if pagina == "Resumen":
    st.header("Resumen")
    st.markdown("""
    La IA permite identificar señales de dislexia, problemas de atención y dificultades lectoras mediante el análisis de datos académicos y patrones de comportamiento. 
    Esto facilita intervenciones más rápidas y personalizadas, promoviendo una educación inclusiva.
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

elif pagina == "Beneficios":
    st.header("Beneficios")
    st.markdown("""
    - Mayor precisión y rapidez  
    - Personalización del aprendizaje  
    - Reducción de sesgos humanos
    """)

elif pagina == "Desafíos":
    st.header("Desafíos")
    st.markdown("""
    - Privacidad de datos  
    - Riesgos de sesgo en algoritmos  
    - Necesidad de capacitación docente  
    - Evitar la deshumanización
    """)

elif pagina == "Conclusiones":
    st.header("Conclusiones")
    st.markdown("""
    La IA mejora la detección temprana y promueve la educación inclusiva, 
    pero debe equilibrarse con valores humanos y ética educativa.
    """)

elif pagina == "Artículos relacionados":
    st.subheader("Artículos relacionados")
    articulos = {
        "Espinosa (2024)": "Revisión sistemática sobre IA en la detección de dislexia, discalculia y TDAH.",
        "NeurekaLAB (2023)": "Plataforma gamificada para detección temprana con IA y minijuegos.",
        "García (2025)": "Modelos predictivos de rendimiento académico mediante machine learning."
    }
    opcion = st.selectbox("Selecciona un artículo:", list(articulos.keys()))
    st.info(articulos[opcion])

elif pagina == "Referencias":
    st.subheader("Referencias bibliográficas")
    with st.expander("Espinosa (2024)"):
        st.write("""
        El artículo presenta una revisión sistemática sobre el uso de la IA para la detección temprana de trastornos del aprendizaje. 
        Señala beneficios en precisión diagnóstica, pero también limitaciones éticas y metodológicas.
        """)
    with st.expander("NeurekaLAB (2023)"):
        st.write("""
        Plataforma gamificada que utiliza IA y minijuegos para detectar dislexia, TDAH y dificultades visoespaciales, 
        con precisión superior al 90 % en estudios iniciales.
        """)
    with st.expander("García (2025)"):
        st.write("""
        Analiza modelos predictivos de rendimiento académico mediante machine learning, 
        destacando su potencial para mejorar la retención escolar y el rendimiento.
        """)

