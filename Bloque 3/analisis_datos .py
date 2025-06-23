import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Librerías cargadas correctamente.")
df = pd.read_csv('Life Expectancy Data.csv')
print(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas.")


# Mensaje de carga de librerías
print("Librerías cargadas correctamente.")

# Cargar el archivo CSV
df = pd.read_csv('Life Expectancy Data.csv')

# Mostrar cantidad de datos
print(f"Datos cargados: {df.shape[0]} filas, {df.shape[1]} columnas.")

# Primeras filas del DataFrame
print(df.head())

# Información general del DataFrame
df.info()

# Estadísticas descriptivas
print(df.describe())

# Llenar valores nulos en la columna 'Life expectancy' con el promedio
df['Life expectancy'].fillna(df['Life expectancy'].mean(), inplace=True)

# Eliminar filas duplicadas
df.drop_duplicates(inplace=True)

# Verificar nuevamente la información
df.info()

# Filtrar datos solo para Ecuador
df_ecuador = df[df['Country'] == 'Ecuador']

# Calcular esperanza de vida promedio por región
avg_life_by_region = df.groupby('Region')['Life expectancy'].mean().sort_values(ascending=False)

# --- GRÁFICA DE LÍNEA: Esperanza de vida en Ecuador ---
plt.figure(figsize=(10,6))
sns.lineplot(data=df_ecuador, x='Year', y='Life expectancy', marker='o')
plt.title('Esperanza de Vida en Ecuador')
plt.xlabel('Año')
plt.ylabel('Esperanza de Vida')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- GRÁFICA DE BARRAS: Promedio por región ---
plt.figure(figsize=(12,6))
avg_life_by_region.plot(kind='bar', color=sns.color_palette('coolwarm', len(avg_life_by_region)))
plt.title('Esperanza de Vida Promedio por Región')
plt.xlabel('Región')
plt.ylabel('Esperanza de Vida Promedio')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# --- GRÁFICA DE DISPERSIÓN: PIB vs Esperanza de vida (2014) ---
df_2014 = df[df['Year'] == 2014].dropna(subset=['GDP', 'Life expectancy'])

plt.figure(figsize=(10,7))
sns.scatterplot(data=df_2014, x='GDP', y='Life expectancy', hue='Region', alpha=0.7)
plt.xscale('log')
plt.title('PIB vs. Esperanza de Vida (2014)')
plt.xlabel('PIB (log)')
plt.ylabel('Esperanza de Vida')
plt.legend(title='Región', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
