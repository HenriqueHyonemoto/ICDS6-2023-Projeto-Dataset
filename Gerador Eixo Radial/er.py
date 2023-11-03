import plotly.express as px
import pandas as pd

df = pd.read_csv("PistaEditado.csv")
fig = px.line_polar(df, r="tipo_de_ocorrencia",
                    theta="data",
                    color="horario",
                    line_close=True,
                    color_discrete_sequence=["#00eb93", "#4ed2ff"],
                    template="plotly_dark")

fig.update_polars(angularaxis_showgrid=False,
                  radialaxis_gridwidth=0,
                  gridshape='linear',
                  bgcolor="#494b5a",
                  radialaxis_showticklabels=False
                  )
fig.update_traces(fill='toself')
fig.update_layout(paper_bgcolor="#2c2f36")
fig.show()