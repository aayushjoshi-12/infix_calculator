import reflex as rx
from calculator import style
from calculator.state import State
from calculator import keypad

#-----to do-----
#add some more design elements 
#add more functionality and learn animations in reflex

def display()->rx.Component:
    return rx.box(
        rx.text(State.ans,margin_x="0.7em",margin_y="0.7em"),
        rx.text(State.expression,position="relative",margin_x="0.7em",top="1em",font_size="30px"),
        style=style.display_style,
    )

def index() -> rx.Component:
    return rx.container(
        rx.box(
            rx.vstack(
                rx.heading("Infix Calculator",style=style.head_style),
                rx.box(
                    # rx.box(
                    #     style=style.shape_style
                    # ),
                    display(),
                    keypad.keypad(),
                    style=style.base_style,
                ),
            ),
        ),
        style=style.page_style
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
