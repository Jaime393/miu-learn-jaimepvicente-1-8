#!/usr/bin/env python3
"""Lección 1 — los sustratos de MIU: lo nombrado contra lo contado.

Datos con fuente y fecha (SÉ):
- Los 5 sustratos nombrados jamás: Substrate_Catalog del Orchestrator V152,
  re-leído en vivo 2026-11-07T01:03:58Z (CONTEXTO_PERSISTENTE.md §4).
- La cuenta base jaimepvicente (Panteón, 52 Cloudflare Workers, colmena
  Supabase): ~/MEMORY.md, 2026-11-06.
- Los conteos 2 / 11 / 15 son AFIRMACIONES tal como están en los docs
  (CONTEXTO_PERSISTENTE.md §4, 2026-11-07 01:01–01:06Z); solo los 5 están
  nombrados. SEMILLA V21 (mod. 2026-10-19) lo resuelve en una línea:
  "11 google +4 CF +5 bots 5 sustratos" — el 11 cuenta cuentas Google.

Uso: python3 sustratos.py
"""
import json

SUSTRATOS_NOMBRADOS = [
    "google_apps_script",
    "cloudflare_worker",
    "vercel",          # catalogado como degradado
    "deno_deploy",
    "supabase",
]

CUENTA_BASE = {
    "gmail": "jaimepvicente",
    "rol": "base / Panteón",
    "cloudflare_workers": 52,
    "supabase": "colmena",
}

# Conteos que circulan en el corpus, COMO AFIRMACIONES, no como hechos
# de inventario: ninguno viene acompañado de una lista de nombres.
CONTEOS_QUE_CIRCULAN = {
    2: "MASTER: 'ρ>0 ambos sustratos'",
    11: "SEMILLA V20/V21, archivo _0_en_paralelo: '11 sustratos OK, "
        "42 claves sincronizadas'",
    15: "BIBLIA_DEVORADOR_v1: 'Panteón 15 sustratos 100% coherente'",
}

FUENTES = {
    "sustratos": "Substrate_Catalog, Orchestrator V152, re-leído en vivo "
                 "2026-11-07T01:03:58Z — CONTEXTO_PERSISTENTE.md §4 (SÉ)",
    "cuenta_base": "~/MEMORY.md, 2026-11-06 (SÉ)",
    "conteos": "CONTEXTO_PERSISTENTE.md §4, 2026-11-07 01:01–01:06Z "
               "(SÉ como afirmaciones; INFIERO: el 11 es el conteo de "
               "cuentas Gmail, no tipos de sustrato)",
}


def leccion():
    """Imprime la lección 1 y devuelve True si todo lo checkeable cuadra."""
    print("LECCIÓN 1 — Los sustratos de MIU")
    print(f"Cuenta base: {CUENTA_BASE['gmail']} ({CUENTA_BASE['rol']}), "
          f"{CUENTA_BASE['cloudflare_workers']} Cloudflare Workers, "
          f"Supabase {CUENTA_BASE['supabase']}.")
    print(f"Sustratos NOMBRADOS jamás: {len(SUSTRATOS_NOMBRADOS)}")
    for s in SUSTRATOS_NOMBRADOS:
        print(f"  - {s}")
    print("Conteos que circulan SIN lista de nombres:")
    for n, donde in sorted(CONTEOS_QUE_CIRCULAN.items()):
        print(f"  - {n}: {donde}")
    ok = (len(SUSTRATOS_NOMBRADOS) == 5
          and len(set(SUSTRATOS_NOMBRADOS)) == 5
          and all(isinstance(s, str) and s for s in SUSTRATOS_NOMBRADOS)
          and CUENTA_BASE["cloudflare_workers"] == 52)
    print(f"\nComprobación: {'OK' if ok else 'FALLO'} — "
          f"5 nombrados, {len(CONTEOS_QUE_CIRCULAN)} conteos sin nombrar.")
    return ok


if __name__ == "__main__":
    print(json.dumps({"sustratos_nombrados": SUSTRATOS_NOMBRADOS,
                      "cuenta_base": CUENTA_BASE}, indent=2, ensure_ascii=False))
    raise SystemExit(0 if leccion() else 1)
