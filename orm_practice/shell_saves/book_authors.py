# coding: utf-8
from apps.book_authors.models import *
Book.objects.get(id=5).name = "C#"
Author.objects.get(id=5).name = "Ketul"
Author.objects.all().first_name
Author.objects.get(id=5).first_name = "Ketul"
for author in Author.objects.all():
    print author.id
    print author.first_name
    
a1
a1 = Author(first_name = "Mike")
a1.save
a1.save()
a2 = Author(first_name = "Speros")
a2.save()
a3 = Author(first_name = "Jonh")
a3.save()
a4 = Author(first_name = "Jadee")
a4.save()
a5 = Author(first_name = "Jay")
a5.save()
Author.objects.get(id=5).name = "Ketul"
Book.objects.get(id_lt=3).authors.add(Author.objects.get(id=1))
Book.objects.filter(id_lt=3).authors.add(Author.objects.get(id=1))
Book.objects.filter(id__lt=3).authors.add(Author.objects.get(id=1))
Book.objects.get(id=1).authors.add(Author.objects.get(id=1))
print Book.objects.get(id=1).authors
print Book.objects.get(id=1).authors.first_name
for a in Book.objects.get(id=1).authors:
    print a.first_name
    
for a in Book.objects.get(id=1).authors:
    print a.first_name
    
b1 = Book.objects.get(id=1)
b1
b1.authors
b1.authors.all()
for a in b1.authors.all():
    print a.first_name
    
Book.object.get(id=2).authors.add(Author.objects.get(id=1))
Book.objects.get(id=2).authors.add(Author.objects.get(id=1))
b4 = Book.objects.get(id__let=4)
b4 = Book.objects.get(id__lt=4)
b4
b4 = Book.objects.get(id__lt=4).all()
b4 = []
b4 += Book.objects.get(id__lt=4).all()
b4 += [Book.objects.get(id__lt=4).all()]
for b in Book.objects.get(id__lt=4):
    b.authors.add(Author.objects.get(id=2))
    
a1
a1.book_set.all()
a2 = Author.objects.get(id=2)
for i in range(1, 4):
    Book.objects.authors.add(Author.objects.get(id=i))
    
for i in range(1, 4):
    Book.objects.get(id=i).authors.add(Author.objects.get(id=2))
    
    
for book in Book.objects.filter(id__lt=4):
    print book.authors
    
for book in Book.objects.filter(id__lt=4):
    for a in book.authors:
        print a.first_name
        
    
for a in Book.objects.filter(id__lt=4).authors:
    print a.first_name
    
for a in Book.objects.filter(id__lt=4).authors.all():
    print a.first_name
    
    
Book.objects.filter(id__lt=4)
bookpile = Book.objects.filter(id__lt=4)
for b in bookpile:
    print b.authors
    
for b in bookpile:
    print b.authors.all()
    
for b in bookpile:
    for a in b.authors.all():
        print a.first_name
        
print Books.objects.all()
print Book..object.all()
print Book.object.all()
print Book.objects.all()
for b in Book.objects.all():
    b.authors.add(Author.object.get(id=4))
    
for b in Book.objects.all():
    b.authors.add(Author.objects.get(id=4))
    
    
for b in Book.objects.all():
    print b.authors()
    
for b in Book.objects.all():
    print b
    
    
for b in Book.objects.all():
    print b.name
    
    
    
for b in Book.objects.all():
    print b.authors
    
    
    
    
for b in Book.objects.all():
    for a in b.authors:
        print a.first_name
        
    
    
    
    
for b in Book.objects.all():
    for a in b.authors.all():
        print a.first_name
        
        
    
    
    
    
for i in range(1,5):
    Book.objects.get(id=i).authors.add(Author.objects.get(id=3))
    
for a in Book.objects.get(id=3).authors.all():
    print a.first_name
    
for a in Book.objects.get(id=3).authors.get(id=5):
    print a.first_name
    
    
Book.objects.get(id=1).authors(id=5)
Book.objects.get(id=1).authors.get(id=5)
Book.objects.get(id=1).authors.all()
b1  = Book.objects.get(id=1)
b1
b1.authors.all()
b1.authors.all().get(id=5)
b1.authors.all().get(id=4)
b1.authors.all().get(id=4).first_name
b1.authors.get(id=4)
b1.authors.get(id=4).first_name
b1.authors.get(id=1)
b1.authors.get(id=1).first_name
b3 = Book.objects.get(id=3)
b3.authors.delete()
b3 = b3.authors.all()
b3.delete()
b3
Book.objects.get(id=3)
b3 = Book.objects.get(id=3)
a1 = Author.objects.get(id=1)
a1
a1.book_set.all()
a1books = a1.book_set.all()
for b in a1books:
    print b.name
    
b4 = Book.objects.get(id=4)
bauthors = b4.author_set.all()
get_ipython().magic(u'save book_authors 1-99')
