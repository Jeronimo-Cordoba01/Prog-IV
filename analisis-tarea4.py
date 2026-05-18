"""Ejercicios Clase 4 - Introducción al Análisis de Datos

Resolución de los ejercicios usando la base EPH del INDEC.
Variables: P21, P47T, NIVEL_ED, PP3E_TOT, ESTADO
Importante: se usan los ponderadores en todas las estimaciones.
"""

# ============================================================
# 0. IMPORTS Y CARGA DE DATOS
# ============================================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import gmean, trim_mean, skew, ttest_ind, chi2_contingency

# --- Opción A: si estás en Colab y querés subir el archivo manualmente ---
# from google.colab import files
# uploaded = files.upload()   # te abre el diálogo para seleccionar el CSV
# nombre_archivo = list(uploaded.keys())[0]

# --- Opción B: si tenés el archivo en Google Drive ---
# from google.colab import drive
# drive.mount('/content/drive')
# nombre_archivo = '/content/drive/MyDrive/ruta/al/archivo.csv'

# --- Opción C: archivo local (ajustá la ruta) ---
nombre_archivo = 'usu_individual.csv'

# La EPH del INDEC suele venir separada por ';'
df = pd.read_csv(nombre_archivo, sep=';')

print("Forma del dataframe:", df.shape)
print("\nPrimeras filas:")
print(df.head())
print("\nColumnas disponibles:")
print(df.columns.tolist())


# ============================================================
# FUNCIONES AUXILIARES: ESTADÍSTICA PONDERADA
# ============================================================
# Pandas no trae mediana/cuantiles ponderados, así que los armamos.

def media_pond(valores, pesos):
    """Media ponderada: Σ(valor × peso) / Σ(pesos)."""
    return np.average(valores, weights=pesos)


def cuantil_pond(valores, pesos, q):
    """
    Cuantil ponderado.
    Ordena los valores, acumula los pesos, y devuelve el valor donde
    el peso acumulado alcanza la proporción q.
    """
    tmp = pd.DataFrame({'val': valores, 'peso': pesos}).sort_values('val')
    tmp['peso_acum'] = tmp['peso'].cumsum() / tmp['peso'].sum()
    return tmp.loc[tmp['peso_acum'] >= q, 'val'].iloc[0]


def var_pond(valores, pesos):
    """Varianza ponderada."""
    m = media_pond(valores, pesos)
    return np.average((valores - m) ** 2, weights=pesos)


def desvio_pond(valores, pesos):
    """Desvío estándar ponderado."""
    return np.sqrt(var_pond(valores, pesos))


def corr_pearson_pond(x, y, w):
    """Correlación de Pearson ponderada. Rango: -1 a +1."""
    mx, my = media_pond(x, w), media_pond(y, w)
    cov = np.average((x - mx) * (y - my), weights=w)
    sx = np.sqrt(np.average((x - mx) ** 2, weights=w))
    sy = np.sqrt(np.average((y - my) ** 2, weights=w))
    return cov / (sx * sy)


# ============================================================
# EJERCICIO 1: ANÁLISIS UNIVARIADO Y MULTIVARIADO
# ============================================================

# Seleccionamos las variables del enunciado + ponderadores + edad + sexo
cols_interes = ['P21', 'P47T', 'NIVEL_ED', 'PP3E_TOT', 'ESTADO',
                'PONDERA', 'PONDIIO', 'PONDII', 'CH06', 'CH04']

# Verificamos que existan (por si tu base tiene nombres distintos)
faltantes = [c for c in cols_interes if c not in df.columns]
if faltantes:
    print(f"⚠️ Estas columnas no aparecen en el df: {faltantes}")

print("\n--- Resumen general de las variables ---")
print(df[['P21', 'P47T', 'NIVEL_ED', 'PP3E_TOT']].describe())


# ------------------------------------------------------------
# 1.a) MEDIA DE INGRESOS DE OCUPACIÓN PRINCIPAL (P21) POR NIVEL EDUCATIVO
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("1.a) MEDIA DE P21 POR NIVEL EDUCATIVO")
print("=" * 60)

