# Abstract Syntax Tree (AST)

An AST is a tree representation of the syntactic structure of source code, where each node represents a construct in the language — but stripped of irrelevant syntactic details (parentheses, semicolons, whitespace).

Author

Benedict Thekkel

## Why “Abstract”?

Unlike a *concrete* syntax tree (parse tree), an AST omits redundant grammatical nodes. For `1 + 2 * 3`:

- **Parse tree** retains every grammar rule node
- **AST** just gives you `BinaryOp(+, Literal(1), BinaryOp(*, Literal(2), Literal(3)))`\### Structure of an AST node

Every node typically carries: - **type** — what construct it represents (`FunctionDef`, `BinaryOp`, `IfStatement`, etc.) - **children** — sub-nodes (operands, body, arguments) - **metadata** — line/column numbers for error reporting, sometimes type annotations

------------------------------------------------------------------------

## How an AST is produced

**1. Lexing (tokenisation)** — raw source → stream of tokens (`INT:1`, `PLUS`, `INT:2`, etc.)

**2. Parsing** — token stream → parse tree (concrete syntax tree, every grammar rule materialised)

**3. AST construction** — parse tree → AST (drop literals, punctuation, redundant grammar nodes)

Most compilers and interpreters expose the AST directly, skipping the intermediate CST from user perspective.

------------------------------------------------------------------------

## What ASTs are used for

| Use case | How the AST is consumed |
|----|----|
| Compilation / interpretation | Walk the tree, emit bytecode or machine code |
| Static analysis / linting | Traverse nodes, pattern-match anti-patterns |
| Type checking | Annotate nodes with inferred types bottom-up |
| Code transformation | Rewrite nodes (Babel, macros, codemods) |
| IDE tooling | Hover info, go-to-definition, rename refactors |
| Minification / bundling | Prune dead nodes, rename identifiers |
| Code generation / templating | Construct an AST programmatically, serialise to source |

------------------------------------------------------------------------

## Tree traversal patterns

The two fundamental traversals you’ll see everywhere:

**Visitor pattern** — define `visit_<NodeType>` methods; the walker dispatches on node type. Used by Python’s `ast` module, ESTree tools, LLVM passes.

**Recursive descent** — write a recursive function that switches on `node.type` and recurses into children. Simple, readable, fine for one-off tools.

**Pre-order vs post-order** matters: for code generation you usually want post-order (evaluate children before the operator). For scope resolution you often want pre-order (enter scope before visiting body).

------------------------------------------------------------------------

## ASTs in popular languages/tools

- **Python** — `import ast`; `ast.parse(src)` gives you the full tree, `ast.dump()` pretty-prints it, `ast.NodeVisitor` / `ast.NodeTransformer` for walking and rewriting
- **JavaScript** — ESTree spec (Acorn, Espree); Babel uses its own AST with `@babel/parser` + `@babel/traverse` + `@babel/types`; ts-morph wraps the TypeScript compiler API
- **Java** — `javax.lang.model` (annotation processing), or JavaParser for source-level ASTs
- **C/C++** — Clang’s LibAST; `clang -ast-dump` prints it
- **Rust** — `syn` crate (proc macros); `rustc`’s HIR/MIR are post-AST lowerings
- **General** — Tree-sitter is a universal parser that generates ASTs for ~100 languages with incremental reparsing (used in Neovim, GitHub’s code search, and many LSPs)

------------------------------------------------------------------------

## AST vs related representations

| Representation | What it captures | When used |
|----|----|----|
| CST / parse tree | Every grammar rule, all tokens | Parser internals |
| **AST** | Logical structure only | Compilation, analysis |
| HIR (High-level IR) | After name resolution + desugaring | Rust, Swift, GHC |
| SSA / three-address | Control flow made explicit | Optimisation passes |
| Bytecode | Stack machine instructions | Python `.pyc`, JVM `.class` |

The AST sits at the sweet spot — high enough to reason about semantics, low enough to still map clearly to source.

------------------------------------------------------------------------

## Practical tips

- **Use existing parsers.** Writing your own full parser is rarely necessary. `ast` (Python), Babel (JS), Tree-sitter (polyglot) cover most needs.
- **Source maps.** Always preserve line/column on nodes — you’ll need them for error messages and debugger stepping.
- **Immutable ASTs + transforms.** It’s safer to produce a new tree than mutate in place; most modern tools (Babel, Roslyn) follow this.
- **AST diffing.** Tools like GumTree diff ASTs to produce semantic diffs rather than line-based diffs — useful for code review and refactoring analysis.

------------------------------------------------------------------------

Back to top
