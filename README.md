# STASRG Sulfur Monitoring Firmware

[![Build](https://img.shields.io/github/actions/workflow/status/STASRG/STASRG-SulfurMonitoring-Firmware/build.yml?style=flat-square)](https://github.com/STASRG/STASRG-SulfurMonitoring-Firmware/actions/workflows/build.yml)
[![ESP-IDF](https://img.shields.io/badge/ESP--IDF-v6.0-blue?style=flat-square)](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/index.html)
[![Target](https://img.shields.io/badge/target-ESP32S3-green?style=flat-square)](https://www.espressif.com/en/products/socs/esp32-s3)
[![License](https://img.shields.io/badge/license-Proprietary-red?style=flat-square)](LICENSE)

Air quality monitoring system for real-time measurement of SO₂, H₂S, wind speed, temperature, and humidity using ESP32-based microcontrollers.

## Tech Stack

| Category | Technology |
|----------|------------|
| MCU | ESP32-S3 |
| Framework | ESP-IDF v6.0 |
| Language | C / C++ |
| Gas Sensor | TB600 (SO₂ / H₂S) |
| Wind Sensor | Anemometer |
| Positioning | GPS (TinyGPSPlus) |
| Display | SSD1306 OLED (I²C) |
| Radio | SX1262 LoRa |
| Power Monitor | INA219 |
| Storage | MicroSD (SPI) |
| Build System | CMake / idf.py |
| CI/CD | GitHub Actions |
| Code Style | astyle (ESP-IDF OTBS) |

## Supported Targets

| Target | Status |
|--------|--------|
| ESP32 | Supported |
| ESP32-C3 | Supported |
| ESP32-S3 | Supported |

## Measured Variables

| Variable | Description | Unit |
|----------|-------------|------|
| `so2_ugm` | Sulfur dioxide concentration | µg/m³ |
| `h2s_ugm` | Hydrogen sulfide concentration | µg/m³ |
| `h2s_temp` | H₂S sensor temperature | °C |
| `h2s_hum` | H₂S sensor humidity | %RH |
| `wind_speed` | Wind speed | m/s |
| `bus_voltage_v` | Bus voltage | V |
| `current_ma` | Current draw | mA |

## Project Structure

```
.
├── application/rx_local_web_uart/    # Main application
│   ├── main/                         # Application source
│   │   ├── battery/                  # INA219 battery monitor
│   │   ├── display/                  # SSD1306 OLED display
│   │   ├── lora/                     # SX1262 LoRa radio
│   │   ├── sensor/                   # TB600, anemometer, GPS, wind direction
│   │   └── storage/                  # MicroSD card logging
│   ├── components/                   # Third-party libraries
│   └── examples/                     # Component usage examples
├── example/                          # Standalone component tests
├── tools/                            # Build tools and CI config
│   ├── fix_compile_commands.py       # Fix clangd compile_commands.json
│   └── ci/astyle-rules.yml           # ESP-IDF code style rules
└── .clang-format                     # C/C++ formatting (ESP-IDF OTBS)
```

## Build Instructions

### Prerequisites

- ESP-IDF v6.0 or later
- Python 3.8+

### Building

```bash
cd application/rx_local_web_uart
idf.py set-target esp32s3
idf.py build
```

### Flashing

```bash
idf.py -p /dev/ttyUSB0 flash monitor
```

### Fix clangd compile_commands.json

```bash
python tools/fix_compile_commands.py application/rx_local_web_uart
```

## Code Style

This project follows ESP-IDF style guide enforced by pre-commit hooks:

```bash
pre-commit run --all-files
```

## License

All Rights Reserved. See [LICENSE](LICENSE) for details.
