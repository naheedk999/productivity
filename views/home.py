import streamlit as st

st.set_page_config(page_title="Productivity Hub", page_icon="📊", layout="wide")

st.title("🚀 Welcome to Your Productivity Hub!")

st.markdown("""
## Boost Your Efficiency and Achieve More!

Welcome to your personal productivity center. Here, you'll find powerful tools to help you manage your time, prioritize tasks, and stay focused on what matters most.

### 🛠️ Available Tools:

1. **⏲️ Pomodoro Timer**: Stay focused and manage your work intervals effectively.
2. **✅ Todo List**: Keep track of your tasks and never miss a deadline.
3. **🔢 Eisenhower Matrix**: Prioritize your tasks based on importance and urgency.

### 💡 Quick Tip of the Day:
""")

tips = [
    "Break large tasks into smaller, manageable chunks.",
    "Take regular breaks to maintain focus and productivity.",
    "Set clear, achievable goals for each day.",
    "Minimize distractions by turning off notifications during focused work.",
    "Celebrate your accomplishments, no matter how small!"
]

import random
st.info(random.choice(tips))

