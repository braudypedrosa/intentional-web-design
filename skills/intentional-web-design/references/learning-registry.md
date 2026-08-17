# Learning registry

This registry stores explicit feedback from real website work. Apply `broad` lessons by default. Treat `provisional` and `project-specific` lessons as contextual evidence.

## Broad lessons

### Decorative promotion strips create noise

- **Evidence:** A moving bakery announcement strip was explicitly rejected as AI-generated visual noise.
- **Principle:** Repeating promotional messages do not help users understand or choose.
- **Apply:** Reject marquees and ticker strips. Put essential fulfillment information near the relevant action.

### Split introductions are not automatically editorial

- **Evidence:** Headline-left and copy-right introductions were repeatedly rejected across different industries.
- **Principle:** Two columns need a functional or narrative relationship, not merely separate text roles.
- **Apply:** Integrate the title into the content surface, use a stacked or centered hierarchy when appropriate, or create a real dependency between columns.

### Standard heading sizes preserve hierarchy

- **Evidence:** Oversized non-hero headings were repeatedly rejected; giant type was reserved for homepage heroes and major CTAs.
- **Principle:** When every section uses display type, hierarchy collapses.
- **Apply:** Start from the ranges in the typography reference and validate real content at representative widths.

### Peer content needs equal stable geometry

- **Evidence:** Unequal grids, staggered peers, width-changing hover states, and uneven card padding were rejected.
- **Principle:** Comparable items should remain comparable.
- **Apply:** Use stable columns, consistent insets, and interactions that do not change sibling hierarchy.

### Images must be specific and varied

- **Evidence:** Repeated portraits, placeholder avatars, and text-heavy major sections required distinct imagery.
- **Principle:** Imagery should carry story or information, not fill rectangles.
- **Apply:** Art-direct major images independently and avoid needless reuse.

### Footers need a clear closing job

- **Evidence:** Sparse multi-column footers with empty fields and detached contact information were rejected.
- **Principle:** A footer should close the journey with useful orientation or action.
- **Apply:** Group identity, description, and contact; preserve navigation and social access; avoid unsupported promotions.

### Do not invent business urgency

- **Evidence:** An unsupported vacation-rental availability window was rejected.
- **Principle:** Availability, scarcity, dates, and urgency are business data, not decorative copy.
- **Apply:** Use verified data or omit the claim.

### Learning must change the next decision

- **Evidence:** Previously rejected patterns returned in cosmetic variations.
- **Principle:** A registry is ineffective if consulted only after implementation.
- **Apply:** Run the rejection gate before coding and reject structural variants of known failures.

### Cosmetic variation does not create a new layout

- **Date:** 2026-08-17
- **Scope:** broad
- **Context:** Quiet Tide and Strandline vacation-rental homepages at desktop and mobile widths.
- **Feedback:** Strandline was rejected as too similar because both sites used an overlay header, full-bleed scenic hero, lower-left white serif headline, and bottom booking rail despite different branding and photography.
- **Principle:** A new visual skin does not create a new composition when the page retains the same dominant geometry and interaction placement.
- **Apply:** Compare the six-part composition fingerprint before coding. Reject directions matching four or more traits from recent same-industry work and rotate section archetypes through the layout catalog.

### Listing captions need one reading axis

- **Date:** 2026-08-17
- **Scope:** broad
- **Context:** Strandline v1 three-property inventory grid at a wide desktop viewport.
- **Feedback:** The `Sea Oats No. 7` title was explicitly rejected when it sat on the far right while its location, metadata, and price remained on the left, with the universal direction to never use that arrangement.
- **Principle:** A listing caption is one information unit. Splitting its title and supporting facts across opposing edges breaks association and creates an unstable scan path.
- **Apply:** Left-align the title, location, metadata, and price to the same reading axis. Place a secondary action on the opposite edge only when it occupies a separate, clearly structured action row.

### Hero and body containers must share one width system

