import sys
import os
import tapeagents
from tapeagents.agent import Agent

print("="*60)
print("🚀 SYMBIOMEMESIS DEPLOYMENT AUDIT - VERIFICADO")
print("="*60)
print(f"ENTORNO ACTIVO: {sys.prefix}")
print(f"UBICACIÓN SCRIPTS: {os.getcwd()}")
print("-" * 60)

# Prueba funcional: Crear un agente vacío del FIS
try:
    test_agent = Agent.create(name="FIS_Auditor")
    print(f"✅ MOTOR AGÉNTICO: Inicializado (Agente '{test_agent.name}' listo)")
except Exception as e:
    print(f"❌ ERROR MOTOR: {e}")

if "Enveroiments" in sys.prefix:
    print("✅ ESTADO: ÓPTIMO. Ejecución fuera de OneDrive.")
else:
    print("⚠️ ESTADO: ADVERTENCIA. Revisar rutas de entorno.")
print("="*60)