"""ExitSimulator: a dependency-free cross-platform exit window."""

from __future__ import annotations

import shutil
import subprocess
import sys


APP_NAME = "ExitSimulator"
INSTRUCTION = "Click the button below to exit."
MESSAGE = "ExitSimulator is eating a hamburger now and will exit immediately."
DEVNULL = {"stdout": subprocess.DEVNULL, "stderr": subprocess.DEVNULL}


def windows_powershell(script: str, *, wait: bool) -> int:
    command = ["powershell", "-NoProfile", "-Command", script]
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    if wait:
        return subprocess.run(command, creationflags=flags, check=False).returncode
    subprocess.Popen(command, creationflags=flags, **DEVNULL)
    return 0


def show_window() -> bool:
    """Show the small native window and report whether Exit was clicked."""
    if sys.platform == "win32":
        return windows_powershell(
            "Add-Type -AssemblyName System.Windows.Forms;"
            "$f=New-Object System.Windows.Forms.Form;"
            "$f.Text='ExitSimulator';"
            "$f.ClientSize=New-Object System.Drawing.Size(300,150);"
            "$f.StartPosition='CenterScreen';"
            "$f.FormBorderStyle='FixedDialog';"
            "$f.MaximizeBox=$false;"
            "$f.ShowIcon=$false;"
            "$l=New-Object System.Windows.Forms.Label;"
            "$l.Text='Click the button below to exit.';"
            "$l.TextAlign='MiddleCenter';"
            "$l.Size=New-Object System.Drawing.Size(240,20);"
            "$l.Location=New-Object System.Drawing.Point(30,38);"
            "$b=New-Object System.Windows.Forms.Button;"
            "$b.Text='Exit';"
            "$b.Size=New-Object System.Drawing.Size(100,36);"
            "$b.Location=New-Object System.Drawing.Point(100,76);"
            "$clicked=$false;"
            "$b.Add_Click({$script:clicked=$true;$f.Close()});"
            "$f.Controls.Add($l);"
            "$f.Controls.Add($b);"
            "$f.AcceptButton=$b;"
            "[void]$f.ShowDialog();"
            "if($clicked){exit 0}else{exit 1}",
            wait=True,
        ) == 0

    if sys.platform == "darwin":
        swift = shutil.which("swift")
        if not swift:
            return False
        script = """
import AppKit
import Darwin

final class AppDelegate: NSObject, NSApplicationDelegate, NSWindowDelegate {
    var window: NSWindow!
    var clicked = false

    func applicationDidFinishLaunching(_ notification: Notification) {
        window = NSWindow(
            contentRect: NSRect(x: 0, y: 0, width: 300, height: 150),
            styleMask: [.titled, .closable, .miniaturizable],
            backing: .buffered,
            defer: false
        )
        window.title = "ExitSimulator"
        window.delegate = self

        let label = NSTextField(labelWithString: "Click the button below to exit.")
        label.frame = NSRect(x: 30, y: 88, width: 240, height: 18)
        label.alignment = .center
        label.font = NSFont.systemFont(ofSize: 12)

        let button = NSButton(
            title: "Exit",
            target: self,
            action: #selector(exitClicked(_:))
        )
        button.frame = NSRect(x: 100, y: 42, width: 100, height: 32)

        window.contentView?.addSubview(label)
        window.contentView?.addSubview(button)
        window.center()
        window.makeKeyAndOrderFront(nil)
        NSApp.activate(ignoringOtherApps: true)
    }

    @objc func exitClicked(_ sender: Any?) {
        clicked = true
        Darwin.exit(0)
    }

    func windowWillClose(_ notification: Notification) {
        if !clicked { Darwin.exit(1) }
    }

    func applicationShouldTerminate(
        _ sender: NSApplication
    ) -> NSApplication.TerminateReply {
        Darwin.exit(clicked ? 0 : 1)
    }
}

let app = NSApplication.shared
app.setActivationPolicy(.regular)
let delegate = AppDelegate()
app.delegate = delegate
app.run()
"""
        return subprocess.run([swift, "-e", script], check=False, **DEVNULL).returncode == 0

    if sys.platform.startswith("linux"):
        if shutil.which("xmessage"):
            command = [
                "xmessage", "-center", "-geometry", "300x150",
                "-buttons", "Exit:0", "-default", "Exit", INSTRUCTION,
            ]
        elif shutil.which("zenity"):
            command = [
                "zenity", "--question", f"--title={APP_NAME}",
                f"--text={INSTRUCTION}", "--ok-label=Exit",
                "--cancel-label=Cancel", "--width=300", "--height=150",
            ]
        else:
            raise RuntimeError("Linux requires xmessage or zenity to show the window.")
        return subprocess.run(command, check=False, **DEVNULL).returncode == 0

    raise RuntimeError(f"Unsupported operating system: {sys.platform}")


def notify() -> None:
    """Start an English error notification without delaying application exit."""
    try:
        if sys.platform == "win32":
            windows_powershell(
                "Add-Type -AssemblyName System.Windows.Forms;"
                "$n=New-Object System.Windows.Forms.NotifyIcon;"
                "$n.Icon=[System.Drawing.SystemIcons]::Error;"
                "$n.BalloonTipTitle='ExitSimulator';"
                "$n.BalloonTipText='ExitSimulator is eating a hamburger now and will exit immediately.';"
                "$n.BalloonTipIcon='Error';"
                "$n.Visible=$true;"
                "$n.ShowBalloonTip(4000);"
                "Start-Sleep -Seconds 4;"
                "$n.Dispose()",
                wait=False,
            )
        elif sys.platform == "darwin":
            swift = shutil.which("swift")
            if not swift:
                return
            script = f'''import AppKit
let app = NSApplication.shared
app.setActivationPolicy(.accessory)
app.activate(ignoringOtherApps: true)
let alert = NSAlert()
alert.alertStyle = .critical
alert.messageText = "{APP_NAME}"
alert.informativeText = "{MESSAGE}"
alert.addButton(withTitle: "OK")
alert.runModal()
'''
            subprocess.Popen([swift, "-e", script], **DEVNULL)
        elif sys.platform.startswith("linux"):
            subprocess.Popen(
                [
                    "notify-send", f"--app-name={APP_NAME}",
                    "--urgency=critical", "--icon=dialog-error",
                    APP_NAME, MESSAGE,
                ],
                **DEVNULL,
            )
    except OSError:
        pass


def main() -> None:
    if show_window():
        notify()


if __name__ == "__main__":
    main()
