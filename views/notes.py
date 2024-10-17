import streamlit as st
import uuid

def notes_app():
    st.title("Notes App")

    # Initialize notes in session state if not present
    if 'notes' not in st.session_state:
        st.session_state.notes = []

    # Input for new note
    note_title = st.text_input("Enter note title (optional):")
    new_note = st.text_area("Create a new note:", height=100)
    if st.button("Add Note"):
        if new_note:
            note_id = str(uuid.uuid4())
            if not note_title:
                # If no title is provided, use the first line of the note as the title
                note_title = new_note.split('\n')[0]
            st.session_state.notes.append({"id": note_id, "title": note_title, "content": new_note})
            st.success("Note added successfully!")
        else:
            st.warning("Please enter some content for the note.")

    # Display and manage existing notes
    if st.session_state.notes:
        st.subheader("Your Notes:")
        for index, note in enumerate(st.session_state.notes):
            # Check if 'title' key exists in the note dictionary
            if 'title' in note:
                with st.expander(f"{note['title']}"):
                    st.text_area("Note content:", value=note["content"], height=200, key=f"note_{note['id']}", disabled=True)
                    if st.button("Delete", key=f"delete_{note['id']}"):
                        st.session_state.notes.remove(note)
                        st.rerun()
            else:
                st.error(f"Note {index + 1} is missing a title.")
    else:
        st.info("You haven't created any notes yet.")

notes_app()
