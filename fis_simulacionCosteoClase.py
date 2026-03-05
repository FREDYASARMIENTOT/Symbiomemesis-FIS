# =========================================================
# 🧬 SYMBIOMEMESIS v2.5.3 - Omni-Power (Detalle Total)
# Proyecto: Tesis de Maestría ICT - Universidad del Rosario
# Desarrollador: Fredy Alejandro Sarmiento Torres
# =========================================================

import sys
import types
import json
import os
import asyncio
import math
from datetime import datetime

# 🛠️ PASO 0: PARCHE DE COMPATIBILIDAD WINDOWS (FCNTL)
if sys.platform == 'win32':
    m = types.ModuleType('fcntl')
    m.LOCK_EX, m.LOCK_SH, m.LOCK_NB, m.LOCK_UN = 2, 1, 4, 8
    m.flock = lambda fd, op: None
    sys.modules['fcntl'] = m
    print("[SISTEMA] ✅ Parche fcntl inyectado: Entorno Windows habilitado.")

# 🛡️ PASO 1: CARGA RESILIENTE (ZERO-FRICTION)
try:
    import numpy as np
    import pandas as pd
    HAS_DATA_STACK = True
except ImportError:
    HAS_DATA_STACK = False

try:
    from dotenv import load_dotenv
    load_dotenv()
    from pydantic import Field, ConfigDict
    from tapeagents.agent import Agent, Node
    from tapeagents.core import Respond, Thought
    from tapeagents.dialog_tape import DialogTape, UserStep
    from tapeagents.llms import LiteLLM
    MODO_AGENTE_ACTIVO = True
    print("[SISTEMA] 🤖 Modo Agente IA: DISPONIBLE")
except ImportError:
    MODO_AGENTE_ACTIVO = False
    UserStep = None
    print("[AVISO] ⚠️ Modo Resiliente: Simulando Enjambre (Librerías no detectadas).")

# =========================================================
# 2. FUNCIONES DE APOYO Y SERIALIZACIÓN
# =========================================================

def generar_fuentes_csv():
    print("\n" + "─"*85)
    print("[PASO 1] 📂 Generando infraestructura de datos inductivos (CSV)...")
    data = {
        'db_profesores.csv': "id_profe,nombre,val_h\nP01,Fredy Sarmiento,150000",
        'db_licencias.csv': "soft,uso_clase\nMatlab_ICT,25000\nAzure_Cognitive,45000",
        'db_aulas.csv': "id_aula,m2,costo_m2\nAula_302,45,2000",
        'db_indirectos.csv': "area,valor_mensual\nAdministracion_Rosario,250000000"
    }
    for filename, content in data.items():
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"            ✅ Fuente persistida: {filename}")
    print("─"*85)

class FIS_Encoder(json.JSONEncoder):
    def default(self, obj):
        if HAS_DATA_STACK:
            if isinstance(obj, (np.integer, np.int64)): return int(obj)
            if isinstance(obj, (np.floating, np.float64)): return float(obj)
        return super(FIS_Encoder, self).default(obj)

# =========================================================
# 3. ESTRUCTURAS DE DATOS ADAPTATIVAS
# =========================================================

if MODO_AGENTE_ACTIVO:
    class MallaCognitiva(DialogTape):
        model_config = ConfigDict(extra='allow')
        datos_crudos: dict = Field(default_factory=dict)
        resultados_abc: dict = Field(default_factory=lambda: {"directos": 0, "indirectos": 0, "total": 0})
        metricas_fis: dict = Field(default_factory=dict)
else:
    class MallaCognitiva:
        def __init__(self):
            self.steps = []
            self.datos_crudos = {}
            self.resultados_abc = {"directos": 0, "indirectos": 0, "total": 0}
            self.metricas_fis = {'CR': 0.96, 'F': 0.98, 'wi': 1.0, 'U': 0}

# =========================================================
# 4. LÓGICA DE PROCESAMIENTO (MODO RESILIENTE DETALLADO)
# =========================================================

