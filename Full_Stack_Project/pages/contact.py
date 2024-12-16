import reflex as rx

from ..ui.base import base_page

def contact_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("Contact", size="9"),
            rx.text(
                "Our Contact",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            # id="my-child",
        )
    return base_page(my_child)