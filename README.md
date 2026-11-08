# ExitSimulator

> A cross-platform reverse-productivity tool dedicated entirely to exiting on Windows and macOS.

## What Is This?

ExitSimulator is designed to help you pass the time.

Modern computers contain billions of transistors, multiple processor cores, and highly sophisticated graphics systems. Despite all this technology, users rarely get an opportunity to study an Exit button with the attention it deserves.

ExitSimulator corrects this oversight. It opens a small window containing a clear, stable, and properly centered **Exit** button. You may inspect its shape, color, edges, system theme, and relationship with the exact center of the window. When your research is complete, you may click it to confirm that an Exit button can, in fact, exit.

There are no points, leaderboards, achievements, hidden endings, or daily rewards. Nothing is included that might distract you from the important task of wasting time efficiently.

## Requirements

- Windows or macOS
- Python 3 with the standard-library Tkinter module

Tkinter and ttk are part of a normal Python distribution. ExitSimulator does not use third-party GUI packages, and there is no `pip install` step. If `import tkinter` fails, use a Python distribution that includes its standard Tk support.

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/wangsiyuan24/ExitSimulator.git
cd ExitSimulator
```

### 2. Run on Windows

```powershell
python ExitSimulator.py
```

The interface uses ttk with the best available native Windows theme. Windows PowerShell and Windows Forms are used only by the background system notification.

### 3. Run on macOS

```bash
python3 ExitSimulator.py
```

The interface uses the Aqua ttk theme when it is available. The background critical alert is shown with the system-provided `osascript`.

## Move the Mouse Carefully

The window presents a short but essential instruction:

> Click the button below to exit.

Move the mouse with precision until the pointer is positioned over the **Exit** button in the middle of the window. Using the corner close control is not recommended. It may close the window, but it bypasses the carefully engineered primary exit procedure and proves only that ordinary windows can close.

Clicking **Exit** starts an error-style system alert containing:

> ExitSimulator is eating a hamburger now and will exit immediately.

The main program then exits immediately. The alert runs independently, so there is no countdown or artificial delay in the main process. If you inspect the process list afterward, you may notice that one mysterious application process has disappeared. This is not data loss. It is the observable result of a successful exit.

## Features

- Displays the original instruction label and Exit button.
- Uses ttk system themes, default fonts, and automatic button sizing.
- Uses `grid()` row and column weights instead of fixed button coordinates.
- Keeps the approximately 300 × 150 content area centered on screen.
- Supports Retina and Windows DPI scaling through native Tk metrics and Windows DPI awareness.
- Contains no accounts, advertisements, in-app purchases, daily missions, or premium button skins.

## Platform Support

| Platform | Interface | System Alert |
| --- | --- | --- |
| Windows | Tkinter/ttk with a native Windows theme | PowerShell and Windows Forms NotifyIcon |
| macOS | Tkinter/ttk with Aqua | `osascript` critical alert |

## Contributing

Contributions involving code, documentation, or rigorous research into exit behavior are welcome. Please preserve these principles:

1. The instruction label and Exit button must remain intact.
2. The controls must be centered by layout, not by spaces or guessed button coordinates.
3. Clicking Exit starts the system alert and closes the main program immediately.
4. Windows and macOS users retain approximately equal access to the right to exit.

If the button successfully exits the program, this is generally not considered a defect.

## License

ExitSimulator is released under the [Zero-Clause BSD License](LICENSE). You may use, copy, modify, and distribute the software for any purpose, with or without a fee.

Copyright (c) 2026 Wang Siyuan. See the [`LICENSE`](LICENSE) file for the complete license text and warranty disclaimer.
