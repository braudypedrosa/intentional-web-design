# Layout usage registry

Use this file as the index and selection procedure for rendered layout history. Load only the industry history relevant to the current project.

## Industry histories

| Industry | History | Current projects |
|---|---|---|
| Vacation rentals and short-term stays | [layout-history-vacation-rentals.md](layout-history-vacation-rentals.md) | Quiet Tide and Strandline |

If no relevant history exists, use the archetype catalog without inventing prior use. After the first rendered desktop and mobile verification, create `layout-history-<industry>.md`, add it here, and link it directly from the task-routing section in `SKILL.md`.

## Selection procedure

1. Classify each major section by catalog category.
2. Open only the matching industry history file.
3. Shortlist archetypes that fit the content, inventory size, interaction, and responsive needs.
4. Exclude archetypes used in the last five relevant projects for that section type when a suitable alternative exists.
5. Compare the page fingerprint against recent same-industry work: header mode, hero image mode, text anchor, inventory rhythm, CTA geometry, and footer density.
6. Reject a proposal when four or more fingerprint traits match a recent project unless the repeated structure is functionally required.
7. Choose the least-recently-used suitable archetype. Never rotate into a worse functional choice merely to be different.
8. After rendered desktop and mobile verification, append the implemented IDs and fingerprint to the matching industry history.
9. If a new successful scaffold is absent from the catalog, add it to `layout-archetypes.md` before recording it.

## Entry format

```markdown
### YYYY-MM-DD — Project or site — page/template

- Industry:
- Implemented: H00, HE00, I00, S00, G00, D00, T00, C00, F00
- Fingerprint: header mode | hero image mode | text anchor | inventory rhythm | CTA geometry | footer density
- Status: approved, implemented, revised, or rejected
- Notes:
```

Record proposals nowhere. A layout enters history only after implementation and rendered verification.
