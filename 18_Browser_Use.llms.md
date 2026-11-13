# Brower Use

**What it is:** an MIT-licensed Python library that gives an LLM control of a Chromium browser — it serializes the page into indexed interactive elements, asks the model what to do next, executes the action, repeats until done. Created by Magnus Müller and Gregor Žunić; the agent takes a natural-language task, drives Chromium over CDP, processes the page, and loops LLM calls until the task completes. ~107k GitHub stars, currently the default reference implementation for “AI browser agent”.

Author

Benedict Thekkel

## Architecture

- **Transport: pure CDP.** Playwright was ripped out in 0.6.0 and as of the Aug 2025 changelog all interaction is 100% CDP-based with no Playwright dependency (they use their own `cdp-use` + `bubus` event bus). Old blog posts saying “wraps Playwright” are stale.
- **Perception:** DOM tree extracted via CDP, filtered to interactive elements, each assigned an integer index. The LLM clicks `index=14`, not a selector. Paint-order filtering (`paint_order_filtering`, default on) drops elements hidden behind others to shrink the tree.
- **Vision is optional and off-by-default-ish:** `use_vision="auto"` exposes a screenshot tool but only sends images when the model asks for one — screenshots are a fallback, not the primary channel. Cheaper and more accurate than pure pixel computer-use.
- **Action schemas are Pydantic v2**, so the loop is structured-output/tool-calling, not text parsing. `max_actions_per_step` defaults to 3 — it can batch e.g. three form fields, executing until the page changes.

------------------------------------------------------------------------

## API surface

``` python
from browser_use import Agent, Browser, Tools, ChatBrowserUse

browser = Browser(headless=False, allowed_domains=['*.example.com'])
agent = Agent(task="...", llm=ChatBrowserUse(), browser=browser, tools=tools)
history = await agent.run(max_steps=100)
```

Four objects matter: `Agent`, `Browser` (an alias for `BrowserSession`), `Tools` (alias `Controller` for backwards compat), and a `Chat*` LLM wrapper. `run()` returns `AgentHistoryList` with `urls()`, `final_result()`, `is_successful()`, `errors()`, `model_actions()`, `total_duration_seconds()`, and `structured_output` when you pass `output_model_schema`.

Default tools: `search`, `navigate`, `go_back`, `wait`, `click`, `input`, `upload_file`, `scroll`, `find_text`, `send_keys`, `evaluate` (raw JS), `switch`/`close` tabs, `extract` (LLM-based extraction), `screenshot`, `dropdown_options`/`select_dropdown`, `write_file`/`read_file`/`replace_file`, and `done`. Custom tools are a decorator:

``` python
@tools.action('Get 2FA code')
async def get_2fa(browser_session: BrowserSession) -> ActionResult: ...
```

Injected params are matched **by name** — `browser_session: BrowserSession`, not `browser: Browser`, or your tool silently fails. That’s the single most common footgun.

Params worth knowing: `page_extraction_llm` (point a cheap model at extraction), `flash_mode` (skips thinking/evaluation/next-goal for speed), `max_history_items` (context control), `sensitive_data`, `initial_actions` (deterministic prefix, no LLM), `extend_system_message`.

------------------------------------------------------------------------

## Models

They now push their own hosted gateway: `ChatBrowserUse()` is tuned for browser automation, claimed 3–5x faster than general models, and accepts provider-prefixed ids (`anthropic/claude-sonnet-4-6`, `openai/gpt-5.5`) so one `BROWSER_USE_API_KEY` reaches everything. `ChatOpenAI` / `ChatAnthropic` / `ChatGoogle` / Ollama all still work with your own keys. There’s also an open-weights preview model, `browser-use/bu-30b-a3b-preview`.

Perf claim: \#1 on the Odysseys leaderboard at 87.4% across 200 long-horizon web tasks — worth treating as vendor-reported, though the 100-task benchmark harness is open source.

------------------------------------------------------------------------

## The commercial layer

The library is genuinely free and self-hostable, but the funnel is real. `Browser(use_cloud=True)` provisions a hosted stealth browser; `@sandbox(cloud_profile_id=..., cloud_proxy_country_code='us')` runs your function next to the browser in their infra; a `profile.sh` script syncs local cookies to a cloud profile so authenticated runs work. Cloud browsers start around \$0.02/hr. CAPTCHA solving and proxy rotation are cloud-only — locally you’ll get flagged, since CDP-launched Chrome is trivially fingerprintable.

------------------------------------------------------------------------

## Where it actually earns its keep

Good: QA/exploratory testing of your own app, one-off scraping of sites you don’t want to reverse-engineer, flows behind login walls with no API, DOM layouts that churn weekly.

Bad: anything you’d run 10k times a day on a stable site. Every step is an LLM round-trip — seconds of latency and real token cost per action, and it’s non-deterministic. For a known flow, write Playwright. A reasonable pattern is browser-use to *discover* the flow, then hand-write the deterministic script.

------------------------------------------------------------------------

## Gotchas

- **Prompt injection is a first-class risk.** Page content goes into the model’s context and the agent has `evaluate` (arbitrary JS) plus file read/write. Always set `allowed_domains` and pass credentials via `sensitive_data`, never inline in the task.
- **Telemetry is on by default** — PostHog. `ANONYMIZED_TELEMETRY=false` to disable.
- **Memory:** headful Chrome per agent; parallelism gets ugly fast on one box.
- API churn is heavy — `Controller`→`Tools`, `BrowserSession`→`Browser`, Playwright→CDP all in ~a year. Pin your version and check the changelog before upgrading.
- Requires Python ≥3.11 (docs use 3.12), `uv` strongly preferred.

Alternatives worth benchmarking against: Playwright MCP (deterministic, accessibility-tree based, no agent loop of its own), Stagehand (TS, mixes deterministic and AI steps), and native computer-use APIs from Anthropic/OpenAI (pixel-level, slower, more general).

------------------------------------------------------------------------

Back to top
