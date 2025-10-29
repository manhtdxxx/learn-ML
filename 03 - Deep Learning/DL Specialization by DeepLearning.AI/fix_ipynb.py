import nbformat

# Path to the notebook you want to fix
notebook_path = "C5_W4_N3 - Question Answering.ipynb"

# Read the notebook
nb = nbformat.read(notebook_path, as_version=4)

# Fix all cells that have metadata.widgets
for cell in nb.cells:
    if "metadata" in cell and "widgets" in cell.metadata:
        cell.metadata["widgets"]["state"] = {}

# Write the notebook back
nbformat.write(nb, notebook_path)

print(f"Fixed metadata.widgets in {notebook_path}")
