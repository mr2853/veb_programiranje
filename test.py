# ovde su svi atributi za predmet_view, treba videti koji se smeju menjati
# broj_predmeta=%(broj_predmeta)s, povrsina=%(povrsina)s, idinvestitor=%(idinvestitor)s, ime_investitor=%(ime_investitor)s, prezime_investitor=%(prezime_investitor)s, napomena_investitor=%(napomena_investitor)s, drzava_investitor=%(drzava_investitor)s, opstina_investitor=%(opstina_investitor)s, mesto_investitor=%(mesto_investitor)s, postanski_broj_investitor=%(postanski_broj_investitor)s, ulica_investitor=%(ulica_investitor)s, broj_ulica_investitor=%(broj_ulica_investitor)s, jmbg_investitor=%(jmbg_investitor)s, broj_mobilnog_investitor=%(broj_mobilnog_investitor)s, email_investitor=%(email_investitor)s, datum_merenja=%(datum_merenja)s, napomena_predmet=%(napomena_predmet)s, obradjivac=%(obradjivac)s, vrsta_teh_dok=%(vrsta_teh_dok)s, parcela=%(parcela)s, idkatastarska_opstina=%(idkatastarska_opstina)s, ulica_parcela=%(ulica_parcela)s, broj_ulice_parcela=%(broj_ulice_parcela)s, ukupno_uplaceno=%(ukupno_uplaceno)s, trenutno_uplaceno=%(trenutno_uplaceno)s, uplaceno=%(uplaceno)s,
    
l = ['broj_predmeta','povrsina','idinvestitor','ime_investitor','prezime_investitor','napomena_investitor','drzava_investitor','opstina_investitor','mesto_investitor','postanski_broj_investitor','ulica_investitor','broj_ulica_investitor','jmbg_investitor','broj_mobilnog_investitor','email_investitor','datum_merenja','napomena_predmet','obradjivac','vrsta_teh_dok','parcela','idkatastarska_opstina','ulica_parcela','broj_ulice_parcela','ukupno_uplaceno','trenutno_uplaceno','uplaceno']
res = ""
for i in range(len(l)):
    res += '{}=%({})s, '.format(l[i], l[i])

print(res)