# Planck Spectral Energy Density

This project calculates and plots Planck's spectral energy density law for
3000 K, 4000 K, and 5000 K.

For the full student-facing explanation, setup guide, requirement checklist,
and physics interpretation, see `STUDENT_PROJECT_DOCUMENTATION.md`.

## Install dependencies

```bash
.venv/bin/python -m pip install -r requirements.txt
```

## Run the script

```bash
.venv/bin/python planck_spectral_energy_density.py
```

The script saves the graph as:

```text
planck_spectral_energy_density.png
```

## Optional: view the output in a browser

This project does not require a server. If you still want to view the saved
plot in a browser, run:

```bash
python3 -m http.server 8000
```

Then open:

```text
http://localhost:8000/
```
