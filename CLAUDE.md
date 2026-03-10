# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Credit card fraud detection project using the ULB credit card fraud dataset (284,807 European cardholder transactions). The `Class` column indicates fraud (1) vs normal (0).

## Setup & Running

- **Python version**: 3.14 (virtual environment in `fintechproject/`)
- **Activate venv (Windows)**: `source fintechproject/Scripts/activate` (Git Bash) or `fintechproject\Scripts\Activate.ps1` (PowerShell)
- **Activate venv (macOS/Linux)**: `source fintechproject/bin/activate`
- **Dataset**: Download `creditcard.csv` from Kaggle (not in repo, gitignored) and place in project root
- **Run EDA**: `python project.py` — loads data, prints shape/nulls/class distribution/stats
- **Run model**: `python model.py` — trains Random Forest classifier, prints confusion matrix and classification report
- `main.py` exists but is currently just a placeholder

## Key Files

- `project.py` — EDA script (data loading, shape/nulls/class distribution/stats)
- `model.py` — Random Forest fraud detection model (train/test split, evaluation metrics)
- `creditcard.csv` — Dataset (must be downloaded separately, ~150MB)
- `.gitignore` — Ignores `creditcard.csv`, `data/`, `models/`, `warehouse/`, `*.db`, `*.parquet`

## Dependencies

- `pandas`, `scikit-learn` (no requirements.txt yet)