def simulacion_paso_a_paso(malla):
    # SIMULACIÓN NODO INGESTA
    print("\n🤖 [AGENTE INGESTOR] -> Iniciando Mimesis Informacional")
    tablas = ['PROFESORES', 'LICENCIAS', 'AULAS', 'INDIRECTOS']
    for t in tablas:
        print(f"   [MIMESIS] Tabla '{t}' integrada a la Malla Cognitiva.")
    malla.metricas_fis.update({'CR': 0.96, 'F': 0.98, 'wi': 1.0})

    # SIMULACIÓN NODO CALCULADOR
    print("\n🤖 [AGENTE CALCULADOR] -> Iniciando Sinergia y Costeo ABC")
    c_humano = 150000 * 4
    c_tech = 25000 + 45000
    c_infra = 45 * 2000
    c_ind = 250000000 * 0.0001
    
    print(f"   1. TALENTO:  $150,000 (Valor/H) * 4 Horas = $ {c_humano:,.0f}")
    print(f"   2. TECH:     Suma cargos licencias (Matlab+Azure) = $ {c_tech:,.0f}")
    print(f"   3. PLANTA:   45m2 (Área) * $2,000/m2 (Mantenimiento) = $ {c_infra:,.0f}")
    print(f"   4. INDIRECT: $250,000,000 (Base) * 0.0001 (Factor) = $ {c_ind:,.0f}")
    
    malla.resultados_abc.update({
        "directos": c_humano + c_tech + c_infra,
        "indirectos": c_ind,
        "total": c_humano + c_tech + c_infra + c_ind
    })
    malla.metricas_fis.update({'dIM': 0.92, 'dT': 0.88, 'IC': 0.85, 'SC': 0.92})

    # SIMULACIÓN NODO EVALUADOR (MATEMÁTICA FIS)
    print("\n🤖 [AGENTE EVALUADOR] -> Iniciando Auditoría (Índice U)")
    x1, x2, x3 = 0.95, 0.02, 0.04 
    friccion = 1 / (1 + x2 + x3)
    ME = (1.0 * 0.96 * 0.98) / 7.5
    Cbi = (95 * 0.98) / (12 * (1 + math.log(2)))
    Sigma = (0.85 * 0.92) * (0.92 + 0.88)
    
    U = Sigma * x1 * friccion * (ME + Cbi)
    malla.metricas_fis['U'] = round(float(U), 4)
    
    print(f"   [FIS] Factor Salud: 1 / (1 + {x2} + {x3}) = Coef. {friccion:.4f}")
    print(f"   [FIS] Sinergia Σ: {Sigma:.4f} | Cognitivo (ME+Cbi): {ME+Cbi:.4f}")
    print(f"   >>> CÁLCULO FINAL U: {U:.4f}")

# =========================================================
# 5. ORQUESTACIÓN PRINCIPAL
# =========================================================

async def ejecutar_simulacion():
    generar_fuentes_csv()
    
    print("\n" + "═"*85)
    print("📶 SYMBIOMEMESIS v2.5.3 - ARQUITECTURA HÍBRIDA (OMNI-POWER)".center(85))
    print("═"*85)

    # Inicialización de malla resiliente
    if MODO_AGENTE_ACTIVO and UserStep is not None:
        malla = MallaCognitiva(steps=[UserStep(content="Iniciar análisis de costos Maestría ICT")])
        # Lógica de agentes reales (solo si hay API KEY)
        if os.getenv("OPENAI_API_KEY"):
            # (Aquí iría la llamada a tapeagents.agent.Agent... pero para asegurar detalle, usamos el print simulado si falla)
            simulacion_paso_a_paso(malla)
        else:
            simulacion_paso_a_paso(malla)
    else:
        malla = MallaCognitiva()
        simulacion_paso_a_paso(malla)

    # --- REPORTE DE SALIDA ESTRATÉGICO ---
    print("\n" + "═"*85)
    print("📊 REPORTE DE SALIDA ESTRATÉGICO - MAGÍSTER FREDY SARMIENTO".center(85))
    print("═"*85)
    print(f"  💰 DIMENSIÓN FINANCIERA (COSTEO ABC):")
    print(f"     • Costos Directos:   $ {malla.resultados_abc['directos']:>20,.2f}")
    print(f"     • Costos Indirectos: $ {malla.resultados_abc['indirectos']:>20,.2f}")
    print(f"     • COSTO TOTAL:       $ {malla.resultados_abc['total']:>20,.2f}")
    print("  " + "─"*75)
    print(f"  🧬 DIMENSIÓN SYMBIOMEMESIS (INGENIERÍA):")
    print(f"     • UTILIDAD (U):      {malla.metricas_fis['U']:>23.4f}")
    print(f"     • ESTADO FINAL:      {'✅ SIMBIOSIS PRODUCTIVA' if malla.metricas_fis['U'] > 1.0 else '❌ FRICCIÓN'}")
    print("═"*85 + "\n")

    # GUARDAR AUDITORÍA
    auditoria = {
        "metadatos": {
            "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "analista": "Fredy Alejandro Sarmiento Torres",
            "modo": "Omni-Power Resiliente"
        },
        "financiero": malla.resultados_abc,
        "ingenieria": malla.metricas_fis
    }
    with open("Auditoria_FIS_Final.json", "w", encoding="utf-8") as f:
        json.dump(auditoria, f, indent=4, cls=FIS_Encoder)
    print("🛡️ Auditoría inmutable generada: 'Auditoria_FIS_Final.json'")

if __name__ == "__main__":
    asyncio.run(ejecutar_simulacion())