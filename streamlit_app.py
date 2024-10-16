import streamlit as st

home = st.Page(
    page="views/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)

about_me = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
)

page1 = st.Page(
    page="views/pomodoro.py",
    title="Pomodoro",
    icon=":material/timer:",
)

page2 = st.Page(
    page="views/todo.py",
    title="Todo",
    icon=":material/checklist:",
)

page3 = st.Page(
    page="views/Eisenhower_Matrix.py",
    title="Eisenhower Matrix",
    icon=":material/thumb_up:",
)

pg = st.navigation(
    {
        "Main": [home, about_me],
        "Tools": [page1, page2, page3]
    }
)

pg.run()

