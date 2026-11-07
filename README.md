# ExitSimulator

> A cross-platform reverse-productivity tool dedicated entirely to exiting.

## What Is This?

ExitSimulator is designed to help you pass the time.

Modern computers contain billions of transistors, multiple processor cores, and highly sophisticated graphics systems. Despite all this technology, users rarely get an opportunity to study an Exit button with the attention it deserves.

ExitSimulator corrects this oversight. It opens a small window containing a clear, stable, and carefully positioned **Exit** button. You may inspect its shape, color, edges, shadows, and relationship with the exact center of the window. When your research is complete, you may click it to confirm that an Exit button can, in fact, exit.

There are no points, leaderboards, achievements, hidden endings, or daily rewards. Nothing is included that might distract you from the important task of wasting time efficiently.

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/wangsiyuan24/ExitSimulator.git
cd ExitSimulator
```

### 2. Run the Program

On macOS or Linux:

```bash
python3 ExitSimulator.py
```

On Windows:

```powershell
python ExitSimulator.py
```

A small window named **ExitSimulator** will appear near the center of the screen. Above the button, the program presents a short but essential instruction:

> Click the button below to exit.

### 3. Move the Mouse Carefully

Move your mouse with precision until the pointer is positioned over the **Exit** button in the middle of the program window.

Using the close button in the upper-left or upper-right corner is not recommended. Those controls may also close the window, but they bypass the carefully engineered primary exit procedure. This reduces the ceremonial value of the operation and fails to demonstrate that you successfully located the button in the center.

### 4. Click Exit

If you finally decide to press the button, the program displays an English system message with an error icon:

> ExitSimulator is eating a hamburger now and will exit immediately.

ExitSimulator then terminates immediately. If you inspect the system process list afterward, you may notice that one mysterious application process has disappeared. This is not data loss or an operating-system failure. It is the observable result of a successful exit.

## Features

- Provides a real and fully clickable Exit button.
- Places the button in the center for convenient long-term observation.
- Displays a concise English instruction above the button.
- Exits immediately after the button is clicked, with no countdown or artificial delay.
- Shows an expanded English system message during the exit procedure.
- Uses an error icon to emphasize the successful completion of a process that is not actually an error.
- Contains no accounts, advertisements, in-app purchases, daily missions, or premium button skins.
- Does not increase in complexity after the user understands how exiting works.

## Platform Support

ExitSimulator supports the major desktop platforms and selects an appropriate native window and notification method for the current operating system.

| Platform | Window Implementation | Exit Message |
| --- | --- | --- |
| Windows | Windows Forms | Error-level system balloon |
| macOS | AppKit | Critical system alert |
| Linux | xmessage or Zenity | Desktop notification with an error icon |

Python 3 is required. macOS uses the system-provided Swift and AppKit tools. Linux requires `xmessage` or `zenity` for the window and uses `notify-send` for the notification. Windows uses the built-in PowerShell and Windows Forms components.

## Contributing

Contributions involving code, documentation, or rigorous research into exit behavior are welcome. Before submitting a change, verify that it preserves the following principles:

1. The window must remain small enough that it does not consume time intended to be wasted elsewhere.
2. The Exit button must be easy to find while remaining worthy of observation.
3. Clicking the button must exit immediately; the exit process must not become so entertaining that it refuses to finish.
4. Windows, macOS, and Linux users should have approximately equal access to the right to exit.

If the button successfully exits the program, this is generally not considered a defect. If the application decides to remain and continue spending time with you, please open an issue and include your operating system, Python version, and approximate button-observation duration.

## Project Goal

ExitSimulator does not attempt to improve productivity or promise a better life. It creates an Exit button and exits when you click it.

From a software-engineering perspective, this is considered feature-complete.

## License

ExitSimulator is released under the [Zero-Clause BSD License](LICENSE). You may use, copy, modify, and distribute the software for any purpose, with or without a fee.

Copyright (c) 2026 Wang Siyuan. See the [`LICENSE`](LICENSE) file for the complete license text and warranty disclaimer.
