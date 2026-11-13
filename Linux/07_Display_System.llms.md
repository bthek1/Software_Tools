# Display System

Below is a complete breakdown designed to give you a **full foundational → intermediate → advanced understanding** of *display servers* (X11, Wayland) and *desktop environments* (GNOME, KDE Plasma, XFCE, etc.).

Author

Benedict Thekkel

## 🖥️ Part 1 — Display Servers / Display Protocols

These are the **low-level systems** responsible for drawing pixels on screen, handling input devices (keyboard, mouse, touch), and communicating with GPU drivers. They are the layer below desktop environments and window managers.

------------------------------------------------------------------------

### 🔷 X11 / X.Org Server

The older and historically dominant display server for Linux/Unix-like systems.

#### Core Concepts

| Feature      | Description                                              |
|--------------|----------------------------------------------------------|
| Protocol     | X11 (1987) — networked GUI protocol                      |
| Server Name  | X.Org Server (most common implementation)                |
| Architecture | Central server handles outputs, clients draw windows     |
| Extensions   | Needed for modern features (compositing, HiDPI, scaling) |

#### Key Characteristics

✔ Mature, stable, compatible with decades of software ✔ Remote network rendering works very well (e.g., `ssh -X`, X forwarding) ✔ Extremely configurable, many window managers (i3, Awesome, bspwm)

✘ Performance overhead — multiple round-trips between client & server ✘ Security limitations — apps can spy on each other’s input events ✘ Extensions (XRandR, XRender, XInput2) bolted on rather than native

**Why it still exists:** compatibility and tooling. Some legacy apps require it.

------------------------------------------------------------------------

### 🔷 Wayland

The **modern successor to X11**, built to fix X11’s inherent design issues.

### Core Ideas

| Feature | X11 | Wayland |
|----|----|----|
| Design | Everything goes through one server | Compositors manage their own windows |
| Rendering | Server manages drawing | Clients draw directly → better latency |
| Security | Weak sandboxing | Strong isolation, apps can’t snoop |
| Remote access | Built-in? No | Under development via PipeWire & RDP |
| Extensions | Many | Protocols modular + evolving |

#### Benefits

✔ Lower input latency → faster responsiveness ✔ Better power efficiency (especially on laptops) ✔ Fractional scaling and HiDPI are cleaner ✔ No screen tearing when compositor is native Wayland

#### Downsides (as of now)

⚠ Older apps may need XWayland (compatibility layer) ⚠ Screen capture + remote desktop required PipeWire & new APIs ⚠ Niche color-critical workflows still maturing

#### Real-world adoption status

| Desktop    | Wayland Ready?                                  |
|------------|-------------------------------------------------|
| GNOME      | Excellent — Wayland by default on most distros  |
| KDE Plasma | Very good — Wayland default in Plasma 6         |
| XFCE       | Improving, still experimental for some features |
| Ubuntu     | Wayland default since 22.04 (for GNOME)         |

------------------------------------------------------------------------

### 🧠 How the stack layers together

    Hardware (GPU, Monitor)
            ↓
    Kernel Drivers (DRM/KMS)
            ↓
    Display Server / Compositor
       X11 (Xorg)   OR   Wayland (Mutter, KWin, etc.)
            ↓
    Window Manager
            ↓
    Desktop Environment (GNOME/KDE/XFCE etc.)
            ↓
    Applications

------------------------------------------------------------------------

## 🖥️ Part 2 — Desktop Environments (DEs)

A Desktop Environment = **shell + window manager + settings + core apps** You can think of DEs as “the full user experience layer”.

> X11/Wayland = backend \| DE = frontend UI

------------------------------------------------------------------------

### 🔷 GNOME

Default on Ubuntu. Minimal, touch-friendly, modern.

#### Philosophy

- **Less UI, more focus**
- Workspaces + Activities Overview instead of desktop icons
- No heavy customization → consistent UX

#### Tech Stack

| Component                   | Tech                               |
|-----------------------------|------------------------------------|
| Window Manager / Compositor | Mutter                             |
| Toolkit                     | GTK (C / GNOME Libs)               |
| Extensions                  | GNOME Shell Extensions (.js based) |

#### Strengths

✔ Clean, simple UI ✔ Great Wayland support ✔ Good accessibility + HiDPI scaling ✔ Huge ecosystem of GTK apps

#### Weaknesses

✘ Limited configurability without extensions ✘ Higher RAM usage than XFCE/Openbox ✘ Some dislike the workflow vs Windows-style taskbar

#### Best for

- Productivity-focused workflow
- Smooth Wayland experience
- Ubuntu users who want zero-config elegance

------------------------------------------------------------------------

### 🔷 KDE Plasma

Often considered the **most customizable DE in Linux history**.

#### Philosophy

