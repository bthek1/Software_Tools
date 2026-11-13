# Make

Here’s a practical, “know-it-for-real” guide to **GNU `make` + Makefiles**—what they are, how they work, the gotchas, and how to write Makefiles that don’t bite you later.

Author

Benedict Thekkel

## What `make` actually is

`make` is a **build orchestration tool**:

- You declare **targets** (things you want), and **prerequisites** (things they depend on).
- `make` decides **what is out of date** by comparing **file timestamps**.
- It runs **recipes** (shell commands) to bring targets up to date.

It’s fundamentally a *dependency graph executor*—not just for compiling C/C++, but also for “run tests”, “build docker”, “deploy”, etc.

------------------------------------------------------------------------

## Core mental model

### Rule format

git rev-parse –short HEAD

``` make
target: prereq1 prereq2
<TAB> command 1
<TAB> command 2
```

**Important:** recipes must start with a **TAB** (unless you change `.RECIPEPREFIX`).

### Timestamp logic

If `target` is missing, or older than any prerequisite, the recipe runs.

So this:

``` make
app: main.o util.o
    $(CC) -o $@ $^
```

means: if `app` is older than `main.o` or `util.o`, rebuild.

------------------------------------------------------------------------

## Most important special variables

| Variable | Meaning                                   |
|----------|-------------------------------------------|
| `$@`     | target name                               |
| `$<`     | first prerequisite                        |
| `$^`     | all prerequisites (deduped)               |
| `$+`     | all prerequisites (keeps duplicates)      |
| `$*`     | “stem” in pattern rules (e.g. `%.o: %.c`) |

Example:

``` make
%.o: %.c
    $(CC) -c $< -o $@
```

------------------------------------------------------------------------

## Phony targets (the \#1 gotcha)

If you have a target like `test:` and there’s a file named `test` in the directory, `make test` can stop working properly.

Fix with:

``` make
.PHONY: test lint format
```

Use `.PHONY` for commands that don’t produce a file with that name.

------------------------------------------------------------------------

## Each recipe line runs in a new shell (common pitfall)

This **doesn’t** work:

``` make
bad:
    cd backend
    python manage.py migrate
```

Because `cd backend` runs in one shell, the next line in another.

Fix by:

### Option A: chain with `&&`

``` make
good:
    cd backend && python manage.py migrate
```

### Option B: use `.ONESHELL`

``` make
.ONESHELL:
good:
    cd backend
    python manage.py migrate
```

If you use `.ONESHELL`, it applies to all recipes (unless scoped with target-specific trickery).

------------------------------------------------------------------------

## Default shell and strictness

By default, make uses `/bin/sh` (often `dash` on Ubuntu). If you rely on bashisms, set:

``` make
SHELL := /usr/bin/env bash
```

If you want “fail fast” behavior:

``` make
SHELL := /usr/bin/env bash
.SHELLFLAGS := -eu -o pipefail -c
```

- `-e`: stop on errors
- `-u`: undefined vars are errors
- `pipefail`: pipelines fail if any command fails

------------------------------------------------------------------------

## Variables: `=`, `:=`, `?=`, `+=`

These matter a lot.

| Operator | Meaning                      |
|----------|------------------------------|
| `=`      | recursive (lazy) expansion   |
| `:=`     | simple (immediate) expansion |
| `?=`     | set only if not already set  |
| `+=`     | append                       |

Example:

``` make
A = $(B)
B = hi
# A expands to "hi" (because = is lazy)

C := $(B)
# C expands to current B right now
```

**Tip:** Prefer `:=` unless you need lazy behavior.

------------------------------------------------------------------------

## Environment variables & overrides

- Environment variables are visible to `make`.
- You can override from CLI:

``` bash
make ENV=prod
```

In Makefile:

``` make
ENV ?= dev
deploy:
    ./deploy.sh $(ENV)
```

If you want a variable to be exported into recipe shells:

``` make
export DJANGO_SETTINGS_MODULE := config.settings
```

------------------------------------------------------------------------

## Includes & multi-file Makefiles

Split Makefiles cleanly:

``` make
include make/django.mk
include make/docker.mk
```

If the file might not exist:

``` make
-include .env.mk
```

------------------------------------------------------------------------

## Pattern rules, automatic builds (why `make` is powerful)

Pattern rule:

``` make
%.min.js: %.js
    minify $< > $@
```

Static pattern rule:

``` make
objects := a.o b.o
$(objects): %.o: %.c
    $(CC) -c $< -o $@
```

------------------------------------------------------------------------

## Functions you’ll use constantly

### `$(wildcard ...)`

``` make
PY_FILES := $(wildcard src/**/*.py)
```

### `$(shell ...)`

``` make
GIT_SHA := $(shell git rev-parse --short HEAD)
```

### `$(patsubst pattern,repl,text)`

``` make
SRC := a.c b.c
OBJ := $(patsubst %.c,%.o,$(SRC))
```

### `$(foreach var,list,text)`

