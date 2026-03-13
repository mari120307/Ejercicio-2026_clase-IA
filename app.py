import streamlit as st

# Configuración general
st.set_page_config(page_title="IA en la detección temprana", layout="wide")

# Estilos CSS para bordes redondeados, tipografía y modal vintage
st.markdown("""
    <style>
    .rounded-box {
        border-radius: 15px;
        padding: 20px;
        background-color: #f9f9f9;
        margin-bottom: 20px;
    }
    .modal {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255,255,255,0.9);
        backdrop-filter: blur(6px);
        border: 2px solid #ccc;
        border-radius: 12px;
        padding: 20px;
        z-index: 9999;
        width: 60%;
        font-family: 'Georgia', serif;
    }
    </style>
""", unsafe_allow_html=True)

# Título y frase motivadora
st.title("El impacto de la inteligencia artificial en la detección temprana de trastornos del aprendizaje")
st.markdown("<p style='text-align:right; font-style:italic;'>La inteligencia artificial no reemplaza al docente, lo potencia: abre caminos para que cada estudiante alcance su máximo potencial.</p>", unsafe_allow_html=True)

# Apartados principales
st.header("Resumen")
st.markdown("<div class='rounded-box'>La IA permite identificar señales de dislexia, problemas de atención y dificultades lectoras mediante el análisis de datos académicos y patrones de comportamiento. Esto facilita intervenciones más rápidas y personalizadas, promoviendo una educación inclusiva.</div>", unsafe_allow_html=True)

st.header("Conceptos clave")
conceptos = {
    "Trastornos del aprendizaje": "Dificultades específicas en lectura, escritura, atención o procesamiento de información.",
    "Detección temprana": "Identificación de señales iniciales para intervenir antes de que se agraven.",
    "Educación inclusiva": "Modelo que atiende la diversidad de estudiantes.",
    "Ética en IA": "Privacidad, transparencia y uso responsable de datos educativos."
}
for k,v in conceptos.items():
    st.markdown(f"<div class='rounded-box'><b>{k}:</b> {v}</div>", unsafe_allow_html=True)

st.header("Beneficios")
st.markdown("- Mayor precisión y rapidez\n- Personalización del aprendizaje\n- Reducción de sesgos humanos")

st.header("Desafíos")
st.markdown("- Privacidad de datos\n- Riesgos de sesgo en algoritmos\n- Necesidad de capacitación docente\n- Evitar la deshumanización")

st.header("Conclusiones")
st.markdown("La IA mejora la detección temprana y promueve la educación inclusiva, pero debe equilibrarse con valores humanos y ética educativa.")

# Botón desplegable de artículos relacionados
st.subheader("Artículos relacionados")
articulos = {
    "Espinosa (2024)": "Revisión sistemática sobre IA en la detección de dislexia, discalculia y TDAH.",
    "NeurekaLAB (2023)": "Plataforma gamificada para detección temprana con IA y minijuegos.",
    "García (2025)": "Modelos predictivos de rendimiento académico mediante machine learning."
}
opcion = st.selectbox("Selecciona un artículo:", list(articulos.keys()))
st.info(articulos[opcion])

# Referencias interactivas (simulación de modal)
st.subheader("Referencias interactivas")
if st.button("Ver referencia: Espinosa (2024)"):
    st.markdown("""
        <div class='modal'>
        <h4>Espinosa (2024)</h4>
        <p>El artículo presenta una revisión sistemática sobre el uso de la IA para la detección temprana de trastornos del aprendizaje. 
        Señala beneficios en precisión diagnóstica, pero también limitaciones éticas y metodológicas.</p>
        </div>
    """, unsafe_allow_html=True)
