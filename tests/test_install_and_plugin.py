import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import install  # noqa: E402


class PluginManifest(unittest.TestCase):
    def test_plugin_json(self):
        m = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
        self.assertEqual(m["name"], "gpt-image-2d-assets")
        for s in m["skills"]:
            self.assertTrue((ROOT / s / "SKILL.md").is_file(), s)

    def test_marketplace(self):
        m = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
        self.assertEqual(m["plugins"][0]["source"], "./")

    def test_skill_frontmatter_name_matches_dir(self):
        text = (ROOT / "gpt-image-2d-assets/SKILL.md").read_text()
        self.assertIn("\nname: gpt-image-2d-assets\n", text)


class Installer(unittest.TestCase):
    def test_resolve(self):
        self.assertEqual(install.resolve_dest("codex", None, False, home="/h"), Path("/h/.codex/skills"))
        self.assertEqual(install.resolve_dest("claude", None, True, cwd="/p"), Path("/p/.claude/skills"))
        self.assertEqual(install.resolve_dest(None, "/x", False), Path("/x"))

    def test_install_excludes_tests_and_backs_up(self):
        with tempfile.TemporaryDirectory() as d:
            out, what = install.install(d)
            self.assertEqual(what, "created")
            self.assertTrue((out / "SKILL.md").is_file())
            self.assertTrue((out / "scripts/asset_tools.py").is_file())
            self.assertFalse((out / "scripts/test_asset_tools.py").exists())
            (out / "marker").write_text("x")
            _, what = install.install(d)
            self.assertEqual(what, "replaced")
            self.assertTrue((Path(d) / "gpt-image-2d-assets.bak/marker").exists())
            self.assertFalse((Path(d) / "gpt-image-2d-assets/marker").exists())

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as d:
            _, what = install.install(d, dry_run=True)
            self.assertEqual(what, "would create")
            self.assertEqual(list(Path(d).iterdir()), [])


if __name__ == "__main__":
    unittest.main()
