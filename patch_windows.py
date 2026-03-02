import sys
import types

def apply_fcntl_patch():
    """Crea un módulo fcntl ficticio para compatibilidad con Windows."""
    if sys.platform == 'win32':
        # Crear un módulo vacío
        fcntl_mock = types.ModuleType('fcntl')
        
        # Definir las constantes que tapeagents busca en el archivo utils.py
        fcntl_mock.LOCK_EX = 2
        fcntl_mock.LOCK_SH = 1
        fcntl_mock.LOCK_NB = 4
        fcntl_mock.LOCK_UN = 8
        
        # Definir la función flock que no hace nada
        def mock_flock(fd, operation):
            pass
        
        fcntl_mock.flock = mock_flock
        
        # Inyectarlo en el registro de módulos del sistema
        sys.modules['fcntl'] = fcntl_mock
        print("✅ Parche 'fcntl' aplicado: Compatibilidad con Windows activada.")

# Ejecutar el parche inmediatamente si se importa
apply_fcntl_patch()