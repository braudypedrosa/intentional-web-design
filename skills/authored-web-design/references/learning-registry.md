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
