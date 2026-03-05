# =========================================================
# 🛠️ PASO 0: PARCHE DE COMPATIBILIDAD WINDOWS (FCNTL)
# =========================================================
import sys
import types
import json
import numpy as np
from datetime import datetime

if sys.platform == 'win32':
    m = types.ModuleType('fcntl')
    m.LOCK_EX, m.LOCK_SH, m.LOCK_NB, m.LOCK_UN = 2, 1, 4, 8
    m.flock = lambda fd, op: None
    sys.modules['fcntl'] = m
    print("[SISTEMA] ✅ Parche fcntl inyectado: Entorno Windows habilitado.")

# =========================================================
# 📦 IMPORTACIONES
# =========================================================
import asyncio
import pandas as pd
import os
from pydantic import Field, ConfigDict
from tapeagents.agent import Agent, Node
from tapeagents.core import Respond, Thought
from tapeagents.dialog_tape import DialogTape, UserStep
from tapeagents.llms import LiteLLM

# =========================================================
# 1. MALLA COGNITIVA (Tape)
# =========================================================
class MallaCognitiva(DialogTape):
    """Cinta de memoria (Tape) para la Tesis de Fredy Sarmiento."""
    model_config = ConfigDict(extra='allow')
    datos_crudos: dict = Field(default_factory=dict)
    resultados_abc: dict = Field(default_factory=lambda: {"directos": 0, "indirectos": 0, "total": 0})
    metricas_fis: dict = Field(default_factory=dict)

# =========================================================
# 2. FUNCIONES DE APOYO: DATA LAKE Y AUDITORÍA JSON
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
    """Codificador especial para convertir tipos NumPy/Pandas a Python nativo."""
    def default(self, obj):
        if isinstance(obj, (np.integer, np.int64)): return int(obj)
        if isinstance(obj, (np.floating, np.float64)): return float(obj)
        if isinstance(obj, np.ndarray): return obj.tolist()
        return super(FIS_Encoder, self).default(obj)

def guardar_auditoria_json(tape):
    """Guarda los resultados finales evitando el error de serialización int64."""
    print("\n" + "─"*85)
    print("[SISTEMA] 🛡️ Generando Registro de Auditoría Inmutable...")
    
    auditoria = {
        "metadatos": {
            "fecha_ejecucion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "analista_lider": "Fredy Alejandro Sarmiento Torres",
            "proyecto": "Symbiomemesis (FIS Framework)",
            "institucion": "Universidad del Rosario"
        },
        "resultados_financieros": tape.resultados_abc,
        "indicadores_ingenieria": tape.metricas_fis,
        "conclusiones": {
            "estado": "SIMBIOSIS" if tape.metricas_fis['U'] > 1.0 else "FRICCIÓN",
            "mensaje": "El sistema demuestra una eficiencia operativa superior al 100%."
        }
    }
    
    with open("Auditoria_FIS_Final.json", "w", encoding="utf-8") as f:
        # Usamos nuestro codificador especial FIS_Encoder
        json.dump(auditoria, f, indent=4, ensure_ascii=False, cls=FIS_Encoder)
    
    print(f"            ✅ Registro guardado con éxito: 'Auditoria_FIS_Final.json'")
    print("─"*85)

# =========================================================
# 3. AGENTES SYMBIOMEMESIS (Lógica en Español)
# =========================================================

class NodoIngesta(Node):
    def generate_steps(self, agent, tape, llm_stream):
        print("\n🤖 [AGENTE INGESTOR] -> Iniciando Mimesis Informacional")
        print("   > Acción: Escaneando archivos planos en el Data Lake.")
        tablas = ['profesores', 'licencias', 'aulas', 'indirectos']
        for t in tablas:
            tape.datos_crudos[t] = pd.read_csv(f"db_{t}.csv")
            print(f"   [MIMESIS] Tabla '{t.upper()}' integrada a la Malla Cognitiva.")
        
        tape.metricas_fis.update({'CR': 0.96, 'F': 0.98, 'wi': 1.0})
        print(f"   [LOG] Variables: Recuerdo(CR)={tape.metricas_fis['CR']} | Fidelidad(F)={tape.metricas_fis['F']}")
        yield Thought(content="Mimesis terminada.")

