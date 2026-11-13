# Platform IO

PlatformIO is a fantastic “batteries-included” toolchain for embedded dev. Here’s a practical, engineer-friendly guide you can use as a cheat-sheet and playbook.

Author

Benedict Thekkel

## What PlatformIO is (and why use it)

- **Cross-platform build & upload** for Arduino, ESP32/8266, STM32, AVR, RP2040/Pico, NRF52, etc.
- **Dependency & library manager** (pin versions, reproducible builds).
- **Multi-environment** configs: one repo can target multiple MCUs/boards/firms.
- **Integrated test, debug, serial monitor, and CI** (GitHub Actions, etc.).
- **IDE-agnostic**: VS Code (most common), CLion, Vim, or headless CLI.

------------------------------------------------------------------------

## Mental model (project anatomy)

    your-project/
    ├─ platformio.ini        # one file to rule them all
    ├─ src/                  # your firmware .cpp/.c/.ino
    ├─ include/              # headers
    ├─ lib/                  # private libs (each in its folder)
    ├─ test/                 # unit/integration tests (Unity)
    └─ .pio/                 # PlatformIO build cache (generated)

------------------------------------------------------------------------

## platformio.ini — the “recipe”

You define **environments** (`[env:...]`) that set the board, framework, upload method, build flags, libs, and per-env overrides.

------------------------------------------------------------------------

## Common patterns (copy-paste)

### 1) ESP32 (Arduino framework) + Serial monitor + OTA

``` ini
[platformio]
default_envs = esp32dev

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino

; Serial monitor
monitor_speed = 115200
monitor_filters = time, log2file

; Build flags
build_flags =
  -DCORE_DEBUG_LEVEL=3
  -DAPP_VERSION=\"1.0.0\"

; Libraries (lock to versions for reproducibility)
lib_deps =
  bblanchon/ArduinoJson@^7
  me-no-dev/AsyncTCP@^1.1.1

; Upload (USB serial by default). For OTA:
upload_protocol = espota
upload_port = 192.168.1.42
```

### 2) Raspberry Pi Pico / RP2040 (Arduino or Pico SDK via `arduino`/`mbed`/`pico-sdk`)

``` ini
[env:pico]
platform = raspberrypi
board = pico
framework = arduino
monitor_speed = 115200
build_flags = -DLED_PIN=25
```

### 3) STM32 (STM32Cube HAL) + ST-Link debug

``` ini
[env:nucleo-f401re]
platform = ststm32
board = nucleo_f401re
framework = stm32cube
upload_protocol = stlink
debug_tool = stlink
build_flags = -DUSE_FULL_ASSERT
```

### 4) AVR (Uno/Nano)

``` ini
[env:uno]
platform = atmelavr
board = uno
framework = arduino
upload_port = /dev/ttyUSB0
monitor_speed = 115200
```

### 5) “native” host tests (run C/C++ on your PC for fast unit tests)

``` ini
[env:native]
platform = native
test_build_src = true
build_flags = -DUNIT_TEST
```

------------------------------------------------------------------------

## Everyday CLI you’ll actually use

``` bash
pio project init        # turn a folder into a PIO project
pio run                 # build default envs
pio run -e esp32dev     # build a specific env
pio run -t clean        # clean build cache
pio run -t upload       # build+upload (serial/JTAG/OTA)
pio device monitor      # serial monitor (Ctrl+C to quit)
pio device list         # list serial ports
pio lib search <name>   # find libs
pio lib install <name>  # add lib (writes to platformio.ini)
pio pkg update          # update platforms/frameworks/libs (pinned)
pio test                # run tests in /test (Unity)
pio debug               # start a debug session (IDE integrates better)
```

> Tip (Linux): add udev rules for ST-Link/J-Link/CP210x/CH34x to avoid `sudo` on upload/debug.

------------------------------------------------------------------------

## Libraries & resolution (the gotchas)

- Prefer **`lib_deps`** in `platformio.ini` (not manual `lib/`) so versions are **pinned**.

- If the indexer can’t find headers, tweak the **Library Dependency Finder**:

  ``` ini
  lib_ldf_mode = chain+  ; or deep+
  lib_extra_dirs = extras/libs
  ```

- Use **semantic versions**: `me-no-dev/AsyncTCP@^1.1.1` or exact `@1.1.1`.

------------------------------------------------------------------------

## Build flags, variants, and conditional code

``` ini
build_flags =
  -DDEBUG
  -DBAUD=115200
  -I include/mocks     ; extra include dir
build_unflags = -Os     ; remove defaults if needed
```

``` cpp
#ifdef DEBUG
  Serial.println("debug mode");
#endif
```

------------------------------------------------------------------------

## Multi-board, one repo (environments)

``` ini
[platformio]
default_envs = uno,esp32dev

[env:uno]
platform = atmelavr
board = uno
framework = arduino

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
```

Run both: `pio run` → builds `uno` then `esp32dev`. Upload one: `pio run -t upload -e esp32dev`.

------------------------------------------------------------------------

## Debugging like a pro

- **ESP32**: on some boards you can use JTAG with an external adapter (FT2232H) or **ESP-PROG**:

  ``` ini
  debug_tool = esp-prog
  debug_init_break = tbreak setup
  ```

- **STM32**: `debug_tool = stlink` (set BOOT0=0). Breakpoints, watch variables, step-through in VS Code’s Run/Debug panel.

- **Pico/RP2040**: use **picoprobe** or CMSIS-DAP debugger.

