"""Raport: ile rocznie zjada sprzet pracujacy non-stop."""

from energia import zuzycie_roczne_kwh, koszt_roczny, moc_lacznie_w
from urzadzenia import INWENTARZ

CENA_DOMYSLNA = 1.04  # zl/kWh brutto, taryfa G11, srednia krajowa 2026


def raport(cena_kwh: float = CENA_DOMYSLNA) -> None:
    print(f"{'Urzadzenie':<48}{'szt':>4}{'W':>8}{'kWh/rok':>10}{'zl/rok':>9}")
    print("-" * 79)
    for u in sorted(INWENTARZ, key=lambda x: -x.moc_lacznie_w):
        kwh = zuzycie_roczne_kwh(u.moc_lacznie_w)
        print(f"{u.nazwa:<48}{u.sztuk:>4}{u.moc_lacznie_w:>8.1f}"
              f"{kwh:>10.1f}{kwh * cena_kwh:>9.2f}")
    print("-" * 79)
    w = moc_lacznie_w(INWENTARZ)
    print(f"{'RAZEM':<48}{'':>4}{w:>8.1f}"
          f"{zuzycie_roczne_kwh(w):>10.1f}{koszt_roczny(w, cena_kwh):>9.2f}")
    print(f"\nPrzy cenie {cena_kwh:.2f} zl/kWh. Miesiecznie: "
          f"{koszt_roczny(w, cena_kwh)/12:.2f} zl")


if __name__ == "__main__":
    raport()
    print("\nWrazliwosc na cene energii:")
    w = moc_lacznie_w(INWENTARZ)
    for c, kto in [(0.97, "Tauron"), (0.98, "Enea"), (1.04, "srednia PL"),
                   (1.10, "PGE"), (1.32, "Energa, cena max")]:
        print(f"  {c:.2f} zl/kWh ({kto:<16}) -> {koszt_roczny(w, c):>7.2f} zl/rok")
