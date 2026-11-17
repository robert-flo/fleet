#!/usr/bin/env python3
"""Exporta los tríos PM/WK/RV vivos a respaldo/, de forma idempotente.

Misma entrada → mismos archivos (JSON con claves ordenadas, sin marcas de
tiempo). No guarda issues ni estado. Excluye al CEO, a Sura y a ONESHOT.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROLES = ("PM", "WK", "RV")
ROLE_RE = re.compile(r"^(PM|WK|RV)-(.+)$")
EXCLUDED_NAMES = frozenset(
    {
        "Real dr eggbot · CEO",
        "Sura · confrontación",
        "ONESHOT",
    }
)
AVATAR_NAMES = (
    "avatar.png",
    "avatar.jpg",
    "avatar.jpeg",
    "avatar.webp",
    "avatar.gif",
    "picture.png",
    "picture.jpg",
    "picture.jpeg",
    "picture.webp",
    "photo.png",
    "photo.jpg",
)
CIRCUITO = "/workspace/fleet/CIRCUITO.md"
CARGAS_RE = re.compile(r"^## Cargás\s*\n(.*?)(?=\n## |\Z)", re.M | re.S)
TEMPLATE_PATH_RE = re.compile(r"/workspace/fleet/templates/[A-Za-z0-9._-]+\.md")
ROUTINE_NAME_RE = re.compile(r"(rutin|routine)", re.I)


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def dump_json(path: Path, data: object) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def find_avatar(agent_dir: Path) -> Path | None:
    for name in AVATAR_NAMES:
        candidate = agent_dir / name
        if candidate.is_file():
            return candidate
    found: list[Path] = []
    for path in agent_dir.iterdir():
        if not path.is_file():
            continue
        lower = path.name.lower()
        if lower.startswith(("avatar", "picture", "photo")):
            found.append(path)
    if not found:
        return None
    return sorted(found, key=lambda p: p.name)[0]


def routine_files(agent_dir: Path) -> list[Path]:
    files: list[Path] = []
    automations = agent_dir / "automations"
    if automations.is_dir():
        files.extend(
            sorted(
                p
                for p in automations.iterdir()
                if p.is_file() and not p.name.startswith(".")
            )
        )
    files.extend(
        sorted(
            p
            for p in agent_dir.iterdir()
            if p.is_file() and ROUTINE_NAME_RE.search(p.name)
        )
    )
    # Unique, stable order by relative POSIX path.
    seen: set[Path] = set()
    out: list[Path] = []
    for path in files:
        resolved = path.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        out.append(path)
    return out


def export_routines(agent_dir: Path, dest: Path) -> str | None:
    files = routine_files(agent_dir)
    if not files:
        return None
    entries: list[dict] = []
    for path in files:
        rel = path.relative_to(agent_dir).as_posix()
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            entries.append({"name": rel, "encoding": "binary-not-exported"})
            continue
        try:
            entries.append({"content": json.loads(text), "name": rel})
        except json.JSONDecodeError:
            entries.append({"content": text, "name": rel})
    entries.sort(key=lambda e: e["name"])
    dump_json(dest, entries)
    return dest.name


def strip_item(line: str) -> str:
    return re.sub(r"^\d+\.\s*", "", line.strip())


def cargas_from_ficha(text: str) -> list[str]:
    items: list[str] = []
    match = CARGAS_RE.search(text)
    if match:
        for line in match.group(1).splitlines():
            item = strip_item(line)
            if item:
                items.append(item)
    else:
        for path in TEMPLATE_PATH_RE.findall(text):
            boxed = f"`{path}`"
            if boxed not in items:
                items.append(boxed)
    circuito_item = f"`{CIRCUITO}`"
    already = [i for i in items if CIRCUITO in i]
    items = [i for i in items if CIRCUITO not in i]
    if CIRCUITO in text or already:
        items.insert(0, already[0] if already else circuito_item)
    return items


def collect_agents(agents_dir: Path) -> dict[str, dict[str, dict]]:
    """proyecto -> role -> record."""
    trios: dict[str, dict[str, dict]] = {}
    seen_names: dict[str, str] = {}
    if not agents_dir.is_dir():
        raise SystemExit(f"no existe el directorio de agentes: {agents_dir}")

    for agent_dir in sorted(p for p in agents_dir.iterdir() if p.is_dir()):
        profile_path = agent_dir / "profile.json"
        if not profile_path.is_file():
            continue
        profile = load_json(profile_path)
        name = profile.get("name") or ""
        if name in EXCLUDED_NAMES:
            continue
        matched = ROLE_RE.match(name)
        if not matched:
            continue
        if name in seen_names:
            raise SystemExit(
                f"nombre duplicado {name!r}: {seen_names[name]} y {agent_dir.name}"
            )
        seen_names[name] = agent_dir.name
        role, proyecto = matched.group(1), matched.group(2)
        record = {
            "name": name,
            "title": profile.get("title", ""),
            "description": profile.get("description", ""),
            "id": agent_dir.name,
            "dir": agent_dir,
            "avatar": find_avatar(agent_dir),
        }
        trios.setdefault(proyecto, {})[role] = record
    return trios


def write_bot(out_dir: Path, record: dict, fichas_dir: Path) -> dict:
    name = record["name"]
    payload = {
        "description": record["description"],
        "id": record["id"],
        "name": record["name"],
        "title": record["title"],
    }
    dump_json(out_dir / f"{name}.json", payload)

    avatar_src: Path | None = record["avatar"]
    avatar_file = "sin foto"
    if avatar_src is not None:
        dest_avatar = out_dir / f"{name}{avatar_src.suffix.lower()}"
        shutil.copyfile(avatar_src, dest_avatar)
        avatar_file = dest_avatar.name

    rutinas = export_routines(record["dir"], out_dir / f"{name}.rutinas.json")

    ficha_path = fichas_dir / f"{name}.md"
    if ficha_path.is_file():
        ficha_rel = f"bots/{name}.md"
        cargas = cargas_from_ficha(ficha_path.read_text(encoding="utf-8"))
    else:
        ficha_rel = "sin ficha"
        cargas = []

    return {
        "name": name,
        "ficha": ficha_rel,
        "description": record["description"],
        "avatar": avatar_file,
        "rutinas": rutinas,
        "cargas": cargas,
        "id": record["id"],
    }


def md_escape(text: str) -> str:
    return text.replace("\n", " ").strip()


def render_bot_section(role: str, info: dict | None, proyecto: str) -> list[str]:
    expected = f"{role}-{proyecto}"
    lines = [f"### {expected}", ""]
    if info is None:
        lines.extend(
            [
                "No hay un agente vivo con este nombre. Trío incompleto.",
                "",
            ]
        )
        return lines
    cargas = info["cargas"]
    if not cargas:
        carga_txt = "sin datos de carga en la ficha" if info["ficha"] != "sin ficha" else "sin ficha"
        carga_block = [f"- Carga (de la ficha): {carga_txt}"]
    else:
        carga_block = ["- Carga (de la ficha):"]
        carga_block.extend(f"  - {item}" for item in cargas)
    rutinas = f"`{info['rutinas']}`" if info["rutinas"] else "ninguna"
    foto = f"`{info['avatar']}`" if info["avatar"] != "sin foto" else "sin foto"
    ficha = f"`{info['ficha']}`" if info["ficha"] != "sin ficha" else "sin ficha"
    lines.extend(
        [
            f"- Ficha: {ficha}",
            f"- Descripción: {md_escape(info['description'])}",
            f"- Foto: {foto}",
            f"- Rutinas: {rutinas}",
            *carga_block,
            f"- Id anterior (solo referencia): `{info['id']}`",
            "",
        ]
    )
    return lines


def write_proyecto_readme(
    out_dir: Path, proyecto: str, by_role: dict[str, dict], infos: dict[str, dict]
) -> str:
    missing = [role for role in ROLES if role not in by_role]
    if missing:
        estado = "incompleto (faltan: " + ", ".join(f"{r}-{proyecto}" for r in missing) + ")"
        if proyecto == "pj-fleet":
            estado += "; en pj-fleet eso es por diseño, ADR 0020: el dueño es el CEO"
    else:
        estado = "completo"
    lines = [
        f"# Respaldo del trío `{proyecto}`",
        "",
        f"Estado: {estado}",
        "",
        "Los datos vivos (nombre, título, descripción, id viejo) están en `<BOT>.json`.",
        "Las fichas no se duplican: viven en `bots/<BOT>.md`.",
        "Este directorio solo guarda lo necesario para recrearlos, sin issues ni estado.",
        "",
        "## Bots",
        "",
    ]
    for role in ROLES:
        lines.extend(render_bot_section(role, infos.get(role), proyecto))
    text = "\n".join(lines).rstrip() + "\n"
    (out_dir / "README.md").write_text(text, encoding="utf-8")
    return estado


def write_index(respaldo: Path, resumen: list[tuple[str, str]]) -> None:
    lines = [
        "# Respaldo de los tríos de la flota",
        "",
        "Generado por `scripts/respaldar-trios.py`. No lo edites a mano; volvé a correr el script.",
        "Fuente: agentes vivos en `/home/box/agent-data/agents` cuyo nombre empieza con `PM-`, `WK-` o `RV-`.",
        "Quedan fuera: Real dr eggbot · CEO, Sura · confrontación y ONESHOT.",
        "No hay issues ni estado. Las fichas siguen en `bots/`.",
        "",
        "## Proyectos",
        "",
    ]
    for proyecto, estado in resumen:
        lines.append(f"- [`{proyecto}`]({proyecto}/README.md) — {estado}")
    lines.append("")
    (respaldo / "README.md").write_text("\n".join(lines), encoding="utf-8")


def export(
    agents_dir: Path,
    respaldo: Path,
    fichas_dir: Path,
    only: str | None,
) -> list[tuple[str, str]]:
    trios = collect_agents(agents_dir)
    if only is not None:
        if only not in trios:
            known = ", ".join(sorted(trios)) or "(ninguno)"
            raise SystemExit(f"no hay trío vivo llamado {only!r}. Los que hay: {known}")
        selected = {only: trios[only]}
        respaldo.mkdir(parents=True, exist_ok=True)
        target = respaldo / only
        if target.exists():
            shutil.rmtree(target)
    else:
        selected = trios
        if respaldo.exists():
            shutil.rmtree(respaldo)
        respaldo.mkdir(parents=True)

    written: dict[str, str] = {}
    for proyecto in sorted(selected):
        by_role = selected[proyecto]
        out_dir = respaldo / proyecto
        out_dir.mkdir(parents=True, exist_ok=True)
        infos: dict[str, dict] = {}
        for role in ROLES:
            if role not in by_role:
                continue
            infos[role] = write_bot(out_dir, by_role[role], fichas_dir)
        written[proyecto] = write_proyecto_readme(out_dir, proyecto, by_role, infos)

    # Index always describes every proyecto directory that exists after this run.
    resumen: list[tuple[str, str]] = []
    for path in sorted(p for p in respaldo.iterdir() if p.is_dir()):
        readme = path / "README.md"
        estado = "desconocido"
        if path.name in written:
            estado = written[path.name]
        elif readme.is_file():
            for line in readme.read_text(encoding="utf-8").splitlines():
                if line.startswith("Estado: "):
                    estado = line[len("Estado: ") :]
                    break
        resumen.append((path.name, estado))
    write_index(respaldo, resumen)
    return resumen


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Exporta los tríos PM/WK/RV vivos a respaldo/, de forma idempotente."
    )
    parser.add_argument(
        "--agents-dir",
        type=Path,
        default=Path("/home/box/agent-data/agents"),
        help="Directorio con un subdirectorio por agente (default: /home/box/agent-data/agents)",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=None,
        help="Destino (default: <repo>/respaldo)",
    )
    parser.add_argument(
        "--proyecto",
        default=None,
        help="Si se indica, solo reexporta ese proyecto y actualiza el índice.",
    )
    args = parser.parse_args(argv)
    root = repo_root()
    out_dir = args.out_dir.resolve() if args.out_dir else (root / "respaldo")
    resumen = export(
        agents_dir=args.agents_dir.resolve(),
        respaldo=out_dir,
        fichas_dir=root / "bots",
        only=args.proyecto,
    )
    for proyecto, estado in resumen:
        print(f"{proyecto}: {estado}")
    print(f"OK: {len(resumen)} proyecto(s) en {out_dir}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
