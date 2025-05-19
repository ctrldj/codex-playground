## In one sentence, what this file does
"""Tkinter-based user interface for creating job folders."""

from __future__ import annotations

import tkinter as tk
from pathlib import Path
from tkinter import messagebox

from .main import BASE_DIR, TEMPLATE_DIR, create_job_structure


def run_gui() -> None:
    """Launch the folder automation window."""

    root = tk.Tk()
    root.title("Folder Automation")

    # Input fields
    tk.Label(root, text="Client Name").grid(
        row=0,
        column=0,
        padx=10,
        pady=5,
        sticky="e",
    )
    client_entry = tk.Entry(root, width=30)
    client_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(root, text="Job Name").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    job_entry = tk.Entry(root, width=30)
    job_entry.grid(row=1, column=1, padx=10, pady=5)

    def on_create() -> None:
        """Handle the Create Job button click."""

        client = client_entry.get().strip()
        job = job_entry.get().strip()

        if not client or not job:
            messagebox.showerror("Input Error", "Please enter both client and job")
            return

        files = create_job_structure(client, job, BASE_DIR, TEMPLATE_DIR)

        msg_lines = [f"Created folder for {client}/{job}."]
        if files:
            msg_lines.extend(f"Copied {Path(f).name}" for f in files)
        else:
            msg_lines.append("No new files were created (they may already exist).")

        messagebox.showinfo("Success", "\n".join(msg_lines))

    # Trigger button
    create_btn = tk.Button(root, text="Create Job", command=on_create)
    create_btn.grid(row=2, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":  # pragma: no cover - manual execution only
    run_gui()
