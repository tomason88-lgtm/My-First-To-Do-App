import streamlit as st
import funcy
# To run - write in terminal: streamlit run web.py

todos = funcy.get_todos()


def add_todo():
    todo_loc = st.session_state['new_todo'] + '\n'
    todo_loc = todo_loc.title()
    todos.append(todo_loc)
    funcy.write_todos(todos)


# Gemini suggestion



st.title('What should I do?')
st.subheader("This is my to-do app")
st.write('This app is to increase your productivity')

st.text_input(label=" ", placeholder='Add a new to-do',
              on_change=add_todo, key='new_todo')

# Define buttons:
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

# Make list of todos and use buttons:
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)


    def edit_todo(i=index):
        new_todo = st.session_state[f'edit_text_{i}']
        todo_loc = new_todo.title() + '\n'
        todos[i] = todo_loc
        funcy.write_todos(todos)
    if checkbox:
        if edit_button:
            st.text_input(
                label=" ",
                placeholder=f"Enter new text for: {todo.strip()}",
                on_change=edit_todo,  # Call our new replacement function
                key=f'edit_text_{index}'  # Unique key for each edit box
            )

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
