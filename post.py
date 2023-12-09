from attr import dataclass


@dataclass
class Post:
    title: str
    content: str