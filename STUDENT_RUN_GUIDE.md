# Planck Radiation Project: Student Run Guide

## What This Project Does

This project uses Python to calculate and plot the spectral energy density of
blackbody radiation using Planck's radiation law:

```text
u(lambda, T) = (8*pi*h*c / lambda^5) * 1 / (exp(h*c / (lambda*k_B*T)) - 1)
```

The graph shows the curves for:

- 3000 K
- 4000 K
- 5000 K

The wavelength range is from 100 nm to 3000 nm.

## Files Included

- `planck_spectral_energy_density.py`
  - Main Python code.

- `requirements.txt`
  - Python packages needed to run the code.

- `planck_spectral_energy_density.png`
  - Example output graph.

- `index.html`
  - Optional browser page for viewing the graph.

- `README.md`
  - Short project instructions.

- `STUDENT_PROJECT_DOCUMENTATION.md`
  - Full detailed documentation explaining the project.

## Applications to Install

The student should install:

1. Python 3
2. Visual Studio Code, optional but recommended
3. VS Code Python extension, optional but recommended

To check if Python is installed:

```bash
python3 --version
```

On Windows, use:

```bash
python --version
```

## How to Run on macOS or Linux

Open Terminal inside the project folder and run:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python planck_spectral_energy_density.py
```

After running, the graph will be saved as:

```text
planck_spectral_energy_density.png
```

## How to Run on Windows

Open Command Prompt or PowerShell inside the project folder and run:

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python planck_spectral_energy_density.py
```

After running, the graph will be saved as:

```text
planck_spectral_energy_density.png
```

## Optional: View the Graph in a Browser

After generating the graph, run:

```bash
python3 -m http.server 8000
```

On Windows, use:

```bash
python -m http.server 8000
```

Then open this in a browser:

```text
http://localhost:8000/
```

## What the Graph Means

The graph shows that as temperature increases:

- the spectral energy density becomes higher
- the peak moves toward shorter wavelengths
- the 5000 K curve is highest
- the 3000 K curve is lowest

This agrees with blackbody radiation theory and Wien's displacement law.

## Common Problems

### Red lines under `numpy` or `matplotlib`

This usually means the Python packages were not installed in the selected
Python environment.

Run:

```bash
python -m pip install -r requirements.txt
```

If using VS Code, select the correct interpreter:

```text
Python: Select Interpreter
```

Then choose the `.venv` interpreter.

### pip upgrade warning

A pip upgrade warning is not an error. The project can still run.

### Browser says "Not Secure"

This is normal for `http://localhost:8000/`. It is only a local browser preview.

### `favicon.ico 404`

This is normal. The browser is asking for a tab icon, but the project does not
need one.
