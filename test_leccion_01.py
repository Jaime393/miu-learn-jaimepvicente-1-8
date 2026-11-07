#!/usr/bin/env python3
"""Tests de la lección 1. Solo stdlib. Sin red, sin secretos.

Ejecutar: python3 test_leccion_01.py
"""
import os
import subprocess
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import sustratos  # noqa: E402


def test_cinco_sustratos_nombrados_exactos():
    """Solo 5 sustratos nombrados jamás (SÉ, Substrate_Catalog V152,
    2026-11-07T01:03:58Z). Nombres exactos, sin duplicados."""
    assert sustratos.SUSTRATOS_NOMBRADOS == [
        "google_apps_script",
        "cloudflare_worker",
        "vercel",
        "deno_deploy",
        "supabase",
    ]


def test_cuenta_base_jaimepvicente():
    """jaimepvicente es base/Panteón, 52 Workers, colmena Supabase
    (SÉ, ~/MEMORY.md, 2026-11-06)."""
    base = sustratos.CUENTA_BASE
    assert base["gmail"] == "jaimepvicente"
    assert base["cloudflare_workers"] == 52
    assert base["supabase"] == "colmena"


def test_conteos_sin_nombrar_no_se_mezclan():
    """Los conteos 2, 11 y 15 existen como afirmaciones, pero ninguno es
    una lista de sustratos: no se pueden confundir con los 5 nombrados."""
    conteos = sustratos.CONTEOS_QUE_CIRCULAN
    assert sorted(conteos) == [2, 11, 15]
    assert all(n != len(sustratos.SUSTRATOS_NOMBRADOS) for n in conteos)
    # Ningún conteo trae nombres: son cadenas de procedencia, no listas.
    assert all(isinstance(v, str) for v in conteos.values())


def test_leccion_imprime_y_pasa():
    """sustratos.py corre y su comprobación final es OK."""
    r = subprocess.run([sys.executable, os.path.join(AQUI, "sustratos.py")],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "Comprobación: OK" in r.stdout
    assert "5 nombrados" in r.stdout


if __name__ == "__main__":
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    fallos = 0
    for t in tests:
        try:
            t()
            print(f"PASS {t.__name__}")
        except AssertionError as e:
            fallos += 1
            print(f"FAIL {t.__name__}: {e}")
    print(f"{len(tests) - fallos}/{len(tests)} tests OK")
    raise SystemExit(1 if fallos else 0)
