from Crypto.Util.number import inverse, long_to_bytes

n = 580642391898843192929563856870897799650883152718761762932292482252152591279871421569162037190419036435041797739880389529593674485555792234900969402019055601781662044515999210032698275981631376651117318677368742867687180140048715627160641771118040372573575479330830092989800730105573700557717146251860588802509310534792310748898504394966263819959963273509119791037525504422606634640173277598774814099540555569257179715908642917355365791447508751401889724095964924513196281345665480688029639999472649549163147599540142367575413885729653166517595719991872223011969856259344396899748662101941230745601719730556631637
e = 65537
ct = 320721490534624434149993723527322977960556510750628354856260732098109692581338409999983376131354918370047625150454728718467998870322344980985635149656977787964380651868131740312053755501594999166365821315043312308622388016666802478485476059625888033017198083472976011719998333985531756978678758897472845358167730221506573817798467100023754709109274265835201757369829744113233607359526441007577850111228850004361838028842815813724076511058179239339760639518034583306154826603816927757236549096339501503316601078891287408682099750164720032975016814187899399273719181407940397071512493967454225665490162619270814464

factors = [13099895578757581201,16656402470578844539,12132158321859677597,14963354250199553339,12834461276877415051,14278240802299816541, 14178869592193599187, 11492065299277279799, 10336650220878499841, 12955403765595949597, 10638241655447339831, 11403460639036243901, 12973972336777979701, 14100640260554622013, 11665347949879312361, 11328768673634243077,9303850685953812323, 11530534813954192171, 15998365463074268941, 13572286589428162097, 11282698189561966721, 9389357739583927789, 15824122791679574573, 17281246625998849649, 15669758663523555763, 14523070016044624039, 17138336856793050757, 11473665579512371723,9282105380008121879, 16898740504023346457, 15364597561881860737, 17174065872156629921]

l = 1
for f in factors:
    l *= (f-1)

d = inverse(e, l)

m = pow(ct, d, n)
Flag= long_to_bytes(m)
print(Flag)