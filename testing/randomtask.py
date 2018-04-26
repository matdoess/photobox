import random

taskdict = {'kuss':'Küsst euch',
            'grimasse':'Schneide eine Grimasse',
            'model':'Mach eine Modelpose',
            'herz':'Mach ein Herz mit der Hand',
            'profil':'Lass ein Profil fotografieren',
            'prost':'Stoße mit jemandem an'}
taskshort = random.choice(list(taskdict.keys()))
tasklong = taskdict[taskshort]

print(tasklong)
print(taskshort)

##foo = ['a', 'b', 'c', 'd', 'e']
##print(random.choice(foo))