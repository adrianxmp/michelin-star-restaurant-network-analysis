# Michelin Network Analysis

This repository contains the code, processed data, Gephi project files, and visualizations used for our project on Michelin-starred restaurants.

## Project Overview

The goal of this project is to analyze the structure of the Michelin-starred restaurant ecosystem using network analysis. We model the dataset as a bipartite network where:

- one node type represents restaurants
- the other node type represents cuisine categories
- an edge connects a restaurant to each of its associated cuisine types

This representation allows us to study cuisine hubs, clustering, community structure, and overall connectivity in the Michelin dining landscape.

## Repository Structure

```text
michelin-network-analysis/
│
├── data/
│   ├── raw/
│   │   └── michelin_my_maps.csv
│   └── processed/
│       ├── nodes.csv
│       └── edges.csv
│
├── code/
│   └── main.py
│
├── gephi/
│   └── Michelin1.gephi
│
├── figures/
│   ├── full_network.png
│   └── filtered_network.png
│
├── README.md
├── requirements.txt
└── .gitignore

## Data

The raw dataset was based on the Michelin Guide Restaurants dataset from Kaggle.

Relevant fields used in this project:

Name
Cuisine
Location
Award

For this analysis, Bib Gourmand entries were removed and only Michelin-starred restaurants were retained.

Code

The script in code/main.py performs the following steps:

Loads the raw Michelin dataset
Removes Bib Gourmand entries
Selects the relevant columns
Splits each restaurant's cuisine string into a list of cuisine categories
Builds restaurant nodes
Builds cuisine nodes
Creates restaurant-to-cuisine edges
Exports the final network files as nodes.csv and edges.csv
Visualization

The processed node and edge files were imported into Gephi to create the final network visualizations.

Two main visualizations were created:

a full network visualization showing the overall bipartite structure
a filtered visualization focusing on the core communities and most important hubs

The Gephi project file is included in gephi/Michelin1.gephi.

How to Run
Install dependencies:
pip install -r requirements.txt
Make sure the raw dataset is located at:
data/raw/michelin_my_maps.csv
Run the script:
python code/main.py
The processed files will be generated in:
data/processed/
Software Used
Python
pandas
Gephi
