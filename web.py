import streamlit as st
import funcy

todos = funcy.get_todos()


def add_todo():
    todo_loc = st.session_state['new_todo'] + '\n'
    todo_loc = todo_loc.capitalize()
    todos.append(todo_loc)
    funcy.write_todos(todos)


def edit_todo():
    todo_loc = st.session_state['edit_todo'] + '\n'
    todo_loc = todo_loc.capitalize()
    todos.append(todo_loc)
    funcy.write_todos(todos)




st.title('נו מה לעשות?')
st.subheader("This is my to-do app")
st.write('This app is to increase your productivity')

st.text_input(label=" ", placeholder='Add a new to do',
              on_change=add_todo, key='new_todo')

col1, col2 = st.columns([1, 1])

with col1:
    edit_button = st.button('Edit',
                            key="edit_button",
                            help="Click to edit the to-do",
                            type="primary",
                            icon=":material/lightbulb:",
                            width='content'
                            )

with col2:
    complete_button = st.button('Complete',
                                key="complete_button",
                                help="Click to complete the to-do",
                                type="primary",
                                icon=":material/lightbulb:",
                                width='content'
                                )

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        if edit_button:
            edited = st.text_input(label=" ", placeholder=f"{todo}",
                                   on_change=edit_todo, key='edit_todo')
            todos[index] = edited

        elif complete_button:
            todos.pop(index)
            funcy.write_todos(todos)
            del st.session_state[todo]
            st.rerun()


text = """
Principles of productivity:  
---------------------------  
  
* Mark your progress.  
* Summarize daily, weekly, monthly. 
* Manage distractions.  
* Theory-to-practice time ratio should be about 1:5.  
* Short deep focus is better prolong day.  
* Systemize all that is repetitive.  
"""
st.write(text)
