# Dashboard Assignment

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
