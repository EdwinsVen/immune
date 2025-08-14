import pandas as pd
import matplotlib.pyplot as plt

anios = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
# Datos en millones
turistas_aereos = [6.18, 6.56, 6.45, 2.65, 4.99, 7.16, 8.06]
turistas_maritimos = [1.02, 1.34, 1.09, 0.28, 0.44, 1.31, 2.19]
turistas_totales = [7.20, 7.90, 7.54, 2.93, 5.43, 8.47, 10.25]


df = pd.DataFrame({
    'Anio': anios, 
    'Aire': turistas_aereos, 
    'Mar': turistas_maritimos,
    'Total': turistas_totales
})

# Ejemplos de mas estilos en https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
plt.style.use('seaborn-v0_8-darkgrid')

plt.figure(figsize=(12, 7))

# Graficar barras una encima de la otra
plt.bar(df['Anio'].astype(str), df['Aire'], color='#1f77b4', label='Llegadas Aéreas')
plt.bar(df['Anio'].astype(str), df['Mar'], bottom=df['Aire'], color='#ff7f0e', label='Llegadas Marítimas')

plt.title('Ingresos de Turistas a la República Dominicana (2017-2023)', fontsize=16)
plt.xlabel('Año', fontsize=12)
plt.ylabel('Número de Turistas (en millones)', fontsize=12)
plt.legend(fontsize=10)

# Añadir numero total de turistas encima de cada barra
for i, total in enumerate(df['Total']):
    plt.text(i, total + 0.2, f'{total:.2f}', ha='center', va='bottom', fontsize=10, fontweight='bold')


plt.show()