``` make
print:
    @$(foreach f,$(SRC),echo $(f);)
```

------------------------------------------------------------------------

## Conditionals

``` make
ifeq ($(ENV),prod)
FLAGS += --optimize
else
FLAGS += --debug
endif
```

------------------------------------------------------------------------

## Target-specific variables (super useful)

``` make
test: PYTEST_FLAGS := -q
test:
    pytest $(PYTEST_FLAGS)
```

Only applies to that target.

------------------------------------------------------------------------

## Parallel builds

Run in parallel:

``` bash
make -j
make -j8
```

But be careful: if recipes write to shared files/dirs without proper deps, parallel runs will race.

------------------------------------------------------------------------

## Order-only prerequisites (directory creation without timestamp sensitivity)

Example: ensure `build/` exists, but don’t rebuild just because `build/` timestamp changes:

``` make
build/app: src/main.c | build
    $(CC) $< -o $@

build:
    mkdir -p build
```

The `|` means **order-only prerequisite**.

------------------------------------------------------------------------

## Good “help” target pattern (what you were using)

The pattern you posted is common: parse `##` comments to auto-generate help.

A minimal form:

``` make
.PHONY: help
help:
    @awk 'BEGIN {FS=":.*## "}; /^[a-zA-Z0-9_.-]+:.*## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)
```

Use `$(MAKEFILE_LIST)` instead of `$(MAKEFILE)` so it works across included Makefiles.

------------------------------------------------------------------------

## Anti-patterns (what breaks Makefiles)

1.  **Not using `.PHONY`** for command targets
2.  **Assuming bash** when `sh` is used
3.  **Multi-line shell state** without `.ONESHELL`
4.  **Tabs vs spaces** issues
5.  **Making everything always run** (turning make into a task runner that ignores deps—sometimes fine, but then `make` gives you less value)

------------------------------------------------------------------------

## Make as a “task runner” vs real dependency builds

For Django/dev workflows, many teams use make as a **task runner**:

- `make migrate`
- `make test`
- `make run`

That’s okay—just be explicit that these targets are `.PHONY`.

If you actually want `make`’s power, use it for:

- generated files (compiled assets)
- build artifacts
- codegen outputs
- docs builds
- container images (with tags as targets)

------------------------------------------------------------------------

## Debugging `make`

### See what it would do (no execution)

``` bash
make -n target
```

### Verbose / debug rule resolution

``` bash
make -d target
```

### Print variable value

``` bash
make -p | less
```

Or add:

``` make
print-%:
    @echo $*=$($*)
```

Then:

``` bash
make print-SHELL
make print-ENV
```

------------------------------------------------------------------------

## A clean Makefile template for a Django project

``` make
SHELL := /usr/bin/env bash
.SHELLFLAGS := -eu -o pipefail -c

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show commands
    @awk 'BEGIN {FS=":.*## "}; /^[a-zA-Z0-9_.-]+:.*## / {printf "  %-20s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.PHONY: venv
venv: ## Create venv
    python -m venv .venv

.PHONY: install
install: ## Install deps
    . .venv/bin/activate && pip install -r requirements.txt

.PHONY: run
run: ## Run dev server
    . .venv/bin/activate && python manage.py runserver

.PHONY: migrate
migrate: ## Apply migrations
    . .venv/bin/activate && python manage.py migrate

.PHONY: test
test: ## Run tests
    . .venv/bin/activate && pytest -q
```

------------------------------------------------------------------------

## When you should *not* use Make

If you:

- need cross-platform Windows support without WSL,
- want rich argument parsing / subcommands,
- want better UX + autocompletion,

then tools like **just**, **task**, **invoke**, **nox**, **poetry scripts**, **npm scripts**, or **uv run** wrappers can be cleaner.

But `make` stays great when you want:

- simple command hub
- dependency-based builds
- ubiquitous tooling with zero extra install on Linux/macOS

------------------------------------------------------------------------

## Cheat sheet (quick reference)

| Need                            | Use                                   |     |
|---------------------------------|---------------------------------------|-----|
| default target                  | `.DEFAULT_GOAL := help`               |     |
| phony targets                   | `.PHONY: ...`                         |     |
| bash + strict mode              | `SHELL := ...` + `.SHELLFLAGS := ...` |     |
| same shell for all recipe lines | `.ONESHELL:`                          |     |
| show help from `##`             | awk over `$(MAKEFILE_LIST)`           |     |
| directories as deps             | order-only prereqs `| dir`            |     |
| override vars in CLI            | `make ENV=prod`                       |     |
| parallel runs                   | `make -j`                             |     |

------------------------------------------------------------------------

If you want, paste your current Makefile (or the top-level layout with `include`s), and I’ll:

- normalize it (bash strict mode + `MAKEFILE_LIST` help)
- remove sharp edges (`cd` issues, missing `.PHONY`)
- and show a “dependency-aware” version where it actually benefits (assets/build artifacts).

------------------------------------------------------------------------

Back to top
