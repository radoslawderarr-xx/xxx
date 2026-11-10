# Kalkulator kosztu energii — sprzet pracujacy non-stop

Liczy roczne zuzycie i koszt dla urzadzen, ktore sa wlaczone caly czas:
serwer domowy, router, bramki Zigbee, zarowki smart w czuwaniu, przekazniki.

## Uzycie

```bash
python3 raport.py      # tabela wszystkich urzadzen + suma + wrazliwosc na cene
```

```python
from energia import koszt_roczny, koszt_lacznie
from urzadzenia import INWENTARZ

koszt_roczny(7, 1.04)            # jedno urzadzenie 7 W -> 63.77 zl/rok
koszt_lacznie(INWENTARZ, 1.04)   # caly zestaw
```

## Inwentarz

Lista urzadzen jest w `urzadzenia.py`. Kazdy wpis ma pole `zrodlo`:

- `"typowa"` — wartosc orientacyjna dla tej klasy sprzetu
- `"zmierzona"` — odczyt z gniazdka z pomiarem mocy albo z Home Assistant

**Wszystkie obecne wartosci sa typowe.** Zeby raport byl wiarygodny, podmien je
na pomiary — gniazdko z pomiarem mocy albo encja `sensor.*_power` w HA.

## Cena energii

Domyslnie 1,04 zl/kWh brutto — srednia krajowa w taryfie G11 na 2026 r.,
z dystrybucja. Realny zakres u dystrybutorow: 0,97–1,32 zl/kWh.
Swoja stawke znajdziesz na fakturze (pozycja za energie czynna + dystrybucja zmienna).

## Testy

```bash
pytest -q
```
