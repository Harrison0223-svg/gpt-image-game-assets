# Contributing

Thanks for considering a contribution. This is a small, single-maintainer project; the rules below keep contributions easy to review.

## Reporting a problem

Open an issue with:

- What you asked the skill (or the tool) to do, and what happened instead.
- For tool bugs: the exact command, the input file type, and the error output.
- For skill/workflow issues: the prompt you used and the returned files, if you can share them.

## Making a change

1. Fork the repository and create a topic branch.
2. Keep the change focused: one bug fix, one recipe improvement, or one tool feature per pull request.
3. Run the tests before submitting:

   ```sh
   python -m pip install Pillow
   python gpt-image-2d-assets/scripts/test_asset_tools.py
   python gpt-image-2d-assets/scripts/test_motion_review.py
   ```

   New tool behavior needs new tests; a bug fix needs a test that fails without the fix.
4. Write the pull request description in your own words: what changed, why, and how you verified it.

## AI-assisted contributions

AI-assisted work is welcome here — this project is itself a workflow for AI-assisted art production. Two conditions:

- **Disclose it** in one line in the pull request (for example: "AI Disclaimer: developed with the assistance of Codex").
- **You are responsible for the change**: you must be able to explain it and respond to review comments yourself. Unattended agent submissions are not accepted.

## Scope

The tools inspect, crop and assemble existing pixels; contributions that make them fabricate art or motion are out of scope. Style recipes should be written so another user can reproduce the result from the recipe alone.
