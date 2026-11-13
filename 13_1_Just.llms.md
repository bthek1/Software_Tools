# Just

`just` is a **command runner** (task runner) that uses a `justfile` with a Make-like feel, but it’s **not a build system**: it doesn’t do timestamp-based dependency rebuilding the way `make` does. (\[GitHub\]\[1\])

Author

Benedict Thekkel

## What `just` is (and isn’t)

### ✅ Great for

- “one command per workflow step”: `dev`, `test`, `lint`, `migrate`, `deploy`, `docker-up`, etc.
- cross-platform-ish command orchestration (especially compared to Makefiles that rely on GNU Make quirks)

### ❌ Not for

- incremental builds based on file timestamps (that’s `make`’s home turf)

`just` is intentionally “task runner first”. (\[GitHub\]\[1\])

------------------------------------------------------------------------

## Install (common ways)

You can install via Cargo, Homebrew, Conda, Nix, etc. (\[Just Systems\]\[2\])

------------------------------------------------------------------------

## The `justfile` basics

A `justfile` defines **recipes**:

``` just
# justfile
dev:
  python manage.py runserver

test:
  pytest -q
```

- Recipes are invoked with: `just <recipe>`
- List recipes: `just --list` (handy for discovery) (\[Medium\]\[3\])

------------------------------------------------------------------------

## Recipe dependencies (ordering)

You can make one recipe depend on another:

``` just
migrate:  # runs after deps
  python manage.py migrate

dev: migrate
  python manage.py runserver
```

This is **task dependency ordering**, not file-based rebuilding.

------------------------------------------------------------------------

## Arguments & parameters

### Positional args

``` just
hello name:
  echo "Hello {{name}}"
```

Run:

``` bash
just hello Ben
```

### Default values

``` just
serve host="127.0.0.1" port="8000":
  python manage.py runserver {{host}}:{{port}}
```

Run:

``` bash
just serve
just serve 0.0.0.0 8000
```

------------------------------------------------------------------------

## Variables & interpolation

Just variables use `:=` and interpolate with `{ }`:

``` just
app := "rm"
sha := `git rev-parse --short HEAD`

build:
  echo "{{app}} @ {{sha}}"
```

- Backticks run shell commands and capture output.
- Interpolation happens before execution, so quoting matters when values contain spaces (this comes up a lot). (\[GitHub\]\[4\])

------------------------------------------------------------------------

## Settings you’ll actually use

Settings live at the top:

``` just
set export
set quiet
```

- `set export` exports `just` variables into the recipe environment. (\[Just Systems\]\[5\])
- `set quiet` makes recipes silent by default (no echoing commands). (\[Charmhub\]\[6\])

(You can still explicitly echo/log when you want.)

------------------------------------------------------------------------

## `.env` / dotenv behavior

`just` supports loading dotenv-style env files and has CLI flags like `--dotenv-filename` and `--dotenv-path`. (\[Fig\]\[7\])

Two practical notes:

- Dotenv behavior has had design discussion and edge-case issues over time (especially around modular/hierarchical setups). (\[GitHub\]\[8\])
- If your workflows rely heavily on `.env`, keep it explicit and test it in CI.

------------------------------------------------------------------------

## Shell, portability, and “it works on my machine”

Unlike Make, `just` isn’t bound to “TABs or bust”, and it tends to be less foot-gun-y for task running. (\[Medium\]\[9\])

Still, portability depends on what you put *inside* recipes:

- `bash`-isms won’t work in `sh` environments
- tools like `sed`, `grep`, `awk` vary between macOS/Linux

If you want predictability, prefer:

- `python -m ...` for Python tasks
- `docker compose ...`
- dedicated scripts in `scripts/`

------------------------------------------------------------------------

## Debugging & quality-of-life commands

Useful flags:

- `just --list` → show available recipes (\[Medium\]\[3\])
- `just --dry-run` → print what would run (\[Fig\]\[7\])
- `just --dump` → print the resolved justfile (\[Fig\]\[7\])
- `just --fmt` → format the justfile (\[Fig\]\[7\])
- `just -e` / `--edit` → open in editor (\[Fig\]\[7\])

------------------------------------------------------------------------

## A “ship-it” `justfile` for Django

``` just
set quiet
set export

# ---- Vars ----
python := "python"
manage := "{{python}} manage.py"

# ---- Help-ish ----
default:
  just --list

# ---- Django ----
run:
  {{manage}} runserver

makemigrations:
  {{manage}} makemigrations

migrate:
  {{manage}} migrate

createsuperuser:
  {{manage}} createsuperuser

collectstatic:
  {{manage}} collectstatic --noinput

# ---- Quality ----
test:
  pytest -q

lint:
  ruff check .

format:
  ruff format .

# ---- Docker (optional) ----
up:
  docker compose up -d

down:
  docker compose down

logs:
  docker compose logs -f
```

Why this structure works well:

- variables keep commands DRY
- `set export` makes vars available as env when needed (\[Just Systems\]\[5\])
- quiet output by default keeps it readable (\[Charmhub\]\[6\])

------------------------------------------------------------------------

## `just` vs `make` (fast comparison)

| Feature         | `just`               | `make`                       |
|-----------------|----------------------|------------------------------|
| Primary goal    | run project commands | build system + deps          |
| Dependency type | recipe ordering      | file timestamps + graph      |
| Syntax pain     | low                  | TABs, shell-per-line gotchas |
| Discoverability | `--list` built-in    | usually custom `help`        |
| Best use        | task runner          | compiling/build artifacts    |

(If you’re replacing your Django Makefile, `just` is usually a straight win.)

------------------------------------------------------------------------

Back to top
