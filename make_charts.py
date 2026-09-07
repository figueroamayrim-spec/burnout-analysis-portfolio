import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_theme(style="whitegrid")
plt.rcParams["figure.dpi"] = 130

# --- Evolución 2019-2025 ---
evol = pd.DataFrame({
    "Año": [2019, 2020, 2021, 2022, 2023, 2024, 2025],
    "Prom_Burnout": [65.295, 65.362, 65.845, 65.479, 65.88, 65.666, 63.431],
    "Rotaciones": [8, 6, 5, 6, 6, 10, 12],
})
fig, ax1 = plt.subplots(figsize=(8, 4.5))
ax1.plot(evol["Año"], evol["Prom_Burnout"], marker="o", color="#4C72B0", label="Burnout promedio")
ax1.set_ylabel("Nivel de burnout promedio", color="#4C72B0")
ax1.set_ylim(60, 70)
ax2 = ax1.twinx()
ax2.bar(evol["Año"], evol["Rotaciones"], alpha=0.3, color="#DD8452", label="Rotaciones")
ax2.set_ylabel("Rotaciones (empleados que se van)", color="#DD8452")
plt.title("Evolución del burnout y rotación (2019–2025)")
fig.tight_layout()
plt.savefig("charts/evolucion_2019_2025.png", bbox_inches="tight")
plt.close()

# --- Por departamento ---
dep = pd.DataFrame({
    "Departamento": ["RRHH", "Operaciones", "Marketing", "Ventas", "TI"],
    "Prom_Burnout": [66.37, 66.03, 64.91, 64.49, 64.39],
    "Rotaciones": [13, 15, 5, 15, 5],
}).sort_values("Prom_Burnout")
plt.figure(figsize=(7, 4))
sns.barplot(data=dep, x="Prom_Burnout", y="Departamento", color="#55A868")
plt.xlim(60, 68)
plt.title("Nivel de burnout promedio por departamento")
plt.tight_layout()
plt.savefig("charts/por_departamento.png", bbox_inches="tight")
plt.close()

# --- Por género ---
gen = pd.DataFrame({"Género": ["Femenino", "Masculino"], "Prom_Burnout": [66.53, 63.75]})
plt.figure(figsize=(4.5, 4))
sns.barplot(data=gen, x="Género", y="Prom_Burnout", palette=["#C44E52", "#4C72B0"], hue="Género", legend=False)
plt.ylim(0, 75)
plt.title("Burnout promedio por género")
plt.tight_layout()
plt.savefig("charts/por_genero.png", bbox_inches="tight")
plt.close()

# --- Por grupo etario ---
edad = pd.DataFrame({
    "Grupo_Etario": ["20–29", "30–39", "40–49", "50–59", "60–69"],
    "Prom_Burnout": [67.01, 65.38, 65.02, 64.99, 55.66],
})
plt.figure(figsize=(6.5, 4))
sns.barplot(data=edad, x="Grupo_Etario", y="Prom_Burnout", color="#8172B2")
plt.ylim(0, 75)
plt.title("Burnout promedio por grupo etario")
plt.tight_layout()
plt.savefig("charts/por_edad.png", bbox_inches="tight")
plt.close()

print("4 gráficos generados en charts/")
