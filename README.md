# Kalkulator kosztu energii

Liczy roczne zuzycie i koszt dla urzadzen pracujacych w trybie ciaglym —
czujniki, bramki Zigbee, routery, serwery domowe.

```python
from energia import koszt_roczny
koszt_roczny(7, 0.90)   # 7 W przy 0,90 zl/kWh -> 55.19 zl/rok
```

## Testy

```
pytest -q
```
