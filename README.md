 # TP53 Genomic Mutation Analysis

## Project Overview

This project analyzes mutation patterns in the TP53 gene using a structured genomic dataset.
TP53 is a critical tumor suppressor gene, and its mutations are widely studied in cancer genomics.

The goal of this project is to:

* Process raw mutation data
* Extract TP53-specific records
* Analyze mutation types
* Generate basic insights and visualizations

---

##  Dataset

* Source: Google Sheets dataset (converted to CSV)
* Format: Mutation Annotation Format (MAF-like)
* Total TP53 records: 344

### Key Columns Used:

* `Hugo_Symbol` → Gene name
* `Variant_Classification` → Type of mutation
* `Tumor_Sample_Barcode` → Sample identifier

---

## Workflow

### 1. Data Processing (`process.py`)

* Loaded raw dataset
* Cleaned column names
* Filtered TP53 mutations
* Saved processed dataset

### 2. Data Analysis (`analysis.py`)

* Calculated mutation frequency
* Analyzed mutation type distribution
* Generated bar plot visualization
* Saved results to file

---

##  Results

### Mutation Frequency

* TP53 Mutation Frequency: **100%** (dataset contains only TP53 records)

### Mutation Type Distribution

* Distribution of mutation types such as:

  * Missense Mutation
  * Nonsense Mutation
  * Frame Shift Deletion
  * Others

### Visualization

* Bar chart showing mutation type frequencies
* Saved at: `results/figures/mutation_plot.png`

---

##  Project Structure

```
tp53_genomic_study/
├── data/
│   ├── raw/data.csv
│   └── processed/tp53_data.csv
├── script/
│   ├── process.py
│   └── analysis.py
├── results/
│   ├── results.txt
│   └── figures/mutation_plot.png
└── README.md
```

---

##  How to Run

```bash
cd script
python3 process.py
python3 analysis.py
```

---

##  Tools & Technologies

* Python
* pandas
* matplotlib
* Linux (WSL)
* Git & GitHub