- Freedom + configurability
- Traditional desktop metaphor
- Aim: Lightweight but powerful

#### Tech Stack

| Component                   | Tech                       |
|-----------------------------|----------------------------|
| Window Manager / Compositor | KWin                       |
| Toolkit                     | Qt                         |
| Framework                   | KDE Frameworks (KF5 → KF6) |

#### Strengths

✔ Ridiculously customizable (themes, panels, animations) ✔ Plasma 6: efficient, fast, excellent Wayland support ✔ KDE Apps: Dolphin, Kate, Okular, Kdenlive, Gwenview ✔ Works well even on old hardware

#### Weaknesses

✘ Can overwhelm new users ✘ Many settings means more surface for breakage ✘ Qt apps sometimes look odd in GTK environments

#### Best for

- Power users
- Folks coming from Windows
- Tinkerers who want full control

------------------------------------------------------------------------

### 🔷 XFCE

Lightweight, traditional, stable for decades.

#### Philosophy

- Fast, light, classic desktop layout
- Minimal resource usage
- Slow + careful development (rock solid)

#### Strengths

✔ Extremely lightweight (great for older laptops) ✔ Simple & predictable UI ✔ Highly stable over long periods ✔ Runs great under X11, improving Wayland support

#### Weaknesses

✘ Visuals more dated unless themed ✘ Less modern UX vs GNOME/KDE ✘ Wayland still catching up

#### Best for

- Older machines or low-power laptops
- Users wanting speed + simplicity

------------------------------------------------------------------------

### Other notable DEs (quick overview)

| DE | Highlights | Best For |
|----|----|----|
| **Cinnamon** | Linux Mint default, Windows-like UI | Windows converts |
| **MATE** | GNOME 2 fork, light & stable | Traditional desktop lovers |
| **LXQt** | Lighter than XFCE, Qt-based | Very low-resource hardware |
| **Budgie** | Sleek GNOME-based shell | Modern aesthetics without clutter |
| **Pantheon** | macOS-like (elementaryOS) | Elegant design focus |

------------------------------------------------------------------------

## 🧭 Recommendations for You (Ubuntu user)

#### If you want default experience

→ Stay with **GNOME on Wayland**

#### If you want more speed + performance

    sudo apt install xfce4

#### If you want full customization power

    sudo apt install kde-standard

#### If apps misbehave under Wayland

Choose X11 session at login screen (gear icon) as fallback.

------------------------------------------------------------------------

### Quick Summary Matrix

| Feature | X11 | Wayland | GNOME | KDE Plasma | XFCE |
|----|----|----|----|----|----|
| Age | Very old | Modern | Modern | Modern/Advanced | Classic |
| Performance | Good but inefficient | Faster, lower latency | Smooth | Very smooth | Efficient |
| Customizable | Depends on WM | Depends on compositor | Limited | Extremely flexible | Moderate |
| RAM usage | Medium | Low-Medium | Higher | Medium-Low | Very low |
| Best for | Legacy + remote display | Future of Linux | Simple workflow | Power users | Lightweight setups |

------------------------------------------------------------------------

## 🛠️ Part 3 - Multi-Monitor Troubleshooting (GNOME on Wayland, NVIDIA)

A runbook from a real three-monitor desktop (Ubuntu, GNOME 50 on Wayland, GTX 1660 SUPER, NVIDIA open driver 595) where two of the three monitors were the same model. Every symptom first looked like one problem and turned out to be another, so it is organised by symptom.

------------------------------------------------------------------------

### How GNOME tells monitors apart

Mutter, GNOME’s compositor, saves layouts in `~/.config/monitors.xml` and identifies each monitor by **connector + vendor + product + serial**, all but the connector read from the monitor’s EDID.

``` bash
# What each port reports (no root needed)
for c in /sys/class/drm/card*-*; do
  echo "$(basename $c): $(cat $c/status)"; strings $c/edid 2>/dev/null | head -2
done

# What Mutter sees, as (connector, vendor, product, serial)
gdbus call --session --dest org.gnome.Mutter.DisplayConfig \
  --object-path /org/gnome/Mutter/DisplayConfig \
  --method org.gnome.Mutter.DisplayConfig.GetCurrentState
```

**Two monitors of the same model often report the same serial**; cheap panels ship `0000000000000`. The connector is then the only thing separating them, which has knock-on effects:

- Swapping their cables swaps their saved positions.
- `monitors.xml` keeps a layout for every cabling it has ever seen, and X11 and Wayland name the same port differently (`HDMI-0` vs `HDMI-1`). Sixteen stale entries had built up here, some describing the twins on ports they no longer used.
- Other tools get confused too. `ddcutil detect` labelled both twins `card1-DP-1`: the NVIDIA driver does not expose which I2C bus belongs to which port (`/sys/class/drm/card*-*/ddc` is empty), so ddcutil matches EDIDs, and identical EDIDs both match the first port.

