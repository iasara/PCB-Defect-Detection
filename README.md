# Automated PCB Defect Detection Using Classical Image Processing Techniques

ARTI 403 - Image Processing | Group 2

College of Computer Science and Information Technology, Imam Abdulrahman Bin Faisal University

## Team

- Sarah Khalid Bahwal
- Sara Abdulaziz Al-Qatari
- Dina Moteb Almsnid
- Raghad Mohammed Alsheddi
- Hawra Habib Alali
- Danah Eid Aldossary

## About

This project detects open and short defects on PCB images using Python and OpenCV. Each test image is compared with its defect-free template, and the detected defects are marked with bounding boxes. No deep learning is used.

## Dataset

DeepPCB: https://github.com/tangsanli5201/DeepPCB (accessed 15 October 2026)

It has 1,500 image pairs, split into 1,000 for development and 500 for testing. The dataset is not uploaded here. The notebook downloads it in the first cells.

## Results

The selected configuration uses no filter, a fixed threshold of 50, no morphology, and a minimum contour area of 200 px². On the 500 test pairs it reached 6.01% precision, 10.11% recall, and 7.54% F1-score (IoU > 0.33).

## Files

All files are in the `Code` folder.

| File | Description |
|---|---|
| `PCB_Defect_Detection.ipynb` | Main notebook. It runs the full project in order: data loading, preprocessing, thresholding and morphology, contour detection, evaluation, and experiments |
| `data.ipynb` | Data loading part: train and test splits, images, and the open/short ground truth boxes |
| `preprocess.py` | Grayscale conversion, noise filtering, and template subtraction |
| `threshold.py` | Fixed, Otsu, and adaptive thresholding, with opening and closing |
| `threshold.ipynb` | Notebook version of the thresholding part, with example images |
| `detection.py` | Contour detection, minimum area filter, and bounding boxes |
| `Detection_BoundingBoxes.ipynb` | Notebook version of the detection part |
| `pipeline.py` | Connects preprocessing, thresholding, and detection |
| `Pipeline_Integration.ipynb` | Notebook version of the pipeline |
| `evaluate.py` | IoU matching, TP/FP/FN, Precision, Recall, and F1-score |
| `experiments.ipynb` | Ablation study on the development split and the final test run |

Other files in the repository:

| File | Description |
|---|---|
| `.gitignore` | Keeps the dataset folders out of the repository |
| `README.md` | This file |

## How to run

1. Open `Code/PCB_Defect_Detection.ipynb` in Google Colab.
2. Run all cells in order. The first cells download the dataset.
3. Section 6 runs the experiments on all development and test images, so it takes longer than the other sections.
