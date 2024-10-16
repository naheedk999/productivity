import streamlit as st

st.title("Todo List")

# Initialize session state for tasks if not already present
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Input for new task
new_task = st.text_input("Add a new task:")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"task": new_task, "completed": False})
        st.success(f"Task '{new_task}' added successfully!")

# Display tasks
if st.session_state.tasks:
    st.write("### Tasks:")
    for i, task in enumerate(st.session_state.tasks):
        col1, col2, col3 = st.columns([3, 1, 1])
        with col1:
            st.write(f"{'✅' if task['completed'] else '❌'} {task['task']}")
        with col2:
            if st.button("Complete", key=f"complete_{i}"):
                st.session_state.tasks[i]['completed'] = True
                st.rerun()
        with col3:
            if st.button("Delete", key=f"delete_{i}"):
                st.session_state.tasks.pop(i)
                st.rerun()
else:
    st.info("No tasks yet. Add a task to get started!")

# Display statistics
completed_tasks = sum(task['completed'] for task in st.session_state.tasks)
total_tasks = len(st.session_state.tasks)

st.write("---")
st.write(f"Total tasks: {total_tasks}")
st.write(f"Completed tasks: {completed_tasks}")
st.write(f"Pending tasks: {total_tasks - completed_tasks}")

# Option to clear all tasks
if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.success("All tasks cleared!")
    st.rerun()
