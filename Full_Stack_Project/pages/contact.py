import reflex as rx

from .. import navigation

from ..ui.base import base_page

class ContactState(rx.State):
    form_data: dict = {}
    did_submit: bool = False
    
    # @rx.event
    def handle_submit(self, form_data: dict):
        # """Handle the form submit."""
        print(form_data)
        self.form_data = form_data
        self.did_submit = True

@rx.page(route=navigation.routes.CONTACT_US_ROUTE)

def contact_page() -> rx.Component:
    my_form = rx.form(
                rx.vstack(
                    rx.hstack(
                        rx.input(
                            name="first_name",
                            placeholder="First Name",
                            required=True,
                            type="text",
                            width="100%",
                        ),
                        rx.input(
                            name="last_name",
                            placeholder="Last Name",
                            type="text",
                            width="100%",
                        ),
                        width="100%",
                    ),
                    rx.input(
                        name="email",
                        placeholder="Your email",
                        type="email",
                        width="100%",
                    ),
                    # rx.hstack(
                    #     rx.checkbox("Checked", name="check"),
                    #     rx.switch("Switched", name="switch"),
                    # ),
                    rx.text_area(
                        name="message",
                        placeholder="Your message",
                        required=True,
                        type="text",
                        width="100%",
                    ),
                    rx.button("Submit", type="submit"),
                ),
                on_submit=ContactState.handle_submit,
                reset_on_submit=False,
    )
    my_child = rx.vstack(
            rx.heading("Contact", size="9"),
            rx.cond(ContactState.did_submit, ContactState.form_data.to_string(), ""),
            rx.desktop_only(
                rx.box(
                    my_form,
                    # id="my-form-box",
                    width="50vw",
                ),
            ),
            rx.tablet_only(
                rx.box(
                    my_form,
                    # id="my-form-box",
                    width="75vw",
                ),
            ),
            rx.mobile_only(
                rx.box(
                    my_form,
                    # id="my-form-box",
                    width="85vw",
                ),
            ),
            # rx.text(
            #     "Our Contact",
            # ),
            # my_form,
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            # id="my-child",
        )
    return base_page(my_child)
