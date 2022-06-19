class Lib:
    def __init__(self):
      self.egz = []
      self.ludzie = []

    def books(self):
        result = []
        for book in self.egz:
            t = (book.title, book.author, self.egz.count(book))
            result.append(t)
        result_set = set(result)     
        result_set = sorted(result_set, key = lambda y: y[0])
        return result_set

class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year= year

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.title == other.title
        return False



library = Lib()

new_egz =int(input())
Book = []
for n in range(new_egz):
  text = eval(input())
  title = text[0]
  author = text[1]
  year = text[2]
  egz = Book(title, author, year)
  library.egz.append(egz)

for book in library.books():
    print(book)