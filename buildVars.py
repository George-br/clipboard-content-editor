# Build customizations
# Change this file instead of SConstruct or manifest files, whenever possible.

from site_scons.site_tools.NVDATool.typings import AddonInfo, BrailleTables, SymbolDictionaries
from site_scons.site_tools.NVDATool.utils import _


addon_info = AddonInfo(
	addon_name="ClipboardContentEditor",
	# Translators: Summary/title for this add-on
	addon_summary=_("Clipboard Content Editor"),
	# Translators: Long description for this add-on
	addon_description=_(
		"Edits the current clipboard text in a simple editor so pasted content reflects the changes. "
		"Shortcuts: NVDA+E opens the editor, NVDA+Z restores the previous clipboard."
	),
	addon_version="1.1.0",
	# Translators: What's new content for the add-on version
	addon_changelog=_(
		"- Global shortcuts are now standardized: NVDA+E opens the editor dialog, "
		"NVDA+Z restores clipboard backups, and NVDA+I announces clipboard "
		"character/word/line counts.\n"
		"- Global shortcuts can now be reassigned via NVDA Input Gestures.\n"
		"- The Clear feature has been removed entirely (button, shortcut, settings, "
		"and notifications) because you can clear text directly in the clipboard editor.\n"
		"- The Read feature has been removed entirely (button, shortcut, settings, "
		"and notifications) because NVDA already provides clipboard reading via NVDA+C.\n"
		"- A Find button was added before Replace, with separate enable/disable options "
		"and updated shortcuts (Alt+F for Find, Alt+R for Replace).\n"
		"- Replace now preserves case by default, matching the capitalization of the "
		"found text.\n"
		"- Checkbox labels were updated to \"Case sensitive\" and "
		"\"Find/Replace whole words only, not part of other words\".\n"
		"- The clipboard info message now reads \"Clipboard information: ...\".\n"
		"- Documentation now includes links to other available languages.\n"
		"- What's New information is now available in both the documentation and "
		"the installation dialog.\n"
		"- Development support information has been removed from the documentation and "
		"the installation dialog."
	),
	addon_author="Fauzan January <surel@fauzanaja.com>",
	addon_url="https://fauzanaja.com/nvda-addon/",
	addon_sourceURL="https://github.com/fauzan-january/clipboard-content-editor/",
	addon_docFileName="readme.html",
	addon_minimumNVDAVersion="2024.1",
	addon_lastTestedNVDAVersion="2025.3",
	addon_updateChannel=None,
	addon_license="GPL-2.0",
	addon_licenseURL="https://www.gnu.org/licenses/gpl-2.0.html",
)

pythonSources: list[str] = [
	"addon/installTasks.py",
	"addon/globalPlugins/ClipboardContentEditor/*.py",
]

i18nSources: list[str] = pythonSources + ["buildVars.py"]

excludedFiles: list[str] = []

baseLanguage: str = "en"

markdownExtensions: list[str] = []

brailleTables: BrailleTables = {}

symbolDictionaries: SymbolDictionaries = {}

