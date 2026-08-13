# Responsive and quality

## Responsive composition

- Recompose layouts at meaningful breakpoints; do not merely scale desktop values down.
- Preserve content order, hierarchy, and primary actions when columns stack.
- Inspect image crops, line lengths, equal peer geometry, section spacing, and footer density at mobile, tablet, laptop, and wide desktop widths.
- Test immediately below and above fragile project breakpoints.
- Keep navigation, filters, forms, carts, dialogs, and sticky elements operable at their responsive sizes.
- Give primary touch controls roughly 44×44 CSS pixels of pointer area.

## Rendered QA

On every page verify:

- Document scroll width does not exceed client width.
- Visible images finish loading with non-zero natural dimensions.
- Headings, body copy, labels, buttons, and form controls do not clip or overlap.
- The intended H1 structure, shared navigation, and footer are present.
- Important controls have usable dimensions and visible focus states.
- Mobile navigation and primary interactions work by pointer and keyboard where supported.
- Console output contains no material errors.

Automated probes are evidence, not the whole audit. Visually inspect every unique template at mobile and desktop and at least one representative full page at each width class.
