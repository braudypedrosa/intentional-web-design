# Intentional Web Design

`intentional-web-design` is an Agent Skill for creating and refining websites that feel deliberately composed rather than assembled from generic AI or template patterns. It works with Codex and Claude Code.

It provides:

- a mandatory pre-code rejection gate;
- practical criteria for composition, typography, spacing, imagery, icons, inventory, responsive behavior, and rendered QA;
- a learning registry that converts explicit project feedback into reusable design judgment;
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
Use $intentional-web-design to create a vacation-rental website.
```

or:

```text
Use $intentional-web-design to audit this interface for generic AI design patterns and refine it.
```

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
/intentional-web-design Create a vacation-rental website.
```

If the skills directory was created after Claude Code started and the skill does not appear immediately, restart Claude Code once.

## Package structure

```text
skills/intentional-web-design/
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
