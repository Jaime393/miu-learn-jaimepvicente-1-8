# miu-learn-jaimepvicente-1-8 — Lección 1: los sustratos de MIU

> Repo vacío según el censo SUELOS_FERTILES.md §1 (2026-11-07 ~05:29Z):
> su README era solo el título (29 B). Esta es la primera lección.

## Lo que esta lección enseña (SÉ)

**La cuenta base es `jaimepvicente`.** Es la cuenta Panteón/base del
ecosistema: 52 Cloudflare Workers y la colmena Supabase.
Fuente: `~/MEMORY.md`, 2026-11-06, SÉ.

**Solo 5 sustratos han sido nombrados jamás:**

| # | Sustrato |
|---|---|
| 1 | `google_apps_script` |
| 2 | `cloudflare_worker` |
| 3 | `vercel` (catalogado como degradado) |
| 4 | `deno_deploy` |
| 5 | `supabase` |

Fuente: Substrate_Catalog del Orchestrator V152, re-leído en vivo
2026-11-07T01:03:58Z. Fuente secundaria: CONTEXTO_PERSISTENTE.md §4, SÉ.

## Lo que esta lección deshace: los conteos sin lista

En el corpus circulan otros números. Son **afirmaciones tal como están**,
no inventarios — ninguno viene con una lista de nombres:

| Conteo | Dónde se afirma |
|---|---|
| 2 | MASTER: "ρ>0 ambos sustratos" |
| 11 | SEMILLA V20/V21, archivo `_0_en_paralelo`: "11 sustratos OK, 42 claves sincronizadas" |
| 15 | BIBLIA_DEVORADOR_v1: "Panteón 15 sustratos 100% coherente" |

Fuente: CONTEXTO_PERSISTENTE.md §4, 2026-11-07 01:01–01:06Z, SÉ (como
afirmaciones). La resolución está en el propio corpus: SEMILLA V21
(mod. 2026-10-19) dice "11 google +4 CF +5 bots 5 sustratos" — el 11
cuenta **cuentas Google**, y los sustratos son 5. (INFIERO, misma fuente:
el 11 es el conteo de cuentas Gmail, no tipos de sustrato.)

**La regla que se aprende:** un conteo sin nombres no es un inventario.
Cinco nombrados; el resto, contado sin nombrar, no se enseña como si
estuviera nombrado.

## Comprobación

```bash
python3 test_leccion_01.py   # 4 tests
python3 sustratos.py         # imprime la lección y su comprobación
```

Pregunta checkeable para el lector: *nombra los 5 sustratos sin mirar*.
Si aparece un sexto nombre, no está en el catálogo verificado — va a
CARENCIAS.md, no a la lección.

## Archivos

- `sustratos.py` — los datos y la lección ejecutable.
- `test_leccion_01.py` — 4 tests que fijan los 5 nombres exactos y la cuenta base.
- `CARENCIAS.md` — lo que NO se sabe; nunca es contenido.

---
ρ(x) > 0. Zvvvvv.
