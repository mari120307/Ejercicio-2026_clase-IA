import streamlit as st
import pandas as pd

# Configuración general
st.set_page_config(page_title="IA en la detección temprana", layout="wide")

# Sidebar de navegación
st.sidebar.title("Navegación")
pagina = st.sidebar.radio(
    "Selecciona una sección:",
    ["Introducción", "Resumen", "Conceptos clave", "Beneficios", "Desafíos", "Perspectivas futuras", "Rol docente", "Conclusiones", "Artículos relacionados", "Referencias"]
)

# Título principal
st.title("El impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje")
st.markdown("<p style='text-align:right; font-style:italic;'>La inteligencia artificial no reemplaza al docente, lo potencia: abre caminos para que cada estudiante alcance su máximo potencial.</p>", unsafe_allow_html=True)

# Contenido según la página seleccionada
if pagina == "Introducción":
    st.header("Introducción")
    st.markdown("""
    La inteligencia artificial (IA) está transformando la educación al permitir la detección temprana de trastornos del aprendizaje. 
    Tradicionalmente, los métodos de observación y pruebas estandarizadas eran lentos y podían pasar por alto señales sutiles. 
    Hoy, la IA analiza grandes volúmenes de datos y reconoce patrones complejos, mejorando la precisión diagnóstica y facilitando intervenciones personalizadas.
    """)

elif pagina == "Resumen":
    st.header("Resumen")
    st.markdown("""
    La IA permite identificar señales de dislexia, problemas de atención y dificultades lectoras mediante el análisis de datos académicos y patrones de comportamiento. 
    Esto facilita intervenciones más rápidas y personalizadas, promoviendo una educación inclusiva.  
    Sin embargo, se subraya la importancia de un uso ético, consciente y complementario al trabajo docente.
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
    st.header("Beneficios de la IA en la detección temprana")
    st.markdown("""
    - Mayor precisión y rapidez en diagnósticos  
    - Personalización del aprendizaje  
    - Reducción de sesgos humanos  
    - Evaluaciones continuas del desempeño estudiantil  
    """)

elif pagina == "Desafíos":
    st.header("Desafíos y consideraciones éticas")
    st.markdown("""
    - Privacidad de datos y transparencia algorítmica  
    - Riesgos de sesgo en algoritmos  
    - Necesidad de capacitación docente  
    - Evitar la deshumanización del proceso educativo  
    """)

elif pagina == "Perspectivas futuras":
    st.header("Perspectivas futuras")
    st.markdown("""
    - Adaptación de la IA a distintos contextos culturales y educativos  
    - Evaluación de la efectividad a largo plazo  
    - Innovaciones en aulas virtuales y educación inclusiva  
    - Integración con neurociencia y gamificación para mejorar diagnósticos  
    """)

elif pagina == "Rol docente":
    st.header("Percepción y rol de los docentes")
    st.markdown("""
    - Actitudes frente al uso de IA en el aula  
    - Integración en la práctica pedagógica  
    - IA como complemento del trabajo docente, nunca como sustituto  
    """)

elif pagina == "Conclusiones":
    st.header("Conclusiones")
    st.markdown("""
    La IA mejora la detección temprana de trastornos del aprendizaje y promueve la educación inclusiva.  
    Sin embargo, requiere un equilibrio entre innovación tecnológica y valores humanos, garantizando ética, transparencia y respeto a la diversidad.  
    """)

elif pagina == "Artículos relacionados":
    st.subheader("Artículos relacionados")
    articulos = {
        "Espinosa (2024)": "Revisión sistemática sobre IA en la detección de dislexia, discalculia y TDAH.",
        "NeurekaLAB (2023)": "Plataforma gamificada para detección temprana con IA y minijuegos.",
        "García (2025)": "Modelos predictivos de rendimiento académico mediante machine learning.",
        "Verzosi et al. (2025)": "Uso de IA en educación infantil, riesgos y oportunidades.",
        "Vargas (2024)": "IA como herramienta para optimizar procesos de enseñanza-aprendizaje."
    }
    opcion = st.selectbox("Selecciona un artículo:", list(articulos.keys()))
    st.info(articulos[opcion])

elif pagina == "Referencias":
    st.subheader("Referencias bibliográficas")
    with st.expander("Espinosa (2024)"):
        st.write("Revisión sistemática sobre IA en la detección temprana de dislexia, discalculia y TDAH. Señala beneficios en precisión diagnóstica, pero también limitaciones éticas y metodológicas.")
    with st.expander("NeurekaLAB (2023)"):
        st.write("Plataforma gamificada que utiliza IA y minijuegos para detectar dislexia, TDAH y dificultades visoespaciales, con precisión superior al 90 % en estudios iniciales.")
    with st.expander("García (2025)"):
        st.write("Analiza modelos predictivos de rendimiento académico mediante machine learning, destacando su potencial para mejorar la retención escolar y el rendimiento.")
    with st.expander("Verzosi et al. (2025)"):
        st.write("Revisión sistemática sobre IA en educación infantil, identificando oportunidades y riesgos como dependencia tecnológica y problemas de privacidad.")
    with st.expander("Vargas (2024)"):
        st.write("Analiza la aplicación de IA en procesos de enseñanza-aprendizaje, destacando beneficios y desafíos como la brecha digital y la necesidad de marcos regulatorios claros.")