- **Date:** 2026-08-17
- **Scope:** broad
- **Context:** Universal website layout and responsive alignment criteria.
- **Feedback:** The hero width container must match the body width container, with a uniform page-width system.
- **Principle:** A separate hero container creates drifting alignment lines and makes the first viewport feel detached from the rest of the page.
- **Apply:** Use the same canonical maximum width and horizontal gutters for hero and body content at every breakpoint. Full-bleed hero media may extend outward, but meaningful hero content must align to the shared container.

### Vacation-rental palettes should support rest

- **Date:** 2026-08-17
- **Scope:** provisional
- **Context:** Strandline v2 homepage and property page using large coral, mustard, and turquoise surfaces.
- **Feedback:** The layout was approved, but the design was rejected as too vibrant for a vacation rental.
- **Principle:** Vacation-rental browsing should make the stay feel calm and inhabitable; several large saturated color fields create campaign energy instead of a restorative sense of place.
- **Apply:** For vacation rentals, begin with low-chroma sand, shell, weathered wood, sea-glass, or coastal ink. Reserve one muted accent for actions and state unless the established brand explicitly requires a brighter world.

### A full redesign is not another cosmetic pass

- **Date:** 2026-08-17
- **Scope:** project-specific
- **Context:** Strandline vacation-rental concept after a palette-only calming revision of v2.
- **Feedback:** After the palette was subdued, the user requested a full redesign.
- **Principle:** Once the underlying art direction is rejected, additional palette or ornament changes preserve the wrong design thesis.
- **Apply:** For Strandline, retain verified functionality and content but replace the typography, composition, section archetypes, interaction framing, and page rhythm when a full redesign is requested.

### Eyebrow spacing is a shared component rule

- **Date:** 2026-08-17
- **Scope:** broad
- **Context:** Strandline homepage hero and section introductions at wide desktop width.
- **Feedback:** When the same subheader or eyebrow style is reused, every instance must keep the same spacing to its associated heading.
- **Principle:** Repeated typographic roles are components. Inconsistent vertical spacing makes a shared pattern look accidental and weakens page rhythm.
- **Apply:** Use one eyebrow-to-heading spacing token across equivalent usages. Keep the pair in one flow container and prevent parent grid gaps from adding accidental vertical space.

### Heading and paragraph do not justify a split intro

- **Date:** 2026-08-17
- **Scope:** broad
- **Context:** Strandline homepage hero and property-collection introduction at wide desktop width.
- **Feedback:** The familiar two-column arrangement with a large heading on one side and a supporting paragraph on the other was explicitly identified as AI-slop and must be avoided.
- **Principle:** Separating two text roles into columns does not create meaningful composition. The layout needs a functional relationship beyond visual counterweight.
- **Apply:** Default section introductions to a coherent single reading flow, or use another archetype with a real comparison, sequence, interaction, or media dependency. Do not recreate the split through cosmetic changes to ratio, alignment, or copy length.

### Display headlines need a bounded role

- **Date:** 2026-08-17
- **Scope:** broad
- **Context:** Strandline homepage hero at wide desktop width.
- **Feedback:** The hero headline was too large and needed to resolve in two lines.
- **Principle:** Display type should establish hierarchy without turning ordinary marketing copy into a poster composition.
- **Apply:** Use the baseline `.h1--lg` scale only for a primary hero or singular campaign statement, and keep it to one or two desktop lines in its intended container. Step down to the standard H1 scale or revise the measure or copy when it wraps further.

## Adding a lesson

Append entries using this format:

```markdown
### Concise lesson title

- **Date:** YYYY-MM-DD
- **Scope:** project-specific | provisional | broad
- **Context:** Page, component, industry, and viewport when relevant.
- **Feedback:** The explicit approval or rejection.
- **Principle:** The reusable underlying reason.
- **Apply:** The future decision rule and its conditions.
```

Promote a lesson to a core reference only after repeated confirmation or an explicit universal instruction. Preserve the evidence entry here after promotion.
