import tkinter as tk
from tkinter import messagebox
import random, time
import numpy as np
import matplotlib.pyplot as plt


class TypingRacer:
    def __init__(self, root):
        self.root = root
        root.title("NEW ERA TYPING RACER")
        root.geometry("850x590")
        root.configure(bg="#101522")

        self.sentences = [
            "Python is simple and powerful",
            "Practice makes typing faster",
            "Programming is a useful skill",
            "Accuracy is important for typing"
        ]
        self.history = []
        self.running = False
        self.build_ui()

    def build_ui(self):
        tk.Label(self.root, text="NEW ERA TYPING RACER",
                 font=("Arial", 22, "bold"),
                 bg="#101522", fg="white").pack(pady=12)

        stats = tk.Frame(self.root, bg="#101522")
        stats.pack()
        self.labels = {}
        for name in ["WPM", "Accuracy", "Time", "Score"]:
            self.labels[name] = tk.Label(
                stats, text=f"{name}: 0",
                font=("Arial", 12, "bold"),
                bg="#202b3c", fg="#66e3ff", width=15, pady=8
            )
            self.labels[name].pack(side="left", padx=4)

        self.track = tk.Canvas(
            self.root, width=810, height=180,
            bg="#252e3d", highlightthickness=0
        )
        self.track.pack(pady=15)

        self.track.create_rectangle(
            15, 30, 795, 155, fill="#414957", outline=""
        )
        self.track.create_line(15, 35, 795, 35, fill="white", width=3)
        self.track.create_line(15, 150, 795, 150, fill="white", width=3)

        for x in range(80, 780, 50):
            self.track.create_line(x, 92, x + 25, 92,
                                   fill="#d4d9e0", width=2)

        # Checkered finish and start line
        for r in range(8):
            for c in range(2):
                color = "white" if (r + c) % 2 == 0 else "#111111"
                self.track.create_rectangle(
                    45 + c * 9, 36 + r * 14,
                    54 + c * 9, 50 + r * 14,
                    fill=color, outline=""
                )

        self.track.create_line(780, 35, 780, 150,
                               fill="#38e8a5", width=4)
        self.track.create_text(60, 18, text="FINISH", fill="white")
        self.track.create_text(755, 18, text="START",
                               fill="#38e8a5")

        self.player = self.car(735, 65, "#36d7ff")
        self.cpu = self.car(735, 120, "#ff6b6b")

        self.target = tk.Label(
            self.root, text="Press START to begin",
            font=("Arial", 14, "bold"),
            bg="#101522", fg="#66e3ff"
        )
        self.target.pack(pady=5)

        self.entry = tk.Entry(
            self.root, font=("Consolas", 15),
            justify="center"
        )
        self.entry.pack(fill="x", padx=30, pady=8)
        self.entry.bind("<KeyRelease>", self.typing)

        self.bar = tk.Canvas(self.root, height=10,
                             bg="#303746", highlightthickness=0)
        self.bar.pack(fill="x", padx=30)

        self.status = tk.Label(
            self.root, text="Ready to race!",
            bg="#101522", fg="white"
        )
        self.status.pack(pady=7)

        buttons = tk.Frame(self.root, bg="#101522")
        buttons.pack(pady=5)
        for name, command in [
            ("START RACE", self.start),
            ("NEW RACE", self.reset),
            ("PERFORMANCE", self.graph),
            ("EXIT", self.root.destroy)
        ]:
            tk.Button(buttons, text=name, command=command,
                      width=13).pack(side="left", padx=4)

    def car(self, x, y, color):
        body = self.track.create_rectangle(
            x-22, y-8, x+22, y+8,
            fill=color, outline="white"
        )
        roof = self.track.create_rectangle(
            x-10, y-14, x+12, y-8,
            fill=color, outline="white"
        )
        wheels = [
            self.track.create_oval(x-16, y+5, x-7, y+14,
                                   fill="black"),
            self.track.create_oval(x+9, y+5, x+18, y+14,
                                   fill="black")
        ]
        return [body, roof] + wheels

    def move_car(self, car, x):
        current = self.track.coords(car[0])[0] + 22
        for part in car:
            self.track.move(part, x-current, 0)

    def start(self):
        if self.running:
            return
        self.reset()
        self.running = True
        self.target.config(text=random.choice(self.sentences))
        self.start_time = time.time()
        self.status.config(text="GO! Type the sentence.")
        self.entry.focus_set()
        self.cpu_move()
        self.update_stats()

    def typing(self, event=None):
        if not self.running:
            return

        typed = self.entry.get()
        target = self.target.cget("text")
        correct = sum(a == b for a, b in zip(typed, target))
        errors = len(typed) - correct
        self.correct, self.errors = correct, errors

        progress = min(len(typed) / len(target), 1)
        self.move_car(self.player, 735 - 660 * progress)

        self.bar.delete("all")
        self.bar.create_rectangle(
            0, 0, self.bar.winfo_width() * progress, 10,
            fill="#36d7ff", outline=""
        )

        if typed == target:
            self.finish("YOU WIN!")

    def cpu_move(self):
        if not self.running:
            return
        x = self.track.coords(self.cpu[0])[0] + 22
        if x <= 75:
            self.finish("CPU WINS!")
        else:
            self.move_car(self.cpu, x - 3)
            self.root.after(100, self.cpu_move)

    def update_stats(self):
        if not self.running:
            return
        elapsed = time.time() - self.start_time
        minutes = max(elapsed / 60, 0.001)
        wpm = self.correct / 5 / minutes
        total = self.correct + self.errors
        accuracy = 100 * self.correct / total if total else 100
        score = max(0, self.correct * 10 - self.errors * 5)

        values = [wpm, accuracy, elapsed, score]
        for name, value in zip(self.labels, values):
            suffix = "%" if name == "Accuracy" else (
                "s" if name == "Time" else "")
            self.labels[name].config(
                text=f"{name}: {value:.1f}{suffix}"
                if name != "Score" else f"Score: {score}"
            )
        self.root.after(200, self.update_stats)

    def finish(self, result):
        if not self.running:
            return
        self.running = False
        elapsed = time.time() - self.start_time
        wpm = self.correct / 5 / max(elapsed / 60, 0.001)
        total = self.correct + self.errors
        accuracy = 100 * self.correct / total if total else 100
        score = max(0, self.correct * 10 - self.errors * 5)
        self.history.append(wpm)
        self.status.config(text=result)
        messagebox.showinfo(
            "Race Result",
            f"{result}\nWPM: {wpm:.1f}\n"
            f"Accuracy: {accuracy:.1f}%\nScore: {score}"
        )

    def reset(self):
        self.running = False
        self.entry.delete(0, tk.END)
        self.target.config(text="Press START to begin")
        self.status.config(text="Ready to race!")
        self.move_car(self.player, 735)
        self.move_car(self.cpu, 735)
        self.bar.delete("all")
        for name in self.labels:
            self.labels[name].config(text=f"{name}: 0")

    def graph(self):
        if not self.history:
            messagebox.showinfo("Performance", "Complete a race first.")
            return
        data = np.array(self.history)
        plt.plot(range(1, len(data)+1), data, marker="o")
        plt.title("Typing Speed Performance")
        plt.xlabel("Race")
        plt.ylabel("WPM")
        plt.grid(True)
        plt.show()


root = tk.Tk()
game = TypingRacer(root)
root.mainloop()