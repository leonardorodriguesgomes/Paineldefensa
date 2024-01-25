import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk




def principal():
       
    chart_data = filtrado
    

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=-23.50798,
            longitude=-46.55123,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
               'HeatmapLayer',
               data=chart_data,
               get_position='[LON, LAT]',
               radius=200,
               elevation_scale=100,
               elevation_range=[1,30],
               pickable=True,
               extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],))
 
st.title('Histórico de Manutenção de Defensas em 2023')

DATA_URL = 'Infodefensa.xlsx'
arq = pd.read_excel(DATA_URL)


    

values = st.sidebar.slider(
'Selecionar um intervalo para quantidade de defensas danificadas em m',
1, 150, (1, 150))


 

filtrado1 = arq[arq['Qtd']>=values[0]]
filtrado2 = filtrado1[filtrado1['Qtd']<=values[1]]
filtrado = filtrado2


if st.sidebar.button('Iniciar'):
   principal()

tabela = st.sidebar.toggle('Tabela')
if tabela:
   st.write(filtrado)






