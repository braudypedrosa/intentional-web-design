# Rejection patterns

Treat these as warnings requiring a specific justification. Reject them by default when they appear as automatic layout answers.

## Composition

- Two-column section introductions whose only logic is a heading in one column and supporting paragraph in the other. Treat this as a rejected AI-default scaffold even when it appears only once; allow it only when the columns have a concrete comparison, sequence, interaction, or other functional dependency.
- Mechanical image-copy alternation across an entire page.
- Generic card stacks, arbitrary bento grids, staggered cards, or floating glass panels.
- Reusing the same editorial scaffold across unrelated sections or brands.
- Reusing four or more composition-fingerprint traits from a recent same-industry project without a functional requirement.
- Decorative collection summaries and stat rows that delay the real inventory.
- Unequal peer grids or hover effects that resize siblings and destabilize comparison.
- Long split stories with an unused quiet column instead of purposeful persistent context.
- Homepage structures copied unchanged onto inner pages.
- Large solid-color conversion slabs when relevant imagery should culminate the visual story.

## Decorative habits

- Eyebrows, kickers, uppercase microcopy, badges, numbers, rules, and callouts without meaning.
- Promotional marquees or ticker strips.
- Decorative micro-images inserted inside headings.
- Excessive empty space, inflated section heights, and gaps used as a substitute for composition.
- Generic avatars, initials, or silhouette placeholders where real people create the required trust.

## Stability

- Inconsistent button geometry, icon treatment, form controls, or hover behavior.
- Motion that shifts essential labels or controls.
- Repeated cards with unequal padding or arbitrary internal alignment.
- Listing captions that push the item title to the opposite edge from its location, metadata, and price without a real tabular comparison need.
- Misaligned content widths across navigation, sections, forms, and footers.
- Hero content containers whose maximum width or horizontal gutters do not match the primary body container.
- Eyebrows, kickers, or subheaders whose spacing to their associated heading changes between otherwise equivalent section-header usages.
- Repeated bordered items that leave an unnecessary rule above the first item or below the last item instead of using internal separators.
- Text-and-action rows whose action stretches across unused space or aligns to the middle or bottom of multi-line copy instead of remaining bounded, end-aligned, and top-aligned.
- Block-length descriptive copy marked up as a span, especially when it directly follows an H1, H2, or H3.

## Bad-design audit gate

Treat the design as failed, not merely unfinished, when any of these conditions remain in a rendered page:

- hierarchy depends on oversized headings, tiny supporting copy, or decorative uppercase labels rather than content structure;
- descriptive prose following an H1, H2, or H3 uses span markup instead of a paragraph;
- any visible text computes below 14px at a supported viewport;
- headings wrap awkwardly, produce avoidable orphans, collide with nearby content, or use manual line breaks that fail across breakpoints;
- equivalent section headers, fields, cards, buttons, or lists use inconsistent spacing or alignment;
- borders describe every item independently and create doubled or unnecessary outer rules instead of clear internal separators;
- a layout uses empty space, opposing text columns, arbitrary offset, or asymmetry without a content or interaction reason;
- controls are visually ambiguous, undersized, stretched by their layout track, or detached from the information they affect;
- responsive behavior merely shrinks the desktop composition, damages reading order, or leaves isolated labels and headings;
- imagery is repeated, poorly cropped, irrelevant, low contrast, or functioning only as rectangle filler;
- the page has horizontal overflow, clipped text, broken states, fake controls, inaccessible focus behavior, or inconsistent containers;
- the interface could be transferred unchanged to an unrelated business without losing meaning.

Run this gate on desktop and mobile before approval. One unresolved failure keeps the design in revision.

Changing color, ratio, labels, or ornamentation does not transform a rejected scaffold into an intentional one.
