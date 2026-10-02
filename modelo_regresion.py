import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.outliers_influence import variance_inflation_factor

SEED = 42

df = pd.read_excel("data/Base_RegresionLineal_Municipios_2024.xlsx",
                   sheet_name="Base_Modelo")
pop = pd.read_excel("PPED-AreaMun-2018-2042_VP.xlsx",
                    sheet_name="PobMunicipalxÁrea", header=7)

df["Código DANE"] = df["Código DANE"].astype(str).str.replace(r"\.0$", "", regex=True).str.zfill(5)

p = pop[pd.to_numeric(pop["AÑO"], errors="coerce").eq(2024)].copy()
p["Código DANE"] = pd.to_numeric(p["MPIO"], errors="coerce").astype("Int64").astype(str).str.zfill(5)
p["TOTAL"] = pd.to_numeric(p["TOTAL"], errors="coerce")

piv = p.pivot_table(index="Código DANE", columns="ÁREA GEOGRÁFICA",
                     values="TOTAL", aggfunc="sum").reset_index()
piv["poblacion_cabecera_2024"] = piv["Cabecera Municipal"]
piv["poblacion_rural_2024"] = piv["Centros Poblados y Rural Disperso"]
piv["pct_poblacion_cabecera"] = 100*piv["poblacion_cabecera_2024"]/piv["Total"]

df = df.merge(piv[["Código DANE","pct_poblacion_cabecera",
                   "poblacion_rural_2024"]],
              on="Código DANE", how="inner", validate="one_to_one")

features = ["poblacion_2024","pct_poblacion_cabecera","poblacion_rural_2024"]
X, y = df[features], df["ingresos_per_capita"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=SEED
)

model = LinearRegression().fit(X_train, y_train)
pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test,pred))
print("MSE:", mean_squared_error(y_test,pred))
print("RMSE:", mean_squared_error(y_test,pred)**0.5)
print("R2:", r2_score(y_test,pred))

bp = het_breuschpagan(y_test-pred, sm.add_constant(X_test))
print("Breusch-Pagan p-value:", bp[1])
