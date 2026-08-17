---
name: intentional-web-design
description: Create, redesign, audit, and refine complete websites and their brand systems so their identity, composition, typography, imagery, commerce patterns, responsive behavior, and interactions feel deliberately art-directed rather than generic or template-generated. Use for brand strategy, logo systems, brand boards, full production brand assets, new multi-page sites, landing pages, frontend visual direction, premium redesigns, anti-slop reviews, generic AI-looking interfaces, inconsistent page systems, weak hierarchy, repetitive cards or split sections, excessive whitespace, and requests to make a website or identity feel custom-made.
---

# Intentional Web Design

Create websites whose visible decisions have a reason. Use one coherent visual idea, compose around real content, and reject generic layout habits before they reach the browser.

## Operating model

Own the brand, audit, layout-selection, rotation, rejection, responsive, and quality judgment inside this skill. Do not depend on another design or redesign skill for those criteria. Pair with the environment's strongest frontend implementation capability only when it helps execute code or operate the target stack. Add image generation when the project needs custom raster imagery, identity concept exploration, or art-directed mockups. Never treat an image-generated logo as a production master.

When the user requests a complete site and supplies no sitemap, build Home, About, Services, and Contact. Use the requested stack when specified; otherwise prefer a self-contained implementation with shared tokens and reusable components.

Before visual decisions, read:

- [references/rejection-patterns.md](references/rejection-patterns.md)
- [references/typography-and-spacing.md](references/typography-and-spacing.md)
- [references/layout-system.md](references/layout-system.md)
- [references/imagery-and-icons.md](references/imagery-and-icons.md)
- [references/responsive-and-quality.md](references/responsive-and-quality.md)

For shops, rentals, directories, service catalogs, or other inventory-led experiences, also read [references/commerce-and-inventory.md](references/commerce-and-inventory.md).

When refining the criteria or applying accumulated user feedback, read [references/learning-registry.md](references/learning-registry.md).

For audits or redesigns of existing sites and apps, read [references/interface-audit.md](references/interface-audit.md). It contains the skill's self-owned typography, surface, layout, component, interaction, responsive, trust, and code-quality criteria.

For complete sites, structural redesigns, or any request for layout variety, read [references/layout-archetypes.md](references/layout-archetypes.md) and [references/layout-usage-registry.md](references/layout-usage-registry.md) before proposing sections. Use the catalog by section type and the registry to avoid recent structural repetition.

When the request includes brand strategy, a logo, a brand board, identity direction, or a complete brand package, read [references/brand-identity-and-assets.md](references/brand-identity-and-assets.md) before creating brand visuals or files. Use its production contract even when branding is only one phase of a larger website build.

## Workflow

1. Inspect the brief, existing project, visible pages, assets, content, and technical constraints.
2. Identify the audience, promise, content hierarchy, visual world, and one defining brand and compositional idea.
3. Inventory the major section scaffolds already visible in the project.
4. Select section archetypes through the layout-rotation procedure and record the proposed composition fingerprint.
5. Run the rejection gate before writing or revising layout code.
6. Establish shared tokens for width, spacing, typography, color, controls, imagery, and breakpoints.
7. Implement complete content, navigation, assets, interactions, responsive behavior, and accessible states.
8. Vary composition when the content changes while preserving the shared system.
9. Run the anti-generic review and rendered QA before completion.
10. Record implemented archetype IDs in the layout usage registry only after rendered desktop and mobile verification.

When branding is in scope, establish or verify the identity before finalizing website tokens. Generate the final brand board from the same canonical logo, colors, fonts, and graphics included in the production asset package. Keep a stable `branding/` directory and update it in place across revisions.

## Mandatory rejection gate

For every proposed major section, state its purpose, composition, typography role, imagery role, and action. Compare it with the rejection references and the broad entries in the learning registry.

Delete or materially recompose a candidate when it matches a known rejected pattern. Renaming a kicker, changing a split ratio, reducing the headline, replacing rules with floating labels, or changing colors does not make the scaffold new.

Do not repeat an existing project scaffold unless recognition or function requires it. Direct user feedback recorded in the registry overrides a proposed composition.

## Layout rotation

Treat layout variety as a section-level system, not a set of complete templates.

1. Classify each section as header, hero, inventory, story or proof, guide or location, detail, trust, CTA or booking, or footer.
2. Shortlist functionally suitable archetypes from the catalog.
3. Exclude recently used same-type archetypes when a suitable alternative exists.
4. Compare header mode, hero image mode, text anchor, inventory rhythm, CTA geometry, and footer density with recent same-industry work.
5. Reject the page direction when four or more fingerprint traits match a recent project without a functional reason.
6. Choose the least-recently-used suitable option, then adapt it to the content and visual world. Never use recency to justify a worse interaction.
7. Mix archetypes independently rather than reusing fixed page bundles.

Changing palette, typeface, copy, crop, split ratio, or ornamentation does not count as layout rotation. When a newly implemented scaffold is genuinely distinct and passes rendered QA, add it to the catalog and record its first use.

## Intentional-design rules

- Give every layout choice a content, interaction, or brand rationale.
- Prefer one strong visual idea over a collection of fashionable effects.
- Keep supporting text readable and headline contrast controlled.
- Align pages and components to a coherent width and spacing system.
- Use one canonical page container for the hero and body. Match their content width and horizontal gutters; full-bleed hero media may extend beyond the container, but hero content may not introduce a separate width system.
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

When branding is requested, also require the brand-board and asset completion checks in [references/brand-identity-and-assets.md](references/brand-identity-and-assets.md). A concept board alone is not a full brand package.

## Updating the criteria

Update the learning registry only from explicit feedback observed during real work. Record the rejected or approved pattern, its context, the underlying principle, its scope, and the rule for future application.

Use `project-specific` for one implementation, `provisional` for a likely preference needing more evidence, and `broad` only after repeated confirmation or an explicit universal instruction. Preserve conflicting lessons with their conditions instead of silently deleting one.

When a lesson becomes broad, promote its concise rule into the appropriate reference file while retaining the evidence entry in the registry. Validate the skill after structural changes.

## Publishing approved improvements

Treat an improvement as approved when the user explicitly asks to add it to the skill, make it a standard, promote it, or publish it. Feedback about one rendered implementation is evidence, not permission to alter the canonical skill, unless the user also requests the skill change.

After approval, complete this workflow in order:

1. Update the canonical source repository and the relevant progressive references. Keep unrelated or unapproved working-tree changes out of the scope.
2. Run `git diff --check` and validate the repository skill with the Skill Creator `quick_validate.py` script.
3. Review the exact staged diff, then create a focused professional commit describing the approved behavior change.
4. Push the current branch to its configured remote and verify that the remote branch SHA matches local `HEAD`. Do not report publication from a local commit alone.
5. Only after remote verification, synchronize the committed skill directory into the configured local installation, including the global Codex skill and any already-configured platform copies.
6. Validate the installed copy and compare it with the committed repository tree. Report the commit, branch, push status, and synchronization result.

If older local improvements remain and explicit approval cannot be established, preserve them without committing or overwriting them and ask the user for approval. Never bundle uncertain changes into an approved commit.
