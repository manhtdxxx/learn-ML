import nbformat


NOTEBOOKS = ["C5_W4_N3 - Question Answering.ipynb"]  # List of notebooks or use glob
WIDGETS_OPTION = "remove"  # "fix" or "remove"


for notebook_path in NOTEBOOKS:
    nb = nbformat.read(notebook_path, as_version=4)

    for cell in nb.cells:
        if "metadata" in cell and "widgets" in cell.metadata:
            if WIDGETS_OPTION == "fix":
                cell.metadata["widgets"]["state"] = {}
            elif WIDGETS_OPTION == "remove":
                del cell.metadata["widgets"]

    nbformat.write(nb, notebook_path)
    print(f"Fixed widgets in notebook: {notebook_path}, Widgets option: {WIDGETS_OPTION}")
