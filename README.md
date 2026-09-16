# Análisis de Síndrome de Burnout en el entorno laboral

Proyecto de análisis de datos (curso de Data Analysis, CoderHouse) sobre el
síndrome de burnout en un entorno corporativo: modelado de datos en esquema
estrella, definición de caso de negocio con stakeholders reales, dashboard
interactivo en Power BI, y análisis de KPIs por departamento, género, edad y
evolución temporal (2019–2025).

## Documentación principal

- 📄 **[Informe_Burnout_Mayrim_Consolidado.pdf](Informe_Burnout_Mayrim_Consolidado.pdf)**
  — informe final completo: caso de negocio, modelo de datos, proceso de
  armado en Power BI/Power Query (con ejemplos de medidas DAX),
  conclusiones, recomendaciones, limitaciones y líneas futuras.
- 📊 **[Proyecto_PowerBI_Mayrim.pbix](Proyecto_PowerBI_Mayrim.pbix)** —
  dashboard interactivo (abrir con Power BI Desktop).
- 📋 **[caso-de-negocio.pdf](caso-de-negocio.pdf)** — material complementario
  con el avance intermedio del curso: destinatarios, niveles de uso,
  glosario y diagrama entidad-relación.

## Caso de negocio

Se trabajó con información histórica sobre síndrome de burnout recolectada en
entornos laborales entre 2015 y 2025, distinguiendo departamentos, empleados,
características sociodemográficas, niveles de burnout, días de licencia y
antigüedad.

**Destinatarios:** directores y gerentes de RR.HH., psicólogos laborales,
áreas de prevención de riesgos laborales, analistas de datos/BI,
departamentos de compliance y salud ocupacional, y directivos interesados en
retención de talento.

**Preguntas de negocio que responde el análisis:**
- ¿Cuál es el departamento con mayor nivel promedio de burnout?
- ¿Qué grupo etario y qué género muestran mayor prevalencia?
- ¿Cómo evolucionó el burnout y la rotación entre 2019 y 2025?
- ¿Qué relación existe entre nivel de burnout y antigüedad/rotación?

## Modelo de datos

Diseñado en **esquema estrella**: una tabla de hechos `Burnout_Laboral`
(nivel de burnout y días de licencia por empleado y período) conectada por
relaciones uno-a-muchos con las tablas dimensión `Empleado` y `Departamento`,
cada una con su propia primary key. Este modelo es la base del dashboard de
Power BI.

El archivo [`Burnout_Mayrim_ENTREGA_FINAL.xlsx`](Burnout_Mayrim_ENTREGA_FINAL.xlsx)
contiene (GitHub no puede previsualizar Excel — hay que descargarlo o abrirlo
con "View raw" — así que acá va el detalle de qué hay en cada pestaña):
-
