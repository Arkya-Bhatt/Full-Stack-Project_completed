from typing import Optional, List

import reflex as rx

from sqlmodel import select

from .model import BlogPostModel

class BlogPostState(rx.State):
    posts: List['BlogPostModel'] = []
    post: Optional['BlogPostModel'] = None
    post_content: str = ""
    
    @rx.var
    def blog_post_id(self):
        # print(self.router.page.params)
        return self.router.page.params.get("blog_id", "")
    
    def get_post_detail(self):
        with rx.session() as session:
            if self.blog_post_id == "":
                self.post = None
                return
            result = session.exec(
                select(BlogPostModel).where(
                    BlogPostModel.id == self.blog_post_id,
                )
            ).one_or_none()
            self.post = result
            self.post_content = self.post.content
        # return
    
    def load_posts(self):
        with rx.session() as session:
            result = session.exec(
                select(BlogPostModel)
            ).all()
            self.posts = result
        # return
        
    def add_post(self, form_data: dict):
        with rx.session() as session:
            post = BlogPostModel(**form_data)
            # print("adding\n", post)
            session.add(post)
            session.commit()
            session.refresh(post)
            # print("added\n", post)
            self.post = post
        # return
    
    def save_post_edits(self, post_id: int, updated_data: dict):
        with rx.session() as session:
            post = session.exec(
                select(BlogPostModel).where(
                    BlogPostModel.id == post_id,
                )
            ).one_or_none()
            if post is None:
                return
            for key, value in updated_data.items():
                setattr(post, key, value)
            session.add(post)
            session.commit()
            session.refresh(post)
            # post.title = updated_data.get("title")
            # post = BlogPostModel(**form_data)
            # # print("adding\n", post)
            # session.add(post)
            # session.commit()
            # session.refresh(post)
            # # print("added\n", post)
            # self.post = post
        # return
    
    # def get_post(self):
    #     with rx.session() as session:
    #         result = session.exec(
    #             select(BlogPostModel)
    #         )
    #         self.posts = result
    #     # return
     
class BlogAddPostFormState(BlogPostState):
    form_data: dict = {}
    
    def handle_submit(self, form_data):
        self.form_data = form_data
        self.add_post(form_data)
        # redirect

class BlogEditFormState(BlogPostState):
    form_data: dict = {}
    # post_content: str = ""
    
    def handle_submit(self, form_data):
        self.form_data = form_data
        post_id = form_data.pop("post_id")
        updated_data = {**form_data}
        self.save_post_edits(post_id, updated_data)
        # redirect