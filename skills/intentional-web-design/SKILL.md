---
name: intentional-web-design
description: Create, redesign, audit, and refine complete websites so their composition, typography, imagery, commerce patterns, responsive behavior, and interactions feel deliberately art-directed rather than generic or template-generated. Use for new multi-page sites, landing pages, frontend visual direction, premium redesigns, anti-slop reviews, generic AI-looking interfaces, inconsistent page systems, weak hierarchy, repetitive cards or split sections, excessive whitespace, and requests to make a website feel custom-made.
---

# Intentional Web Design

Create websites whose visible decisions have a reason. Use one coherent visual idea, compose around real content, and reject generic layout habits before they reach the browser.

## Operating model

Pair this judgment skill with the environment's strongest frontend implementation skill for new builds and its interface-refinement skill for existing work. Add image generation only when the project needs custom raster imagery.

When the user requests a complete site and supplies no sitemap, build Home, About, Services, and Contact. Use the requested stack when specified; otherwise prefer a self-contained implementation with shared tokens and reusable components.

Before visual decisions, read:

- [references/rejection-patterns.md](references/rejection-patterns.md)
- [references/typography-and-spacing.md](references/typography-and-spacing.md)
- [references/layout-system.md](references/layout-system.md)
- [references/imagery-and-icons.md](references/imagery-and-icons.md)
- [references/responsive-and-quality.md](references/responsive-and-quality.md)

For shops, rentals, directories, service catalogs, or other inventory-led experiences, also read [references/commerce-and-inventory.md](references/commerce-and-inventory.md).

When refining the criteria or applying accumulated user feedback, read [references/learning-registry.md](references/learning-registry.md).

## Workflow

1. Inspect the brief, existing project, visible pages, assets, content, and technical constraints.
2. Identify the audience, promise, content hierarchy, visual world, and one defining compositional idea.
3. Inventory the major section scaffolds already visible in the project.
4. Run the rejection gate before writing or revising layout code.
5. Establish shared tokens for width, spacing, typography, color, controls, imagery, and breakpoints.
6. Implement complete content, navigation, assets, interactions, responsive behavior, and accessible states.
7. Vary composition when the content changes while preserving the shared system.
8. Run the anti-generic review and rendered QA before completion.

## Mandatory rejection gate

For every proposed major section, state its purpose, composition, typography role, imagery role, and action. Compare it with the rejection references and the broad entries in the learning registry.

Delete or materially recompose a candidate when it matches a known rejected pattern. Renaming a kicker, changing a split ratio, reducing the headline, replacing rules with floating labels, or changing colors does not make the scaffold new.

Do not repeat an existing project scaffold unless recognition or function requires it. Direct user feedback recorded in the registry overrides a proposed composition.

## Intentional-design rules

- Give every layout choice a content, interaction, or brand rationale.
- Prefer one strong visual idea over a collection of fashionable effects.
- Keep supporting text readable and headline contrast controlled.
- Align pages and components to a coherent width and spacing system.
- Use relevant, varied, correctly cropped imagery that adds meaning.
- Keep peer components stable and internally consistent.
- Let responsive layouts recompose rather than merely shrink.
- Preserve restraint. Intentional does not mean visually busy.
- Treat diagnostic warnings as prompts for justification, not universal bans.

## Anti-generic review

For every major section, ask:

1. Why is this composition right for this content?
2. Could it belong unchanged to an unrelated generated website?
3. Is the supporting text comfortably readable?
4. Are whitespace and height doing compositional work?
5. Does imagery add story, atmosphere, identity, or information?
6. Are repeated elements aligned and consistently sized?
7. Does the page belong to the same system without feeling cloned?
8. Does the responsive composition preserve hierarchy and intent?

Revise any section that lacks a concrete answer.

## Completion contract

Do not call the work complete until:

- Every requested page exists and is reachable through shared navigation.
- Content is specific and contains no placeholders or invented business claims.
- Major sections have defensible content or brand rationale.
- Shared components, controls, widths, and interaction states are consistent.
- Images load, crops are intentional, and major imagery is not needlessly repeated.
- Desktop and mobile have been visually inspected on every page.
- Important navigation, forms, filters, menus, and primary actions work.
- There is no unintended horizontal overflow, clipping, broken JavaScript, or browser error.
- The most useful finished page is left open for review when browser tooling is available.

## Updating the criteria

Update the learning registry only from explicit feedback observed during real work. Record the rejected or approved pattern, its context, the underlying principle, its scope, and the rule for future application.

Use `project-specific` for one implementation, `provisional` for a likely preference needing more evidence, and `broad` only after repeated confirmation or an explicit universal instruction. Preserve conflicting lessons with their conditions instead of silently deleting one.

When a lesson becomes broad, promote its concise rule into the appropriate reference file while retaining the evidence entry in the registry. Validate the skill after structural changes.
