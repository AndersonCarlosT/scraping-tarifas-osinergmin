import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import io

def generar_excel(actualizacion="Última actualización"):
    chrome_options = Options()
    chrome_options.binary_location = "/usr/bin/chrome-linux64/chrome"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    service = Service("/usr/bin/chromedriver-linux64/chromedriver")
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 20)

    regiones = [
        {"id": "150000", "indices": [0, 4, 18, 21, 23, 13, 7, 5, 9, 6, 8, 31, 29, 1, 3, 2],
         "nombres": ["Lima norte", "Huacho", "Supe-Barranca", "Huaral-Chancay", "Pativilca",
                     "Churín", "Ravira-Pacaraos", "Canta", "Yaso", "Hoyos-Acos", "Sayán-Humaya", 
                     "SER Chillón", "Valle del Caral", "Lima Sur", "Cañete", "Lunahuaná"]},
    ]

    df_final = pd.DataFrame()

    for region in regiones:
        url = f"https://www.osinergmin.gob.pe/Tarifas/Electricidad/PliegoTarifario?Id={region['id']}"
        
        for idx, nombre in zip(region["indices"], region["nombres"]):
            print(f"Extrayendo datos de: {nombre} (índice {idx}) | URL ID: {region['id']}")
            
            driver.get(url)
            time.sleep(4)
            
            select_depa = Select(wait.until(EC.presence_of_element_located((By.ID, "DDLSE"))))
            select_depa.select_by_index(idx)

            time.sleep(4)
            select_fecha = Select(driver.find_element(By.ID, "DDLFecha"))
            if actualizacion == "Última actualización":
                select_fecha.select_by_index(0)
            else:
                select_fecha.select_by_index(1)

            time.sleep(4)
            tabla = driver.find_element(By.ID, "TbPliego")
            html_tabla = tabla.get_attribute('outerHTML')
            df = pd.read_html(html_tabla)[0]

            columna_d = df.iloc[4:190, 3].reset_index(drop=True)
            df_final[nombre] = columna_d

    driver.quit()

    # Guardar a buffer de bytes para streamlit
    output = io.BytesIO()
    df_final.to_excel(output, index=False)
    output.seek(0)
    return output.read()
