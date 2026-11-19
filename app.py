"""
Contraportada de registro · Alimentación para el Bienestar
Arriba: diseño institucional con toda la información del evento.
El proveedor elige su horario en tus tarjetas y abajo aparece Bookings YA con ese horario
(enlace directo al servicio). Bookings hace el cupo, el correo y el calendario.

Ejecutar:  streamlit run app.py
No necesita secretos.
"""
import streamlit as st
import streamlit.components.v1 as components

# ─────────────── CONFIGURACIÓN: cambia aquí tus datos ───────────────
PAGINA = "https://bookings.cloud.microsoft/book/RegistrodeProveedoresAbarrotes@alimentacionbienestar.gob.mx/"
# Enlace directo de cada horario (Bookings > Servicios > "Página de reserva de servicio")
HORARIOS = {
    "11:00 a 12:00": PAGINA + "s/rOjGrpx8GUmoMs0ht5kNDw2?ismsaljsauthenabled",
    "13:00 a 14:00": PAGINA + "s/gGQ5tkmrlEmIo5XD-w9DXQ2?ismsaljsauthenabled",
    "15:00 a 16:00": PAGINA + "s/FmkSeZnzYkOC_0vVg_FTSA2?ismsaljsauthenabled",
    "17:00 a 18:00": PAGINA + "s/cetFubhcRE2MfkcZyNOWpQ2?ismsaljsauthenabled",
}
BOOKINGS = PAGINA + "?ismsaljsauthenabled"   # página completa (respaldo)
TITULO = "Registro de Asistencia - Proveedores Abarrotes PAR 2027"
EVENTO = "Mesa de trabajo con proveedores para bienes a comercializar"
PROGRAMA = "Programa de Abasto Rural 2027"
FECHA = "15 de enero de 2027"
# Bookings se muestra recortado: arriba se oculta su encabezado y la tarjeta del horario,
# abajo se oculta el pie de Microsoft. Valores medidos con la página actual de Bookings;
# si cambias el nombre de la página o los textos de Bookings, ajústalos.
RECORTE = 330            # px ocultos arriba en computadora/tableta
RECORTE_CELULAR = 366    # px ocultos arriba en celular
ALTO_BOOKINGS = 960      # px visibles en computadora/tableta (con la fecha elegida, termina justo antes del pie de Microsoft)
ALTO_CELULAR = 958       # px visibles en celular
# ─────────────────────────────────────────────────────────────────────

BANDA, DORADO, GUINDA = "#4A0E25", "#BC955C", "#9D2449"

LOGO = f"""<svg width="46" height="46" viewBox="0 0 120 120" role="img" aria-label="Alimentación para el Bienestar">
<defs>
 <linearGradient id="c" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#EAD39B"/><stop offset="1" stop-color="#C9A563"/></linearGradient>
 <linearGradient id="o" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#C99A3F"/><stop offset="1" stop-color="#8F6A22"/></linearGradient>
 <clipPath id="k"><rect x="28" y="8" width="64" height="84"/></clipPath>
</defs>
<g clip-path="url(#k)">
 <rect x="28" y="8" width="64" height="84" fill="url(#c)"/>
 <path stroke="{BANDA}" stroke-width="2.4" d="M60 60 L20 40 M60 60 L20 10 M60 60 L42 0 M60 60 L60 0 M60 60 L78 0 M60 60 L100 10 M60 60 L100 40"/>
 <circle cx="60" cy="58" r="17" fill="url(#o)" stroke="{BANDA}" stroke-width="2.6"/>
 <g stroke="{BANDA}" stroke-width="2.6">
  <path d="M20 56 C40 58 54 70 60 96 L20 96 Z" fill="url(#c)"/><path d="M100 56 C80 58 66 70 60 96 L100 96 Z" fill="url(#c)"/>
  <path d="M20 66 C38 68 52 78 60 96 L20 96 Z" fill="#B88A3A"/><path d="M100 66 C82 68 68 78 60 96 L100 96 Z" fill="#B88A3A"/>
  <path d="M20 76 C36 78 50 86 60 96 L20 96 Z" fill="url(#c)"/><path d="M100 76 C84 78 70 86 60 96 L100 96 Z" fill="url(#c)"/>
 </g>
</g>
<path d="M14 93 Q60 116 106 89 Q62 106 14 93 Z" fill="url(#o)"/>
</svg>"""

st.set_page_config(page_title=TITULO, page_icon=":material/how_to_reg:", layout="centered")

