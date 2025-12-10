# Thermo Lab

## Environment Setup

1. Install [pixi](https://pixi.sh/latest/installation/).

2. Clone the Thermo Lab repository and install the required dependencies:

```bash
git clone https://github.com/mvondomaros-lab/thermolab
cd thermolab
pixi install
```

3. Launch the notebook:

```bash
pixi run jupyter-lab thermolab.ipynb
```

## Using the Notebook Interface

The notebook consists of executable cells. Each cell contains Python code or explanatory text.

- To run a single cell, click the Run button (▶).
- To run all cells, use the Run All command (≫).
- You can also press Shift + Enter to execute the current cell.

Python code appears throughout the notebook. You do not need programming experience to carry out the calculations; simply execute the cells as instructed. If you are comfortable with Python, you may adapt or extend the examples, including more advanced PySCF workflows.

Comments within code cells provide guidance:

```python
# This is a comment.
```

They do not affect execution and are included to support your progress through the notebook.