# Filtramos casos con ingreso > 0 (los ceros suelen ser no-respuesta)
df_p21 = df[df['P21'] > 0].copy()

# Mapeamos códigos de NIVEL_ED a etiquetas legibles
niveles_ed = {
    1: '1-Primaria inc.',
    2: '2-Primaria comp.',
    3: '3-Secundaria inc.',
    4: '4-Secundaria comp.',
    5: '5-Superior inc.',
    6: '6-Superior comp.',
    7: '7-Sin instrucción',
    9: '9-Ns/Nr'
}
df_p21['nivel_ed_lbl'] = df_p21['NIVEL_ED'].map(niveles_ed)

# Media ponderada de P21 dentro de cada nivel educativo
media_p21_por_nivel = df_p21.groupby('nivel_ed_lbl').apply(
    lambda g: media_pond(g['P21'], g['PONDIIO'])
).sort_index()

print(media_p21_por_nivel.round(2))

# Visualización
plt.figure(figsize=(10, 5))
media_p21_por_nivel.plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Media ponderada de ingresos (P21) por nivel educativo')
plt.ylabel('Ingreso medio ($)')
plt.xlabel('Nivel educativo')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 1.b) MEDIA DE P47T SEGÚN DÉCADA DE VIDA
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("1.b) MEDIA DE P47T POR DÉCADA DE VIDA")
print("=" * 60)

df_p47 = df[df['P47T'] > 0].copy()

