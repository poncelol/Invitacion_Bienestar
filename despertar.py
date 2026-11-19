"""
Despertador de la app de Streamlit Community Cloud.

GitHub Actions lo ejecuta cada pocas horas (ver .github/workflows/despertador.yml).
Abre la app en un navegador automático; si Streamlit la durmió, da clic en el
botón "Yes, get this app back up!" y espera a que arranque.

No forma parte de la app: NO se agrega a requirements.txt.
"""

import os
import sys

from playwright.sync_api import TimeoutError as PlaywrightTimeout
from playwright.sync_api import sync_playwright

APP_URL = os.environ.get("APP_URL", "").strip()
TEXTO_BOTON = "get this app back up"


def buscar_boton(page):
    """Busca el botón de despertar en la página y en sus iframes."""
    for frame in [page.main_frame, *page.frames]:
        boton = frame.get_by_role("button", name=TEXTO_BOTON)
        try:
            if boton.count() > 0:
                return boton.first
        except Exception:
            pass
    return None


def main():
    if not APP_URL:
        print("Falta la variable APP_URL.")
        sys.exit(1)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        print(f"Abriendo {APP_URL}")
        page.goto(APP_URL, wait_until="domcontentloaded", timeout=90_000)

        # Damos tiempo a que cargue la página de Streamlit
        page.wait_for_timeout(15_000)

        boton = buscar_boton(page)
        if boton is None:
            print("La app ya estaba despierta.")
        else:
            print("La app estaba dormida: la despierto.")
            boton.click()
            # Esperamos a que desaparezca el botón (la app arrancando)
            try:
                boton.wait_for(state="detached", timeout=180_000)
                print("Listo, la app está arrancando.")
            except PlaywrightTimeout:
                print("Di clic, pero el botón sigue visible. Revisa la app.")
                browser.close()
                sys.exit(1)
            page.wait_for_timeout(30_000)

        browser.close()


if __name__ == "__main__":
    main()
