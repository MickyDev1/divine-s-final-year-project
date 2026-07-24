"""Compute and plot Planck's spectral energy density law.

The calculation uses SI units:
- wavelength is converted from nanometers to meters
- temperature is measured in kelvin
- u(lambda, T) is returned in J m^-4
"""

from pathlib import Path

import matplotlib.pyplot as plt  # type: ignore[reportUnknownMemberType]
import numpy as np
from numpy.typing import NDArray


# Physical constants in SI units.
PROJECT_DIR = Path(__file__).resolve().parent
PLANCK_CONSTANT = 6.62607015e-34  # J s
SPEED_OF_LIGHT = 2.99792458e8  # m/s
BOLTZMANN_CONSTANT = 1.380649e-23  # J/K


def planck_spectral_energy_density(
    wavelength_m: NDArray[np.float64], temperature_k: float
) -> NDArray[np.float64]:
    """Calculate spectral energy density using Planck's radiation law."""
    exponent = (
        PLANCK_CONSTANT
        * SPEED_OF_LIGHT
        / (wavelength_m * BOLTZMANN_CONSTANT * temperature_k)
    )

    # np.expm1(exponent) is more accurate than np.exp(exponent) - 1.
    denominator = np.expm1(exponent)

    numerator = 8 * np.pi * PLANCK_CONSTANT * SPEED_OF_LIGHT
    return (numerator / wavelength_m**5) / denominator


def main() -> None:
    """Create the plot and save it as a PNG image."""
    # Wavelength range: 100 nm to 3000 nm.
    wavelength_nm = np.linspace(100, 3000, 2000)

    # Convert wavelength from nanometers to meters for the calculation.
    wavelength_m = wavelength_nm * 1e-9

    # Temperatures to plot.
    temperatures_k = [3000, 4000, 5000]

    plt.figure(figsize=(10, 6))  # type: ignore[reportUnknownMemberType]

    # Calculate and plot one curve for each temperature.
    for temperature_k in temperatures_k:
        u_lambda = planck_spectral_energy_density(wavelength_m, temperature_k)
        plt.plot(wavelength_nm, u_lambda, linewidth=2, label=f"{temperature_k} K")  # type: ignore[reportUnknownMemberType]

    plt.title("Planck Spectral Energy Density vs Wavelength")  # type: ignore[reportUnknownMemberType]
    plt.xlabel("Wavelength, lambda (nm)")  # type: ignore[reportUnknownMemberType]
    plt.ylabel("Spectral energy density, u(lambda, T) (J m^-4)")  # type: ignore[reportUnknownMemberType]
    plt.legend()  # type: ignore[reportUnknownMemberType]
    plt.grid(True, alpha=0.35)  # type: ignore[reportUnknownMemberType]
    plt.tight_layout()  # type: ignore[reportUnknownMemberType]

    output_path = PROJECT_DIR / "planck_spectral_energy_density.png"
    plt.savefig(output_path, dpi=300)  # type: ignore[reportUnknownMemberType]
    print(f"Plot saved as {output_path}")


if __name__ == "__main__":
    main()
