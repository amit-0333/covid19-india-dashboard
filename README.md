<div align="center">

```
 ██████╗ ██████╗ ██╗   ██╗██╗██████╗     ██╗ █████╗ 
██╔════╝██╔═══██╗██║   ██║██║██╔══██╗   ███║██╔══██╗
██║     ██║   ██║██║   ██║██║██║  ██║   ╚██║╚██████║
██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║    ██║ ╚═══██║
╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝   ██║  █████╔╝
 ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝    ╚═╝  ╚════╝ 
```

### 🦠 COVID-19 India Dashboard

> An interactive web dashboard for visualizing COVID-19 statistics across Indian states and union territories — built with Plotly, Dash, Pandas, and Bootstrap.

<br/>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-008DE4?style=for-the-badge&logo=plotly&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)

</div>

---

## 📌 About

This is my **COVID-19 India Dashboard project** — an interactive data visualization app built using Dash and Plotly, tracking confirmed cases, recoveries, active cases, and deaths across all Indian states and union territories.

Built to practice:
- Building multi-component interactive dashboards with Dash
- Creating dynamic Plotly GO charts with callbacks
- Working with real-world time-series COVID data
- Applying Bootstrap layout with custom CSS theming

---

## 💡 Why Dash + Plotly?

| Feature | Matplotlib/Seaborn | Plotly + Dash |
|--------|-------------------|---------------|
| **Interactivity** | Static images | Fully interactive (zoom, hover, filter) |
| **Web App** | Not supported | Built-in web server via Dash |
| **Callbacks** | Not available | Reactive UI with Input/Output callbacks |
| **Deployment** | Not applicable | Deployable as a web app |
| **Real-time feel** | ❌ | ✅ Dropdown filters update charts instantly |

---

## 📊 Dashboard Features

- **KPI Cards** — At-a-glance totals for Confirmed, Active, Recovered, and Deaths
- **Line Chart** — India-wide cumulative trend over time for all three metrics
- **Bar Chart** — State-wise breakdown with a dropdown to switch between Confirmed, Recovered, and Deaths
- **Histograms (Log Scale)** — Distribution of cases across states using log10 binning for better readability

---

## 🗺️ App Structure

```
covid19-india-dashboard/
│
├── 📂 assets/
│   └── style.css          # Custom dark theme styles (auto-loaded by Dash)
│
├── 📂 datasets/
│   └── covid_19_india.csv # State-wise daily COVID-19 data
│
├── 📄 app.py              # Main Dash application
├── 📓 analysis.ipynb      # Exploratory data analysis notebook
└── 📄 README.md
```

---

## 📂 Assets Folder

Dash automatically serves any file placed in the `assets/` folder — no manual linking needed in the layout.

| File | Purpose |
|------|---------|
| `style.css` | Overrides Bootstrap 4 defaults — applies dark background (`#111`), card spacing, heading colors, and layout padding across the entire dashboard |

---

## ⚙️ How to Run

```bash
# 1. Clone the repository
git clone https://github.com/amit-0333/covid19-india-dashboard.git

# 2. Navigate into the folder
cd covid19-india-dashboard

# 3. Install dependencies
pip install dash plotly pandas numpy

# 4. Run the app
python app.py

# 5. Open in browser
http://127.0.0.1:5000/
```

---

## 🧪 Dataset

| File | Description |
|------|-------------|
| `covid_19_india.csv` | State/UT-wise daily data including Confirmed, Cured, and Deaths columns from the start of the pandemic |

**Key columns used:**

- `Date` — Daily timestamp
- `State/UnionTerritory` — Indian state or UT name
- `Confirmed` — Total confirmed cases
- `Cured` — Total recovered cases
- `Deaths` — Total deaths
- `Active` — Computed as `Confirmed - Cured - Deaths`

---

## 🧩 My Approach

```
1. 📥 Load and clean the dataset using Pandas
2. 📊 Compute KPI metrics from the latest date snapshot
3. 🎨 Build the layout using Dash HTML components + Bootstrap grid
4. 🔁 Wire up interactivity using Dash callbacks (Input → Output)
5. 📈 Render charts using Plotly Graph Objects (go.Scatter, go.Bar, go.Histogram)
6. 🪵 Fix log-scale histogram using NumPy manual binning
7. 🎨 Apply custom dark theme via assets/style.css
```

---

## 🎯 Learning Goals

- [x] Build a multi-page style dashboard layout with Dash
- [x] Use `dcc.Graph` and `dcc.Dropdown` with callbacks
- [x] Create line, bar, and histogram charts with Plotly GO
- [x] Apply Bootstrap 4 grid for responsive layout
- [x] Use `assets/` folder for custom CSS in Dash
- [x] Handle real-world messy COVID data with Pandas
- [x] Fix log-scale histogram rendering using NumPy binning
- [ ] Add date range slider for time filtering
- [ ] Deploy the dashboard on Render or Railway

---

## 🛠️ Tech Stack

- 🐍 **Python** — Core programming language
- 💻 **Dash** — Web framework for the dashboard
- 📊 **Plotly GO** — Interactive chart rendering
- 🐼 **Pandas** — Data loading and manipulation
- 🔢 **NumPy** — Log-scale histogram bin computation
- 🎨 **Bootstrap 4** — Responsive grid layout and card components
- 🖌️ **Custom CSS** — Dark theme via `assets/style.css`

---

## 👨‍💻 Author

**Amit Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-amit--0333-181717?style=flat&logo=github)](https://github.com/amit-0333)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Amit%20Kumar-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/amit-kumar-a62a3640a/)
[![Kaggle](https://img.shields.io/badge/Kaggle-amitkumar038975-20BEFF?style=flat&logo=kaggle)](https://www.kaggle.com/amitkumar038975)

---

<div align="center">

> 📝 *Built as part of my Data Science and Python learning journey.*

⭐ **Star this repo if you found it useful!**

</div>
