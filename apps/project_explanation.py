from dash import html, Input,Output,State,dcc
import dash_bootstrap_components as dbc 


md_docs = ''' 
#####   Pronosticar la cantidad de pasajeros en Aeropuerto
---

Este projecto usa la inforamción de los pasajeros del San Fransisco Airport desde 2005 al 2016.
 
 
Este projecto fue creado con los siguientes objetivos : 

- Crear un **Modelo de Series de tiempo** para pronosticar.
- Crear un **Tablero de Business Intelligence** .
    
##### PROJECT WORKFLOW 
___
1. Limpieza de los datos
2. Exploración de los datos
3. Creación de modelo de Pronostico 
4. Evaluación del modelo
5. Crear Tablero de BI
6. Crear API








'''





def render_project_explanation() : 
    content = dcc.Markdown(md_docs)
    content = dbc.Container(
        children = [
            html.Br(), 
            dbc.Row(className='dashboard_picture',
                children = [html.Img(src='https://raw.githubusercontent.com/fakhrirobi/forecast_passenger_BI/main/assets/path-digital-tR0jvlsmCuQ-unsplash.jpg',alt='Dashboard Picture', 
                         style={

                             'height':700,
                               "display": "block",
                                "margin-left": "auto",
                                "margin-right": "auto"
                         })]),
        html.Br(),
        dcc.Markdown(md_docs)
            
        
        ])
    
    return content


'''
| No       | Model | MAPE |
| ----------- | ----------- |-----------  |
| 1      | Exponential Smoothing Base Model        | 0.0008154384896421845 |
| 2   | ARIMA p,d,q (1,0,1)   ts_log_diff     | 1.521088082512651 | 
| 3   | ARIMA p,d,q (1,0,1) ts_moving_avg_diff       | 1.521088082512651 |
| 4   | ARIMA p,d,q (1,0,1) ts_log_moving_avg_diff      | 4.003097132106808 |
| 5  | ARIMA p,d,q (1,0,1) moving_avg_sqrt     | 0.0022336601438086657 |
'''


'''
| No       | Model | MAPE |
| ----------- | ----------- |-----------  |
| 1      | RandomForestRegressor       | 0.02821705982449663 |
| 2   | CastBoostRegressor   | 0.06058001839160664 | 
| 3   | XGBoost        | 0.03835722560008849 |
| 4   | Linear Regression     | 0.08068713742097987 |

'''


'''
| No       | Model | MAPE |
| ----------- | ----------- |-----------  |
| 1      | NeuralProphet Base Model 1000 epochs       | 0.015608695722430762 |


'''

