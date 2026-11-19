# PCB-Defect-Detection
# Automated PCB Defect Detection Using Classical Image Processing Techniques

ARTI 403 - Image Processing | Group 2

College of Computer Science and Information Technology, Imam Abdulrahman Bin Faisal University

## Team

- Sarah Khalid Bahwal
- Sara Abdulaziz Al-Qatari
- Dina Moteb Almsnid
- Raghad Mohammed Alsheddi
- Hawra Habib Alali

## About

This project detects open and short defects on PCB images using Python and OpenCV. Each test image is compared with its defect-free template, and the detected defects are marked with bounding boxes. No deep learning is used.

## Dataset

DeepPCB: https://github.com/tangsanli5201/DeepPCB (accessed 15 October 2026)

It has 1,500 image pairs, split into 1,000 for training and 500 for testing. The dataset is not uploaded here. The notebook downloads it in the first cell.

## Files

| File | Description |
|---|---|
| `Code/data.ipynb` | Loads the DeepPCB train and test splits, the test and template images, and the open/short ground truth boxes. It also shows the dataset statistics and example images |
| `.gitignore` | Keeps the `DeepPCB` folder out of the repository |
| `README.md` | This file |
| `Code/evaluate.py` | Evaluates PCB defect detections by comparing predicted boxes with ground-truth boxes. It reports overall precision, recall, and F1-score, plus separate recall for Open and Short defects. |
## How to run

1. Open `Code/data.ipynb` in Google Colab.
2. Run all cells. The first cell downloads the dataset.
3. To try the evaluation module in Google Colab, open a new notebook, paste the code from `Code/evaluate.py` into a cell, and run it. The script prints example metrics using synthetic bounding boxes. These are not the final DeepPCB test results.
