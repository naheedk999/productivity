import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

def habit_tracker():
    st.title("Habit Tracker")

    # Initialize session state for habits if not already present
    if 'habits' not in st.session_state:
        st.session_state.habits = []

    # Add new habit
    new_habit = st.text_input("Add a new habit:")
    if st.button("Add Habit"):
        if new_habit:
            st.session_state.habits.append({"name": new_habit, "history": {}})
            st.success(f"Habit '{new_habit}' added successfully!")

    # Display habits and allow marking completion
    if st.session_state.habits:
        st.write("### Your Habits:")
        
        # Get date range for the last 7 days
        today = datetime.now().date()
        date_range = [today - timedelta(days=i) for i in range(6, -1, -1)]

        # Create a DataFrame to display habits and their completion status
        data = []
        for habit in st.session_state.habits:
            row = [habit['name']]
            for date in date_range:
                row.append('✅' if habit['history'].get(str(date), False) else '❌')
            data.append(row)

        df = pd.DataFrame(data, columns=['Habit'] + [d.strftime('%m/%d') for d in date_range])
        st.dataframe(df, use_container_width=True)

        # Allow marking habits as complete for today
        st.write("### Mark habits as complete for today:")
        for i, habit in enumerate(st.session_state.habits):
            if st.button(f"Complete '{habit['name']}'", key=f"complete_{i}"):
                habit['history'][str(today)] = True
                st.success(f"'{habit['name']}' marked as complete for today!")
                st.rerun()

    else:
        st.info("No habits added yet. Add a habit to get started!")

    # Option to remove habits
    if st.session_state.habits:
        st.write("### Remove Habits:")
        habit_to_remove = st.selectbox("Select a habit to remove:", [habit['name'] for habit in st.session_state.habits])
        if st.button("Remove Habit"):
            st.session_state.habits = [habit for habit in st.session_state.habits if habit['name'] != habit_to_remove]
            st.success(f"Habit '{habit_to_remove}' removed successfully!")
            st.rerun()

habit_tracker()

