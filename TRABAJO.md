# Proyecto Final

Objetivo: El objetivo de este proyecto es la predicción de corto y mediano plazo de el total de casos confirmados, los nuevos casos, los casos activos, recuperados y muertes para las 5 principales ciudades de Colombia, utilizando técnicas estadísticas, de inteligencia artificial o modelos híbridos.

## Extracción de datos

*Nota: Para ejecutar cada una de las lineas de código puede dirgirse al notebook de colab publicado en este mismo repositorio.*

La información para el analisis de COVID en Colombia es tomada de la url: https://www.datos.gov.co/Salud-y-Protecci-n-Social/Casos-positivos-de-COVID-19-en-Colombia/gt2j-8ykr/data

Instalación de paquetes requeridos para la elaboración de modelos y analisis de data.

```
! pip install fbprophet
```
```
import requests
import pandas as pd
import numpy as np
from datetime import date, timedelta
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import GridSearchCV, train_test_split, KFold, cross_val_score
import seaborn as sns

from fbprophet import Prophet
from fbprophet.diagnostics import cross_validation
from fbprophet.diagnostics import performance_metrics
from fbprophet.plot import plot_cross_validation_metric
```

