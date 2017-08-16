# coding: utf-8
#saved from iPython
from apps.users.models import *
User.objets.all()
User.objects.all()
User.objects.create(first_name="Bob", last_name="Slob", email="bob@slob.com", age=1000)
User.objects.create(first_name="Bob", last_name="Slob", email_address="bob@slob.com", age=1000)
doug = User(first_name="Doug", last_name="Slug")
doug.email_address = "doug@slug.gov"
doug.age = 3000000
User.objects.all()
soug
doug
User.get_last()
User.objects.last()
User.objects.last().first_name
doug.save
User.objects.last().first_name
User.objects.all()
doug
User.objects.count()
clear
doug.save()
User.objects.last().first_name
User.objects.all()
User.objects.get(id=2).last_name
Users.objects.order_by(first_name)
User.objects.order_by(first_name)
User.objects.order_by("first_name")
User.objects.order_by("first_name").first_name
User.objects.order_by("-first_name")
for user in User.objects.order_by("first_name"):
    print user.first_name
    
frank = User(first_name = "Frank", last_name = "Dank", email_address = "frank@dank.gov", age=99)
frank.save()
update = User.objects.get(id=3)
update
update.last_name = "Stank"
update.save()
update.last_name
User.objects.get(id=3).first_name
User.objects.create(first_name = "Gary", last_name = "Scary", email_address = "gary@scary.edu", age=100)
User.objects.get(id=4).delete()
get_ipython().magic(u'save orm_practice1')
get_ipython().magic(u'save orm_practice1 1-42')
