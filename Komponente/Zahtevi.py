zahtev1 = {
"verb": "GET",
"noun": "student",
"query": "ime='Jelena';prezime='Ilic'", 
"fields": "brindeksa; ime; prezime" 
}
zahtev2 = {
"verb": "GET",
"noun": "profesor",
"query": "ime='Imre'",
"fields": "ime; prezime; predmet"
}
zahtev3 = {
"verb": "GET",
"noun": "fakultet",
"query": "naziv='FTN'",
"fields": "naziv; brojstudenata"
}

zahtev4 = {
"verb": "POST",
"noun": "student",
"query": "idstudent=6; ime='Zdravko'; prezime='Milinkovic'; brindeksa='PR36/2019'",
"fields": ""
}
zahtev5 = {
"verb": "POST",
"noun": "profesor",
"query": "idprofesor=6; ime='Janko'; prezime='Radovanovic'; predmet='Matematika'",
"fields": ""
}
zahtev6 = {
"verb": "POST",
"noun": "fakultet",
"query": "idfakultet=6; naziv='PF'; brojstudenata=5000; grad='Novi Sad'",
"fields": ""
}

zahtev7 = {
"verb": "PATCH",
"noun": "student",
"query": "ime='Lana'; prezime='Slovic'",
"fields": "brindeksa='PR1/2022'"
}

zahtev8 = {
"verb": "PATCH",
"noun": "profesor",
"query": "ime='Milana'; prezime='Bojanic'",
"fields": "predmet='RVA'"
}
zahtev9 = {
"verb": "PATCH",
"noun": "fakultet",
"query": "naziv='FTN'; grad='Novi Sad'",
"fields": "brojstudenata=17000"
}

zahtev10 = {
"verb": "DELETE",
"noun": "student",
"query": "ime='Zdravko'",
"fields": ''
}

zahtev11 = {
"verb": "DELETE",
"noun": "profesor",
"query": "ime='Janko'",
"fields": ""
}

zahtev12 = {
"verb": "DELETE",
"noun": "fakultet",
"query": "naziv='PF'",
"fields": ""
}
# Dva nepravilna zahteva jer su verb i noun obavezna polja
zahtev13 = {
"verb": "",
"noun": "fakultet",
"query": "naziv='PF'",
"fields": ""
}

zahtev14 = {
"verb": "GET",
"noun": "",
"query": "naziv='PF'",
"fields": ""
}
# Dva nepravilna zahteva za get
zahtev15 = {
"verb": "GET",
"noun": "fakultet",
"query": "naziv='PF'"
}

zahtev16 = {
"verb": "GET",
"noun": "fakultet",
}
# Dva nepravilna zahteva za post
zahtev17 = {
"verb": "POST",
"noun": "student",
"fields": "ime"
}

zahtev18 = {
"verb": "POST",
"noun": "fakultet",
}
# Dva nepravilna zahteva za patch
zahtev19 = {
"verb": "PATCH",
"noun": "student",
"fields": "ime"
}

zahtev20 = {
"verb": "PATCH",
"noun": "student",
}
# Dva nepravilna zahteva za delete
zahtev21 = {
"verb": "DELETE",
"noun": "student",
"fields": "ime"
}

zahtev22 = {
"verb": "DELETE",
"noun": "student"
}