Moving both twins onto DisplayPort does **not** fix any of this. It only removes HDMI from the picture.

------------------------------------------------------------------------

### Symptom 1: one screen stays black after lock and unlock

Super+L blanks the monitors (DPMS off). On unlock GNOME only powers the outputs back on; it does not redo a full modeset, because as far as it knows nothing changed. A monitor that fails to resync stays black while the system insists it is on:

``` bash
for c in /sys/class/drm/card*-*; do
  echo "$(basename $c) dpms=$(cat $c/dpms) enabled=$(cat $c/enabled)"
done
```

`dpms=On enabled=enabled` on a black screen means it is this problem and not a layout problem. Nothing is logged by the kernel or gnome-shell.

The tell-tale: **changing the refresh rate in Settings brings it back.** Any mode change forces a full modeset, and the monitor relocks onto the signal. The prime suspect is 4K at 60 Hz over HDMI on NVIDIA, which needs HDMI 2.0 scrambling renegotiated after the monitor sleeps; DisplayPort does not need that handshake.

The same flip can be scripted against Mutter’s D-Bus API. `monitors-wake` switches each monitor to another refresh rate at the same resolution, waits, then restores the original layout:

``` python
#!/usr/bin/python3 -I
"""Wake a monitor that stayed black after unlock by forcing a full modeset.

    monitors-wake                # cycle every monitor
    monitors-wake HDMI-1 DP-3    # cycle only these connectors
    monitors-wake --dry-run      # validate with Mutter, change nothing
"""

import argparse
import sys
import time

from gi.repository import Gio, GLib

BUS_NAME = "org.gnome.Mutter.DisplayConfig"
OBJ_PATH = "/org/gnome/Mutter/DisplayConfig"
METHOD_VERIFY, METHOD_TEMPORARY = 0, 1


def proxy():
    return Gio.DBusProxy.new_for_bus_sync(
        Gio.BusType.SESSION, Gio.DBusProxyFlags.NONE, None, BUS_NAME, OBJ_PATH, BUS_NAME, None
    )


def current_state(p):
    serial, monitors, logical, props = p.call_sync(
        "GetCurrentState", None, Gio.DBusCallFlags.NONE, -1, None
    ).unpack()
    return serial, monitors, logical, props


def current_modes(monitors):
    """connector -> (current mode tuple, list of all mode tuples)."""
    out = {}
    for spec, modes, _props in monitors:
        cur = next((m for m in modes if m[6].get("is-current")), None)
        if cur is not None:
            out[spec[0]] = (cur, modes)
    return out


def alternate_mode(cur, modes):
    """Same resolution, closest different refresh rate."""
    _id, w, h, rate = cur[:4]
    same_res = [m for m in modes if m[1] == w and m[2] == h and abs(m[3] - rate) > 0.01]
    return min(same_res, key=lambda m: abs(m[3] - rate)) if same_res else None


def build_config(logical, mode_for):
    """Rebuild the logical layout, picking each connector's mode via mode_for."""
    cfg = []
    for x, y, scale, transform, primary, specs, _props in logical:
        mons = [(s[0], mode_for(s[0]), {}) for s in specs]
        cfg.append((x, y, scale, transform, primary, mons))
    return cfg


def apply(p, serial, method, cfg):
    p.call_sync(
        "ApplyMonitorsConfig",
        GLib.Variant("(uua(iiduba(ssa{sv}))a{sv})", (serial, method, cfg, {})),
        Gio.DBusCallFlags.NONE,
        -1,
        None,
    )


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("connectors", nargs="*", help="connectors to cycle (default: all)")
    ap.add_argument("--dry-run", action="store_true", help="ask Mutter to verify only")
    ap.add_argument("--pause", type=float, default=2.0, help="seconds on the alternate rate")
    args = ap.parse_args()

    p = proxy()
    serial, monitors, logical, _ = current_state(p)
    modes = current_modes(monitors)
    original = {c: cur[0] for c, (cur, _) in modes.items()}

    targets = args.connectors or list(modes)
    unknown = [c for c in targets if c not in modes]
    if unknown:
        sys.exit(f"unknown connector(s): {', '.join(unknown)}; active: {', '.join(modes)}")

    swapped = dict(original)
    for c in targets:
        cur, all_modes = modes[c]
        alt = alternate_mode(cur, all_modes)
        if alt is None:
            print(f"{c}: no other refresh rate at {cur[1]}x{cur[2]}, leaving it alone")
            continue
        swapped[c] = alt[0]
        print(f"{c}: {cur[3]:.3f} Hz -> {alt[3]:.3f} Hz -> back")

    if swapped == original:
        sys.exit("nothing to cycle")

    method = METHOD_VERIFY if args.dry_run else METHOD_TEMPORARY
    apply(p, serial, method, build_config(logical, swapped.get))
    if args.dry_run:
        apply(p, serial, METHOD_VERIFY, build_config(logical, original.get))
        print("dry run: Mutter accepted both configurations, nothing changed")
        return

    time.sleep(args.pause)
    # Every apply bumps the serial, so fetch it again before restoring.
    serial, _, logical, _ = current_state(p)
    apply(p, serial, METHOD_TEMPORARY, build_config(logical, original.get))
    print("restored original layout")


if __name__ == "__main__":
    try:
        main()
    except GLib.Error as e:
        sys.exit(f"Mutter refused: {e.message}")
```

