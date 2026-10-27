import streamlit as st

# ── Page configuration ───────────────────────────
st.set_page_config(
    page_title="Python Learning Journey",
    page_icon="🐍",
    layout="centered",
)

st.title("🐍 Python Learning Journey")
st.caption("Adjust the widgets to explore your progress and learning path.")

st.divider()

# ════════════════════════════════════
# Widget 1 — st.slider
# ═══════════════════════════════════
st.subheader("1. Experience Level")
weeks = st.slider(
    "How many weeks have you been coding?",
    min_value=0,
    max_value=52,
    value=8,
    step=1
)

if weeks < 12:
    level_label = "Beginner"
elif weeks < 26:
    level_label = "Intermediate"
else:
    level_label = "Advanced"

st.metric(
    label="Your Python Experience",
    value=level_label,
    delta=f"{weeks} weeks",
    delta_color="off"
)

st.divider()

# ═══════════════════════════════════
# Widget 2 — st.selectbox
# ════════════════════════════════
st.subheader("2. Current Topic")
topics = [
    "Python Basics",
    "Data Structures",
    "pandas",
    "FastAPI",
    "Streamlit",
    "SQLAlchemy"
]

topic = st.selectbox(
    "What Python topic are you studying?",
    topics
)

tips = {
    "Python Basics": "Practice variables, loops, and functions.",
    "Data Structures": "Learn lists, dictionaries, sets, and tuples.",
    "pandas": "Practice filtering and grouping DataFrames.",
    "FastAPI": "Build REST endpoints using GET, POST, and PATCH.",
    "Streamlit": "Experiment with widgets and session state.",
    "SQLAlchemy": "Practice creating and querying database models."
}
st.info(tips[topic])

st.divider()

# ═════════════════════════════════
# Widget 3 — st.radio
# ═══════════════════════════════
st.subheader("3. Learning Style")
style = st.radio(
    "How do you learn best?",
    [
        "Reading docs",
        "Watching videos",
        "Building projects",
        "Pair programming"
    ],
    horizontal=True
)

if style == "Reading docs":
    st.write("Recommendation: Read the official Python documentation.")

elif style == "Watching videos":
    st.write("Recommendation: Follow a Python video tutorial.")

elif style == "Building projects":
    st.write("Recommendation: Build a small Python application.")

else:
    st.write("Recommendation: Practice coding with a partner.")
st.divider()

# ════════════════════════════════
# Widget 4 — st.multiselect
# ════════════════════════════════
st.subheader("4. Tools & Libraries You Use")
selected_tools = st.multiselect(
    "Which tools and libraries have you used?",
    [
        "pandas",
        "requests",
        "FastAPI",
        "Streamlit",
        "SQLite",
        "matplotlib",
        "SQLAlchemy"
    ],
    default=["requests", "Streamlit"]
)

if selected_tools:
    st.write("Your selected tools:")

    for tool in selected_tools:
        st.write(f"✅ {tool}")

else:
    st.warning("Select at least one tool.")

st.divider()

# ═══════════════════════════════════
# Widget 5 — st.text_input
# ══════════════════════════════════
st.subheader("5. Project Idea Generator")

project_keyword = st.text_input(
    "Enter a project keyword:",
    placeholder="Examples: weather, fitness, travel"
)

if project_keyword.strip():

    keyword = project_keyword.strip()

    st.write("Suggested Python projects:")

    st.write(
        f"1. A {keyword} tracker that stores data in SQLite."
    )
    st.write(
        f"2. A {keyword} dashboard built with Streamlit."
    )
    st.write(
        f"3. A {keyword} REST API built with FastAPI."
    )
    st.write(
        f"4. A {keyword} data analysis project using pandas."
    )
else:
    st.info("Enter a keyword to generate project ideas.")

st.divider()

# ════════════════════════════
# Widget 6 — st.checkbox
# ══════════════════════════════
st.subheader("6. Progress Summary")
show_summary = st.checkbox(
    "Show my personalized learning summary",
    value=True
)

if show_summary:

    tools_text = ",".join(selected_tools) if selected_tools else "None"

    project_text = (
        project_keyword.strip()
        if project_keyword.strip()
        else "Not entered"
    )

    st.success(
        f""" 
        **Your Python Learning Summary**

        -Experience: {weeks} weeks
        -Level: {level_label}
        -Current topic: {topic}
        -Learning style: {style}
        -Tools: {tools_text}
        -Project keyword: {project_text}
        """
    )
st.divider()

st.subheader("7. Learning Progress Calculator")

progress_percent = (weeks / 52) * 100

remaining_weeks = 52 - weeks

st.metric(
    label="Learning Goal Completion",
    value=f"{progress_percent:.1f}%"
)

st.progress(weeks / 52)

st.write(f"Weeks completed: {weeks}")
st.write(f"Weeks remaining: {remaining_weeks}")

if progress_percent == 100:
    st.success("Congratulations! You've reached your 52-week goal!")

elif progress_percent >= 50:
    st.info("You're more than halway to your goal!")

else:
    st.info("Keep learning! Every week counts.")