#!/usr/bin/env python3
"""Plot the exact critical-ring stiffness and gap; no fitted data are used."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from check_critical_ising import expected_stiffness_spectrum


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parents[1] /
                        "figures" / "critical_stiffness.svg")
    parser.add_argument("--preview", type=Path,
                        help="Optional PNG preview path.")
    args = parser.parse_args()
    sizes = np.unique(np.rint(np.geomspace(4, 1024, 260)).astype(int))
    magnetizations = 1.0 / (sizes * np.sin(np.pi / (2.0 * sizes)))
    stiffness = np.array([expected_stiffness_spectrum(float(m))[0]
                          for m in magnetizations])
    gaps = 2.0 * np.tan(np.pi / (4.0 * sizes))
    limit = float(expected_stiffness_spectrum(2.0 / np.pi)[0])
    # Formula and finite-Hamiltonian comparison are implemented in the
    # canonical check_critical_ising.py. This plot imports its stiffness map.
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "font.size": 11,
        "axes.spines.top": False, "axes.spines.right": False,
        "svg.hashsalt": "qet-critical-stiffness",
    })
    fig, ax = plt.subplots(figsize=(8.2, 4.6), layout="constrained")
    ax.plot(sizes, stiffness, color="#82374b", linewidth=2.6,
            label=r"Local stiffness $\kappa_B/J$")
    ax.plot(sizes, gaps, color="#276987", linewidth=2.6,
            label=r"Bulk gap $\Delta_N/J$")
    ax.axhline(limit, color="#82374b", linewidth=1.0,
               linestyle=(0, (4, 4)), alpha=0.6)
    ax.text(35, limit + 0.012, r"$\kappa_\infty/J = 0.37125\ldots$",
            color="#82374b", fontsize=10)
    ax.set_xscale("log", base=2)
    ax.set_xticks([4, 16, 64, 256, 1024])
    ax.set_xticklabels(["4", "16", "64", "256", "1024"])
    ax.set_xlim(4, 1024)
    ax.set_ylim(0, 0.54)
    ax.set_xlabel("Number of spins, N")
    ax.set_ylabel("Energy in units of J")
    ax.set_title("Local excitation stiffness stays finite at criticality",
                 loc="left", fontsize=13, pad=14)
    ax.grid(axis="y", color="#e2e5e8", linewidth=0.7)
    ax.set_axisbelow(True)
    ax.legend(loc="upper right", frameon=False)
    fig.text(0.018, -0.045,
             "Periodic critical Ising chain; one-site receiver; "
             "stiffness includes all complex local operators.",
             fontsize=9, color="#4d5359")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.output, format="svg", bbox_inches="tight",
                facecolor="white", metadata={"Date": None,
                "Description": "Exact formulas from science/local_stiffness.md"})
    if args.preview:
        args.preview.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(args.preview, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(args.output)


if __name__ == "__main__":
    main()
