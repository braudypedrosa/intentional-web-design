# Layout system

Use this baseline for spacing, containers, section rhythm, grids, and common component internals. Preserve the tokens unless the project already has an equivalent coherent system.

```css
:root {
  --space-3xs: 0.25rem;  /*   4 */
  --space-2xs: 0.5rem;   /*   8 */
  --space-xs:  0.75rem;  /*  12 */
  --space-sm:  1rem;     /*  16 */
  --space-md:  1.5rem;   /*  24 */
  --space-lg:  2rem;     /*  32 */
  --space-xl:  3rem;     /*  48 */
  --space-2xl: 4rem;     /*  64 */
  --space-3xl: 6rem;     /*  96 */
  --space-4xl: 8rem;     /* 128 */
  --space-5xl: 10rem;    /* 160 */

  /* containers */
  --width-prose: 68ch;    /* long-form text */
  --width-narrow: 40rem;  /* 640  - forms, checkout */
  --width-default: 75rem; /* 1200 - most pages */
  --width-wide: 90rem;    /* 1440 - dashboards, galleries */

  /* fluid: 375px -> 1440px viewport */
  --gutter: clamp(1rem, 0.6rem + 1.7vw, 2.5rem);       /* 16 -> 40 */
  --section-space: clamp(4rem, 2.3rem + 7.2vw, 8rem);  /* 64 -> 128 */
  --gap-grid: clamp(1rem, 0.7rem + 1.3vw, 1.5rem);     /* 16 -> 24 */
}

/* container + section rhythm */
.container {
  width: 100%;
  max-width: var(--width-default);
  margin-inline: auto;
  padding-inline: var(--gutter);
}
.section { padding-block: var(--section-space); }

/* columns */
.grid {
  display: grid;
  gap: var(--gap-grid);
  grid-template-columns: repeat(12, minmax(0, 1fr));
}
.cards {
  display: grid;
  gap: var(--gap-grid);
  grid-template-columns: repeat(auto-fit, minmax(17.5rem, 1fr));
}

/* vertical rhythm - space above a heading, not below */
h2 + *, h3 + *, h4 + * { margin-top: 0; }
h2 { margin-block: var(--space-xl) var(--space-sm); }
h3 { margin-block: var(--space-lg) var(--space-xs); }
h4, h5, h6 { margin-block: var(--space-md) var(--space-2xs); }
p, ul, ol, figure, table { margin-block: 0 var(--space-md); }
:is(h1, h2, h3, h4, h5, h6):first-child { margin-top: 0; }

/* component internals */
.card { padding: var(--space-md); border-radius: 12px; }
.card--lg { padding: var(--space-lg); }
.field-stack { display: grid; gap: var(--space-md); }
.field { display: grid; gap: var(--space-2xs); } /* label -> input */
.btn-row { display: flex; gap: var(--space-xs); flex-wrap: wrap; }
.btn { padding: var(--space-xs) var(--space-md); min-height: 2.75rem; }
```

## Usage contract

- Use `--width-default` for the canonical page container. The header, hero content, body sections, and footer must share its maximum width and gutters.
- Use `--width-prose` inside the canonical container for long-form reading and `--width-narrow` for forms or checkout. Use `--width-wide` only when a gallery, dashboard, data table, or similarly dense visual surface needs it.
- Full-bleed media and backgrounds may leave the container; their meaningful content must return to the canonical alignment grid.
- Apply `.section` spacing once at each major page region. Do not stack section padding on nested wrappers or add arbitrary spacer elements to compensate for weak composition.
- Use the 12-column `.grid` only when child spans express a real hierarchy. Use `.cards` for stable peer collections, not as the default answer for unrelated content.
- Keep all component padding, field gaps, button rows, and heading rhythm on the shared tokens. Introduce a new token only when the existing scale cannot express a repeatedly verified need.
- For an eyebrow or subheader followed by a heading, use `--space-xs` as the single gap. Put the pair in one flow container and do not combine an eyebrow margin with a parent row gap.
- For a group whose items are separated by rules, draw only internal separators. Prefer `.item + .item { border-top: 1px solid; }`; the first item must not have a top border and the last item must not have a bottom border. Add an outer border only when the entire group is intentionally contained.
- For a horizontal copy-and-action row, keep the action intrinsically or explicitly width-bounded, place it at the inline end, and align it to the row's top. Do not stretch the action across its grid track or vertically center or bottom-align it against multi-line copy. Recompose deliberately on small screens while retaining a bounded action.
- Treat `12px` card radius as a baseline, not a mandate. Square or differently rounded brand systems may change the radius consistently while retaining the spacing tokens.
