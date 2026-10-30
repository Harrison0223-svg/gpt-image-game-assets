# Codex 2D art: from style choice to a nine-frame GIF

> **Media note:** demo media loads from a pinned revision of the [original project repository](https://github.com/Harrison0223-svg/gpt-image-2d-assets) while migration into this repository remains incomplete.

This is the shareable version of the fox courier demo. The workflow combines the style-selection skill with the 2D asset skill and runs in Codex. The current setup uses GPT-image-2.5 for background removal and continuous-frame generation.

The style side started with Yang's handdraw-style skill and its library of 261 reference styles. We later added 24 game-art recipes for the kinds of characters, props, effects and UI pieces used in game production.

## Same fox, three directions

The outfit, shoulder bag and standing pose stay the same while the drawing language changes.

![Cel, pixel and watercolor foxes](https://raw.githubusercontent.com/Harrison0223-svg/gpt-image-2d-assets/7182cd260f054832537807fb43c84c01def2271b/examples/fox-motion/fox-style-comparison.png)

The cel version is my favorite for this character. Its outline stays clean and the teal cape sits well against the orange fur. The watercolor version leans toward illustration. The pixel version is a useful direction for another game style.

Pick a style ID, attach a reference image or mix a few traits. For example: keep the cel color blocks and add cut-paper edges. Make a small sample first, then continue with the chosen direction.

## Nine frames

The motion request was simple: face right, run through nine continuous poses, arrange them as a 3×3 sheet, and keep the outfit and proportions stable.

![Revised 3×3 sheet](https://raw.githubusercontent.com/Harrison0223-svg/gpt-image-2d-assets/7182cd260f054832537807fb43c84c01def2271b/examples/fox-motion/fox-run-3x3-v2.png)

We cut the sheet into nine PNGs and assembled a GIF at 90 ms per frame. The source sheet and individual frames are in the original project repository; the timing data is also recorded here. A later pass can change the loop speed or hold one pose for longer.

![Nine-frame run preview](https://raw.githubusercontent.com/Harrison0223-svg/gpt-image-2d-assets/7182cd260f054832537807fb43c84c01def2271b/docs/images/03-run.gif)

The first attempt had several poses that looked too similar. We called that out and generated a revised pass. This GIF is useful for checking the direction of the motion; foot timing and the loop seam still need work before it goes into a game. Playing it is a faster way to judge the sequence than staring at nine stills.

## A matching prop set

We also made a potion, key, gem and scroll in one grouped image, then split them out. Shared lighting and palette make them easier to keep together. The small preview shows which details survive at icon size.

![Inventory items](https://raw.githubusercontent.com/Harrison0223-svg/gpt-image-2d-assets/7182cd260f054832537807fb43c84c01def2271b/examples/inventory/small-preview.png)

The same process fits chest open/close states, character expressions, skill icons and spell stages from charge to fade. In Codex, call the skill and describe the style you want. The subject can be a character or a scene in the same visual language.

## Files

- [Motion source files and prompts](../examples/fox-motion)
- [Frame crops and timing](../examples/fox-motion/sequence-v2.json)
- [Motion review record](../examples/fox-motion/record.json)
- [Inventory source and alpha measurements](../examples/inventory)
- [Installation and usage](../README.md)
