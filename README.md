# Intentional Web Design

`intentional-web-design` is an Agent Skill for creating and refining brand systems and websites that feel deliberately composed rather than assembled from generic AI or template patterns. It works with Codex and Claude Code.

It provides:

- a mandatory pre-code rejection gate;
- task-specific routing for creation, redesign, refinement, audits, layout planning, branding, and skill improvement;
- practical criteria for composition, typography, spacing, imagery, icons, inventory, responsive behavior, and rendered QA;
- a section-level layout archetype library with industry-specific usage history to prevent structural repetition;
- a learning registry that converts explicit project feedback into reusable design judgment;
- a brand-identity workflow for strategy, logo systems, exact brand boards, and full production asset packages;
- deterministic structural validation for internal links, reference discovery, archetype IDs, and layout-history integrity;
- a completion contract covering multi-page consistency, interactions, accessibility, and browser verification.

## Installation

Clone the repository first:

```bash
git clone https://github.com/braudypedrosa/intentional-web-design.git
cd intentional-web-design
```

### Codex

Copy `skills/intentional-web-design` into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/intentional-web-design ~/.codex/skills/intentional-web-design
```

Then invoke it in a prompt:

```text
Use $intentional-web-design create to build a vacation-rental website.
```

or:

```text
Use $intentional-web-design audit to review this interface for generic AI design patterns.
```

For a complete identity package:

```text
Use $intentional-web-design brand to create the brand direction, final brand board, logo system, and full production brand assets for my product.
```

Subcommands are optional. The skill can infer a primary route from natural-language requests, but an explicit route makes the intended action boundary clear.

## Task routes

| Route | Purpose |
|---|---|
| `create` | Build a new site, landing page, or visual system. |
| `redesign` | Replace the structural and visual direction of an existing interface. |
| `refine` | Improve a focused part of an existing design while preserving its direction. |
| `audit` | Produce a read-only design and technical UI assessment. |
| `layout` | Plan section architecture, alternatives, and structural rotation. |
| `brand` | Create brand strategy, identity, logo, board, and production assets. |
| `improve` | Extend or reorganize the skill's own criteria and capabilities. |

All routes share the same intentional-design rules and completion contract. Each route loads only the references relevant to its job, reducing unrelated context while preserving one source of truth.

### Claude Code

To make the skill available in every project, copy it to your personal Claude Code skills directory:

```bash
mkdir -p ~/.claude/skills
cp -R skills/intentional-web-design ~/.claude/skills/intentional-web-design
```

For a project-scoped installation, run this from the target project's root instead:

```bash
mkdir -p .claude/skills
cp -R /path/to/intentional-web-design/skills/intentional-web-design \
  .claude/skills/intentional-web-design
```

Claude Code can load the skill automatically when a request matches its description. You can also invoke it directly:

```text
/intentional-web-design create a vacation-rental website.
```

If the skills directory was created after Claude Code started and the skill does not appear immediately, restart Claude Code once.

## Package structure

```text
skills/intentional-web-design/
├── SKILL.md
├── agents/openai.yaml
├── references/
    ├── rejection-patterns.md
    ├── typography-and-spacing.md
    ├── layout-system.md
    ├── imagery-and-icons.md
    ├── brand-identity-and-assets.md
    ├── commerce-and-inventory.md
    ├── interface-audit.md
    ├── layout-archetypes.md
    ├── layout-usage-registry.md
    ├── layout-history-vacation-rentals.md
    ├── responsive-and-quality.md
    ├── learning-registry.md
    └── skill-evolution.md
└── scripts/
    └── validate_skill_structure.py
```

The core workflow stays concise. Detailed criteria are loaded progressively by task route. Layout usage is indexed separately from industry history so new industries do not force unrelated project evidence into every design decision.

## Layout rotation

The layout catalog groups independent archetypes for headers, heroes, inventory, stories, guides, detail pages, trust, calls to action, booking, and footers. The skill mixes these section by section rather than reusing fixed page templates.

For same-industry work, it compares six composition traits: header mode, hero image mode, text anchor, inventory rhythm, CTA geometry, and footer density. A proposal matching four or more recent traits requires a functional justification or a different direction. Color, typeface, copy, crop, and ornament changes do not count as layout rotation.

## Baseline typography and layout standards

The skill includes a production-ready fluid type scale in [`typography-and-spacing.md`](skills/intentional-web-design/references/typography-and-spacing.md) and a companion spacing, container, grid, and component system in [`layout-system.md`](skills/intentional-web-design/references/layout-system.md). Together they cover the 375px-to-1440px range, semantic heading roles, readable body copy, canonical page widths, section rhythm, grid gaps, fields, cards, and buttons.

Use `.h1--lg` only for the primary hero or a singular campaign statement, and keep it to one or two lines at desktop widths. Equivalent eyebrows or subheaders use one shared `--space-xs` gap to their heading. The rejection criteria prohibit the default two-column introduction that places a large heading in one column and supporting copy in the other without a functional relationship.

## Strict audit gates

Every build must pass the bad-design audit in [`rejection-patterns.md`](skills/intentional-web-design/references/rejection-patterns.md) at desktop and mobile. Visible text has an absolute computed minimum of 14px. Repeated bordered groups use internal separators without an unnecessary rule above the first item or below the last. Horizontal copy-and-action rows keep the action width-bounded, right aligned, and top aligned.

An unresolved audit failure keeps the design in revision; changing color, typeface, or decoration does not convert a failed structure into an approved design.

## Evolving the criteria

Add explicit real-world feedback to `references/learning-registry.md` with its context, principle, scope, and future application rule. Promote a lesson into a core reference only after repeated confirmation or a clear universal instruction.

Each operational rule has one canonical owner. Industry layout histories are stored separately, large evidence registries can be sharded, and new routes remain thin entry points into shared standards. This keeps the skill opinionated without turning one implementation preference into an unconditional law or duplicating rules across commands.

Validate the installed or repository skill after structural changes:

```bash
python skills/intentional-web-design/scripts/validate_skill_structure.py
```

The validator rejects broken Markdown links, references that are not directly discoverable from `SKILL.md`, duplicate archetype definitions, unindexed history files, and unknown archetype IDs in recorded layouts.

## License

MIT
