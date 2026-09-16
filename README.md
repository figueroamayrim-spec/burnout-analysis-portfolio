
## Hallazgos principales

- **100 empleados** analizados a lo largo de **7 años** (2019–2025), con un
  nivel de burnout promedio de **65.3** (escala 30–95) y una tasa de rotación
  del **53%** en el período.
- **RR.HH. y Operaciones** son los departamentos con mayor burnout promedio
  (66.4 y 66.0), y también los de mayor rotación (13 y 15 salidas). **TI** y
  **Ventas** tienen el burnout más bajo (64.4) pero Ventas igual concentra 15
  rotaciones — sugiere que ahí la salida de gente responde a otros factores,
  no solo al burnout.
- El grupo etario **20-29 años** tiene el burnout más alto (67.0), y baja de
  forma sostenida con la edad hasta 55.7 en 60-69 — contraintuitivo si se
  espera que la carga aumente con la seniority; puede reflejar menor
  tolerancia al estrés o menor experiencia en manejarlo en los primeros años
  de carrera.
- El género **femenino** reporta un burnout promedio más alto que el
  masculino (66.5 vs 63.8).
- La rotación **se duplicó entre 2019 y 2025** (de 8 a 12 salidas/año) pese a
  que el burnout promedio bajó levemente en el último año — señal de que la
  rotación no depende solo del nivel de burnout medido, sino probablemente de
  factores externos (mercado laboral, compensación) que valdría la pena
  cruzar en una siguiente iteración.

![Evolución 2019-2025](evolucion_2019_2025.png)
![Por departamento](por_departamento.png)
![Por género](por_genero.png)
![Por grupo etario](por_edad.png)

## Estructura del proyecto
├── Informe_Burnout_Mayrim_Consolidado.pdf # informe final completo (documentación principal)
├── Proyecto_PowerBI_Mayrim.pbix # dashboard interactivo de Power BI
├── Burnout_Mayrim_ENTREGA_FINAL.xlsx # modelo de datos + tablas de análisis
├── caso-de-negocio.pdf # caso de negocio, destinatarios, ER, glosario (complementario)
├── evolucion_2019_2025.png # gráficos de los hallazgos
├── por_departamento.png
├── por_genero.png
├── por_edad.png
├── make_charts.py # script que genera los gráficos
└── README.md
## Nota sobre el dataset base

El dataset original (sin segmentar) usado como punto de partida del curso
fue provisto por la profesora del curso; este proyecto usa el modelo de
datos y el análisis propio desarrollado a partir de esa base — la
segmentación en esquema estrella, las tablas dimensión, el dashboard de
Power BI, los KPIs y el caso de negocio son trabajo propio.

## Stack

Power BI (Power Query, DAX) · Modelado de datos (esquema estrella) ·
Excel/Google Sheets · Python (pandas, Matplotlib/Seaborn) para los gráficos
de este README
