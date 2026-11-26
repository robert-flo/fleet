#!/usr/bin/env bash
# Falla si una ficha o plantilla no carga CIRCUITO.md, o si contradice C5/C6/C9/C11/C13.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

REQUIRED="Antes que nada leé /workspace/fleet/CIRCUITO.md; gana sobre tu memoria y sobre esta ficha."

# Frases que contradicen C5/C9 (el RV publica sin pedir permiso; nadie
# le pide confirmación a Roberto dentro del circuito).
# "sin publicar" suelto es demasiado amplio: las fichas RV ya dicen
# "Nunca dejes un veredicto escrito sin publicar esperando su orden."
FORBIDDEN_REGEXES=(
  'espero la confirmación de Roberto'
  'todavía sin publicar'
  'sin publicar porque'
  'sin publicar hasta'
  'no alcanza con que me lo transmitas'
  'espero a Roberto para publicar'
  'esperando (a )?Roberto para publicar'
  'no public(o|és|ar) hasta'
  # C11: un encargo del PM ya está aprobado (ADR 0029).
  'propias palabras'
  'que vos digas que (él|Roberto) lo aprobó'
  # C6/C13: las ramas de spec se conservan después del merge (ADR 0029).
  # Solo el comando: mencionar «sin `--delete-branch`» está bien.
  'pr merge[^`]*--delete-branch'
)

fail=0

while IFS= read -r -d '' f; do
  rel="${f#"$ROOT"/}"
  base="$(basename "$f")"
  if [[ "$base" == "CIRCUITO.md" ]]; then
    continue
  fi

  if ! grep -qF "$REQUIRED" "$f"; then
    echo "FALTA la línea de CIRCUITO.md: $rel"
    fail=1
  fi

  for re in "${FORBIDDEN_REGEXES[@]}"; do
    if matches="$(grep -Eni -e "$re" "$f" || true)"; then
      if [[ -n "$matches" ]]; then
        echo "Contradice C5/C6/C9/C11/C13 (/$re/): $rel"
        echo "$matches"
        fail=1
      fi
    fi
  done
done < <(find bots templates -type f -name '*.md' -print0 | sort -z)

if [[ "$fail" -ne 0 ]]; then
  exit 1
fi

echo "OK: fichas y plantillas alineadas con CIRCUITO.md"
