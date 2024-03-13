from voto import Libretto, Voto

lib = Libretto ()

v1 = Voto("Analisi 1", 10, 28, False, "2022-01-30")
lib.append(v1)
lib.append(Voto("Fisica 1", 10, 25, False, "2022-07-12"))
lib.append(Voto("Analisi 2", 8, 30, True, "2023-02-15"))

voti25 = (lib.findByPunteggio(25, False))

for v in voti25:
    print(v.esame)

voto_analisi2 = lib.findByEsame("Analisi 2")
if voto_analisi2 is None:
    print("Nessun voto trovato")
else:
    print (f"Hai preso {voto_analisi2.str_punteggio()}")
try:
    voto_analisi2 = lib.findByEsame2("Analisi 3")
    print(f"Hai preso {voto_analisi2.str_punteggio}")
except ValueError:
    print("Nessun voto trovato")
nuovo1 = Voto("Fisica 1", 10, 25, False, "2022-07-13")
nuovo2 = Voto("Fisica 2", 10, 25, False, "2022-07-13")
print("1)", lib.has_voto(nuovo1))
print("2)", lib.has_voto(nuovo2))

