import streamlit as st
import streamlit.components.v1 as components
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
## st.page_link("https://forms.office.com/r/6g0DgBXLLS?origin=lprLink", label="Please click here for Suggestion Form to get more Out of Box Experience", icon=":material/question_answer:")
# Your HTML content (paste the entire HTML from the immersive block above here)
# Make sure to replace 'https://forms.office.com/Pages/ResponsePage.aspx?id=...'
# with the actual embed URL of YOUR Microsoft Form.
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Embedded Microsoft Form</title>
    <style>
        body {
            font-family: 'Inter', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f0f2f5;
        }
        .form-container {
            width: 100%;
            max-width: 1200px; /* Max width for larger screens */
            height: 1000px; /* Fixed height for the iframe */
            background-color: #ffffff;
            border-radius: 5px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            overflow: hidden; /* Ensures iframe stays within bounds */
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 20px;
            box-sizing: border-box; /* Include padding in width/height */
        }
        iframe {
            width: 100%;
            height: 100%;
            border: none;
            border-radius: 1px;
        }
        h1 {
            color: #333;
            margin-bottom: 5px;
            font-size: 1.8em;
            text-align: center;
        }
        p {
            color: #666;
            margin-bottom: 5px;
            text-align: center;
            line-height: 1.5;
        }

        /* Responsive adjustments */
        @media (max-width: 1080px) {
            .form-container {
                height: 500px; /* Adjust height for smaller screens */
                padding: 10px;
            }
            h1 {
                font-size: 1.5em;
            }
        }

        @media (max-width: 80px) {
            .form-container {
                height: 600px; /* Further adjust height for mobile */
                padding: 5px;
                border-radius: 4px;
            }
            h1 {
                font-size: 1.2em;
            }
            p {
                font-size: 0.9em;
            }
        }
    </style>
    <!-- Tailwind CSS CDN for general utility classes if needed, though custom CSS is used here -->
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body>
    <div class="form-container">
        <h1>Please Fill Out Our Form for Enhance User Experience</h1>
        <p>Your feedback is important to us. Kindly complete the form below.</p>
        <iframe
            src="https://forms.office.com/r/6g0DgBXLLS?origin=lprLink"
            frameborder="0"
            marginwidth="0"
            marginheight="0"
            style="border: none; max-width:100%; max-height:100vh"
            allowfullscreen
            webkitallowfullscreen
            mozallowfullscreen
            msallowfullscreen
        >
            Loading...
        </iframe>
    </div>
</body>
</html>
"""

st.set_page_config(layout="wide") # Optional: Use wide layout for better display


# Embed the HTML content
# The height parameter is crucial for the iframe to be visible in Streamlit
components.html(html_content, height=1080, scrolling=True)

st.markdown("---")
st.markdown("Made with ❤️ for Indian job seekers by PriciplePath ")
