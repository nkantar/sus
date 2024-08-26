# sus Changelog


<!--
- Added: for new features
- Changed: for changes in existing functionality
- Deprecated: for soon-to-be removed features
- Removed: for now removed features
- Fixed: for any bug fixes
- Security: in case of vulnerabilities
-->


## [Unreleased]

### Added
- Python 3.11, 3.12, and 3.13-dev to CI version matrix
- macOS and Windows to CI OS matrix

### Removed
- Python 3.6, 3.7, and 3.8 from CI version matrix


## [1.3.0] - 2021-10-16

### Added
- Comment support (lines starting with `#`)
- Blank line support, for legibility


## [1.2.0] - 2020-11-22

### Added
- Stripping of edge whitespace in line parts in `input`.


## [1.1.0] - 2020-09-30

### Added
- README:
  - Pronunciation section
  - Python 3.6+ requirement
  - Homepage section
- `make` commands for convenience
  - `make package` creates the wheel and tarball for publishing to PyPI
  - `make publish` publishes the above to PyPI
  - `make publish-test` publishes the above to TestPyPI
- Support for homepage via `home.html`

### Changed
- README phrasing
- Primes (`'`) and double primes (`"`) into apostrophes (`’`) and double quotes (`“` and `”`) in documentation
- Delete every directory before creating it:
  - `output/`
  - every slug directory inside `output/`

### Removed
- Unused code

### Fixed
- README typo


## [1.0.0] - 2020-09-17

### Added
- Initial implementation


[Unreleased]: https://github.com/nkantar/sus/compare/1.3.0...HEAD
[1.3.0]: https://github.com/nkantar/sus/compare/1.2.0...1.3.0
[1.2.0]: https://github.com/nkantar/sus/compare/1.1.0...1.2.0
[1.1.0]: https://github.com/nkantar/sus/compare/1.0.0...1.1.0
[1.0.0]: https://github.com/nkantar/sus/releases/tag/1.0.0
