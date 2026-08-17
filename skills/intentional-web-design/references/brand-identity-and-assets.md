# Brand Identity and Asset Production

Use this workflow when the request includes brand strategy, naming support, a logo, a brand board, identity direction, or a complete brand asset package. Treat the identity as the upstream system for the website, not as decoration added after the interface.

## Core contract

Deliver two connected layers:

1. **Brand direction** — the strategic idea, visual concept, and presentation board.
2. **Production system** — exact, reusable master files and exports that match the approved direction.

Never present an image-generated logo as a finished production logo. Image generation can explore atmosphere, mockups, imagery, or broad mark direction, but rebuild the selected logo and wordmark as exact vector artwork before calling the brand kit complete.

Generate the final brand board from the same master logo, typefaces, color values, and supporting assets included in the package. A board that shows a different mark from the delivered logo files fails the completion contract.

## Brand discovery

Inspect the supplied brief, existing identity, product, audience, competitors, category conventions, website content, and technical constraints. Infer only what can be supported by the available context.

Define:

- audience and buying context;
- category and positioning;
- practical and emotional promise;
- three to five personality traits;
- one central brand idea or metaphor;
- what the identity must avoid;
- primary digital and physical touchpoints;
- accessibility, language, and localization needs.

If the user supplies an existing logo or identity element, preserve it unless redesign is explicitly requested. If the user asks for a complete direction without an approval checkpoint, choose one coherent, defensible direction and complete it. If several materially different directions are requested, present them as concept boards and productionize only the selected direction.

Do not claim that a name, symbol, or logo is legally clear. Flag obvious similarity risks and recommend professional trademark review before registration or launch.

## Concept standard

Base the identity on meaning rather than a fashionable visual treatment. Explain the link between the brand idea, mark geometry, typography, palette, imagery, and interface behavior.

Require the identity to be:

- distinctive at small size;
- recognizable in one color;
- usable on light and dark surfaces;
- legible in horizontal and compact arrangements;
- compatible with the intended website and product UI;
- reproducible without proprietary effects;
- restrained enough to remain coherent across applications.

Avoid generic startup gradients, arbitrary sparkles, copied monograms, meaningless geometry, overcomplicated crests, fake heritage devices, random mockups, and logo variants whose geometry changes from panel to panel.

## Brand-board workflow

Create one art-directed overview board by default. Choose the board layout according to the story rather than filling a fixed template. A useful default is a 3 by 3 system containing:

1. primary logo and concise brand idea;
2. symbol construction or concept logic;
3. horizontal or alternate lockup;
4. color system;
5. typography hierarchy;
6. imagery or material direction;
7. digital application;
8. physical or environmental application;
9. graphic system, pattern, icons, or UI detail.

Keep the board sparse, coherent, and readable. Use a deliberate grid, strong negative space, consistent gutters, controlled hierarchy, and only enough text to explain the system. Mockups must demonstrate likely real touchpoints, not decorate empty panels.

Use image generation for photographic atmosphere, material studies, or concept exploration when helpful. Use deterministic layout tools such as HTML/CSS, SVG, canvas, or presentation software for the final board whenever exact logo geometry, typography, and color reproduction matter. Render and visually inspect the final board before delivery.

## Logo production

Create a single canonical vector master, then derive every variant from it. Do not redraw each variant independently.

Produce the applicable set:

- primary horizontal lockup;
- stacked or compact lockup;
- standalone symbol;
- wordmark;
- tagline lockup when the tagline is stable and requested;
- full-color light-background version;
- full-color dark-background version;
- black, white, and one-color versions;
- small-size or simplified mark only when the master genuinely loses clarity at favicon scale.

For each SVG:

- use a correct `viewBox` and tight, consistent bounds;
- remove hidden layers, editor metadata, linked files, and rasterized logo content;
- convert special lettering to outlines when exact wordmark appearance must be preserved;
- also retain an editable live-type source when licensing permits;
- use named or documented colors rather than near-duplicate values;
- test transparency and both light and dark backgrounds;
- avoid clipping, stray points, malformed paths, and unnecessary transforms.

Export raster versions from the canonical vectors. Do not upscale a raster concept image.

## Color system

Define colors by role, not only by swatch name:

- primary brand color;
- secondary or supporting colors;
- accent and interaction color;
- paper or canvas color;
- text and muted text colors;
- border and surface colors;
- success, warning, and error colors when the product needs them.

Record HEX and RGB for all colors. Add CMYK and Pantone only when the workflow can produce or verify them responsibly; label unverified print conversions as starting values, not press-ready matches.

Check essential text/background combinations against WCAG contrast. A logo color may be expressive without being suitable for body text; document that distinction.

