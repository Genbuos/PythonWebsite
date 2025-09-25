
import streamlit as st
import panel as pn
from pythreejs import Mesh, MeshBasicMaterial, BoxGeometry, Scene, PerspectiveCamera, Renderer, OrbitControls

pn.extension('threejs')

st.set_page_config(layout='wide')
st.title("3D Model Viewer (Panel + Three.js)")

# Example: Display a simple Three.js box
geometry = BoxGeometry(1, 1, 1)
material = MeshBasicMaterial(color='green')
cube = Mesh(geometry=geometry, material=material)
scene = Scene(children=[cube])
camera = PerspectiveCamera(position=[3, 3, 3], up=[0, 0, 1], children=[cube])
controls = OrbitControls(controlling=camera)
renderer = Renderer(scene=scene, camera=camera, controls=[controls], width=600, height=400)

st.write(pn.panel(renderer))

st.title("3D Model Viewer (iframe HTML)")
# Embed your test.html viewer using an iframe
st.markdown(
	'<iframe src="http://localhost:8000/test.html" width="100%" height="500" frameborder="0"></iframe>',
	unsafe_allow_html=True
)
