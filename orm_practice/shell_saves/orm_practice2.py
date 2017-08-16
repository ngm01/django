# coding: utf-8
# saved w/ iPython
from apps.dojo_ninjas.models import *
Dojos.create(name = "Foot Clan Dojo", city="New York", state="NY")
Dojos.objects.create(name = "Foot Clan", city="New York", state="NY")
dojo2 = Dojos(name="Master Splinter's Dojo", city="New York", state="NY")
dojo2.save()
dojo3 = Dojos(name="Deletion Dojo", city="Nowhere" state="KS")
dojo3 = Dojos(name="Deletion Dojo", city="Nowhere", state="XX")
Dojos.objects.all()
Dojos.objects.all().delete()
dojo3.save()
Dojos.objects.all()
Dojos.objects.all().delete()
Dojos.objects.all()
Dojos.objects.create(name="Foot Clan", city="New York", state="NY")
Dojos.objects.create(name="Turtle Dojo", city="New York", state="NY")
Dojos.objects.create(name="Strike Force Eagle II: The Return", city="classified", state="XX")
for dojo in Dojos.objects:
    print dojo.name
    
for dojo in Dojos.objects.all():
    print dojo.name
    
for dojo in Dojos.objects.all():
    print dojo.name, dojo.city, dojo.state
    
 
Ninjas.objects.create(dojo=Dojos.objects.get(name="Foot Clan"), first_name = "Shredder", last_name = "")
krang = Ninjas(dojo=Dojos.objects.get(id=1), first_name = "Krang", last_name = "!!!")
Dojos.objects.get(id=1)
for dojo in Dojos.objects.all():
    print dojo.id
    
krang = Ninjas(dojo=Dojos.objects.get(id=4), first_name = "Krang", last_name = "!!!")
krang.save()
Ninjas.objects.create(dojo=Dojos.objects.get(id=4), first_name = "Bebop", last_name = "the Warthog")
for ninja in Ninjas.objects.all():
    print ninja.first_name, ninja.last_name
    
leonardo = Ninjas(dojo=Dojos.objects.get(id=5), first_name = "Leonardo", last_name = "the turtle")
leonardo.save()
for ninja in Ninjas:
    print ninja.first_name, ninja.last_name
    
for ninja in Ninjas.objects.all()
    print ninja.first_name, ninja.last_name
    
for ninja in Ninjas.objects.all():
    print ninja.first_name, ninja.last_name
    
Ninjas.objects.create(dojo=Dojos.objects.get(id=5), first_name = "Donatello", last_name = 'the turtle')
Ninjas.objects.create(dojo=Dojos.obejcts.get(id=5), first_name = "Raphael", last_name = 'the turtle')
Ninjas.objects.create(dojo=Dojos.objects.get(id=5), first_name = "Raphael", last_name = 'the turtle')
for dojo in Dojos.objects.all():
    print dojo.id + ": " + dojo.name
    
for dojo in Dojos.objects.all():
    print str(dojo.id) + ": " + dojo.name
    
    
Ninjas.objects.create(dojo=Dojos.objects.get(id=6), first_name: "Codename:", last_name: "Striker")
Ninjas.objects.create(dojo=Dojos.objects.get(id=6), first_name= "Codename:", last_name= "Striker")
Ninjas.objects.create(dojo=Dojos.objects.get(id=6), first_name = "Codename:", last_name="Eagle")
Ninjas.objects.create(dojo=Dojos.objects.get(id=6), first_name = "Codename:", last_name="Larry")
Ninjas.objects.filter(dojo.id = 5)
for ninja in Ninjas.objects.all():
    print ninja.dojo
    
for ninja in Ninjas.objects.all():
    print ninja.dojo.id
    
    
foot_clan = Ninjas.objects.filter(dojo.id=4)
foot_clan = Ninjas.objects.filter(dojo_id=4)
print foot_clan
for ninja in foot_clan:
    print ninja.first_name, ninja.last_name
    
strikeforce = Ninjas.objects.filter(dojo_id=6)
for ninja in strikeforce:
    print ninja.first_name, ninja.last_name
    
for ninja in strikeforce:
    print ninja.first_name, ninja.last_name
    print ninja.dojo.name
    
get_ipython().magic(u'save ormpractice2 1-52')