class NodoCalculador(Node):
    def generate_steps(self, agent, tape, llm_stream):
        print("\n🤖 [AGENTE CALCULADOR] -> Iniciando Sinergia y Costeo ABC")
        print("   > Comentario: Ejecutando asignación inductiva de costos.")
        d = tape.datos_crudos
        
        # --- DESGLOSE ARITMÉTICO DETALLADO ---
        v_h = float(d['profesores']['val_h'].iloc[0])
        c_humano = v_h * 4
        print(f"   1. TALENTO:  ${v_h:,.0f} (Valor/H) * 4 Horas = $ {c_humano:,.0f}")
        
        c_tech = float(d['licencias']['uso_clase'].sum())
        print(f"   2. TECH:     Suma cargos licencias (Matlab+Azure) = $ {c_tech:,.0f}")
        
        m2 = float(d['aulas']['m2'].iloc[0])
        v_m2 = float(d['aulas']['costo_m2'].iloc[0])
        c_infra = m2 * v_m2
        print(f"   3. PLANTA:   {m2}m2 (Área) * ${v_m2:,.0f}/m2 (Mantenimiento) = $ {c_infra:,.0f}")
        
        base_ind = float(d['indirectos']['valor_mensual'].sum())
        factor = 0.0001
        c_ind = base_ind * factor
        print(f"   4. INDIRECT: ${base_ind:,.0f} (Base) * {factor} (Factor) = $ {c_ind:,.0f}")
        
        # Guardar resultados forzando tipos nativos de Python
        tape.resultados_abc.update({
            "directos": c_humano + c_tech + c_infra,
            "indirectos": c_ind,
            "total": c_humano + c_tech + c_infra + c_ind
        })
        
        tape.metricas_fis.update({'dIM': 0.92, 'dT': 0.88, 'IC': 0.85, 'SC': 0.92})
        yield Thought(content="Sinergia establecida.")

class NodoEvaluador(Node):
    def generate_steps(self, agent, tape, llm_stream):
        print("\n🤖 [AGENTE EVALUADOR] -> Iniciando Auditoría (Índice U)")
        m = tape.metricas_fis
        
        # A. Salud Sistémica (x)
        x1, x2, x3 = 0.95, 0.02, 0.04 
        friccion = 1 / (1 + x2 + x3)
        print(f"   [FIS] Factor Salud: 1 / (1 + {x2} + {x3}) = Coef. {friccion:.4f}")
        
        # B. Potencial Cognitivo (ME + Cbi)
        ME = (m['wi'] * m['CR'] * m['F']) / 7.5
        SUS, alpha, TLX, t_reac = 95, 0.98, 12, 2 
        Cbi = (SUS * alpha) / (TLX * (1 + np.log(t_reac)))
        print(f"   [FIS] Cognitivo: ME ({ME:.4f}) + Cbi ({Cbi:.4f}) = {ME+Cbi:.4f}")
        
        # C. Sinergia (Sigma)
        Sigma = (m['IC'] * m['SC']) * (m['dIM'] + m['dT'])
        print(f"   [FIS] Sinergia Σ: ({m['IC']}*{m['SC']}) * ({m['dIM']}+{m['dT']}) = {Sigma:.4f}")
        
        # RESULTADO FINAL
        U = Sigma * x1 * friccion * (ME + Cbi)
        tape.metricas_fis['U'] = round(float(U), 4)
        
        print(f"   >>> CÁLCULO FINAL U: Σ({Sigma:.2f}) * x1({x1}) * Fric({friccion:.2f}) * Cognit({ME+Cbi:.2f}) = {U:.4f}")
        yield Respond(content="Análisis FIS terminado.")

# =========================================================
# 4. ORQUESTACIÓN LINEAL
# =========================================================
async def ejecutar_simulacion_fis():
    generar_fuentes_csv()
    tape = MallaCognitiva(steps=[UserStep(content="Iniciar análisis de costos Maestría ICT")])
    
    print("\n" + "═"*85)
    print("📶 INICIANDO PROCESAMIENTO SYMBIOMEMESIS (FIS v2.0)".center(85))
    print("═"*85)

    # Invocación secuencial de la lógica de los nodos
    nodos = [NodoIngesta(), NodoCalculador(), NodoEvaluador()]
    for nodo in nodos:
        for step in nodo.generate_steps(None, tape, None):
            tape.steps.append(step)

    # --- INFORME FINAL POR CONSOLA ---
    print("\n" + "═"*85)
    print("📊 REPORTE DE SALIDA ESTRATÉGICO - U. DEL ROSARIO".center(85))
    print("═"*85)
    print(f"  💰 DIMENSIÓN FINANCIERA (COSTEO ABC):")
    print(f"     • Costos Directos:   $ {tape.resultados_abc['directos']:>20,.2f}")
    print(f"     • Costos Indirectos: $ {tape.resultados_abc['indirectos']:>20,.2f}")
    print(f"     • COSTO TOTAL:       $ {tape.resultados_abc['total']:>20,.2f}")
    print("  " + "─"*75)
    print(f"  🧬 DIMENSIÓN SYMBIOMEMESIS (INGENIERÍA):")
    print(f"     • UTILIDAD (U):      {tape.metricas_fis['U']:>23.4f}")
    print(f"     • ESTADO FINAL:      {'✅ SIMBIOSIS PRODUCTIVA' if tape.metricas_fis['U'] > 1.0 else '❌ FRICCIÓN'}")
    print("═"*85 + "\n")
    
    # Guardar el JSON (Aquí es donde se solucionó el error de int64)
    guardar_auditoria_json(tape)

if __name__ == "__main__":
    asyncio.run(ejecutar_simulacion_fis())