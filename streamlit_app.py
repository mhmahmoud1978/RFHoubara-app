import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="One Health Animation Dashboard",
    page_icon="🌍",
    layout="wide",
)

st.title("🌍 One Health Collaboration in Motion")
st.markdown(
    """
    The **One Health** approach recognises that the wellbeing of people, animals, and the environment are tightly linked.
    Use the animated chart below to explore how risk levels and preparedness evolve together across sectors and time.
    """
)

st.write("### Explore the evolving One Health landscape")
st.write(
    "Each bubble represents a One Health domain. The horizontal axis shows preparedness, the vertical axis "
    "captures the scale of impact, and bubble size conveys the intensity of risk. Press play to watch how the "
    "domains respond over time."
)

data = [
    {"Year": 2015, "Domain": "Human Health", "Preparedness": 55, "Impact": 62, "Risk Level": 38,
     "Focus": "Strengthen infection prevention"},
    {"Year": 2015, "Domain": "Animal Health", "Preparedness": 48, "Impact": 58, "Risk Level": 35,
     "Focus": "Improve farm biosecurity"},
    {"Year": 2015, "Domain": "Environment", "Preparedness": 41, "Impact": 65, "Risk Level": 42,
     "Focus": "Mitigate ecosystem degradation"},
    {"Year": 2017, "Domain": "Human Health", "Preparedness": 60, "Impact": 66, "Risk Level": 40,
     "Focus": "Expand vaccination coverage"},
    {"Year": 2017, "Domain": "Animal Health", "Preparedness": 54, "Impact": 60, "Risk Level": 37,
     "Focus": "Integrate veterinary surveillance"},
    {"Year": 2017, "Domain": "Environment", "Preparedness": 46, "Impact": 69, "Risk Level": 44,
     "Focus": "Restore wetlands and buffers"},
    {"Year": 2019, "Domain": "Human Health", "Preparedness": 63, "Impact": 72, "Risk Level": 47,
     "Focus": "Monitor antimicrobial use"},
    {"Year": 2019, "Domain": "Animal Health", "Preparedness": 58, "Impact": 66, "Risk Level": 42,
     "Focus": "Scale livestock vaccination"},
    {"Year": 2019, "Domain": "Environment", "Preparedness": 50, "Impact": 74, "Risk Level": 48,
     "Focus": "Track climate-sensitive hazards"},
    {"Year": 2021, "Domain": "Human Health", "Preparedness": 70, "Impact": 75, "Risk Level": 52,
     "Focus": "Invest in resilient care systems"},
    {"Year": 2021, "Domain": "Animal Health", "Preparedness": 65, "Impact": 69, "Risk Level": 46,
     "Focus": "Coordinate wildlife monitoring"},
    {"Year": 2021, "Domain": "Environment", "Preparedness": 57, "Impact": 78, "Risk Level": 50,
     "Focus": "Reduce pollution hotspots"},
    {"Year": 2023, "Domain": "Human Health", "Preparedness": 76, "Impact": 80, "Risk Level": 55,
     "Focus": "Advance genomic surveillance"},
    {"Year": 2023, "Domain": "Animal Health", "Preparedness": 71, "Impact": 73, "Risk Level": 50,
     "Focus": "Share cross-border intelligence"},
    {"Year": 2023, "Domain": "Environment", "Preparedness": 63, "Impact": 82, "Risk Level": 53,
     "Focus": "Scale green infrastructure"},
]


df = pd.DataFrame(data)

fig = px.scatter(
    df,
    x="Preparedness",
    y="Impact",
    size="Risk Level",
    color="Domain",
    animation_frame="Year",
    animation_group="Domain",
    hover_name="Domain",
    hover_data={"Risk Level": True, "Focus": True, "Year": False},
    size_max=60,
    range_x=[35, 85],
    range_y=[50, 90],
    labels={
        "Preparedness": "Preparedness Index",
        "Impact": "Impact Severity Index",
        "Risk Level": "Risk Level",
    },
)

fig.update_layout(
    title="Integrated risk and preparedness across the One Health spectrum",
    legend_title="Domain",
    margin=dict(l=40, r=40, t=80, b=40),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
)

fig.update_traces(marker=dict(line=dict(width=1, color="rgba(0,0,0,0.4)")))

st.plotly_chart(fig, use_container_width=True)

st.write("### Key takeaways")
st.markdown(
    """
    - **Human Health** investments steadily boost preparedness, but continued innovation is needed to curb risk.
    - **Animal Health** gains momentum as veterinary systems integrate with public health surveillance networks.
    - **Environmental Health** remains a critical driver of impact, underscoring the need for climate-smart policies.
    """
)

st.info(
    "Collaboration across sectors unlocks solutions that protect people, animals, and the ecosystems we share."
)
