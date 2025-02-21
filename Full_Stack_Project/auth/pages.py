import reflex as rx

from reflex_local_auth.pages import LoginState, login_form, PADDING_TOP

from ..ui.base import base_page

def my_login_page() -> rx.Component:
    
    return base_page(
        rx.center(
        rx.cond(
            LoginState.is_hydrated,  # type: ignore
            rx.card(login_form()),
        ),
        padding_top=PADDING_TOP,
    ),
        min_height="85vh",
    )

# def my_register_page() -> rx.Component:
    
#     return base_page(
#         register_page()
#     )