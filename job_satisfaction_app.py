import streamlit as st

st.set_page_config(page_title="Lifetime Job Satisfaction Planner", layout="centered")

# Title
st.title("📈 Lifetime Job Satisfaction Planner in India")
st.write("A smart assistant to guide your career with long-term satisfaction and stability.")

# Sidebar inputs
st.sidebar.header("👤 User Profile")
age = st.sidebar.slider("Your Age", 15, 70, 25)
career_stage = st.sidebar.selectbox("Career Stage", [
    "Student (15-25)",
    "Early Career (22-35)",
    "Mid Career (35-50)",
    "Late Career / Freedom Phase (50+)"
])
stress = st.sidebar.slider("Current Stress Level", 0, 10, 5)
growth = st.sidebar.slider("Career Growth Satisfaction", 0, 10, 5)
income = st.sidebar.slider("Income Satisfaction", 0, 10, 5)
purpose = st.sidebar.slider("Sense of Purpose", 0, 10, 5)

# Dynamic recommendation logic
def get_recommendations():
    score = (income + growth + purpose - stress) / 5
    recommendations = []

    if career_stage == "Student (15-25)":
        recommendations += [
            "✅ Explore internships on Internshala or LinkedIn.",
            "✅ Take NPTEL/Coursera courses based on your interests.",
            "✅ Match your skills with trending job markets (AI, biotech, etc)."
        ]
    elif career_stage == "Early Career (22-35)":
        recommendations += [
            "💼 Switch jobs every 2-3 years to grow skills & salary.",
            "💰 Start SIPs and invest 25% of your salary.",
            "📚 Consider an MBA, MTech, or online upskilling."
        ]
    elif career_stage == "Mid Career (35-50)":
        recommendations += [
            "🧘 Focus on work-life balance.",
            "🚀 Pivot if your current field feels stagnant.",
            "🏡 Invest in long-term assets like real estate/business."
        ]
    elif career_stage == "Late Career / Freedom Phase (50+)":
        recommendations += [
            "👨‍🏫 Consider part-time teaching or mentoring.",
            "📹 Share your experience on YouTube/Udemy.",
            "🎯 Focus on hobbies, health, and legacy."
        ]

    if score < 3:
        recommendations.append("⚠️ Your satisfaction is very low. Consider therapy, job change, or sabbatical.")
    elif score < 6:
        recommendations.append("🔁 You're in a transition zone. Re-evaluate your goals.")
    else:
        recommendations.append("✅ You are on the right track. Stay consistent!")

    return score, recommendations

# Display results
score, advice = get_recommendations()

st.subheader("🧠 Your Career Satisfaction Score")
st.metric(label="Score (out of 10)", value=round(score * 2, 1))
st.text("​💔​ >10 Score shows lies in a user's real life")

st.subheader("📌 Personalized Recommendations")

for item in advice:
    st.write("-", item)
st.page_link("https://forms.office.com/r/6g0DgBXLLS?origin=lprLink", label="Please click here for Suggestion Form to get more Out of Box Experience", icon=":material/question_answer:")
st.markdown("---")
st.markdown("Made with ❤️ for Indian job seekers by PriciplePath")
