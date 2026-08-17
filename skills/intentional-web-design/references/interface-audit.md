# Interface audit

Use this audit for existing sites and apps before proposing changes. Intentional Web Design owns these criteria; do not depend on another design or redesign skill to supply them.

## Typography

- Replace anonymous default typography when it weakens identity; choose type for the brand and content, not trend compliance.
- Keep display scale reserved for real focal moments. Use balanced wrapping, controlled tracking, and readable line lengths.
- Establish semantic roles for display, H1–H3, lead, body, labels, metadata, and numeric data.
- Avoid all-caps labels as an automatic hierarchy device. Prefer sentence case or real functional labels.
- Check real longest labels, orphans, wrapping, and clipping at intermediate widths.

## Color, surface, and depth

- Use one coherent neutral temperature and a restrained accent system.
- Reject familiar purple-blue AI gradients, generic black shadows, and abrupt unrelated dark sections.
- Use surface contrast, texture, imagery, and tinted shadows only when they strengthen material or hierarchy.
- Keep lighting direction, border strength, radius, and elevation consistent with the visual world.
- Do not add glass, grain, gradients, or shadows as automatic signals of premium quality.

## Layout and composition

- Identify the dominant scaffold of every section before judging its styling.
- Reject automatic centered symmetry, three-equal-card feature rows, mechanical image-copy alternation, and arbitrary bento grids.
- Use max-widths, shared alignment lines, stable comparison geometry, and optically balanced spacing.
- Confirm that hero content and body content use the same canonical maximum width and horizontal gutters at every breakpoint. Treat full-bleed media as an outer layer, not a second content container.
- Introduce asymmetry, overlap, sticky context, horizontal movement, or broken grids only when content or interaction benefits.
- Avoid multiple competing sticky regions and viewport-height sections that ignore persistent header or mobile browser chrome.
- Check the six-part composition fingerprint against recent same-industry work before coding.

## Components and patterns

- Use a card only when containment, comparison, selection, or elevation communicates meaning.
- Replace generic feature cards, three-tower pricing, testimonial carousels with dots, and link-farm footers with content-specific structures.
- Keep peer controls, images, facts, prices, and actions internally aligned.
- Do not use pills, badges, avatars, icons, or floating panels as decoration.
- Prefer inline disclosure or a contextual tray over a modal when the action does not require interruption.

## Interaction and state

- Provide visible hover, focus, active, disabled, loading, empty, success, and error states where the interface can reach them.
- Keep motion on transform and opacity where possible; remove motion that shifts essential labels or comparison geometry.
- Ensure keyboard access, focus return for dialogs, Escape handling, and approximately 44 × 44 CSS-pixel touch targets.
- Make navigation state and current selection visible without relying on color alone.
- Reject dead links, fake controls, and interactions that exist only for visual novelty.

## Content and trust

- Replace placeholder language, generic names, invented urgency, and unsupported claims with specific draft content or clearly labeled concept data.
- Place availability, policies, fees, fulfillment, safety, and cancellation information next to the action they affect.
- Keep headings useful when scanned without body copy.
- Use real attribution and distinguish verified facts, illustrative examples, and unverified claims.

## Imagery and iconography

- Assign each image a role and an intentional crop; do not reuse one scene as universal filler.
- Audit subject position and text contrast at every supported breakpoint.
- Use one coherent icon family or a deliberately authored custom set. Avoid default icon-library clichés when they erase identity.
- Require descriptive alt text for meaningful imagery and empty alt text only for genuinely decorative media.

## Responsive behavior

- Recompose instead of merely shrinking. Preserve hierarchy, reading order, primary action, and useful context.
- Test mobile, tablet, laptop, and wide desktop plus widths immediately around fragile breakpoints.
- Verify navigation, filters, forms, dialogs, carousels, booking controls, sticky elements, and comparison layouts at their responsive states.
- Check document scroll width, clipped text, image dimensions, touch targets, and footer density.

## Code and completion

- Preserve the existing stack unless the user requests a migration.
- Use semantic landmarks, shared tokens, reusable components, and real imports that exist in the project.
- Include title, description, social metadata when applicable, skip navigation, back paths, form validation, legal paths, and a useful not-found state for complete sites.
- Run syntax, lint, build, and targeted interaction checks supported by the project.
- Inspect every unique template at desktop and mobile, check the console, and leave the most useful finished page open for review.

## Audit output

Before implementation, summarize:

1. Structural repetitions and rejected scaffolds.
2. Typography and hierarchy weaknesses.
3. Surface, imagery, and identity weaknesses.
4. Missing interaction, responsive, accessibility, and trust states.
5. Proposed archetype IDs and their six-part composition fingerprint.
