# Skill evolution

Use this reference only when changing Intentional Web Design itself. Preserve one authoritative skill while allowing task routes, criteria, histories, and deterministic checks to grow without loading unrelated material.

## Capability routing

- Add a subcommand only when it represents a recurring workflow with a distinct input, action boundary, or completion contract.
- Keep subcommands as thin routes into shared references. Do not copy the typography, layout, rejection, or QA standards into command-specific files.
- Add every new route to the task-routing table in `SKILL.md` and name the minimum required references.
- Prefer one primary route plus conditional add-ons. Do not make an agent load all routes for a mixed request.
- Preserve natural-language triggering. Users do not need to know a subcommand for the skill to work.

## Canonical ownership

Every operational rule must have one detailed owner:

| Rule family | Canonical owner |
|---|---|
| Typography, text semantics, and vertical type rhythm | `typography-and-spacing.md` |
| Containers, grids, component spacing, borders, and action alignment | `layout-system.md` |
| Structural options and compatibility | `layout-archetypes.md` |
| Rejected patterns and explicit fail conditions | `rejection-patterns.md` |
| Existing-interface evaluation procedure | `interface-audit.md` |
| Responsive behavior and rendered verification | `responsive-and-quality.md` |
| Image and icon behavior | `imagery-and-icons.md` |
| Inventory, business truth, and footer behavior | `commerce-and-inventory.md` |
| Identity and production assets | `brand-identity-and-assets.md` |
| Feedback evidence and scope classification | `learning-registry.md` |
| Layout-history indexing and selection procedure | `layout-usage-registry.md` |
| Industry-specific implemented layout evidence | `layout-history-<industry>.md` |
| Skill routing, growth, and publishing mechanics | `skill-evolution.md` and `SKILL.md` |

The completion contract may repeat a concise pass/fail invariant when it must be checked on every build. Other references should link to the owner instead of maintaining competing explanations.

## Registry sharding

### Layout history

- Keep `layout-usage-registry.md` as the index, entry schema, and selection procedure.
- Store implemented history in `layout-history-<industry>.md` files.
- Create a new industry file after the first verified entry rather than appending unrelated work to an existing history.
- Link each industry file from the registry index and directly from the task-routing section in `SKILL.md` so it remains discoverable through progressive disclosure.
- Load only the relevant industry history during layout selection. If no matching history exists, use the catalog and start a new file after verification.

### Learning evidence

- Keep active evidence in `learning-registry.md` while it remains easy to scan.
- When the file exceeds 250 lines, move older detailed entries into `learning-evidence-<year>.md` or a stable domain file, retain a concise index of active broad lessons, and link every shard directly from `SKILL.md`.
- Preserve the original evidence when promoting a rule. Do not treat a rewritten summary as the only record of explicit feedback.

## Growth thresholds

- Keep `SKILL.md` below 500 lines and focused on routing, shared workflow, invariants, and publishing.
- Give any reference over 100 lines a contents section when the headings are not already self-explanatory.
- Consider splitting a reference at 250 lines when it contains separable domains or append-only evidence.
- Create scripts when a check is deterministic, repeated, or easy to apply inconsistently by judgment alone.
- Do not add README files, changelogs, quick-reference copies, or review snapshots inside the installed skill.

## Improvement workflow

For every approved improvement:

1. Identify the primary route affected.
2. Identify the one canonical owner reference.
3. Add the feedback evidence and classify its scope when it came from rendered work.
4. Update cross-route completion checks only when the rule is universally required.
5. Update routing if a new capability or history shard was added.
6. Run `python scripts/validate_skill_structure.py` and Skill Creator validation.
7. Review for duplicated or conflicting wording before publishing.

## When to split into another skill

Keep a capability inside Intentional Web Design when it shares the same design system, rejection gate, rendered QA, and website outcome. Create a separate skill only when it has a materially different trigger, toolchain, artifact type, or operational authority and can stand alone without copying Intentional Web Design's core standards.
