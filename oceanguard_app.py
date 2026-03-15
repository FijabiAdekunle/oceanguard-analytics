import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# ── PAGE CONFIG ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="OceanGuard Analytics",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── CUSTOM CSS ───────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Main background */
    .stApp { background-color: #F0F4F8; }

    /* Header banner */
    .og-header {
        background: linear-gradient(135deg, #0E6655, #154360);
        padding: 28px 36px;
        border-radius: 12px;
        margin-bottom: 24px;
    }
    .og-title {
        color: white;
        font-size: 2.4rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: 1px;
    }
    .og-subtitle {
        color: #A9DFBF;
        font-size: 1rem;
        margin: 4px 0 0 0;
    }
    .og-motto {
        color: #A9DFBF;
        font-size: 0.85rem;
        margin-top: 8px;
        font-style: italic;
        letter-spacing: 1px;
    }

    /* KPI cards */
    .kpi-card {
        background: white;
        border-radius: 10px;
        padding: 20px 18px;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border-left: 5px solid #0E6655;
        height: 110px;
        display: flex;
        flex-direction: column;
        justify-content: center;
    }
    .kpi-value {
        font-size: 2rem;
        font-weight: 800;
        color: #0E6655;
        line-height: 1.1;
    }
    .kpi-label {
        font-size: 0.78rem;
        color: #7F8C8D;
        margin-top: 4px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .kpi-card-red  { border-left-color: #C0392B !important; }
    .kpi-card-red .kpi-value { color: #C0392B !important; }
    .kpi-card-blue { border-left-color: #154360 !important; }
    .kpi-card-blue .kpi-value { color: #154360 !important; }
    .kpi-card-gold { border-left-color: #9A7D0A !important; }
    .kpi-card-gold .kpi-value { color: #9A7D0A !important; }

    /* Section headers */
    .section-hdr {
        color: #154360;
        font-size: 1.1rem;
        font-weight: 700;
        border-bottom: 3px solid #0E6655;
        padding-bottom: 6px;
        margin: 24px 0 16px 0;
    }

    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #154360 !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    [data-testid="stSidebar"] .stSelectbox label,
    [data-testid="stSidebar"] .stMultiSelect label,
    [data-testid="stSidebar"] .stSlider label {
        color: #A9DFBF !important;
        font-weight: 600;
    }

    /* Footer */
    .og-footer {
        background: #154360;
        color: #A9DFBF;
        padding: 14px 24px;
        border-radius: 10px;
        text-align: center;
        font-size: 0.8rem;
        margin-top: 32px;
    }

    /* Hide default streamlit footer */
    footer { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── LOAD DATA ────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    df = pd.read_csv(
        "maib_dashboard_ready.csv",
        parse_dates=["Date"]
    )
    df["Year"]  = df["Date"].dt.year
    df["Month"] = df["Date"].dt.month_name()
    df["Quarter"] = df["Date"].dt.to_period("Q").astype(str)

    # Normalise Damage column (two spellings of "No damage")
    df["Damage"] = df["Damage"].str.replace("No Damage", "No damage", case=False)

    # Simplify long damage labels
    df["Damage_Short"] = df["Damage"].apply(lambda x:
        "No damage"       if "No damage" in str(x) else
        "Loss of ship"    if "Loss of ship" in str(x) else
        "Material damage" if "Material damage" in str(x) else
        "Minor damage"    if "Minor damage" in str(x) else str(x)
    )

    # Ensure Country column exists (future-proofs for multi-country data)
    if "Country" not in df.columns:
        df["Country"] = "United Kingdom"

    # Fatality flag
    df["Fatal"] = df["Fatalities"] > 0
    return df

df = load_data()


# ── HEADER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="og-header">
    <p class="og-title">🌊 OceanGuard Analytics</p>
    <p class="og-subtitle">UK Maritime Accident Intelligence Dashboard &nbsp;|&nbsp; MAIB 2020–2024</p>
    <p class="og-motto">Navigating Data &nbsp;|&nbsp; Unveiling Insights &nbsp;|&nbsp; Driving Impact</p>
</div>
""", unsafe_allow_html=True)


# ── SIDEBAR FILTERS ───────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🔧 Filters")
    st.markdown("---")

    country_opts = sorted(df["Country"].dropna().unique())
    sel_countries = st.multiselect(
        "🌍 Country / Data Source", country_opts, default=country_opts
    )

    years = sorted(df["Year"].dropna().unique())
    sel_years = st.multiselect(
        "📅 Year", years, default=years
    )

    vessel_types = sorted(df["Vessel Type"].dropna().unique())
    sel_vessels = st.multiselect(
        "🚢 Vessel Type", vessel_types, default=vessel_types
    )

    weather_opts = sorted(df["Weather"].dropna().unique())
    sel_weather = st.multiselect(
        "🌤 Weather", weather_opts, default=weather_opts
    )

    location_opts = sorted(df["Location"].dropna().unique())
    sel_locations = st.multiselect(
        "📍 Location Zone", location_opts, default=location_opts
    )

    damage_opts = sorted(df["Damage_Short"].dropna().unique())
    sel_damage = st.multiselect(
        "💥 Damage Level", damage_opts, default=damage_opts
    )

    st.markdown("---")
    st.markdown("**Data Source:** UK Marine Accident Investigation Branch (MAIB)")
    st.markdown("**Coverage:** November 2020 – December 2024")
    st.markdown("**Records:** 1,840 maritime accidents")
    st.markdown("---")
    st.markdown("Built by **Fijabi J. Adekunle**")
    st.markdown("[Portfolio](https://sites.google.com/view/fijabi-j-adekunle/project-page)")


# ── APPLY FILTERS ─────────────────────────────────────────────────────────────
filtered = df[
    df["Country"].isin(sel_countries) &
    df["Year"].isin(sel_years) &
    df["Vessel Type"].isin(sel_vessels) &
    df["Weather"].isin(sel_weather) &
    df["Location"].isin(sel_locations) &
    df["Damage_Short"].isin(sel_damage)
]

if filtered.empty:
    st.warning("No records match your current filters. Please adjust the sidebar.")
    st.stop()


# ── KPI CARDS ─────────────────────────────────────────────────────────────────
st.markdown('<p class="section-hdr">📊 Key Performance Indicators</p>', unsafe_allow_html=True)

total_accidents   = len(filtered)
total_fatalities  = int(filtered["Fatalities"].sum())
top_vessel        = filtered["Vessel Type"].mode()[0] if not filtered.empty else "N/A"
top_injury        = filtered["Injury Type"].dropna().mode()[0] if filtered["Injury Type"].dropna().any() else "N/A"
top_location      = filtered["Location"].mode()[0] if not filtered.empty else "N/A"
fatal_incidents   = int(filtered["Fatal"].sum())
loss_of_ship      = int((filtered["Damage_Short"] == "Loss of ship").sum())

# ── KPI Row 1 ──
r1c1, r1c2, r1c3, r1c4 = st.columns(4)

with r1c1:
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-value">{total_accidents:,}</div>
        <div class="kpi-label">Total Accidents</div>
    </div>""", unsafe_allow_html=True)

with r1c2:
    st.markdown(f"""<div class="kpi-card kpi-card-red">
        <div class="kpi-value">{total_fatalities}</div>
        <div class="kpi-label">Fatalities</div>
    </div>""", unsafe_allow_html=True)

with r1c3:
    st.markdown(f"""<div class="kpi-card kpi-card-red">
        <div class="kpi-value">{fatal_incidents}</div>
        <div class="kpi-label">Fatal Incidents</div>
    </div>""", unsafe_allow_html=True)

with r1c4:
    st.markdown(f"""<div class="kpi-card kpi-card-red">
        <div class="kpi-value">{loss_of_ship}</div>
        <div class="kpi-label">Ships Lost</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<div style='margin-top:12px'></div>", unsafe_allow_html=True)

# ── KPI Row 2 ──
r2c1, r2c2, r2c3 = st.columns(3)

with r2c1:
    st.markdown(f"""<div class="kpi-card kpi-card-blue">
        <div class="kpi-value" style="font-size:1.1rem">{top_vessel}</div>
        <div class="kpi-label">Top Vessel Type</div>
    </div>""", unsafe_allow_html=True)

with r2c2:
    short_injury = top_injury[:30] + "…" if len(top_injury) > 30 else top_injury
    st.markdown(f"""<div class="kpi-card kpi-card-gold">
        <div class="kpi-value" style="font-size:1.1rem">{short_injury}</div>
        <div class="kpi-label">Top Injury Type</div>
    </div>""", unsafe_allow_html=True)

with r2c3:
    short_loc = top_location[:30] + "…" if len(top_location) > 30 else top_location
    st.markdown(f"""<div class="kpi-card">
        <div class="kpi-value" style="font-size:1.1rem">{short_loc}</div>
        <div class="kpi-label">Top Location Zone</div>
    </div>""", unsafe_allow_html=True)


# ── ROW 1: ACCIDENTS BY YEAR + VESSEL TYPE ────────────────────────────────────
st.markdown('<p class="section-hdr">📈 Accident Trends & Vessel Analysis</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    yearly = filtered.groupby("Year").size().reset_index(name="Accidents")
    fig1 = px.bar(
        yearly, x="Year", y="Accidents",
        title="Accidents per Year",
        color="Accidents",
        color_continuous_scale=["#A9DFBF", "#0E6655"],
        text="Accidents"
    )
    fig1.update_traces(textposition="outside")
    fig1.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        title_font=dict(size=15, color="#154360"),
        coloraxis_showscale=False,
        xaxis=dict(tickmode="linear"),
        margin=dict(t=50, b=20)
    )
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    vessel_counts = filtered["Vessel Type"].value_counts().reset_index()
    vessel_counts.columns = ["Vessel Type", "Count"]
    fig2 = px.pie(
        vessel_counts, names="Vessel Type", values="Count",
        title="Accidents by Vessel Type",
        color_discrete_sequence=px.colors.sequential.Teal,
        hole=0.4
    )
    fig2.update_traces(textposition="inside", textinfo="percent+label")
    fig2.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        title_font=dict(size=15, color="#154360"),
        showlegend=False,
        margin=dict(t=50, b=20)
    )
    st.plotly_chart(fig2, use_container_width=True)


# ── ROW 2: INJURY TYPE + WEATHER ─────────────────────────────────────────────
st.markdown('<p class="section-hdr">🏥 Injury Patterns & Weather Conditions</p>', unsafe_allow_html=True)

col3, col4 = st.columns(2)

with col3:
    injury_counts = (
        filtered["Injury Type"].dropna()
        .value_counts()
        .head(8)
        .reset_index()
    )
    injury_counts.columns = ["Injury Type", "Count"]
    # Shorten long labels
    injury_counts["Short Label"] = injury_counts["Injury Type"].apply(
        lambda x: x[:40] + "…" if len(x) > 40 else x
    )
    fig3 = px.bar(
        injury_counts, x="Count", y="Short Label",
        orientation="h",
        title="Top 8 Injury Types",
        color="Count",
        color_continuous_scale=["#D5F5E3", "#0E6655"],
        text="Count"
    )
    fig3.update_traces(textposition="outside")
    fig3.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        title_font=dict(size=15, color="#154360"),
        coloraxis_showscale=False,
        yaxis=dict(autorange="reversed"),
        margin=dict(t=50, b=20, l=10)
    )
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    weather_counts = filtered["Weather"].value_counts().reset_index()
    weather_counts.columns = ["Weather", "Count"]
    fig4 = px.bar(
        weather_counts, x="Weather", y="Count",
        title="Accidents by Weather Condition",
        color="Count",
        color_continuous_scale=["#D6EAF8", "#154360"],
        text="Count"
    )
    fig4.update_traces(textposition="outside")
    fig4.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        title_font=dict(size=15, color="#154360"),
        coloraxis_showscale=False,
        margin=dict(t=50, b=20)
    )
    st.plotly_chart(fig4, use_container_width=True)


# ── ROW 3: LOCATION ZONE + DAMAGE ─────────────────────────────────────────────
st.markdown('<p class="section-hdr">📍 Location Zones & Damage Assessment</p>', unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    loc_counts = filtered["Location"].value_counts().reset_index()
    loc_counts.columns = ["Location", "Count"]
    fig5 = px.bar(
        loc_counts, x="Count", y="Location",
        orientation="h",
        title="Accidents by Location Zone",
        color="Count",
        color_continuous_scale=["#A9DFBF", "#0E6655"],
        text="Count"
    )
    fig5.update_traces(textposition="outside")
    fig5.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        title_font=dict(size=15, color="#154360"),
        coloraxis_showscale=False,
        yaxis=dict(autorange="reversed"),
        margin=dict(t=50, b=20)
    )
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    damage_counts = filtered["Damage_Short"].value_counts().reset_index()
    damage_counts.columns = ["Damage", "Count"]
    DAMAGE_COLORS = {
        "No damage":       "#2ECC71",
        "Minor damage":    "#F39C12",
        "Material damage": "#E74C3C",
        "Loss of ship":    "#7B241C",
    }
    fig6 = px.pie(
        damage_counts, names="Damage", values="Count",
        title="Damage Level Distribution",
        color="Damage",
        color_discrete_map=DAMAGE_COLORS,
        hole=0.4
    )
    fig6.update_traces(textposition="inside", textinfo="percent+label")
    fig6.update_layout(
        plot_bgcolor="white", paper_bgcolor="white",
        title_font=dict(size=15, color="#154360"),
        showlegend=True,
        margin=dict(t=50, b=20)
    )
    st.plotly_chart(fig6, use_container_width=True)


# ── ROW 4: VESSEL TYPE vs FATALITIES HEATMAP ─────────────────────────────────
st.markdown('<p class="section-hdr">⚠️ Risk Intelligence — Vessel Type vs Year</p>', unsafe_allow_html=True)

heat_data = filtered.groupby(["Year", "Vessel Type"]).size().reset_index(name="Accidents")
heat_pivot = heat_data.pivot(index="Vessel Type", columns="Year", values="Accidents").fillna(0)

fig7 = px.imshow(
    heat_pivot,
    title="Accident Heatmap — Vessel Type by Year",
    color_continuous_scale="Teal",
    aspect="auto",
    text_auto=True
)
fig7.update_layout(
    plot_bgcolor="white", paper_bgcolor="white",
    title_font=dict(size=15, color="#154360"),
    margin=dict(t=50, b=20)
)
st.plotly_chart(fig7, use_container_width=True)


# ── ROW 5: COUNTRY BREAKDOWN ─────────────────────────────────────────────────
st.markdown('<p class="section-hdr">🌍 Accidents by Country / Data Source</p>', unsafe_allow_html=True)

country_counts = filtered["Country"].value_counts().reset_index()
country_counts.columns = ["Country", "Accidents"]

fig8 = px.bar(
    country_counts, x="Country", y="Accidents",
    title="Accident Records by Country",
    color="Accidents",
    color_continuous_scale=["#A9DFBF", "#0E6655"],
    text="Accidents"
)
fig8.update_traces(textposition="outside")
fig8.update_layout(
    plot_bgcolor="white", paper_bgcolor="white",
    title_font=dict(size=15, color="#154360"),
    coloraxis_showscale=False,
    margin=dict(t=50, b=20)
)
st.plotly_chart(fig8, use_container_width=True)

# Info box for future data
if len(country_counts) == 1:
    st.info(
        "🌍 **More countries coming soon.** "
        "OceanGuard will integrate accident data from EMSA (Europe), USCG (USA), "
        "Transport Canada, ATSB (Australia), and NIMASA (Nigeria) — "
        "enabling the first open cross-country maritime safety comparison platform for Africa."
    )


# ── ACCIDENT LOG TABLE ────────────────────────────────────────────────────────
st.markdown('<p class="section-hdr">📋 Accident Log</p>', unsafe_allow_html=True)

search = st.text_input("🔍 Search descriptions, vessel types, locations...", "")

display_df = filtered[[
    "Date", "Country", "Vessel Type", "Location", "Weather",
    "Injury Type", "Fatalities", "Damage_Short", "Description"
]].copy()
display_df.columns = [
    "Date", "Country", "Vessel Type", "Location", "Weather",
    "Injury Type", "Fatalities", "Damage", "Description"
]
display_df["Date"] = display_df["Date"].dt.strftime("%b %Y")

if search:
    mask = display_df.apply(
        lambda row: row.astype(str).str.contains(search, case=False).any(), axis=1
    )
    display_df = display_df[mask]

st.dataframe(
    display_df.reset_index(drop=True),
    use_container_width=True,
    height=380
)
st.caption(f"Showing {len(display_df):,} of {len(filtered):,} filtered records")


# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="og-footer">
    🌊 <strong>OceanGuard Analytics</strong> &nbsp;|&nbsp;
    Built by <strong>Fijabi J. Adekunle</strong> &nbsp;|&nbsp;
    Data: UK Marine Accident Investigation Branch (MAIB) 2020–2024 &nbsp;|&nbsp;
    <em>Navigating Data | Unveiling Insights | Driving Impact</em>
</div>
""", unsafe_allow_html=True)
