class Manga:
    def __init__(self, title, titleEN, chapters, author = "", cover = "", coverLink = ""):
        self.title = title
        self.titleEN = titleEN
        self.author = author
        self.chapters = chapters
        self.cover = cover
        self.coverLink = coverLink


class Chapter:
    def __init__(self, title, pages, size = 0):
        self.title = title
        self.pages = pages
        self.size = size


class Page:
    def __init__(self, title, link):
        self.title = title
        self.link = link