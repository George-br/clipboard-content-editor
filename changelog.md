## Changelog - Version 1.1.0

- Global shortcuts are now standardized: NVDA+E opens the editor dialog, NVDA+Z restores clipboard backups, and NVDA+I announces clipboard character/word/line counts.
- Global shortcuts can now be reassigned via NVDA Input Gestures.
- The Clear feature has been removed entirely (button, shortcut, settings, and notifications) because you can clear text directly in the clipboard editor.
- The Read feature has been removed entirely (button, shortcut, settings, and notifications) because NVDA already provides clipboard reading via NVDA+C.
- A Find button was added before Replace, with separate enable/disable options and updated shortcuts (Alt+F for Find, Alt+R for Replace).
- Replace now preserves case by default, matching the capitalization of the found text.
- Checkbox labels were updated to "Case sensitive" and "Find/Replace whole words only, not part of other words".
- The clipboard info message now reads "Clipboard information: ...".
- Documentation now includes links to other available languages.
- What's New information is now available in both the documentation and the installation dialog.
- Development support information has been removed from the documentation and installation dialog.

## Changelog - Version 1.0.0

- Initial release.
- Added **Clipboard Editor** dialog with the following features:
  - Speech
  - Information
  - Find/Replace
  - Clear
  - Save
  - Cancel
- Introduced global shortcuts for:
  - Opening the editor
  - Speaking clipboard
  - Showing clipboard information
- Implemented **Clipboard Backup (Protect Mode)** with restore functionality.
- Added settings to configure:
  - Button visibility
  - Shortcut behavior