st.markdown(f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, .stApp {{ font-family: 'Inter', system-ui, 'Segoe UI', sans-serif; background: #f7f4f1; }}
html, body, .stApp, [data-testid="stAppViewContainer"], [data-testid="stMain"] {{ overflow-x: hidden !important; }}
.block-container {{ padding-top: .5rem !important; max-width: 820px; }}
#MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {{ display: none !important; }}
header[data-testid="stHeader"] {{ background: transparent; pointer-events: none; }}
.hero {{ position: relative; background: {BANDA}; padding: 24px 0 26px; margin-bottom: 24px;
  box-shadow: 0 0 0 100vmax {BANDA}; clip-path: inset(-100vmax -100vmax 0 -100vmax); }}
.hero::after {{ content: ""; position: absolute; left: -100vmax; right: -100vmax; bottom: 0; height: 4px; background: {DORADO}; }}
.marca {{ display: flex; align-items: center; gap: 12px; margin-bottom: 14px; }}
.marca .sep {{ width: 1px; align-self: stretch; background: rgb(255 255 255 / .45); }}
.marca b {{ font-size: 1.5rem; font-weight: 800; color: #fff; line-height: 1.1; }}
.hero .dir {{ font-size: 1.9rem; font-weight: 800; color: #fff; line-height: 1.15; }}
.hero .ger {{ margin-top: 4px; font-size: 1.15rem; font-weight: 700; color: #fff; }}
.hero .sub {{ margin-top: 2px; font-size: 1rem; font-weight: 700; color: {DORADO}; }}
.titulo {{ font-size: 1.7rem !important; font-weight: 800; color: #1f2937; margin: 0 0 4px !important; line-height: 1.2; }}
.evento {{ font-size: 1.05rem !important; color: #4b5563; margin: 0 0 18px; }}
.tarjeta {{ background: #fff; border-radius: 14px; border: 1px solid #ece4da; padding: 18px 20px; margin-bottom: 16px;
  box-shadow: 0 1px 3px rgb(0 0 0 / .05); }}
.fecha {{ display: flex; flex-wrap: wrap; align-items: baseline; gap: 4px 14px; }}
.fecha b {{ font-size: 1.35rem; color: {GUINDA}; }}
.fecha span {{ color: #6b7280; font-weight: 600; }}
.horas {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 8px; margin-top: 14px; }}
.horas div {{ border: 1.5px solid {GUINDA}; border-radius: 10px; padding: 8px 10px; text-align: center;
  font-weight: 700; color: {GUINDA}; background: #fdf6f8; }}
ul.avisos {{ margin: 0; padding-left: 0; list-style: none; }}
ul.avisos li {{ display: flex; gap: 10px; padding: 7px 0; color: #374151; border-bottom: 1px dashed #eee; }}
ul.avisos li:last-child {{ border-bottom: 0; }}
ul.avisos li i {{ font-style: normal; color: {DORADO}; font-weight: 800; }}
.pasos {{ background: #f6efe4; border-radius: 12px; padding: 14px 18px; color: #4b5563; margin-bottom: 14px; }}
.pasos b {{ color: #1f2937; }}
.pasos ol {{ margin: 6px 0 0 18px; padding: 0; }}
.pasos li {{ margin: 3px 0; }}
.paso {{ display: flex; align-items: center; gap: 10px; font-size: 1.15rem !important; font-weight: 700;
  color: #1f2937; margin: 22px 0 10px !important; }}
.paso span {{ display: inline-grid; place-items: center; width: 28px; height: 28px; border-radius: 50%;
  background: {GUINDA}; color: #fff; font-size: .95rem; }}
.espera {{ text-align: center; color: #6b7280; padding: 26px; border: 1.5px dashed #d9cfc4; border-radius: 14px;
  background: #fff; }}
.st-key-horario, .st-key-horario [data-testid="stButtonGroup"], .st-key-horario div[role="radiogroup"] {{
  width: 100% !important; max-width: 100% !important; }}
[data-testid="stButtonGroup"] div[role="radiogroup"] {{ display: grid !important;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 10px; width: 100%; }}
[data-testid="stButtonGroup"] button {{ width: 100%; padding: 12px 10px !important; border-radius: 12px !important;
  border: 1.5px solid {GUINDA} !important; background: #fff !important; color: {GUINDA} !important; }}
[data-testid="stButtonGroup"] button p {{ font-weight: 800 !important; font-size: 1.15rem !important; color: inherit !important; }}
[data-testid="stButtonGroup"] button:hover {{ background: #fdf6f8 !important; }}
[data-testid="stButtonGroup"] button[aria-checked="true"] {{ background: {GUINDA} !important; color: #fff !important;
  box-shadow: 0 4px 12px rgb(157 36 73 / .25); }}
.pie {{ text-align: center; margin: 24px 0 8px; font-size: .78rem; color: #9ca3af; }}
@media (max-width: 640px) {{ .marca b {{ font-size: 1.1rem; }} .hero .dir {{ font-size: 1.5rem; }} .hero .ger {{ font-size: 1rem; }} .titulo {{ font-size: 1.35rem; }} }}
</style>""", unsafe_allow_html=True)

# Encabezado institucional con la jerarquía
st.markdown(f"""<div class="hero">
<div class="marca">{LOGO}<span class="sep"></span><b>Alimentación para el Bienestar</b></div>
<div class="dir">Dirección Comercial</div>
<div class="ger">Gerencia de Abasto de Granos y Abarrotes</div>
<div class="sub">Subgerencia de Abarrotes</div>
</div>""", unsafe_allow_html=True)

st.markdown(f'<p class="titulo">{TITULO}</p><p class="evento">{EVENTO}<br>{PROGRAMA}</p>', unsafe_allow_html=True)

# Fecha
st.markdown(f"""<div class="tarjeta">
<div class="fecha"><b>{FECHA}</b><span>Sesiones de 1 hora · cupo de 30 por horario</span></div>
</div>""", unsafe_allow_html=True)

# Avisos, uno por renglón
st.markdown(f"""<div class="tarjeta"><ul class="avisos">
<li><i>•</i><span><b>Favor de llegar 15 minutos antes</b> de tu horario.</span></li>
<li><i>•</i><span>Solo se permite <b>un representante por proveedor</b>.</span></li>
<li><i>•</i><span>Al terminar recibirás un <b>correo de confirmación</b> de Microsoft.</span></li>
</ul></div>""", unsafe_allow_html=True)

# Paso 1: el proveedor elige su horario con tus tarjetas
st.markdown('<p class="paso"><span>1</span>Elige tu horario</p>', unsafe_allow_html=True)
horario = st.pills("Horario", list(HORARIOS), selection_mode="single", label_visibility="collapsed",
                   key="horario")

# Paso 2: Bookings ya con ese horario seleccionado
if horario:
    st.markdown(f'<p class="paso"><span>2</span>Completa tu registro · {FECHA} · {horario}</p>'
                '<div class="pasos">En el calendario avanza a <b>enero 2027</b> si es necesario, elige el día '
                '<b>15</b>, da clic en la hora, escribe tus datos y el nombre del proveedor, y da clic en '
                '<b>Reservar</b>.</div>', unsafe_allow_html=True)
    # Bookings dentro de un marco que recorta su encabezado (logo y título de Microsoft):
    # el iframe se sube RECORTE px y el marco oculta lo que queda arriba. scrolling="no" impide que
    # el proveedor se desplace dentro de Bookings y vea el pie de Microsoft.
    marco = f"""<style>
      html,body{{margin:0;padding:0;background:transparent;overflow:hidden}}
      .marco{{height:{ALTO_BOOKINGS}px;overflow:hidden;border-radius:14px;border:1px solid #ece4da;background:#fff}}
      .marco iframe{{display:block;width:100%;border:0;height:{RECORTE + ALTO_BOOKINGS}px;margin-top:-{RECORTE}px}}
      @media (max-width:430px){{
        .marco{{height:{ALTO_CELULAR}px}}
        .marco iframe{{height:{RECORTE_CELULAR + ALTO_CELULAR}px;margin-top:-{RECORTE_CELULAR}px}}
      }}
    </style>
    <div class="marco"><iframe src="{HORARIOS[horario]}" title="Registro en Microsoft Bookings" scrolling="no"></iframe></div>"""
    if hasattr(st, "iframe"):
        st.iframe(marco, height=max(ALTO_BOOKINGS, ALTO_CELULAR) + 4)
    else:   # versiones de Streamlit anteriores a st.iframe
        components.html(marco, height=max(ALTO_BOOKINGS, ALTO_CELULAR) + 4)
else:
    st.markdown('<div class="espera">Selecciona un horario para continuar con tu registro.</div>',
                unsafe_allow_html=True)

st.markdown('<div class="pie">Gerencia de Abasto de Granos y Abarrotes · Dirección Comercial · '
            'Alimentación para el Bienestar</div>', unsafe_allow_html=True)