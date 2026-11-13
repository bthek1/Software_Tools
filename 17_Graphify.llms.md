# Graphify

Graphify

Author

Benedict Thekkel

**Graphify** is an open-source CLI + AI-assistant skill that parses a repo into a knowledge graph you query instead of grepping. Type `/graphify` in your AI coding assistant and it maps your project (code, docs, PDFs, images, videos) into a knowledge graph. Currently ~99k stars, Apache-2.0/MIT dual-licensed, by Safi Shamsi / Graphify Labs (YC S26).

**The core idea** Code is parsed with tree-sitter AST — deterministic, no LLM, nothing leaves your machine. Docs, PDFs, images and video use your assistant’s model for a semantic pass. Each connection is tagged `EXTRACTED` (explicit in the source) or `INFERRED` (resolved by graphify). No embeddings, no vector store: a real graph you traverse. That’s the pitch versus RAG — traversal with file:line provenance instead of fuzzy top-k chunks.

**Install and use**

    uv tool install graphifyy    # note the double-y; graphify* on PyPI is not affiliated
    graphify install             # registers the skill (Claude Code by default)
    /graphify .

Output is three files in `graphify-out/`: `graph.html` (interactive), `GRAPH_REPORT.md` (key concepts, surprising connections, suggested questions), and `graph.json` (the full graph).

Query surface:

    graphify query "what connects auth to the database?"
    graphify path "UserService" "DatabasePool"
    graphify explain "APIRouter"

**What’s in the box** - God nodes (most-connected concepts), Leiden community detection with LLM-free labels, cross-file `calls`/`imports`/`inherits` edges across ~40 languages - `# NOTE:` / `# WHY:` comments and ADR/RFC citations become first-class nodes linked to the code - MCP server (`python -m graphify.serve`) exposing `query_graph`, `get_node`, `get_neighbors`, `shortest_path`; stdio or shared HTTP transport with `--api-key` - Exports to Neo4j/FalkorDB cypher, GraphML, SVG, Obsidian vault, markdown wiki - Git hooks for auto-rebuild on commit, plus a merge driver that union-merges `graph.json` so parallel commits don’t conflict - `--postgres DSN` for live PostgreSQL schema introspection - 20+ assistant platforms; `graphify claude install` writes a `PreToolUse` hook that nudges the assistant to query the graph before grepping, `--strict` blocks the first raw source read of a session

**Relevant to your stack:** the Postgres introspection plus `.py`/`.tsx`/`.sql` extraction means a Django + React monorepo maps reasonably well, and `graphify-out/` is meant to be committed so the whole team starts with a map.

**My honest read** - The AST layer is the real product and it’s sound — tree-sitter, deterministic, free, offline. That part I’d trust. - The benchmarks (LOCOMO recall@10 0.497 vs mem0 0.048; LongMemEval-S 76% tied with dense RAG) are self-published by the maintainer on his own harness. Treat as directional, not validated. - 99k stars with ~1,300 commits and a release nearly every day, plus a heavily marketed enterprise waitlist, is a pattern worth being skeptical of. The star count is not evidence of engineering quality. - Practical gotchas: HTML viz falls over above ~5000 nodes, and the `graphifyy`-vs-`graphify` package/command split causes a lot of the reported install failures.

If you want to evaluate it, run it on Recovery Metrics code-only (`graphify extract . --code-only`) — zero API cost, fully local, and you’ll know within ten minutes whether the graph actually reflects your architecture.

Back to top
