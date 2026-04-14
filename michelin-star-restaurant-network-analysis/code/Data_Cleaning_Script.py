import pandas as pd

# Load the dataset (make sure the CSV file is in the same folder or update the path)
df = pd.read_csv("michelin_my_maps.csv")

# Remove Bib Gourmand entries since we only want Michelin-starred restaurants
df = df[df["Award"] != "Bib Gourmand"]

# Keep only the columns we actually need and drop any missing values
df = df[["Name", "Cuisine", "Location", "Award"]].dropna()

# Split the cuisine string into a list (some restaurants have multiple cuisines)
# Example: "French, Contemporary" -> ["French", "Contemporary"]
df["Cuisine_List"] = df["Cuisine"].apply(lambda x: [c.strip() for c in str(x).split(",")])

# Lists to store nodes and edges for the network
nodes = []
edges = []

# Counter to assign unique IDs to each node
node_id = 0

# Dictionary to map restaurant names to their node IDs
node_map = {}

# Step 1: Add restaurant nodes
for r in df["Name"]:
    node_map[r] = node_id
    nodes.append([node_id, r, "Restaurant"])  # [Id, Label, Type]
    node_id += 1

# Step 2: Add cuisine nodes
cuisine_nodes = {}

for cuisines in df["Cuisine_List"]:
    for c in cuisines:
        # Only create a new node if we haven't seen this cuisine before
        if c not in cuisine_nodes:
            cuisine_nodes[c] = node_id
            nodes.append([node_id, c, "Cuisine"])
            node_id += 1

# Step 3: Create edges
# Each restaurant connects to all of its cuisine types
for i, row in df.iterrows():
    restaurant_id = node_map[row["Name"]]
    
    for cuisine in row["Cuisine_List"]:
        cuisine_id = cuisine_nodes[cuisine]
        edges.append([restaurant_id, cuisine_id])  # [Source, Target]

# Convert lists into DataFrames
nodes_df = pd.DataFrame(nodes, columns=["Id", "Label", "Type"])
edges_df = pd.DataFrame(edges, columns=["Source", "Target"])

# Export the final node and edge lists for Gephi
nodes_df.to_csv("nodes.csv", index=False)
edges_df.to_csv("edges.csv", index=False)
