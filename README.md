# 🌊 OceanGuard Analytics
[![Ocean_Guard_poster.png](https://i.postimg.cc/4323drgt/Ocean_Guard_poster.png)](https://postimg.cc/zLWN223X)
### Maritime Accident Prevention Intelligence Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://oceanguard-analytics-egg7zqwswgdmzrnybexkbj.streamlit.app/)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=flat&logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.18+-3F4F75?style=flat&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-0E6655?style=flat)
![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=flat)

> *Navigating Data | Unveiling Insights | Driving Impact*

**Built independently in Lagos, Nigeria — zero institutional funding, fully open-source.**

---

## 🔗 Live Platform

| Resource | Link |
|---|---|
| 🚀 Live App | [oceanguard-analytics.streamlit.app](https://oceanguard-analytics-egg7zqwswgdmzrnybexkbj.streamlit.app/) |
| 📊 Portfolio Page | [OceanGuard Analytics — Fijabi J. Adekunle](https://sites.google.com/view/fijabi-j-adekunle/oceanguard-analytics) |
| 🔬 MAIB Source Analysis | [UK MAIB Accidents 2020–2024](https://sites.google.com/view/fijabi-j-adekunle/uk-maib-maritime-accidents-2020-2024) |
| 👤 Author Portfolio | [fijabi-j-adekunle](https://sites.google.com/view/fijabi-j-adekunle/project-page) |

---

## 📖 Overview

OceanGuard Analytics is a live, open-access maritime accident prevention platform built on five years of verified UK government accident data. It transforms raw incident records from the **UK Marine Accident Investigation Branch (MAIB)** into real-time, actionable intelligence — designed for port authority officers, coastguard commanders, maritime regulators, and environmental NGOs across Africa.

**The core question OceanGuard answers:**

> *Which vessel types, location zones, weather conditions, and seasonal patterns are most likely to produce the next maritime accident — and the next ocean pollution event — before it happens?*

This is not another analysis project. It is a deployed prevention tool — and the foundation of a continent-wide maritime safety intelligence initiative for Africa's 38 coastal nations.

---

## 🎯 The Problem

Every year, hundreds of maritime accidents release fuel, chemicals, and debris into our oceans. These events are not random — they follow repeatable patterns across vessel types, routes, seasons, and conditions. Yet most maritime safety decisions remain **reactive**: authorities investigate after disasters happen.

The data that could prevent the next accident exists. What was missing was a platform that makes those patterns **actionable in real time** — accessible to the port officer who has two minutes and no data science background.

For Africa's coastal communities — from Lagos to Mombasa — this is not an abstract problem. Maritime accidents in African waters threaten fishing livelihoods, destroy coral reefs, contaminate coastal water sources, and undermine the blue economy that millions depend on. Almost none of Africa's 38 coastal nations have structured maritime accident intelligence systems.

**OceanGuard changes that.**

---

## 📊 Platform Features

| Feature | Description |
|---|---|
| **7 KPI Cards** | Total accidents, fatalities, fatal incidents, ships lost, top vessel type, top injury, top location — visible in 5 seconds |
| **Accidents by Year** | Bar chart tracking year-over-year accident trends 2020–2024 |
| **Vessel Type Breakdown** | Donut chart showing which vessel categories dominate accident records |
| **Injury Intelligence** | Top 8 injury types by frequency — informing safety training priorities |
| **Weather Correlation** | Reveals that clear weather — not storms — produces the most accidents |
| **Location Zone Analysis** | Accident frequency mapped across coastal, port, open sea, and inland zones |
| **Accident Heatmap** | Vessel type vs year risk matrix — the most powerful single view for regulators |
| **Damage Assessment** | Distribution from no damage through to total ship loss |
| **Searchable Accident Log** | Free-text search across all 1,840 verified records |
| **Multi-Country Architecture** | Country filter live and ready for NIMASA, EMSA, and USCG data integration |
| **Sidebar Filters** | Year, vessel type, weather, location zone, damage level — all interactive |

---

## 🔑 Key Insights

### 1. Passenger Ships Dominate Incidents — But Not Fatalities
With **758 incidents**, passenger ships are the most accident-prone vessel type. Their fatality rate is remarkably low — evidence of strong ISM and STCW compliance. Prevention implication: focus on port congestion and navigation aids, not crew training.

### 2. Recreational Craft Are the Deadliest Vessel Type
Despite fewer total incidents, recreational craft account for the **highest fatalities** — operators without professional oversight, limited safety equipment, and no mandatory weather monitoring. A targeted public education campaign could prevent the majority of these deaths.

### 3. Clear Weather Is the Most Dangerous Condition
**46–50% of all accidents occur in clear weather** — not storms, not fog. Overconfidence in good visibility drives human-error collisions. This single finding challenges conventional maritime safety assumptions and has direct policy implications.

### 4. Port Areas Are the Highest-Risk Location Zone
Internal waters and port areas account for the highest accident frequency — dense traffic, complex manoeuvring, and human fatigue converge in the same space. Targeted port safety interventions are the highest-leverage prevention opportunity.

### 5. Prevention Beats Reaction
**82 fatal incidents over 4 years are entirely preventable.** The patterns are clear. The data exists. What was missing was a platform that makes those patterns actionable in real time. That is what OceanGuard provides.

---

## 🗄️ Dataset

| Attribute | Detail |
|---|---|
| **Source** | UK Marine Accident Investigation Branch (MAIB) — official government records |
| **Coverage** | November 2020 — December 2024 |
| **Records** | 1,840 verified maritime accident incidents |
| **Columns** | 14: ID, Country, Location, Vessel Type, Flag, Gross Tonnage, Length (m), Port, Injury Type, Fatalities, Description, Weather, Damage, Date |
| **Vessel Types** | Passenger, Cargo, Fishing, Recreational, Service, Inland Waterway, Navy |
| **Location Zones** | Coastal waters, Port area, Open sea (EEZ / outside EEZ), Inland waters, Rivers |
| **Damage Levels** | No damage, Minor damage, Material damage, Loss of ship |
| **Architecture** | Multi-country ready — Country column built in for NIMASA, EMSA, USCG integration |

### Dataset Stats at a Glance

```
Total Records    :  1,840
Total Fatalities :  87
Fatal Incidents  :  82
Ships Lost       :  50
Date Range       :  Nov 2020 — Dec 2024
Top Vessel Type  :  Passenger Ship (758 incidents)
Top Injury       :  Bone Fractures (705 cases)
Top Location     :  Internal Waters — Port Area (681 incidents)
Top Weather      :  Clear (839 incidents)
```

---

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.10+
pip
```

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/FijabiAdekunle/oceanguard-analytics.git
cd oceanguard-analytics

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app locally
streamlit run oceanguard_app.py
```

The app will open automatically in your browser at `http://localhost:8501`

### Requirements

```
streamlit>=1.32.0
pandas>=2.0.0
plotly>=5.18.0
```

---

## 📁 Repository Structure

```
oceanguard-analytics/
│
├── oceanguard_app.py          # Main Streamlit application
├── maib_dashboard_ready.csv   # Cleaned dataset (1,840 records, 14 columns)
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

---

## 🌍 Why Africa

Africa has **38 coastal nations**, over **40,000 km of coastline**, and some of the world's most biodiverse marine ecosystems. Maritime accidents in African waters threaten:

- Fishing communities that depend on healthy coastal waters
- Coral reefs and seagrass beds destroyed by vessel groundings
- Coastal drinking water sources contaminated by fuel spills
- The blue economy underpinning millions of livelihoods

Almost none of Africa's coastal nations have structured maritime accident intelligence systems. Accident data sits in PDF reports — unstructured and inaccessible to the officers who need it most.

**OceanGuard is built to change that — starting with Nigeria, replicable across the continent.** The multi-country architecture is already live. The methodology is open-source and free. Any African maritime authority can adopt it using their own national data.

---

## 🔮 Roadmap

### Phase 1 — Nigeria Data Integration *(Months 1–3)*
Digitise and structure NIMASA (Nigerian Maritime Administration and Safety Agency) accident records — creating the first comparative West African maritime safety dataset alongside MAIB data.

### Phase 2 — Multi-Country Expansion *(Months 3–7)*
Integrate EMSA (Europe), USCG (USA), and Transport Canada data — enabling the first cross-continental open maritime safety comparison platform.

### Phase 3 — Predictive Risk Scoring *(Months 6–9)*
ML model flagging high-risk vessel-route-season combinations before accidents occur — building on the existing [Predictive Maintenance for Marine Engines](https://sites.google.com/view/fijabi-j-adekunle/predictive-maintenance-for-marine-engines) project.

### Phase 4 — Open Replication Toolkit *(Months 9–12)*
Free methodology guide enabling Ghana, Kenya, Tanzania, and other African coastal nations to build their own national maritime safety intelligence systems at near-zero cost.

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| **Python** | Core language |
| **Pandas** | Data cleaning, transformation, filtering |
| **Plotly** | Interactive charts — bar, donut, heatmap |
| **Streamlit** | Web app framework and deployment |
| **Streamlit Cloud** | Free cloud hosting and public URL |
| **Power BI** | Enterprise-grade dashboard (separate deployment) |
| **GitHub** | Version control and open-source hosting |

---

## 🤝 How to Contribute

Contributions are welcome — especially from maritime professionals, data engineers, and African coastal data advocates.

```bash
# Fork the repository
# Create a feature branch
git checkout -b feature/your-feature-name

# Make your changes and commit
git commit -m "Add: your feature description"

# Push and open a Pull Request
git push origin feature/your-feature-name
```

**Priority contribution areas:**
- Adding new country datasets (NIMASA, EMSA, USCG)
- Improving the predictive risk model
- Translating the platform into French or Portuguese (for Francophone and Lusophone African nations)
- UI/UX improvements for low-bandwidth environments

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

---

## 👤 Author

**Fijabi Jeleel Adekunle**
Marine Engineer turned Data Professional | Lagos, Nigeria

| | |
|---|---|
| 🌐 Portfolio | [sites.google.com/view/fijabi-j-adekunle](https://sites.google.com/view/fijabi-j-adekunle/project-page) |
| 💼 LinkedIn | [linkedin.com/in/fijabi-j-adekunle](https://www.linkedin.com/in/fijabi-j-adekunle/) |
| 🐙 GitHub | [github.com/FijabiAdekunle](https://github.com/FijabiAdekunle) |
| 📊 Kaggle | [kaggle.com/jeleeladekunlefijabi](https://www.kaggle.com/jeleeladekunlefijabi) |
| 📧 Email | fijaytwo@gmail.com |

---

## 🌊 Related Projects

| Project | Description |
|---|---|
| [UK MAIB Accident Analysis](https://sites.google.com/view/fijabi-j-adekunle/uk-maib-maritime-accidents-2020-2024) | The source research project that powers OceanGuard |
| [Maritime Port Performance](https://sites.google.com/view/fijabi-j-adekunle/maritime-port-performance-analysis-2022-2023) | UNCTAD port performance analysis — Streamlit + Power BI |
| [Predictive Maintenance — Marine Engines](https://sites.google.com/view/fijabi-j-adekunle/predictive-maintenance-for-marine-engines) | ML model for marine engine failure prediction |
| [Ship Performance Clustering](https://sites.google.com/view/fijabi-j-adekunle/ship-performance-clustering-analysis) | Unsupervised ML on maritime operational data |

---

<div align="center">

**"The ocean does not need more reports. It needs a system that keeps running."**

*— Fijabi Jeleel Adekunle*

🌊 **OceanGuard Analytics** — Built in Lagos, Designed for Africa, Open to the World

</div>
