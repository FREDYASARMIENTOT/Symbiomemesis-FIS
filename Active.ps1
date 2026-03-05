# =========================================================
# SYMBIOMEMESIS - Lanzador Proactivo v2.5
# Sincronizado para: Maestria ICT - U. Rosario
# =========================================================
Clear-Host

# 1. RUTAS Y CONFIGURACION
$VENV = "D:\Enveroiments\venvSymbiomemesisDeploy\Scripts\Activate.ps1"
$SCRIPT_PY = "fis_simulacionCosteoClase.py"

Write-Host "--- VALIDANDO ENTORNO: SYMBIOMEMESIS FIS ---" -ForegroundColor Cyan

# 2. ACTIVACION DEL AMBIENTE
if (Test-Path $VENV) {
    . $VENV
    Write-Host "[OK] Ambiente Virtual Activo." -ForegroundColor Green
} else {
    Write-Host "[!] AVISO: No se detecto venv en la ruta D:\. Usando Python Global." -ForegroundColor Yellow
}

# 3. VERIFICACION DE DEPENDENCIAS (Optimizada)
Write-Host "--- Verificando Activos (Librerias) ---" -ForegroundColor Gray
$pythonVersion = python --version
Write-Host "Detected: $pythonVersion" -ForegroundColor Gray

# Intentamos importar una libreria clave para ver si hace falta instalar
$check = python -c "import numpy; print('OK')" 2>$null
if ($check -ne "OK") {
    Write-Host "[+] Instalando dependencias necesarias para el profesor..." -ForegroundColor Yellow
    # Instalacion silenciosa
    pip install pandas numpy pydantic tapeagents python-dotenv litellm --quiet
} else {
    Write-Host "[OK] Librerias validadas." -ForegroundColor Green
}

# 4. EJECUCION DEL MOTOR SYMBIOMEMESIS
if (Test-Path $SCRIPT_PY) {
    Write-Host "--- LANZANDO MOTOR DE DECISION PROACTIVA ---" -ForegroundColor Blue
    python $SCRIPT_PY
} else {
    Write-Host "[ERROR] No se encuentra el archivo $SCRIPT_PY en esta ruta." -ForegroundColor Red
}

Write-Host "--- FIN DEL PROCESO ---" -ForegroundColor Cyan