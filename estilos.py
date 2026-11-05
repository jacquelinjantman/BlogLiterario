
import base64
from pathlib import Path

import streamlit as st

CARPETA = Path(__file__).parent


@st.cache_data
def imagen_base64(nombre):
    
    ruta = CARPETA / "portadas" / nombre
    return "data:image/png;base64," + base64.b64encode(ruta.read_bytes()).decode()


def particulas(puntos, tam):
   
    return ",".join(
        f"radial-gradient({tam}px {tam}px at {x}% {y}%, {c}, transparent)"
        for x, y, c in puntos
    )


def castillo_svg(cuerpo, ventanas):
   
    svg = (
        "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 330 200'>"
        f"<g fill='{cuerpo}'><rect x='20' y='100' width='50' height='100'/>"
        "<polygon points='15,100 45,55 75,100'/>"
        "<rect x='90' y='120' width='170' height='80'/>"
        "<rect x='140' y='50' width='50' height='150'/>"
        "<polygon points='135,50 165,5 195,50'/>"
        "<rect x='250' y='90' width='55' height='110'/>"
        "<polygon points='245,90 277,45 310,90'/></g>"
        f"<g fill='{ventanas}'><rect x='160' y='90' width='10' height='18'/>"
        "<rect x='40' y='130' width='8' height='14'/>"
        "<rect x='272' y='125' width='8' height='14'/>"
        "<rect x='110' y='150' width='8' height='14'/></g></svg>"
    )
    return f'url("data:image/svg+xml;utf8,{svg}")'



NOCHE = {
    "fondo": "radial-gradient(ellipse at 50% 108%, rgba(243,220,154,.5), transparent 55%),"
    "radial-gradient(ellipse at 25% 45%, rgba(29,92,134,.8), transparent 55%),"
    "radial-gradient(ellipse at 90% 0%, #1a2f6b, transparent 50%), #070b1f",
    "p1": particulas([(10, 20, "#f0c05a"), (30, 75, "#f6ecd2"), (55, 35, "#f0c05a"), (80, 65, "#f6ecd2"), (92, 15, "#f0c05a")], 2),
    "p2": particulas([(20, 50, "#f6ecd2"), (45, 10, "#f0c05a"), (65, 85, "#f6ecd2"), (88, 45, "#f0c05a"), (5, 90, "#f6ecd2")], 2),
    "anim": "brillar 4s ease-in-out infinite alternate",
    "texto": "#f6ecd2",
    "acento": "#f0c05a",
    "sobre": "#0a1030",
    "card": "rgba(9,14,40,.78)",
    "borde": "rgba(240,192,90,.45)",
    "boton": "rgba(20,32,74,.85)",
    "brillo": "rgba(240,192,90,.35)",
    "dragonfx": "drop-shadow(0 0 8px rgba(240,192,90,.75))",
    "castillo": castillo_svg("%23060a1c", "%23f0c05a"),
}


DIA = {
    "fondo": "radial-gradient(ellipse at 15% 0%, #fff7c8, transparent 50%),"
    "radial-gradient(ellipse at 85% 15%, rgba(255,224,140,.6), transparent 45%),"
    "linear-gradient(180deg, #d6e8a6 0%, #92c077 55%, #3f7342 100%)",
    "p1": particulas([(12, 25, "#fff4b0"), (28, 70, "#ffe48a"), (52, 40, "#fff4b0"), (75, 60, "#ffe48a"), (90, 20, "#fff4b0")], 5),
    "p2": particulas([(22, 55, "#ffe48a"), (40, 15, "#fff4b0"), (62, 80, "#ffe48a"), (85, 40, "#fff4b0"), (6, 85, "#ffe48a")], 4),
    "anim": "flotar 12s ease-in-out infinite alternate",
    "texto": "#1d3a25",
    "acento": "#9a5e0f",
    "sobre": "#fff8dc",
    "card": "rgba(250,247,226,.86)",
    "borde": "rgba(154,94,15,.5)",
    "boton": "rgba(255,250,228,.92)",
    "brillo": "rgba(255,200,90,.5)",
    "dragonfx": "drop-shadow(0 6px 8px rgba(0,0,0,.35))",
    "castillo": castillo_svg("%23587a5a", "%23ffd27a"),
}

FUENTES = "@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=Cormorant+Garamond:ital,wght@0,500;0,700;1,500&family=Great+Vibes&display=swap');"


def aplicar_estilo(noche):
  
    modo = "noche" if noche else "dia"
    paleta = NOCHE if noche else DIA
    variables = ";".join(f"--{nombre}:{valor}" for nombre, valor in paleta.items())
    variables += f';--dragon:url("{imagen_base64("dragon.png")}")'
    adornos = f"<div class='astro {modo}'></div><div class='castillo'></div><div class='dragon'></div>"
    if not noche:  # el hada solo vuela de día
        variables += f';--hada:url("{imagen_base64("hada.png")}")'
        adornos += "<div class='hada'></div>"
    css = (CARPETA / "estilos.css").read_text(encoding="utf-8")
    st.markdown(
        f"<style>{FUENTES}:root{{{variables}}}{css}</style>{adornos}",
        unsafe_allow_html=True,
    )