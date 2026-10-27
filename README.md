# 🏎️ NEW ERA TYPING RACER

### An Interactive Typing Speed Game Using Python

## About the Project

NEW ERA TYPING RACER is a Python desktop application that makes typing practice more fun by turning it into a car race.

The idea is simple: instead of only typing sentences and checking your speed, you compete against a computer-controlled car. As you type the sentence shown on the screen, your car moves towards the finish line. The game also tracks typing speed and accuracy so you can review your performance after a race.

I created this project as part of my Python learning journey to practise GUI development, keyboard event handling, calculations, and data visualization.

## ✨ Features

- **Player vs CPU:** Race against a computer-controlled car.
- **Typing challenge:** Type the sentence displayed on the screen.
- **Racing track:** Watch the cars move towards the finish line.
- **Typing speed:** Calculate typing speed in words per minute (WPM).
- **Accuracy tracking:** Measure typing accuracy.
- **Live statistics:** View your performance during the race.
- **Performance graph:** Visualize typing-speed results using Matplotlib.
- **Restart option:** Start another race and practise again.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Tkinter | Creates the graphical user interface |
| NumPy | Supports numerical data handling |
| Matplotlib | Displays the performance graph |
| `random` | Selects typing sentences |
| `time` | Tracks elapsed time and typing speed |

## 📋 Requirements

- Python 3.10 or a compatible newer version
- Tkinter (usually included with Python on Windows)
- NumPy
- Matplotlib

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/kushagrakushh02/new-era-typing-racer.git
```

If your repository has a different name, replace the URL with your repository's HTTPS URL.

### 2. Open the project folder

```bash
cd new-era-typing-racer
```

### 3. Install the required libraries

```bash
python -m pip install numpy matplotlib
```

### 4. Run the application

If the main Python file is named `typing_racer.py`, run:

```bash
python typing_racer.py
```

If your Python file has a different name, use that filename instead.

## 🎮 How to Play

1. Run the Python application.
2. Read the sentence displayed on the screen.
3. Click **Start Race** to begin.
4. Type the sentence in the typing box.
5. Watch your car move as you make progress.
6. Try to reach the finish line before the CPU car.
7. Review your typing speed, accuracy, time, and score.
8. Use the new-race option to practise again.

## ⚙️ How It Works

1. The game selects a sentence for the player to type.
2. The application reads the player's keyboard input.
3. Typing progress is used to move the player's car along the track.
4. The CPU car moves automatically during the race.
5. The program updates statistics such as WPM, accuracy, elapsed time, and score.
6. When the race ends, a result message is displayed.
7. The performance graph can be used to compare recorded WPM results across races.

## 📈 Typing Speed Calculation

The game uses this formula to calculate words per minute (WPM):

`WPM = (Correct Characters / 5) / Time in Minutes`

Typing accuracy is calculated as:

`Accuracy (%) = (Correct Characters / Total Characters Typed) × 100`

These measurements give the player a simple way to check typing speed and accuracy.

## 📂 Project Structure

```text
new-era-typing-racer/
├── typing_racer.py
├── README.md
└── screenshots/
    ├── game-interface.png
    ├── gameplay.png
    ├── race-result.png
    └── typing-performance.png
```

This is a suggested structure. Keep the filenames in the README consistent with the files you actually upload.

## 🖼️ Screenshots

The screenshots below show the main screen, an active race, the result popup, and the typing-speed graph.

### Game Interface
![Game Interface](screenshots/game-interface.png)

### Gameplay
![Gameplay](screenshots/gameplay.png)

### Race Result
![Race Result](screenshots/race-result.png)

### Typing Speed Performance
![Typing Speed Performance](screenshots/typing-performance.png)

**Note:** Upload the four image files to the `screenshots` folder using these exact filenames, or update the image paths above to match your own filenames.

## 🎯 What I Learned

While building this project, I practised:

- Organizing Python code with a class and methods.
- Creating a desktop interface using Tkinter.
- Handling keyboard input and button events.
- Calculating typing speed and accuracy.
- Moving objects on a canvas.
- Displaying a graph with Matplotlib.
- Writing documentation for a GitHub project.

## 🔮 Future Improvements

Some features I may add in future versions are:

- Different difficulty levels.
- A countdown before each race.
- Saving previous results and personal best scores.
- More typing sentences and challenges.
- Improved car designs and animations.
- A leaderboard for comparing scores.

## 🎓 Academic Information

- **Project:** NEW ERA TYPING RACER
- **Submitted by:** Kushagra
- **UID:** 26MCC20027
- **Program:** MCA CC & DevOps
- **Semester:** I
- **University:** Chandigarh University, Mohali
- **Academic session:** 2026–2027

## 📚 References

- [Python Documentation](https://docs.python.org/3/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [NumPy Documentation](https://numpy.org/doc/)
- [Matplotlib Documentation](https://matplotlib.org/stable/)

---

**Built with Python 🐍**

*Learn, Type, Race, Improve!*
