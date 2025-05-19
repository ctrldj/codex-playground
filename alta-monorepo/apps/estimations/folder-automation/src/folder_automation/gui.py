"""## In one sentence, what this file does
Provides a basic Tkinter GUI for the job folder automation tool.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox

from .main import create_job_structure


def run_gui() -> None:
    """Launch the graphical interface for creating job folders."""

    root = tk.Tk()
    root.title("Folder Automation")

    tk.Label(root, text="Client Name").grid(row=0, column=0, padx=5, pady=5)
    client_entry = tk.Entry(root, width=40)
    client_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text="Job Name").grid(row=1, column=0, padx=5, pady=5)
    job_entry = tk.Entry(root, width=40)
    job_entry.grid(row=1, column=1, padx=5, pady=5)

    def on_create() -> None:
        client = client_entry.get().strip()
        job = job_entry.get().strip()
        if not client or not job:
            messagebox.showerror("Error", "Please enter both client and job names")
            return

        files = create_job_structure(client, job)
        if files:
            messagebox.showinfo(
                "Success", f"Created job folder with {len(files)} files"
            )
        else:
            messagebox.showinfo(
                "Info", "No new files were created (they may already exist)."
            )

    tk.Button(root, text="Create Job Folder", command=on_create).grid(
        row=2, column=0, columnspan=2, pady=10
    )

    root.mainloop()


if __name__ == "__main__":  # pragma: no cover - manual execution only
    run_gui()
