# coding: utf-8
from apps.likes_books.models import *
Book.objects.all()
u2 = User.objects.get(id=2)
Book.objects.create(name="Java", desc="coffee", uploader = u2)
Book.objects.create(name="MySql", desc="Mice Equal", uploader=u2)
Book.objects.all()
u3 = User.objects.get(id=3)
Book.objects.create(name="MEAN", desc="google's stack", uploader=u3)
Book.objects.create(name="Angular", desc="front end framework", uploader=u3)
Book.objects.all()
u1
u1 = User.objects.first()
u1
u1.liked_books.add(Book.objects.first(), Book.objects.last())
u1.liked_books
u1.liked_books.all()
u2.liked_books.add(Book.objects.first(), Book.objects.get(id=2))
u2.liked_books.all()
u3.liked_books.add(Book.objects.all())
for book in Book.objects.all():
    print book
    
for book in Book.objects.all():
    u3.liked_books.add(book)
    
    
u3.liked_books.all()
for user in User.objects.all():
    print user.first_name, user.last_name
    
Book.objects.first().liked_users.all()
Book.objects.first().uploader
Book.objects.get(id=2).liked_users.all()
Book.objects.get(id=2).uploader
get_ipython().magic(u'save likes_books_orm_practice 1-28')
