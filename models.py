from dataclasses import dataclass

from basemodels import BaseModel


@dataclass
class Blog(BaseModel):
    preview: str
    title: str
    date: str
    content: str
    author: str
    comment_count: int


@dataclass
class Category(BaseModel):
    name: str
    posts_count: int


@dataclass
class Comment(BaseModel):
    photo: str
    user: str
    date: str
    text: str


@dataclass
class Tag(BaseModel):
    name: str


@dataclass
class Recommendation(BaseModel):
    user: str
    photo: str
    review: str


@dataclass
class Product(BaseModel):
    image: str
    name: str
    price: int


if __name__ == '__main__':
    pass
