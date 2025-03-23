import reflex as rx

from ..ui.base import base_page

from . import forms

from .state import BlogEditFormState

# class EditExampleState(rx.State):
#     title: str = "Hello World"
#     content: str = "This is my blog post"
    
#     def handle_submit(self, form_data: dict):
#         print(form_data)
#         # self.form_data = form_data
    
#     # def handle_content_change(self, value):
#     #     self.content = value


    
def blog_post_edit_page() -> rx.Component:
    my_form = forms.blog_post_edit_form()
    post = BlogEditFormState.post
    my_child = rx.vstack(
            rx.heading("Editing ", post.title, size="9"),
            # rx.text(ContactState.timeleft_label),
            # rx.cond(state.ContactState.did_submit, state.ContactState.thank_you, ""),
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
            # justify="center",
            align="center",
            min_height="95vh",
            # id="my-child",
        )
    return base_page(my_child)
