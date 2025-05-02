# browser-use-linkedin-agent

Automatiza tareas en LinkedIn y otros sitios web usando la herramienta `browser_use` basada en Playwright.

## Requisitos previos

- Python 3.8+
- [Playwright](https://playwright.dev/python/)
- Instalar dependencias del proyecto (ver más abajo)

## Instalación

Instala Playwright y las dependencias necesarias:

```bash
pip install -r requirements.txt
playwright install
```

## Uso de `browser_use`

`browser_use` permite automatizar acciones en el navegador para pruebas y scraping. Ejemplo básico:

```python
from browser_use import Browser

browser = Browser()
browser.open("https://example.com")
browser.click("#button-id")
browser.type("#input-id", "example text")
browser.close()
```

Consulta la [documentación oficial de `browser_use`](https://pypi.org/project/browser-use/) para más detalles.

## Ejemplo: `agent.py`

El archivo `agent.py` demuestra cómo automatizar tareas en el navegador:

- Inicializa el navegador.
- Abre una página web.
- Realiza acciones (clics, escritura, etc.).
- Cierra el navegador.

Para ejecutar el ejemplo:

```bash
python agent.py
```

Asegúrate de haber instalado todas las dependencias antes de ejecutar el script.

## Contribuciones

¿Tienes sugerencias o mejoras? ¡Las contribuciones son bienvenidas! Abre un issue o pull request.

## Licencia

Este proyecto está bajo la licencia MIT.