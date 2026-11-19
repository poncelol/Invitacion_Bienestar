"""
Contraportada de registro · Alimentación para el Bienestar
Arriba: diseño institucional con toda la información del evento.
Abajo: la página de Microsoft Bookings incrustada (Bookings hace el cupo, el correo y el calendario).

Ejecutar:  streamlit run app.py
No necesita secretos.
"""
import streamlit as st
import streamlit.components.v1 as components

# ─────────────── CONFIGURACIÓN: cambia aquí tus datos ───────────────
BOOKINGS = ("https://bookings.cloud.microsoft/book/"
            "RegistrodeProveedoresAbarrotes@alimentacionbienestar.gob.mx/?ismsaljsauthenabled")
TITULO = "Registro de Asistencia / Proveedores Abarrotes"
EVENTO = "Mesa de trabajo con proveedores para bienes a comercializar"
PROGRAMA = "Programa de Abasto Rural 2027"
FECHA = "15 de enero de 2027"
HORARIOS = ["11:00 a 12:00", "13:00 a 14:00", "15:00 a 16:00", "17:00 a 18:00"]
ALTO_BOOKINGS = 1500   # alto en píxeles del recuadro de Bookings
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
.block-container {{ padding-top: .5rem !important; max-width: 820px; }}
#MainMenu, footer, [data-testid="stToolbar"], [data-testid="stDecoration"] {{ display: none !important; }}
header[data-testid="stHeader"] {{ background: transparent; pointer-events: none; }}
.hero {{ position: relative; background: {BANDA}; padding: 24px 0 26px; margin-bottom: 24px;
  box-shadow: 0 0 0 100vmax {BANDA}; clip-path: inset(-100vmax -100vmax 0 -100vmax); }}
.hero::after {{ content: ""; position: absolute; left: -100vmax; right: -100vmax; bottom: 0; height: 4px; background: {DORADO}; }}
.marca {{ display: flex; align-items: center; gap: 12px; margin-bottom: 14px; }}
.marca .sep {{ width: 1px; align-self: stretch; background: rgb(255 255 255 / .45); }}
.marca b {{ font-size: 1.5rem; font-weight: 800; color: #fff; line-height: 1.1; }}
.hero .dir {{ font-size: 1.6rem; font-weight: 700; color: #fff; }}
.hero .ger {{ margin-top: 2px; font-size: 1.1rem; font-weight: 600; color: {DORADO}; }}
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
.pie {{ text-align: center; margin: 24px 0 8px; font-size: .78rem; color: #9ca3af; }}
@media (max-width: 640px) {{ .marca b {{ font-size: 1.1rem; }} .hero .dir {{ font-size: 1.3rem; }} .titulo {{ font-size: 1.35rem; }} }}
</style>""", unsafe_allow_html=True)

# Encabezado institucional con la jerarquía
st.markdown(f"""<div class="hero">
<div class="marca">{LOGO}<span class="sep"></span><b>Alimentación para el Bienestar</b></div>
<div class="dir">Dirección Comercial</div>
<div class="ger">Gerencia de Abasto de Granos y Abarrotes</div>
</div>""", unsafe_allow_html=True)

st.markdown(f'<p class="titulo">{TITULO}</p><p class="evento">{EVENTO}<br>{PROGRAMA}</p>', unsafe_allow_html=True)

# Fecha y horarios
st.markdown(f"""<div class="tarjeta">
<div class="fecha"><b>{FECHA}</b><span>Sesiones de 1 hora · cupo de 30 por horario</span></div>
<div class="horas">{"".join(f"<div>{h}</div>" for h in HORARIOS)}</div>
</div>""", unsafe_allow_html=True)

# Avisos, uno por renglón
st.markdown(f"""<div class="tarjeta"><ul class="avisos">
<li><i>•</i><span><b>Favor de llegar 15 minutos antes</b> de tu horario.</span></li>
<li><i>•</i><span>Solo se permite <b>un representante por proveedor</b>.</span></li>
<li><i>•</i><span>Al terminar recibirás un <b>correo de confirmación</b> de Microsoft.</span></li>
</ul></div>""", unsafe_allow_html=True)

st.markdown(f"""<div class="pasos"><b>¿Cómo registrarte?</b>
<ol>
<li>Elige tu horario.</li>
<li>En el calendario avanza a <b>enero 2027</b>, elige el día <b>15</b> y da clic en la hora.</li>
<li>Escribe tu nombre, tu correo y el nombre del proveedor, y da clic en <b>Reservar</b>.</li>
</ol></div>""", unsafe_allow_html=True)

# Bookings incrustado (código oficial de "Insertar")
if hasattr(st, "iframe"):
    st.iframe(BOOKINGS, height=ALTO_BOOKINGS)
else:   # versiones de Streamlit anteriores a st.iframe
    components.iframe(BOOKINGS, height=ALTO_BOOKINGS, scrolling=True)

st.markdown(f'<div class="pie">Gerencia de Abasto de Granos y Abarrotes · Dirección Comercial · Alimentación para el Bienestar<br>'
            f'¿No se ve el formulario? <a href="{BOOKINGS}" target="_blank" style="color:{GUINDA}">Ábrelo aquí</a></div>',
            unsafe_allow_html=True)
