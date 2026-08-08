"""
🛰️ PRACTICAS DE PYTHON | Playground de Pruebas Rápidas
================================================================================
Entorno de ejecución libre para probar conceptos, validar snippets de código,
medir rendimiento básico y experimentar con sintaxis de Python.
"""

import time
from typing import Any


def run_playground() -> None:
    """
    📋 Sección principal para escribir y ejecutar fragmentos de código de prueba.
     Modifica esta función libremente para tus experimentos locales.
    """
    print("\n📝 [ÁREA DE EXPERIMENTACIÓN]")
    print("-" * 50)

    # -------------------------------------------------------------------------
    # 🧪 Escribe tu código de prueba aquí abajo:
    # -------------------------------------------------------------------------
    test_identifier: str = "Script de Prácticas"
    is_active: bool = True
    iterations: int = 3

    print(f"🔍 Identificador: {test_identifier}")
    print(f"🔍 Estado activo: {is_active}")

    for index in range(1, iterations + 1):
        print(f"   ⚙️ Ejecutando prueba interna [{index}/{iterations}]...")

    # Resultado o validación final del experimento
    print("✅ Prueba local ejecutada correctamente.")


def main() -> None:
    """
    🔌 Punto de entrada principal con gestión de entorno, control de errores
    y medición de tiempo de ejecución.
    """
    # ⚙️ [1] Banner visual de inicio
    print("=" * 80)
    print("🚀 PYTHON PLAYGROUND | Entorno Local de Prácticas (`demos/index.py`)")
    print("=" * 80)

    start_time: float = time.perf_counter()

    try:
        # 📋 [2] Ejecución del área de pruebas
        run_playground()

    except Exception as error:
        # ❌ Manejo seguro de errores en tiempo de ejecución
        print(f"\n❌ [ERROR EN TIEMPO DE EJECUCIÓN]: {error}")
        print("🔍 Revisa la sintaxis o los tipos de datos en la función run_playground().")

    finally:
        # 🏁 [3] Cierre y métricas de tiempo
        execution_time: float = (time.perf_counter() - start_time) * 1000
        print("\n" + "=" * 80)
        print(f"✅ Fin de la ejecución. (Tiempo transcurrido: {execution_time:.2f} ms)")
        print("=" * 80)


if __name__ == "__main__":
    main()