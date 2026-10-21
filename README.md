# GPT Image 2D Game Assets

A Codex skill for making and reviewing 2D game art with the current GPT-image-2.5 workflow: pick a style, generate a sprite sheet, cut it into frames, check the alpha and the key poses, and assemble a timed GIF preview.

The bundled Python tools inspect, crop and assemble real pixels. They do not draw replacement art or invent missing animation frames.

## What's in this repository

- `gpt-image-2d-assets/` — the skill itself: `SKILL.md`, the agent configuration, seven reference guides, the recipe data, and the tool scripts.
- **Tools** — `scripts/asset_tools.py` (alpha inspection, coordinate-based sheet cutting, timed sequence assembly) and `scripts/motion_review.py` (key-pose and motion review), each with its own test file.
- **24 game-art recipes (G01–G24)** — characters, portraits, inventory icons, effects and backgrounds, written for game production rather than one-off illustration; bundled in [`game-styles.json`](gpt-image-2d-assets/references/game-styles.json).
- `docs/` and `examples/` — the fox run-cycle demo write-up, the September 2026 motion-validation notes, and the prompts, timing data and review records behind them.

## Install

Use Codex with the GPT-image-2.5 image workflow. Copy the skill folder into your Codex skills directory, usually `~/.codex/skills/`:

```text
gpt-image-2d-assets/
```

Back up an existing folder with this name before updating. You can also give Codex this repository URL and ask it to install the skill.

The crop and inspection tools need Python 3 and Pillow:

```sh
python -m pip install Pillow
```

**Optional companion style library:** the skill can also browse a 261-style reference library provided by Yang's separate `handdraw-style-prompter` skill ([yang0/handraw-style](https://github.com/yang0/handraw-style)). Install that skill alongside this one if you want the full style catalogue. The 24 game-art recipes in this repository work without it. See [CREDITS.md](CREDITS.md) for provenance.

## Try it

```text
In Codex, call `$gpt-image-2d-assets` to make a fox courier in G03 style.
Keep the background transparent.

Make a 3×3 run cycle for this fox, facing right.
Cut the sheet into frames and make a GIF preview.

Show this same character in cel, pixel and watercolor styles.
Keep the outfit, camera and pose the same.

Make a matching set of a potion, key, gem and scroll.
Check how they read at inventory-icon size.
```

## Tests

```sh
python gpt-image-2d-assets/scripts/test_asset_tools.py
python gpt-image-2d-assets/scripts/test_motion_review.py
```

CI runs both test files on Python 3.11 and 3.12 for every push and pull request.

## Honest limits

Always inspect the returned files: model output can still drift between frames or change a character's identity. Alpha checks, visual review, playback, engine testing and user approval are recorded separately — a successful file check does not establish animation quality or game readiness. The fox demo's gait still needs refinement before use in a game, and the motion experiments do not establish reliable production-quality animation.

## Demo media

The demo images and GIFs referenced from `docs/` and `examples/` are being migrated into this repository. Until that migration lands, they remain available in the original project repository: [Harrison0223-svg/gpt-image-2d-assets](https://github.com/Harrison0223-svg/gpt-image-2d-assets) (see its `examples/` and `docs/images/` folders).

## Project history

This project was developed in public from September 2026 and became an independent repository on 2026-10-21.

- **2026-09-21** — The game-asset workflow, this skill and its Python tools were first built in the author's fork [Harrison0223-svg/gpt-image-2d-assets](https://github.com/Harrison0223-svg/gpt-image-2d-assets): see the [initial integration commit](https://github.com/Harrison0223-svg/gpt-image-2d-assets/commit/837bfcef14) and the [documentation commit](https://github.com/Harrison0223-svg/gpt-image-2d-assets/commit/fc698d0a87).
- **2026-09-22** — The motion workflow was improved with verified key poses and recorded review evidence: [commit](https://github.com/Harrison0223-svg/gpt-image-2d-assets/commit/7182cd260f). The author's full commit list in that fork is [here](https://github.com/Harrison0223-svg/gpt-image-2d-assets/commits?author=Harrison0223-svg).
- **2026-10-21** — The original skill, tools, tests and docs were extracted into this repository as v0.1.0, so the project is maintained independently, with its own license, CI and releases.

The fork built on Yang's handdraw-style skill. Nothing in this repository inherits that project's stars, contributors or history. See [CREDITS.md](CREDITS.md) for what is original here, what comes from upstream, and the licensing boundary between the two.

## License

MIT — see [LICENSE](LICENSE). The companion style library is licensed separately in its own repository.
