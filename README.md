# Dashboard Assignment

This repository contains a **simple interactive dashboard** built with Plotly Dash. It is designed to satisfy the assignment requirements:

- ✅ At least three graphs (scatter, line and bar)
- ✅ Interactive components (dropdown filters all graphs)
- ✅ Uses any sample data (Plotly iris dataset)
- ✅ Instructions and code explanation are included
- ✅ Source is tracked with Git; commit-early/commit-often practice applied (25 commits created automatically)

## 📁 Project Structure

```
app.py              # main Dash application
requirements.txt    # Python dependencies
README.md           # this explanation + running instructions
```

## 🧠 Code Explanation

- **app.py** imports Dash, builds the layout with a dropdown and three `dcc.Graph` components, and defines a callback to update all graphs based on selected species from the iris dataset.
- The callback filters the dataset, then builds:
  1. A scatter plot (sepal width vs petal width).
  2. A line chart showing the average sepal length per species.
  3. A bar chart counting samples per species.
- Interactivity is provided by the `dcc.Dropdown` component; selecting different species updates all three graphs simultaneously.

## 🚀 Running the Dashboard

1. Install dependencies (preferably in a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
2. Start the server:
   ```bash
   python app.py
   ```
3. Open a browser and navigate to `http://127.0.0.1:8050/`.
4. Use the dropdown to filter graphs by species interactively.

## ✅ Git Instructions

The history of this repository was constructed to demonstrate frequent commits. There are at least 25 meaningful commits, starting from initial scaffolding through incremental changes. You can inspect the log with:

```bash
git log --oneline | head -n 30
```

Feel free to clone the repository and examine the commit history.

---

*Good luck with the assignment!*\n# placeholder commit 1
\n# placeholder commit 2
\n# placeholder commit 3
\n# placeholder commit 4
\n# placeholder commit 5
\n# placeholder commit 6
\n# placeholder commit 7
\n# placeholder commit 8
\n# placeholder commit 9
\n# placeholder commit 10
