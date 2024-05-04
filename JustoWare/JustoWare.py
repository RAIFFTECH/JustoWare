from rxconfig import config
#from justo_creditos import Liquida_cre
import reflex as rx


class State(rx.State):
    count = 0
    def incremento(self):
        self.count += 1
    def decremento(self):
        self.count -= 1


def index():
    return rx.center(
        rx.hstack(
            rx.button(
                "Decrecer",
                color_scheme="red",
                border_radius="1em",
                on_click=State.decremento
            ),
            rx.heading(State.count,font_size="2em"),
            rx.button(
                "Incrementar",
                color_scheme="green",
                border_radius="1em",
                on_click=State.incremento
            ),
        )
    )
 
#miclase = Liquida_cre() 
app = rx.App()
app.add_page(index)
app.compile