Save it as `~/.local/bin/monitors-wake` and `chmod +x` it. Three details matter:

- **The shebang is `/usr/bin/python3`, not `python3`.** PyGObject (`gi`) comes from the apt package `python3-gi` and exists only in the system interpreter; a project venv on `PATH` does not have it.
- **`ApplyMonitorsConfig` takes a method.** `0` (verify) makes Mutter validate a config without applying it, which is how `--dry-run` tests the script without the screens flickering. `1` (temporary) applies without writing `monitors.xml` and without the “Keep changes?” dialog. `2` (persistent) saves.
- **The serial changes on every apply**, so it is fetched again before restoring; reusing the old one is rejected.

------------------------------------------------------------------------

### Symptom 2: the monitor is connected but GNOME leaves it off

sysfs says `status=connected`, and Mutter lists the monitor with its modes in `GetCurrentState`, but no logical monitor uses it. Here that happened right after re-cabling the twins: GNOME saved a two-monitor layout and left the third out. It is a GNOME layout decision, not hardware.

Confirm by asking Mutter to verify a config that includes it (method `0`). If Mutter accepts, apply it temporarily (method `1`), then arrange the screens in **Settings -\> Displays -\> Apply -\> Keep Changes** so the layout is saved.

------------------------------------------------------------------------

### Symptom 3: enabled everywhere, still no picture

GNOME, the driver and sysfs all say the output is on, and dropping it to 1920x1080 (a quarter of the 4K bandwidth) is still blank. The picture is leaving the card and the monitor is not showing it.

**Check the monitor’s own input source before blaming the cable or port.** Many monitors do not switch inputs automatically. One moved from HDMI to DisplayPort keeps listening on HDMI, and shows nothing however the computer drives it. That was the whole cause here, and the fix was one button press on the monitor’s menu.

The clue is DDC/CI. The card can still read the EDID over the DisplayPort cable (that is how it knew the model), but DDC commands to the monitor fail:

``` bash
sudo apt install ddcutil && sudo modprobe i2c-dev
sudo ddcutil detect                  # the dead one: "DDC communication failed"
sudo ddcutil --bus 6 getvcp 60       # input source of the working twin
sudo ddcutil --bus 3 setvcp 60 0x08  # try to switch the dead one; fails if it is not listening
```

- Run these from GNOME Terminal. `sudo` does not work from a VS Code integrated terminal, which runs with `no_new_privs`.
- **Address twins by `--bus N`, not `--display N`**, since ddcutil may have mislabelled them.
- **VCP `0x60` input codes are vendor-specific in practice.** The MCCS standard gives DisplayPort-1 as `0x0f`, but this Kogan model reports `0x08` for DisplayPort, which ddcutil prints as “S-Video-2”. Read the code from a working twin rather than trusting the table.
- A monitor that ignores DDC cannot be switched over DDC either. Use its on-screen menu buttons.

------------------------------------------------------------------------

### Elimination order

| Step | Check | What a pass rules out |
|----|----|----|
| 1 | `cat /sys/class/drm/card*-*/status` says `connected` | Cable unplugged, monitor unpowered |
| 2 | Mutter’s `GetCurrentState` puts the connector in a logical monitor | GNOME leaving it out of the layout (Symptom 2) |
| 3 | `dpms=On enabled=enabled` in sysfs | The output being switched off |
| 4 | Still blank at 1920x1080 | A cable or port that cannot carry 4K at 60 Hz |
| 5 | `ddcutil` gets an answer from it | The monitor listening on another input (Symptom 3) |
| 6 | Swap cables with a working twin | Isolates the cable, the card’s port, or the monitor’s input |

If the screen comes back after a refresh-rate change, skip the table: it is Symptom 1.

------------------------------------------------------------------------

### Clearing stale layouts

``` bash
cp ~/.config/monitors.xml ~/.config/monitors.xml.bak-$(date +%F)
rm ~/.config/monitors.xml
# log out and back in, then arrange the screens once in Settings -> Displays
```

Log out straight after deleting. While the session runs, Mutter holds every stored layout in memory and writes them all back on the next save.

------------------------------------------------------------------------

Back to top
