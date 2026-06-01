# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial project structure with ESP-IDF build system
- TB600 gas sensor driver (SO₂ and H₂S measurement)
- INA219 battery voltage and current monitoring
- SSD1306 OLED display support
- SX1262 LoRa radio communication
- GPS module integration via TinyGPSPlus
- Anemometer wind speed measurement
- Wind direction sensor interface
- MicroSD card data logging
- Pre-commit hooks for code style (ESP-IDF astyle OTBS)
- .clang-format configuration matching ESP-IDF style guide
- Standalone example projects for each component
- fix_compile_commands.py tool for clangd support

[Unreleased]: https://github.com/STASRG/STASRG-SulfurMonitoring-Firmware
