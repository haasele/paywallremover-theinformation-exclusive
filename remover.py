import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from bs4 import BeautifulSoup  # Zum Extrahieren von Text aus HTML

def extract_article_from_json_selenium(url):
    # Chrome Optionen für den Browser
    chrome_options = Options()
    # Entferne den headless-Modus und füge Optionen für das Logging hinzu, falls benötigt
    # chrome_options.add_argument("--headless")  # Für sichtbar Modus, falls nötig

    # Starte den Chrome WebDriver mit den Optionen
    driver = webdriver.Chrome(options=chrome_options)

    try:
        driver.get(url)

        # Warte, bis das spezifische Element geladen ist
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//script[@data-component-name="Article"]')))
        
        # Finde das Skript-Tag mit den Artikeldaten
        script_tag = driver.find_element(By.XPATH, '//script[@data-component-name="Article"]')
        script_content = script_tag.get_attribute('innerHTML')
    except Exception as e:
        print(f"Fehler beim Laden der Seite oder Extrahieren des Artikels: {e}")
        driver.quit()
        return None

    # Beende die Browser-Instanz nach dem Abrufen der Daten
    driver.quit()

    try:
        # Versuche, den JSON-Inhalt zu extrahieren
        json_data = json.loads(script_content)
        article_data = json_data.get("article", {})
        title = article_data.get("title", "Kein Titel verfügbar")
        authors = ", ".join([author["name"] for author in article_data.get("authors", [])])
        blurb_html = article_data.get("freeBlurb", "Kein Artikelinhalt verfügbar")
        
        # Bereinige den HTML-Text im "blurb"-Feld
        blurb_text = clean_html(blurb_html)
        
        # Formatierte Ausgabe mit mehr Details und schöner Formatierung
        formatted_result = f"""
        Artikel Informationen:
        -----------------------
        Titel: {title}
        Autoren: {authors}
        
        Artikel:
        {blurb_text}
        """
        return formatted_result

    except json.JSONDecodeError as e:
        return f"Fehler beim Parsen des JSON-Inhalts: {str(e)}"

# Funktion zum Bereinigen von HTML-Tags aus dem Text
def clean_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()  # Entfernt alle HTML-Tags und gibt nur den Text zurück

# Hauptfunktion, die die URL akzeptiert und das Ergebnis ausgibt
def main():
    url = input("Bitte die URL des Artikels eingeben: ")  # Benutzer gibt die URL ein
    result = extract_article_from_json_selenium(url)
    if result:
        print(result)
    else:
        print("Es gab ein Problem beim Extrahieren des Artikels.")

# Aufruf der Hauptfunktion
if __name__ == "__main__":
    main()