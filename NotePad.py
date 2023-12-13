import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import os

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad")

        self.note_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        self.note_text.pack(pady=10)

        add_note_button = tk.Button(root, text="Add Note", command=self.add_note)
        add_note_button.pack(side=tk.LEFT, padx=5)

        show_notes_button = tk.Button(root, text="Show Notes", command=self.show_notes)
        show_notes_button.pack(side=tk.LEFT, padx=5)

        quit_button = tk.Button(root, text="Quit", command=root.destroy)
        quit_button.pack(side=tk.RIGHT, padx=5)

    def add_note(self):
        note = self.note_text.get("1.0", tk.END)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"note_{timestamp}.txt"

        with open(filename, "w") as file:
            file.write(note)

        print(f"Note added and saved to {filename}")

    def show_notes(self):
        saved_notes = []
        for file_name in os.listdir():
            if file_name.startswith("note_") and file_name.endswith(".txt"):
                with open(file_name, "r") as file:
                    note_content = file.read()
                    saved_notes.append((file_name, note_content))

        if saved_notes:
            print("Showing saved notes:")
            for note in saved_notes:
                print(f"{note[0]}:\n{note[1]}\n{'=' * 30}")
        else:
            print("No saved notes found.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
