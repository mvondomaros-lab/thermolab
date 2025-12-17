# Thermo Lab

## Environment setup

1. Install [pixi](https://pixi.sh/latest/installation/).

2. Clone the Thermo Lab repository and install the required dependencies:

```bash
git clone https://github.com/mvondomaros-lab/thermolab
cd thermolab
pixi install
```

3. Launch JupyterLab and open the landing notebook:

```bash
pixi run jupyter-lab thermolab.ipynb
```

If JupyterLab starts without opening the notebook automatically, open `thermolab.ipynb` from the file browser.

## Using the notebook interface

The lab consists of Jupyter notebooks made up of executable cells. Cells contain either Python code or explanatory text.

- Run the current cell: click **Run** (▶) or press **Shift + Enter**.
- Run all cells: use **Run All** (≫) from the notebook menu.

You do not need programming experience to complete the lab; execute the cells as instructed. If you are comfortable with Python, you may adapt or extend the examples (for example, to explore more advanced PySCF workflows).

### Code comments

Some code cells include comments to clarify what a block does or what you are expected to change:

```python
# This is a comment.
```

Comments do not affect execution; they are included as guidance.
