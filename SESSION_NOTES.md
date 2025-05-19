# Session Notes – Scaffold Audit Tool

This markdown file captures the key details and open questions from our current
conversation so that you can easily resume work in a later session.

---

## What has been implemented

1. Git repository initialised (`main` branch, empty root commit).
2. Python package `scaffold_audit` scaffolded with (now located under
   `alta-monorepo/apps/scaffold-audit/src`):
   * CLI (`python -m scaffold_audit <drawing.dxf>`)
   * Core pipeline (parse → rule engine → annotate → report)
   * YAML-based rule loading (with placeholder rule that always passes)
   * HTML report template and stub DXF annotation
3. Dev tooling: Poetry `pyproject.toml`, unit smoke-test, code formatted & type-hinted.

## Outstanding features (next steps)

1. **Layer / block-name mapping** – need actual conventions used in your CAD
   drawings so geometry can be categorised as standards, ledgers, ties, etc.
2. Implement real geometry analysis rules:
   * Tie spacing (≤4 m vertical, ≤6 m horizontal)
   * Edge protection (guard-rails / toe-boards) for >2 m drops
   * Loading-bay bracing
   * Head-clearance under transoms (<2.0 m)
   * Baseplate level check (Δy ≤25 mm across 2 m)
3. DXF mark-ups: add `AI_AUDIT` layer, draw red cloud bubbles & numbered leaders.
4. Write detailed HTML & optional PDF report; include screenshot thumbnails.
5. Add more property-based tests (Hypothesis) and golden-file comparisons.

## Action needed from you

Please provide the **layer / block naming conventions** or share a sample DXF so the
parsing heuristics can be coded accurately.

---

When you return, share the requested information and we can continue building
the full rule set. Everything above is committed, so the repo will persist.
