# Simple Guitar Simulation 🎸

A Python-based guitar string simulation that produces realistic string vibration sounds using the Karplus-Strong algorithm and physical modeling synthesis.

## Features

- Simulates the vibration and sound of guitar strings
- Uses accurate frequency calculations for standard guitar tuning (E2, A2, D3, G3, B3, E4)
- Real-time audio playback through your system's audio output
- Simple and intuitive interface

## Requirements

- numpy
- pygame

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/guitar-simulation.git
cd guitar-simulation
```

2. Generate a virtual environment and install the packages:

```bash
python -m venv venv
# For Windows
.\venv\Scripts\activate
# For Linux/Mac
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python guitar.py
```
    Use the following keyboard keys to play different notes:
        q 2 w e 4 r 5 t y 7 u 8 i 9 o p - [ = ]
    
    Each key corresponds to a different frequency, following a chromatic scale where each note is 1.059463 times the frequency of the previous note, centered around A440 (A4 = 440 Hz).

    The simulation uses the Karplus-Strong algorithm to create realistic string vibration sounds, with each key triggering a different pitch based on this frequency relationship.
