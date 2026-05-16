# 🛡️ Subdominator 

**Subdominator** es una herramienta para investigadores de seguridad y equipos Red Team que permite identificar subdominios activos y detectar contenido potencialmente útil para pentesting, como paneles de login, APIs expuestas o formularios sensibles.

> ⚔️ Creado por [Haak Cybersecurity Consulting](https://haak.com.mx) — Seguridad que actúa, no solo advierte.

## 🎯 ¿Qué hace?

- Enumera subdominios a partir de una wordlist.
- Verifica si están activos (`200`, `301`, `302`, `403`, `401`).
- Extrae contenido HTML y busca indicadores como:
  - Formularios
  - Palabras clave: `login`, `admin`, `api`, `dashboard`, etc.
- Resalta subdominios listos para evaluación ofensiva.

## 🚀 Instalación

Requiere Python 3.7+

```bash
git clone https://github.com/tuusuario/subdominator.git
cd subdominator
pip install -r requirements.txt
```

## ⚙️ Uso

```bash
python3 subdominator.py -d example.com -w subdomains.txt -t 50
```

### Argumentos:
- `-d`, `--domain`: Dominio objetivo (ej. `example.com`)
- `-w`, `--wordlist`: Archivo con lista de subdominios (sin el dominio)
- `-t`, `--threads`: Número de hilos para ejecución concurrente (opcional, default: 20)

## 📌 Ejemplo de salida

```bash
[+] login.example.com - Status: 200 | Found: login, form_detected
[+] api.example.com - Status: 403 | Found: api
[+] devpanel.example.com - Status: 200 | Found: admin, dashboard, form_detected
```

## 💡 Casos de uso

- Reconocimiento en pruebas de penetración.
- Identificación rápida de superficies expuestas.
- Automatización de análisis inicial en bug bounty o auditorías web.

## 👨‍💻 Autor

[Haak Cybersecurity Consulting](https://haak.com.mx)

## ⚠️ Aviso legal

Este proyecto es solo para fines educativos y pruebas controladas. No lo uses en infraestructuras sin autorización. Haak Consulting no se responsabiliza por usos indebidos.

---

Made with 💻 by Alan Contreras - Haak Cybersecurity Consulting
