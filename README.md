# Authored Web Design

`authored-web-design` is a Codex skill for creating and refining websites that feel deliberately composed rather than assembled from generic AI or template patterns.

It provides:

- a mandatory pre-code rejection gate;
- practical criteria for composition, typography, spacing, imagery, icons, inventory, responsive behavior, and rendered QA;
- a learning registry that converts explicit project feedback into reusable design judgment;
- a completion contract covering multi-page consistency, interactions, accessibility, and browser verification.

## Install

Copy `skills/authored-web-design` into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R skills/authored-web-design ~/.codex/skills/authored-web-design
```

Then invoke it in a prompt:

```text
Use $authored-web-design to create a vacation-rental website.
```

or:

```text
Use $authored-web-design to audit this interface for generic AI design patterns and refine it.
```

## Package structure

```text
skills/authored-web-design/
├── SKILL.md
├── agents/openai.yaml
└── references/
    ├── rejection-patterns.md
    ├── typography-and-spacing.md
    ├── imagery-and-icons.md
    ├── commerce-and-inventory.md
    ├── responsive-and-quality.md
    └── learning-registry.md
```

The core workflow stays concise. Detailed criteria are loaded progressively based on the task.

## Evolving the criteria

Add explicit real-world feedback to `references/learning-registry.md` with its context, principle, scope, and future application rule. Promote a lesson into a core reference only after repeated confirmation or a clear universal instruction.

This keeps the skill opinionated without turning a single implementation preference into an unconditional design law.

## License

MIT
