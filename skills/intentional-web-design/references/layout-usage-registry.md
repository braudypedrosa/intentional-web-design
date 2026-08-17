# Layout usage registry

Track rendered layout use so future projects rotate structure instead of repeating recent scaffolds. Record implemented layouts only; proposals do not count.

## Selection procedure

1. Classify each major section by catalog category.
2. Shortlist archetypes that fit the content, inventory size, interaction, and responsive needs.
3. Exclude archetypes used in the last five relevant projects for that section type when a suitable alternative exists.
4. Compare the page fingerprint against recent same-industry work: header mode, hero image mode, text anchor, inventory rhythm, CTA geometry, and footer density.
5. Reject a proposal when four or more fingerprint traits match a recent project unless the repeated structure is functionally required.
6. Choose the least-recently-used suitable archetype. Never rotate into a worse functional choice merely to be different.
7. After rendered desktop and mobile verification, append the implemented IDs and fingerprint below.
8. If a new successful scaffold is absent from the catalog, add it to `layout-archetypes.md` before recording it here.

## Entry format

```markdown
### YYYY-MM-DD — Project or site — page/template

- Industry:
- Implemented: H00, HE00, I00, S00, G00, D00, T00, C00, F00
- Fingerprint: header mode | hero image mode | text anchor | inventory rhythm | CTA geometry | footer density
- Status: approved, implemented, revised, or rejected
- Notes:
```

## Recorded use

### 2026-08-17 — Quiet Tide — homepage

- Industry: vacation rentals
- Implemented: H01, HE01, I10, C02, F02
- Fingerprint: overlay header | full-bleed scenic hero | lower-left white serif | immersive property chapters | rectangular booking rail | compact dark action footer
- Status: implemented
- Notes: Establishes a recent same-industry scaffold that should not be repeated automatically.

### 2026-08-17 — Strandline v1 — homepage

- Industry: vacation rentals
- Implemented: H01, HE01, I01, G01, C01, F02
- Fingerprint: overlay header | full-bleed scenic hero | lower-left white serif | three-item image grid | four-part booking rail | dark three-group footer
- Status: rejected
- Notes: User identified the design as too similar to Quiet Tide. Palette, photography, and copy did not materially change the shared header, hero, headline anchor, or booking-rail scaffold.

### 2026-08-17 — Strandline v1 — property page

- Industry: vacation rentals
- Implemented: H02, D01, T02, C04, F02
- Fingerprint: solid header | mosaic gallery | title below gallery | linear content with sticky side booking | card-like booking action | dark three-group footer
- Status: revised
- Notes: Functional widget coverage was retained, but the redesign should reorganize the gallery, facts, and booking geometry.

### 2026-08-17 — Strandline v2 — homepage

- Industry: vacation rentals
- Implemented: H04, HE03, I04, G03, S05, C03, F03
- Fingerprint: solid atlas header | framed poster window | oversized left sans poster | interactive index-to-image explorer | perforated booking ticket | oversized wordmark floor
- Status: implemented
- Notes: Verified at desktop, tablet, and mobile widths. Structurally replaces the overlay header, full-bleed scenic hero, lower-left white serif, three-card grid, and bottom hero booking rail shared by Quiet Tide and Strandline v1.

### 2026-08-17 — Strandline v2 — property page

- Industry: vacation rentals
- Implemented: H04, D02, D08, T02, C04, F03
- Fingerprint: solid atlas header | horizontal photo reel | title before media | compact facts rail with editorial sections | full-width booking dock | oversized wordmark floor
- Status: implemented
- Notes: Verified gallery, save/share controls, booking calculation, expandable amenities, contact dialog, image loading, console state, and responsive recomposition.

### 2026-08-17 — Strandline v3 — homepage

- Industry: vacation rentals
- Implemented: H05, HE04, I02, G05, S01, C05, F05
- Fingerprint: centered solid masthead | contained three-image ribbon | headline-first quiet editorial | featured stay plus secondary pair | calm planner canvas | compact local-desk footer
- Status: implemented
- Notes: Full art-direction redesign after v2 was rejected. Verified uniform hero/body container, navigation, neighborhood lenses, planner behavior, image loading, console state, and desktop, tablet, and mobile recomposition. Later approved refinements applied the baseline type scale, constrained the hero to two lines, standardized eyebrow spacing, and replaced the non-functional split collection introduction with one reading flow.

### 2026-08-17 — Strandline v3 — property page

- Industry: vacation rentals
- Implemented: H05, D05, D06, D08, T02, C05, F05
- Fingerprint: centered solid masthead | planner-first introduction | selected gallery with thumbnail rail | compact fact rail and editorial body | review ledger | compact local-desk footer
- Status: implemented
- Notes: Verified selected-gallery state, lightbox, save/share controls, booking calculation, amenity disclosure, availability, image loading, console state, and responsive behavior.
