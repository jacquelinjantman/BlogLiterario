
from os import link
import re

import streamlit as st
import streamlit.components.v1 as components

from estilos import aplicar_estilo
from libros import BOOKS, GENRES, PLAYLIST_GENERAL
from textos import UI



st.set_page_config(
    page_title="Entre Páginas y Hechizos",
    page_icon="🌙",
    layout="wide"
)

def mostrar_portada(libro):
   
    if libro["cover"]:
        st.image(libro["cover"])
    else:
        with st.container(border=True, height=250):
            st.markdown("# 📖")


def mostrar_playlist(link, alto=352):
   

    m = re.search(
        r"(playlist|album|track)/([A-Za-z0-9]+)",
        link or ""
    )

    if m:
        src = f"https://open.spotify.com/embed/{m.group(1)}/{m.group(2)}?theme=0"

        if hasattr(st, "iframe"):
            st.iframe(src, height=alto)
        else:
            components.iframe(src, height=alto)


col_idioma, col_modo = st.columns([3, 2])
with col_idioma:
    lang = st.radio(
        "Idioma / Idioma",
        ["es", "pt"],
        format_func=lambda x: {"es": "Español", "pt": "Português (BR)"}[x],
        horizontal=True,
    )
t = UI[lang]
with col_modo:
    noche = st.toggle(t["night"], value=True)
aplicar_estilo(noche)

st.title(f"{'🌙' if noche else '🌿'} Entre Páginas y Hechizos")


id_elegido = st.query_params.get("libro")
libro_elegido = next((b for b in BOOKS if b["id"] == id_elegido), None)

if libro_elegido:
    # ===== PÁGINA DEL LIBRO =====
    if st.button(t["back"]):
        st.query_params.clear()
        st.rerun()

    col_foto, col_texto = st.columns([1, 2])
    with col_foto:
        mostrar_portada(libro_elegido)
    with col_texto:
        st.header(libro_elegido["title"])
        st.caption(f"{libro_elegido['author']} · {GENRES[libro_elegido['genre']][lang]}")
        estrellas = "★" * libro_elegido["stars"] + "☆" * (5 - libro_elegido["stars"])
        st.markdown(f"<div class='estrellas'>{estrellas}</div>", unsafe_allow_html=True)
        st.subheader(t["summary"])
        st.write(libro_elegido["summary"][lang])
        st.subheader(t["opinion"])
        st.write(libro_elegido["review"][lang])
    if libro_elegido.get("playlist"):
        st.subheader(t["playlist_book"])
        mostrar_playlist(libro_elegido["playlist"])
else:
    # ===== PÁGINA DE INICIO =====
    st.write(t["tagline"])

    genero = st.pills(
        t["genres"],
        ["all", *GENRES],
        default="all",
        format_func=lambda g: t["all"] if g == "all" else GENRES[g][lang],
    ) or "all"

    mostrar = [b for b in BOOKS if genero == "all" or b["genre"] == genero]
    if not mostrar:
        st.info(t["empty"])

    # Los libros se acomodan de a 3 por fila
    for i in range(0, len(mostrar), 3):
        columnas = st.columns(3)
        for col, libro in zip(columnas, mostrar[i : i + 3]):
            with col:
                mostrar_portada(libro)
                if st.button(libro["title"], key=libro["id"]):
                    st.query_params["libro"] = libro["id"]
                    st.rerun()
    st.divider()

if PLAYLIST_GENERAL:
    st.subheader("🎵 Playlist para leer")

    st.link_button(
        "🎧 Abrir playlist en Spotify",
        PLAYLIST_GENERAL
    )