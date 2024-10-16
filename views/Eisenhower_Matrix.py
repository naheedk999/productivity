import streamlit as st
import pandas as pd

def create_eisenhower_matrix():
    st.title("Eisenhower Matrix")

    tasks = {}
    nt = st.number_input("Enter the number of tasks:", min_value=1, value=1, step=1)

    for i in range(1, int(nt) + 1):
        task = st.text_input(f"Enter your task #{i}:")
        col1, col2 = st.columns(2)
        with col1:
            imp = st.checkbox(f"Is task #{i} important?")
        with col2:
            urg = st.checkbox(f"Is task #{i} urgent?")
        
        if task:
            tasks[task] = [imp, urg]

    if st.button("Generate Eisenhower Matrix"):
        matrix = {
            'Do First': [],
            'Schedule': [],
            'Delegate': [],
            'Eliminate': []
        }
        for task, (important, urgent) in tasks.items():
            if important and urgent:
                matrix['Do First'].append(task)
            elif important and not urgent:
                matrix['Schedule'].append(task)
            elif not important and urgent:
                matrix['Delegate'].append(task)
            else:
                matrix['Eliminate'].append(task)

        st.subheader("Eisenhower Matrix:")
        
        # Create a DataFrame for the matrix
        df = pd.DataFrame({
            'Urgent': ['Do First', 'Delegate'],
            'Not Urgent': ['Schedule', 'Eliminate']
        }, index=['Important', 'Not Important'])

        # Style the DataFrame
        def highlight_cells(val):
            return 'background-color: #002b36; font-weight: bold;'

        styled_df = df.style.map(highlight_cells)

        # Display the matrix as a table
        st.table(styled_df)

        # Display tasks in each quadrant
        for quadrant in matrix:
            with st.expander(f"{quadrant} Tasks"):
                if matrix[quadrant]:
                    for task in matrix[quadrant]:
                        st.write(f"• {task}")
                else:
                    st.write("No tasks in this category.")

create_eisenhower_matrix()