Deliver color tokens in both CSS and JSON. Keep token names semantic enough to survive palette refinements.

## Typography system

Prefer freely licensed, production-available families unless the user requests a commercial typeface. Google Fonts and other OFL-licensed families are good defaults when they suit the brand.

Define:

- display or headline family;
- body and interface family;
- optional accent family only when it has a clear role;
- weights actually required;
- fallback stacks;
- headline, body, label, and UI roles;
- recommended tracking, leading, and case behavior;
- web loading guidance.

Avoid choosing monospace merely because the product is technical. Match the emotional and reading needs of the brand. Do not bundle font binaries unless their license permits redistribution. When bundling an OFL font, include its license and source information.

## Graphic language

Define only systems that can be used consistently:

- grid and framing logic;
- shape or container language;
- icon style and stroke rules;
- pattern or texture rules;
- illustration or photography direction;
- image crops and treatments;
- motion principles when relevant;
- border radius, stroke, and shadow behavior for digital products.

Derive these from the central brand idea. Do not add a pattern, texture, mascot, or icon set just to make the package appear larger.

## Full asset package

Use one stable `branding/` directory and update it in place as the identity evolves. Do not create a new ZIP or versioned duplicate for every revision unless the user explicitly requests release archives.

Use this baseline structure, omitting only genuinely irrelevant categories:

```text
branding/
├── README.md
├── brand-board/
│   ├── brand-board.png
│   └── brand-board.pdf
├── guidelines/
│   ├── brand-guidelines.md
│   └── brand-guidelines.pdf
├── logos/
│   ├── svg/
│   ├── png/
│   └── source/
├── icons/
│   ├── favicon.ico
│   ├── favicon.svg
│   ├── apple-touch-icon.png
│   ├── icon-192.png
│   └── icon-512.png
├── social/
│   ├── avatar.png
│   └── open-graph.png
├── colors/
│   ├── color-tokens.css
│   ├── color-tokens.json
│   └── swatches.svg
├── typography/
│   ├── typography.css
│   ├── font-sources.md
│   └── licenses/
├── graphics/
│   ├── patterns/
│   ├── icons/
│   └── imagery/
├── templates/
└── manifests/
    ├── asset-manifest.json
    └── checksums.sha256
```

The package `README.md` must explain the directory, preferred logo variants, minimum-size and clear-space rules, color roles, font setup, and how to regenerate exports. Keep source files or generation scripts beside the relevant assets when the environment supports them.

### Required baseline exports

Unless the brief narrows the deliverable, include:

- exact SVG masters for all approved logo configurations;
- transparent PNG exports at practical small, medium, and large sizes;
- favicon SVG and ICO;
- 180 px Apple touch icon;
- 192 px and 512 px application icons;
- square avatar at 1024 px;
- Open Graph image at 1200 by 630 px;
- color token CSS and JSON;
- typography CSS and font-source documentation;
- brand board PNG and PDF;
- concise guidelines in editable Markdown and rendered PDF;
- asset manifest describing files, dimensions, color mode, and intended use;
- SHA-256 checksums for delivered files.

Add platform-specific social banners, stationery, slide templates, email signatures, product splash screens, or campaign templates only when relevant to the requested touchpoints.

## Guidelines content

Document:

- brand idea and personality;
- logo concept and approved configurations;
- clear space and minimum size;
- correct and incorrect logo usage;
- light, dark, monochrome, and photographic-background behavior;
- color values, semantic roles, and accessible combinations;
- typography roles and examples;
- imagery, iconography, pattern, and layout principles;
- digital UI translation;
- file-selection guidance;
- licensing and source notes.

Use real delivered assets in the guidelines. Do not draw substitute logos or invent type specimens.

## Quality assurance

Before completion:

1. Compare every logo shown on the brand board and in the guidelines with the canonical SVG.
2. Render all SVGs and inspect for clipping, incorrect bounds, missing fonts, malformed paths, and inconsistent geometry.
3. Inspect transparent PNGs on both light and dark backgrounds.
4. Verify every raster dimension and confirm that alpha is preserved where intended.
5. Confirm favicon readability at 16, 24, and 32 px.
6. Verify color values across the guidelines, CSS, JSON, and SVG assets.
7. Confirm font names, weights, source URLs, and redistribution licenses.
8. Render every PDF and visually inspect each page for overflow, substitution, or broken imagery.
9. Check the asset manifest against the actual directory and regenerate checksums last.
10. Remove temporary, duplicate, obsolete, and misleading draft files from the delivery directory.

Do not call the package complete when it contains only a board image, only logo PNGs, or assets that cannot reproduce the displayed identity.