# Década: edad // 10 * 10  →  23 años → 20, 47 años → 40, etc.
df_p47['decada'] = (df_p47['CH06'] // 10) * 10

media_p47_por_decada = df_p47.groupby('decada').apply(
    lambda g: media_pond(g['P47T'], g['PONDII'])
).sort_index()

print(media_p47_por_decada.round(2))

plt.figure(figsize=(10, 5))
media_p47_por_decada.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Media ponderada de P47T por década de vida')
plt.ylabel('Ingreso total individual medio ($)')
plt.xlabel('Década de vida (edad)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 1.c) MEDIDAS DE TENDENCIA CENTRAL PARA P21
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("1.c) MEDIDAS DE TENDENCIA CENTRAL - P21")
print("=" * 60)

P21 = df_p21['P21'].values
W = df_p21['PONDIIO'].values

print(f"Media aritmética ponderada: ${media_pond(P21, W):,.2f}")
print(f"Mediana ponderada:          ${cuantil_pond(P21, W, 0.5):,.2f}")
print(f"Media geométrica:           ${gmean(P21):,.2f}")
print(f"Media podada (10%):         ${trim_mean(P21, 0.1):,.2f}")
print(f"Moda:                       ${df_p21['P21'].mode().iloc[0]:,.2f}")

# Histograma para visualizar la distribución
plt.figure(figsize=(10, 5))
plt.hist(P21, bins=50, weights=W, color='teal', edgecolor='black', alpha=0.7)
plt.axvline(media_pond(P21, W), color='red', linestyle='--',
            label=f'Media: ${media_pond(P21, W):,.0f}')
plt.axvline(cuantil_pond(P21, W, 0.5), color='orange', linestyle='--',
            label=f'Mediana: ${cuantil_pond(P21, W, 0.5):,.0f}')
plt.title('Distribución ponderada de ingresos (P21)')
plt.xlabel('Ingreso')
plt.ylabel('Frecuencia ponderada')
plt.legend()
plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 1.d) MEDIDAS DE POSICIÓN Y DISPERSIÓN PARA P21
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("1.d) MEDIDAS DE POSICIÓN Y DISPERSIÓN - P21")
print("=" * 60)

# Cuartiles
Q1 = cuantil_pond(P21, W, 0.25)
Q2 = cuantil_pond(P21, W, 0.50)
Q3 = cuantil_pond(P21, W, 0.75)
print(f"Q1 (25%):  ${Q1:,.2f}")
print(f"Q2 (50%):  ${Q2:,.2f}  (mediana)")
print(f"Q3 (75%):  ${Q3:,.2f}")
print(f"Rango intercuartílico (IQR): ${Q3 - Q1:,.2f}")

# Deciles
print("\nDeciles:")
for d in range(1, 10):
    print(f"  D{d} ({d*10}%): ${cuantil_pond(P21, W, d/10):,.2f}")

# Brecha de desigualdad: D9 / D1
D1 = cuantil_pond(P21, W, 0.1)
D9 = cuantil_pond(P21, W, 0.9)
print(f"\nRatio D9/D1: {D9/D1:.2f}  "
      f"(el 10% más rico gana {D9/D1:.1f}x lo que el 10% más pobre)")

# Dispersión
print(f"\nVarianza ponderada:        {var_pond(P21, W):,.2f}")
print(f"Desvío estándar ponderado: {desvio_pond(P21, W):,.2f}")
print(f"Coef. de variación:        {desvio_pond(P21, W)/media_pond(P21, W)*100:.2f}%")
print(f"Rango muestral:            ${P21.max() - P21.min():,.2f}")

# Asimetría y curtosis (no ponderadas - scipy/pandas no las traen ponderadas)
print(f"\nAsimetría (Fisher-Pearson): {skew(P21):.4f}")
print(f"Curtosis:                   {df_p21['P21'].kurtosis():.4f}")


# ============================================================
# EJERCICIO 2: CORRELACIÓN DE PEARSON ENTRE P21 Y PP3E_TOT
# ============================================================
print("\n" + "=" * 60)
print("2) CORRELACIÓN DE PEARSON: P21 vs PP3E_TOT")
print("=" * 60)

# Filtramos casos con valores válidos en las dos variables
mask = (df['P21'] > 0) & (df['PP3E_TOT'] > 0)
sub = df.loc[mask].copy()

r = corr_pearson_pond(sub['P21'], sub['PP3E_TOT'], sub['PONDIIO'])
print(f"Correlación de Pearson ponderada: {r:.4f}")

# Interpretación automática
abs_r = abs(r)
if abs_r < 0.3:
    fuerza = "débil"
elif abs_r < 0.7:
    fuerza = "moderada"
else:
    fuerza = "fuerte"
sentido = "positiva (directa)" if r > 0 else "negativa (inversa)"
print(f"→ Correlación {fuerza} y {sentido}")

# Gráfico de dispersión
muestra = sub.sample(min(2000, len(sub)), random_state=42)
plt.figure(figsize=(9, 6))
sns.scatterplot(data=muestra, x='PP3E_TOT', y='P21', alpha=0.3)
plt.title(f'P21 vs PP3E_TOT  (r = {r:.3f})')
plt.xlabel('Horas trabajadas (PP3E_TOT)')
plt.ylabel('Ingreso ocupación principal (P21)')
plt.tight_layout()
plt.show()


# ============================================================
# EJERCICIO 3: V DE CRAMER Y T DE STUDENT
# ============================================================

# ------------------------------------------------------------
# V DE CRAMER: asociación entre variables CATEGÓRICAS
# ------------------------------------------------------------
print("\n" + "=" * 60)
print("3) V DE CRAMER y T DE STUDENT")
print("=" * 60)

def v_de_cramer(x, y):
    """
    Asociación entre variables categóricas.
    Basada en chi-cuadrado. Rango: 0 (sin asociación) a 1 (perfecta).
    """
    tabla = pd.crosstab(x, y)
    chi2 = chi2_contingency(tabla)[0]
    n = tabla.to_numpy().sum()
    min_dim = min(tabla.shape) - 1
    return np.sqrt(chi2 / (n * min_dim))


# Aplicamos: ¿Está asociado el nivel educativo con el estado de actividad?
v = v_de_cramer(df['NIVEL_ED'], df['ESTADO'])
print(f"\nV de Cramer (NIVEL_ED vs ESTADO): {v:.4f}")
if v < 0.1:
    print("→ Asociación muy débil o inexistente")
elif v < 0.3:
    print("→ Asociación débil")
elif v < 0.5:
    print("→ Asociación moderada")
else:
    print("→ Asociación fuerte")

# Tabla cruzada para visualizar
print("\nTabla de contingencia NIVEL_ED × ESTADO:")
print(pd.crosstab(df['NIVEL_ED'], df['ESTADO']))


# ------------------------------------------------------------
# T DE STUDENT: comparar medias entre dos grupos
# Ejemplo: ¿hay brecha salarial entre varones y mujeres?
# CH04: 1 = varón, 2 = mujer
# ------------------------------------------------------------
varones = df.loc[(df['P21'] > 0) & (df['CH04'] == 1), 'P21']
mujeres = df.loc[(df['P21'] > 0) & (df['CH04'] == 2), 'P21']

t_stat, p_value = ttest_ind(varones, mujeres, equal_var=False)

print(f"\nT de Student - Ingresos de varones vs. mujeres")
print(f"Media varones:  ${varones.mean():,.2f}  (n={len(varones)})")
print(f"Media mujeres:  ${mujeres.mean():,.2f}  (n={len(mujeres)})")
print(f"Diferencia:     ${varones.mean() - mujeres.mean():,.2f}")
print(f"Estadístico t:  {t_stat:.4f}")
print(f"p-valor:        {p_value:.6f}")

if p_value < 0.05:
    print("→ Diferencia estadísticamente significativa (rechazamos H0)")
else:
    print("→ Diferencia no significativa (no rechazamos H0)")


# ============================================================
# EJERCICIO 4: TASA DE DESOCUPACIÓN
# ============================================================
print("\n" + "=" * 60)
print("4) TASA DE DESOCUPACIÓN")
print("=" * 60)
# Códigos de ESTADO en la EPH:
#   1 = Ocupado    2 = Desocupado    3 = Inactivo    4 = Menor de 10 años
#
# Tasa de desocupación = Desocupados / PEA × 100
# PEA = Ocupados + Desocupados

ocupados    = df.loc[df['ESTADO'] == 1, 'PONDERA'].sum()
desocupados = df.loc[df['ESTADO'] == 2, 'PONDERA'].sum()
inactivos   = df.loc[df['ESTADO'] == 3, 'PONDERA'].sum()
pea         = ocupados + desocupados
poblacion_total = df['PONDERA'].sum()

tasa_desocupacion = desocupados / pea * 100
tasa_actividad   = pea / poblacion_total * 100
tasa_empleo      = ocupados / poblacion_total * 100

print(f"Población ocupada:     {ocupados:>15,.0f}")
print(f"Población desocupada:  {desocupados:>15,.0f}")
print(f"Población inactiva:    {inactivos:>15,.0f}")
print(f"PEA total:             {pea:>15,.0f}")
print(f"Población total:       {poblacion_total:>15,.0f}")

print(f"\nTasa de desocupación: {tasa_desocupacion:.2f}%")
print(f"Tasa de actividad:    {tasa_actividad:.2f}%")
print(f"Tasa de empleo:       {tasa_empleo:.2f}%")


# ============================================================
# CIERRE: ANÁLISIS MULTIVARIADO DEL CONJUNTO
# ============================================================
print("\n" + "=" * 60)
print("ANÁLISIS MULTIVARIADO - Matriz de correlación")
print("=" * 60)

variables_num = ['P21', 'P47T', 'PP3E_TOT', 'CH06']
df_num = df[variables_num].copy()
# Filtramos casos válidos
df_num = df_num[(df_num['P21'] > 0) & (df_num['P47T'] > 0)]

print("\nMatriz de correlación:")
print(df_num.corr().round(3))

# Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(df_num.corr(), annot=True, cmap='coolwarm', fmt='.2f',
            linewidths=0.5, vmin=-1, vmax=1)
plt.title('Matriz de correlación')
plt.tight_layout()
plt.show()

print("\n✅ Análisis completo terminado.")