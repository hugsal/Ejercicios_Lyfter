import unittest
import time
import sys


def run():
    print("=" * 60)
    print(" 🚀 PET SHOT API AUTOMATED TEST SUITE RUNNER")
    print("=" * 60)

    start_time = time.time()
    loader = unittest.TestLoader()
    suite = loader.discover("tests")

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    elapsed_time = time.time() - start_time

    total_tests = result.testsRun
    failures = len(result.failures)
    errors = len(result.errors)
    successful = total_tests - failures - errors
    success_rate = (successful / total_tests * 100) if total_tests > 0 else 0

    print("\n" + "=" * 60)
    print(" 📊 RESUMEN EJECUTIVO DE PRUEBAS UNITARIAS")
    print("=" * 60)
    print(f" Total de Pruebas Ejecutadas : {total_tests}")
    print(f" Pruebas Exitosas            : {successful} ✅")
    print(f" Pruebas Fallidas            : {failures} ❌")
    print(f" Errores de Ejecución        : {errors} ⚠️")
    print(f" Tasa de Éxito               : {success_rate:.1f}%")
    print(f" Tiempo Total de Ejecución   : {elapsed_time:.3f} segundos")
    print("=" * 60)

    if result.wasSuccessful():
        print("\n🎉 ¡TODAS LAS PRUEBAS UNITARIAS PASARON EXITOSAMENTE! 🎉\n")
        sys.exit(0)
    else:
        print("\n❌ ALGUNAS PRUEBAS FALLARON. REVISA EL LOG ANTERIOR. ❌\n")
        sys.exit(1)


if __name__ == "__main__":
    run()
