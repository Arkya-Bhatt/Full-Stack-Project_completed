import reflex as rx

from reflex_local_auth.pages import login_page, register_page

from ..ui.base import base_page

def my_login_page() -> rx.Component:
    
    return base_page(
        login_page()
    )

def my_register_page() -> rx.Component:
    
    return base_page(
        register_page()
    )