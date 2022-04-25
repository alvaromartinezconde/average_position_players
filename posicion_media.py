import pandas as pd
import matplotlib.pyplot as plt
import matplotlib; matplotlib.style.use('ggplot')
from paint_field import paint_field


# Fichero con información de jugadores


ruta_jugadores = "inputs/eventos_2020_2021.csv"
df = pd.read_csv(ruta_jugadores)


dfmatch = (
    
    ((df['team']=='Atletico de Madrid') | (df['team']=='Cadiz CF')) & ((df['year']==2021) & (df['month']==1) & (df['day']==31)))


    
df_match = df[dfmatch]

pos_media_Atl = ((df_match['team']=='Atletico de Madrid'))

df_match[pos_media_Atl]


jug_atletico = df_match[pos_media_Atl].loc[:, ['player','x','y']]

jug_atletico.groupby(['player']).mean()

pos_atletico = jug_atletico.groupby(['player']).mean()

color_campo = 'green'


paint_field.field_mean_position(color_campo, pos_atletico)