> If you hit “Could not open port”, close the serial monitor (it locks the port) or set `monitor_rts`/`monitor_dtr` to avoid board resets.

------------------------------------------------------------------------

## Testing (Unity) patterns that scale

    test/
    ├─ test_main.cpp
    └─ test_utils/
       └─ test_crc.cpp

**test/test_main.cpp**

``` cpp
#include <Arduino.h>
#include <unity.h>

void test_addition() { TEST_ASSERT_EQUAL(4, 2+2); }

void setup() {
  UNITY_BEGIN();
  RUN_TEST(test_addition);
  UNITY_END();
}

void loop() {}
```

Run on device: `pio test -e esp32dev`. Run on PC (fast): `pio test -e native`.

------------------------------------------------------------------------

## Serial monitor & logging

``` ini
monitor_speed = 921600
monitor_filters = time, colorize, default
; Auto-reconnect on reset:
monitor_rts = 0
monitor_dtr = 0
```

Use **`pio device monitor --raw`** when you stream JSON or binary.

------------------------------------------------------------------------

## Source layout & selective builds

To exclude big examples or mocks from firmware builds:

``` ini
src_filter =
  +<*>       ; include everything...
  -<**/demo> ; ...except demos
```

------------------------------------------------------------------------

## Custom boards (when your exact board isn’t listed)

Create `boards/my_custom.json`:

``` json
{
  "build": {
    "core": "arduino",
    "f_cpu": "80000000L",
    "mcu": "esp32",
    "variant": "esp32"
  },
  "connectivity": ["wifi","bluetooth"],
  "debug": { "openocd_target": "esp32.cfg" },
  "frameworks": ["arduino"],
  "name": "MyESP32Mini",
  "upload": { "maximum_ram_size": 327680, "maximum_size": 1310720, "speed": 921600 },
  "url": "https://example.com",
  "vendor": "MyCo"
}
```

Then:

``` ini
board = my_custom
board_dir = boards
```

------------------------------------------------------------------------

## Continuous Integration (GitHub Actions)

``` yaml
name: Firmware CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -U platformio
      - run: pio pkg update
      - run: pio run -e esp32dev -e uno
      - run: pio test -e native
```

Pin library versions → deterministic CI.

------------------------------------------------------------------------

## Reproducibility & speed tips

- **Pin everything** (`lib_deps`, frameworks). Commit `platformio.ini`.
- **Cache**: CI runners cache `~/.platformio` between builds if you want faster CI.
- **Clean only when needed**: `pio run -t clean` slows iteration; prefer incremental builds.
- **Multiple serial ports**: specify `upload_port` and `monitor_port` to avoid auto-detection delays.

------------------------------------------------------------------------

## Over-the-Air (OTA) uploads (ESP32/8266)

- Set `upload_protocol = espota` + `upload_port = <ip>`.
- Ensure your sketch has OTA server code (e.g., ArduinoOTA in `setup()`).

------------------------------------------------------------------------

## Typical “why isn’t upload working?” checklist

- Wrong **port** → `pio device list` and set `upload_port`.
- Serial **driver** missing (CP210x/CH34x/FTDI) → install OS drivers.
- On Linux, **udev rules** not installed → board shows but upload fails (`dmesg` hints).
- **Monitor open** → close it before upload or use `--upload-port` to avoid port race.
- Wrong **boot mode** (e.g., STM32 BOOT0/BOOT1, ESP32 EN/BOOT buttons).

------------------------------------------------------------------------

## Migration from Arduino IDE

- Keep your `.ino` as `src/main.ino` or convert to `.cpp` (`setup()`, `loop()` remain).
- Map **Board** → `board = ...` in `platformio.ini`.
- List all libraries in `lib_deps` with versions (from Arduino Library Manager names or PIO registry).

------------------------------------------------------------------------

## Quality-of-life flags you’ll love

``` ini
; Build with more warnings:
build_flags = -Wall -Wextra -Werror

; Faster logs while debugging:
monitor_eol = LF
monitor_echo = yes

; Per-env upload/monitor overrides:
[env:debug-esp32]
extends = esp32dev
build_type = debug
upload_speed = 921600
```

------------------------------------------------------------------------

## Example: multi-MCU starter `platformio.ini`

``` ini
[platformio]
default_envs = native,uno,esp32dev

[env:native]
platform = native
test_build_src = true
build_flags = -DUNIT_TEST

[env:uno]
platform = atmelavr
board = uno
framework = arduino
monitor_speed = 115200
lib_deps = olikraus/U8g2@^2.35.19

[env:esp32dev]
platform = espressif32
board = esp32dev
framework = arduino
monitor_speed = 115200
lib_deps =
  bblanchon/ArduinoJson@^7
  knolleary/PubSubClient@^2
build_flags =
  -DAPP_NAME=\"TelemetryNode\"
  -DCORE_DEBUG_LEVEL=3
```

------------------------------------------------------------------------

## Quick start checklist (print this)

1.  `pip install -U platformio`
2.  `pio project init --ide vscode --board esp32dev` (or your board)
3.  Add your code to `src/`, headers to `include/`
4.  Pin libs in `lib_deps`
5.  `pio run -t upload` → flash
6.  `pio device monitor` → logs
7.  Add tests in `test/` → `pio test`
8.  Add CI (snippet above)

If you tell me your target boards (e.g., ESP32 + STM32 + RP2040) and what you’re building (sensors? MQTT? display?), I’ll generate a tailored `platformio.ini`, skeleton code in `src/`, a `test/` example, and a GitHub Actions workflow so you can just push and go.

------------------------------------------------------------------------

Back to top
