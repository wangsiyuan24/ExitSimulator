"""ExitSimulator: a tiny exit window for Windows and macOS."""

from __future__ import annotations

import ctypes
import shutil
import subprocess
import sys

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError as error:
    print(
        "ExitSimulator requires Python 3 with the standard Tkinter module.",
        file=sys.stderr,
    )
    raise SystemExit(1) from error


APP_NAME = "ExitSimulator"
INSTRUCTION = "Click the button below to exit."
MESSAGE = "ExitSimulator is eating a hamburger now and will exit immediately."
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 150


def enable_windows_dpi_awareness() -> None:
    if sys.platform != "win32":
        return

    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except (AttributeError, OSError):
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except (AttributeError, OSError):
            pass


def configure_system_theme(window: tk.Tk) -> ttk.Style:
    style = ttk.Style(window)
    themes = set(style.theme_names())
    preferred = ("vista", "xpnative", "winnative") if sys.platform == "win32" else ("aqua",)

    for theme in preferred:
        if theme in themes:
            style.theme_use(theme)
            break

    return style


def center_window(window: tk.Tk) -> None:
    window.update_idletasks()
    x = max(0, (window.winfo_screenwidth() - WINDOW_WIDTH) // 2)
    y = max(0, (window.winfo_screenheight() - WINDOW_HEIGHT) // 2)
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")


def windows_notification_command() -> list[str]:
    powershell = shutil.which("powershell") or shutil.which("powershell.exe")
    if powershell is None:
        raise RuntimeError("Windows PowerShell is required to show the system notification.")

    script = (
        "Add-Type -AssemblyName System.Windows.Forms;"
        "$n=New-Object System.Windows.Forms.NotifyIcon;"
        "$n.Icon=[System.Drawing.SystemIcons]::Error;"
        "$n.BalloonTipTitle='ExitSimulator';"
        "$n.BalloonTipText='ExitSimulator is eating a hamburger now and will exit immediately.';"
        "$n.BalloonTipIcon='Error';"
        "$n.Visible=$true;"
        "$n.ShowBalloonTip(4000);"
        "Start-Sleep -Seconds 4;"
        "$n.Dispose()"
    )
    return [powershell, "-NoProfile", "-Command", script]


def macos_notification_command() -> list[str]:
    osascript = "/usr/bin/osascript"
    script = (
        "const app=Application.currentApplication();"
        "app.includeStandardAdditions=true;"
        f"app.displayAlert('{APP_NAME}',{{message:'{MESSAGE}',"
        "as:'critical',buttons:['OK'],defaultButton:'OK'});"
    )
    return [osascript, "-l", "JavaScript", "-e", script]


def show_system_notification() -> None:
    if sys.platform == "win32":
        command = windows_notification_command()
        creation_flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    elif sys.platform == "darwin":
        command = macos_notification_command()
        creation_flags = 0
    else:
        raise RuntimeError("ExitSimulator supports only Windows and macOS.")

    subprocess.Popen(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=creation_flags,
    )


def create_window() -> tk.Tk:
    window = tk.Tk()
    window.title(APP_NAME)
    window.resizable(False, False)
    configure_system_theme(window)

    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)

    content = ttk.Frame(window, padding=20)
    content.grid(row=0, column=0, sticky="nsew")
    content.columnconfigure(0, weight=1)
    content.rowconfigure(0, weight=1)
    content.rowconfigure(3, weight=1)

    label = ttk.Label(content, text=INSTRUCTION, anchor="center")
    label.grid(row=1, column=0, sticky="ew", pady=(0, 12))

    def exit_clicked() -> None:
        try:
            show_system_notification()
        except (OSError, RuntimeError) as error:
            print(f"{APP_NAME} notification error: {error}", file=sys.stderr)
        window.destroy()

    button = ttk.Button(content, text="Exit", command=exit_clicked)
    button.grid(row=2, column=0)

    center_window(window)
    return window


def main() -> int:
    if sys.platform not in {"win32", "darwin"}:
        print("ExitSimulator supports only Windows and macOS.", file=sys.stderr)
        return 1

    enable_windows_dpi_awareness()
    try:
        window = create_window()
        window.mainloop()
    except tk.TclError as error:
        print(f"{APP_NAME} GUI error: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
