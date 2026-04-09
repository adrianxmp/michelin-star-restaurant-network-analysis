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
```text
