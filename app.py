
import streamlit as st
from scraper import generar_excel
import datetime

st.title("Scraping Tarifas de Electricidad")

distribuidora = st.selectbox("Selecciona distribuidora", ["Pluz Energia Perú", "Luz del Sur"])
actualizacion = st.selectbox("Selecciona actualización", ["Última actualización", "Penúltima actualización"])

if distribuidora == "Pluz Energia Perú":
    if st.button("Generar Excel"):
        with st.spinner("Generando archivo, por favor espera..."):
            excel_file = generar_excel(actualizacion)
            st.success("Archivo generado con éxito.")
            st.download_button(
                label="Descargar Excel",
                data=excel_file,
                file_name=f"tarifas_{datetime.date.today()}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
elif distribuidora == "Luz del Sur":
    st.warning("Funcionalidad aún no implementada para Luz del Sur.")
