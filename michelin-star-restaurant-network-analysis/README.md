# Michelin Network Analysis

This repository contains the code, data, and visualizations for a network analysis project on Michelin-starred restaurants. The goal of this project is to explore how restaurants are connected through shared cuisine types and to uncover structural patterns in the global fine dining ecosystem.

---

## Project Overview

The Michelin Guide evaluates restaurants individually, but this project treats the Michelin ecosystem as a network.

We construct a **bipartite network** where:
- One type of node represents **restaurants**
- The other type represents **cuisine categories**
- An edge connects a restaurant to each of its associated cuisines

This allows us to analyze:
- Which cuisines act as major hubs
- How restaurants cluster based on cuisine
- The overall structure and connectivity of the network

---

## Repository Structure


michelin-network-analysis/
│
├── data/
│ ├── raw/
│ │ └── michelin_my_maps.csv
│ └── processed/
│ ├── nodes.csv
│ └── edges.csv
│
├── code/
│ └── main.py
│
├── gephi/
│ └── Michelin1.gephi
│
├── figures/
│ ├── full_network.png
│ └── filtered_network.png
│
├── README.md
├── requirements.txt
└── .gitignore


---

## Data

The dataset is based on the Michelin Guide Restaurants dataset from Kaggle.

Relevant fields used:
- `Name` – restaurant name
- `Cuisine` – one or more cuisine categories
- `Location` – restaurant location
- `Award` – Michelin distinction

For this project:
- Bib Gourmand entries were removed
- Only Michelin-starred restaurants were retained
- Missing values were dropped

---

## Code

The script `code/main.py` constructs the network and outputs files for visualization.

### What the script does:

1. Loads the raw Michelin dataset
2. Removes Bib Gourmand entries
3. Selects relevant columns
4. Splits cuisine strings into lists
5. Creates:
   - Restaurant nodes
   - Cuisine nodes
6. Builds edges between restaurants and cuisines
7. Exports:
   - `nodes.csv`
   - `edges.csv`

These files are used directly in Gephi for visualization.

---

## Visualization

The processed data is visualized using **Gephi**.

Two main visualizations were created:

### 1. Full Network Visualization
- Displays the entire bipartite network
- Node size represents degree (connectivity)
- Highlights major cuisine hubs (e.g., Modern, Contemporary)

### 2. Filtered Network Visualization
- Removes low-degree nodes to reduce noise
- Uses modularity to highlight communities
- Provides a clearer view of core structure

The Gephi project file is included:

gephi/Michelin1.gephi


---

## How to Run

### 1. Install dependencies


pip install -r requirements.txt


### 2. Place dataset

Make sure the raw dataset is located at:


data/raw/michelin_my_maps.csv


### 3. Run the script


python code/main.py


### 4. Output

The following files will be generated:


data/processed/nodes.csv
data/processed/edges.csv


---

## Tools Used

- Python
- pandas
- Gephi

---

## Key Insights

- The network is highly structured and dominated by a few cuisine hubs
- Modern, Contemporary, and Creative cuisine connect large portions of the network
- The network exhibits strong clustering and short path lengths
- The structure is **disassortative**, meaning high-degree cuisine nodes connect to many low-degree restaurant nodes

---

## Notes

This repository is designed to support reproducibility of the project results. All data processing, network construction, and visualization steps are documented and organized for clarity.

---

## Author

Created as part of a CPSC 572 Network Science course project.
