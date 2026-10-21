# Credits and provenance

## Original to this repository

The following were written by Harrison Hu ([Harrison0223-svg](https://github.com/Harrison0223-svg)) in September 2026 and are released under the MIT License (see [LICENSE](LICENSE)):

- The `gpt-image-2d-assets` Codex skill (`SKILL.md`, agent configuration, reference guides)
- The 24 game-art recipes (G01–G24)
- `scripts/asset_tools.py` and `scripts/motion_review.py`, with their test files
- The documentation in `docs/` and the demo records in `examples/`

## Upstream

This workflow began by building on Yang's handdraw-style skill:
[yang0/handraw-style](https://github.com/yang0/handraw-style) (MIT License).
The source baseline at the time was commit `70bf51d6b4c301805dd6c083355a2ad18db1023b`.

The 261-style reference library from that project is **not** bundled in this repository. It remains available in the upstream project under its own license, and this skill can use it when the companion `handdraw-style-prompter` skill is installed alongside.

The reference images in that upstream library are credited source material, not original artwork by this project or by upstream. Their presence anywhere is not a guarantee of rights to use them as commercial game assets.

## Extraction note

Until 2026-10-21, this work lived in the author's fork
[Harrison0223-svg/gpt-image-2d-assets](https://github.com/Harrison0223-svg/gpt-image-2d-assets),
where the original parts were developed across four commits in September 2026 on top of the upstream history. From v0.1.0 onward it is maintained in this repository.
