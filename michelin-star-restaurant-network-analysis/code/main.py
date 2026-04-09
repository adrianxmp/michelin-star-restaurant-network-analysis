import pandas as pd

df = pd.read_csv("michelin_my_maps.csv")

# Remove Bib Gourmand
df = df[df["Award"] != "Bib Gourmand"]

df = df[["Name", "Cuisine", "Location", "Award"]].dropna()

df["Cuisine_List"] = df["Cuisine"].apply(lambda x: [c.strip() for c in str(x).split(",")])

nodes = []
edges = []
node_id = 0
node_map = {}

# Add restaurant nodes
for r in df["Name"]:
    node_map[r] = node_id
    nodes.append([node_id, r, "Restaurant"])
    node_id += 1

# Add cuisine nodes
cuisine_nodes = {}

for cuisines in df["Cuisine_List"]:
    for c in cuisines:
        if c not in cuisine_nodes:
            cuisine_nodes[c] = node_id
            nodes.append([node_id, c, "Cuisine"])
            node_id += 1

# Create edges
for i, row in df.iterrows():
    restaurant_id = node_map[row["Name"]]
    
    for cuisine in row["Cuisine_List"]:
        cuisine_id = cuisine_nodes[cuisine]
        edges.append([restaurant_id, cuisine_id])

nodes_df = pd.DataFrame(nodes, columns=["Id","Label","Type"])
edges_df = pd.DataFrame(edges, columns=["Source","Target"])

nodes_df.to_csv("nodes.csv", index=False)
edges_df.to_csv("edges.csv", index=False)