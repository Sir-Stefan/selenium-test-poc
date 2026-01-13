# Selenium Test Automation – Proof of Concept

## Ziel
Dieses Projekt dient als Proof of Concept zur Demonstration grundlegender
Kenntnisse in der automatisierten Softwaretestung mit Selenium und Python.

## Technologien
- Python 3
- Selenium WebDriver
- pytest
- webdriver-manager
- Page Object Pattern

## Testumfang
- Automatisierter UI-Test einer stabilen Beispiel-Webseite
- Prüfung von Seitentitel und Textinhalten
- Strukturierte Trennung von Testlogik und Seitenobjekten

## Projektstruktur
- tests/: Testfälle
- pages/: Page Objects
- utils/: Hilfsfunktionen (Driver Setup)

## Ausführung
```bash
pip install -r requirements.txt
pytest
