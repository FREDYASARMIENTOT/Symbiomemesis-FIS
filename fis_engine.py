import numpy as np
import pandas as pd
import json
import os

def calcular_utilidad_fis(momento_label, variables_tester):
    """
    Calcula la Utilidad Simbiótica (U) basada en la Ecuación Maestra del FIS.
    """
    v = variables_tester # Diccionario con los promedios (0.0 a 1.0)
    
    # 1. Componente: Sinergia del Enjambre (Sigma)
    # Relaciona interacción, contribución y ahorro de recursos
    sigma = (v['IC'] * v['SC']) * (v['dIM'] + v['dT'])
    
    # 2. Componente: Salud Sistémica (Vector de Estado x)
    x1 = 1 - abs(v['rho'])  # Perpendicularidad (Independencia)
    x2 = v['I_sicof']       # Sicofancia
    x3 = v['I_red']         # Redundancia
    
    filtro_friccion = 1 / (1 + x2 + x3)
    
    # 3. Componente: Potencial Cognitivo (ME + Cbi)
    # ME: Educación de Máquina
    ME = (v['w_i'] * v['CR'] * v['F']) / v['D_task']
    
    # Cbi: Eficiencia Comunicativa (Penalizada por carga mental y latencia)
    # Usamos logaritmo natural para t_react como en la fórmula original
    denominador_cbi = v['TLX'] * (1 + np.log(max(1, v['t_react'])))
    Cbi = (v['SUS'] * v['alpha']) / denominador_cbi
    
    # ECUACIÓN MAESTRA FINAL
    U = sigma * x1 * filtro_friccion * (ME + Cbi)
    
    return round(U, 4)

# =========================================================
# CONFIGURACIÓN DEL MOMENTO 1 (FRICCIÓN)
# Estos valores representan tu primera medición real
# =========================================================
datos_m1 = {
    # Bloque Técnico (ME)
    'w_i': 0.90, 'CR': 0.75, 'F': 0.80, 'D_task': 7.0,
    # Bloque Interfaz (Cbi)
    'SUS': 65.0, 'alpha': 0.70, 'TLX': 80.0, 't_react': 15.0,
    # Bloque Sinergia (Sigma)
    'IC': 0.40, 'SC': 0.50, 'dIM': 0.20, 'dT': 0.15,
    # Bloque Estado (x)
    'rho': 0.85, 'I_sicof': 0.60, 'I_red': 0.70
}

u_m1 = calcular_utilidad_fis("Momento 1 - Fricción", datos_m1)

print("="*60)
print(f"📊 RESULTADOS SYMBIOMEMESIS - {os.getcwd()}")
print("="*60)
print(f"RESULTADO UTILIDAD (U) M1: {u_m1}")
print("-" * 60)

if u_m1 < 1.0:
    print("ESTADO: FRICCIÓN OPERATIVA (U < 1)")
    print("ACCIÓN: Incrementar independencia de agentes y reducir carga mental (TLX).")
else:
    print("ESTADO: SIMBIOSIS INCIPIENTE (U >= 1)")

print("="*60)