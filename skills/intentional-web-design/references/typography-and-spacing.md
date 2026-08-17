# Typography and spacing

## Type hierarchy

- Reserve display-scale typography for the primary homepage hero or a genuinely major conversion moment.
- Use the baseline fluid scale below unless an established design system supplies an equivalent semantic scale.
- Keep body copy comfortably readable. Avoid huge headlines paired with tiny paragraphs, navigation, labels, or metadata.
- Define shared semantic roles for body, lead, H1, H2, H3, feature copy, and display text.
- Test the longest real label in every repeated component at intermediate widths, not only wide desktop and mobile.
- Treat text containment as a design requirement; unplanned overflow or clipping invalidates the scale.

### Baseline fluid type scale

Use this as the default implementation standard. It interpolates from a 375px viewport to a 1440px viewport while preserving conventional heading hierarchy.

```css
:root {
  /* fluid: min at 375px viewport -> max at 1440px */
  --fs-h1-lg: clamp(2.5rem, 1.97rem + 2.25vw, 4rem);       /* 40 -> 64 */
  --fs-h1: clamp(2.125rem, 1.82rem + 1.31vw, 3rem);        /* 34 -> 48 */
  --fs-h2-lg: clamp(1.875rem, 1.65rem + 0.94vw, 2.5rem);   /* 30 -> 40 */
  --fs-h2: clamp(1.625rem, 1.49rem + 0.56vw, 2rem);        /* 26 -> 32 */
  --fs-h3-lg: clamp(1.5rem, 1.41rem + 0.38vw, 1.75rem);    /* 24 -> 28 */
  --fs-h3: clamp(1.3125rem, 1.25rem + 0.28vw, 1.5rem);     /* 21 -> 24 */
  --fs-h4: clamp(1.125rem, 1.08rem + 0.19vw, 1.25rem);     /* 18 -> 20 */
  --fs-h5: clamp(1.0625rem, 1.04rem + 0.09vw, 1.125rem);   /* 17 -> 18 */
  --fs-h6: 1rem;                                           /* 16 */
  --fs-body: clamp(1.0625rem, 1.04rem + 0.09vw, 1.125rem); /* 17 -> 18 */
  --fs-small: 0.875rem;                                    /* 14 */
}

h1 { font-size: var(--fs-h1); line-height: 1.1; letter-spacing: -0.025em; }
h2 { font-size: var(--fs-h2); line-height: 1.2; letter-spacing: -0.02em; }
h3 { font-size: var(--fs-h3); line-height: 1.3; }
h4 { font-size: var(--fs-h4); line-height: 1.35; }
h5 { font-size: var(--fs-h5); line-height: 1.4; }
h6 { font-size: var(--fs-h6); line-height: 1.4; letter-spacing: 0.08em; text-transform: uppercase; }

.h1--lg { font-size: var(--fs-h1-lg); line-height: 1.05; letter-spacing: -0.03em; }
.h2--lg { font-size: var(--fs-h2-lg); line-height: 1.15; letter-spacing: -0.02em; }
.h3--lg { font-size: var(--fs-h3-lg); line-height: 1.25; letter-spacing: -0.01em; }

p, li { font-size: var(--fs-body); line-height: 1.6; }
p { max-width: 68ch; }
ul, ol { padding-left: 1.25em; }
li + li { margin-top: 0.4em; }
ul ul, ol ol, ul ol, ol ul { font-size: 1em; margin-top: 0.4em; }

a {
  font-size: inherit;
  font-weight: inherit;
  text-decoration: underline;
  text-decoration-thickness: 1px;
  text-underline-offset: 3px;
}
small, .text-small { font-size: var(--fs-small); line-height: 1.5; }
```

### Scale usage contract

- Use H1 through H6 for semantic hierarchy, not for visual convenience.
- Use `.h1--lg` only for the primary homepage hero or a singular campaign-level statement. At desktop widths, keep it to one or two lines in its intended container; if it wraps to three or more lines, use the standard H1 scale, widen the text measure within the canonical container, or revise the copy.
- Use `.h2--lg` for one major section or conversion statement at a time, not every section heading.
- Use `.h3--lg` for a featured card, property, product, or editorial title that genuinely needs more emphasis than peer H3 headings.
- Keep body content on `--fs-body`; use `--fs-small` for metadata, captions, and secondary controls rather than ordinary paragraphs.
- Treat `--fs-small` as a strict rendered floor. No visible text, including footer legal copy, labels, captions, metadata, table content, navigation, helper text, and control text, may compute below 14px at any supported viewport.
- Keep typeface selection separate from this scale. A brand may change font families and weights while preserving these semantic size, line-height, and letter-spacing roles.
- Do not introduce arbitrary pixel heading sizes between these roles without a rendered, content-specific reason.
- During rendered QA, inspect computed font sizes for every visible text-bearing element and fail the page if the minimum is below 14px. Do not rely on a token existing in `:root`; verify that component overrides obey it.

## Spacing and alignment

- Establish a shared content-width system and explicit internal alignment rules.
- Define one canonical page container for primary hero and body content. The hero container must match the body container's maximum width and horizontal gutters at every breakpoint.
- Full-bleed hero backgrounds, images, video, or color fields may extend to the viewport edge, but their inner text, controls, and meaningful content must return to the canonical page container.
- Reject hero-only max-widths or gutters that create a second alignment grid without a functional requirement explicitly approved by the user.
- Define one shared eyebrow-to-heading token and use it everywhere the same eyebrow or subheader pattern appears. Do not let a parent grid's general `gap` add a second, accidental row gap.
- Keep the eyebrow and its heading in the same flow container. Apply the spacing to the eyebrow's block-end margin or a dedicated row gap, never both.
- Use `--space-xs` from the layout system as the default eyebrow-to-heading gap, and verify the computed gap across hero and section-heading variants.
- Make whitespace perform a compositional task. Avoid viewport-height sections unless the content needs them.
- Give peer cards equal inset tokens and a consistent vertical-distribution rule.
- Measure both shortest and longest peer content to confirm stable top and bottom padding.
- Align descriptions with the headings, icons, or controls they explain.
- Use sticky contextual columns only when a shorter column genuinely orients a longer scrolling story.
