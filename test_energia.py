import pytest
from energia import (zuzycie_roczne_kwh, koszt_roczny,
                     moc_lacznie_w, koszt_lacznie)
from urzadzenia import Urzadzenie, INWENTARZ


def test_zuzycie_7w():
    # 7 W * 8760 h = 61320 Wh = 61.32 kWh
    assert zuzycie_roczne_kwh(7) == pytest.approx(61.32, abs=0.01)


def test_koszt_7w():
    assert koszt_roczny(7, 1.04) == pytest.approx(63.77, abs=0.01)


def test_zuzycie_zerowe():
    assert zuzycie_roczne_kwh(0) == 0


def test_sztuki_mnoza_moc():
    assert Urzadzenie("x", 0.9, sztuk=7).moc_lacznie_w == pytest.approx(6.3)


def test_moc_lacznie_sumuje_sztuki():
    zestaw = [Urzadzenie("a", 10), Urzadzenie("b", 2, sztuk=3)]
    assert moc_lacznie_w(zestaw) == pytest.approx(16)


def test_koszt_lacznie_zgadza_sie_z_recznym():
    zestaw = [Urzadzenie("a", 10), Urzadzenie("b", 2, sztuk=3)]
    assert koszt_lacznie(zestaw, 1.04) == pytest.approx(16 * 8760 / 1000 * 1.04, abs=0.01)


def test_inwentarz_ma_dodatnie_moce():
    assert INWENTARZ, "inwentarz nie moze byc pusty"
    assert all(u.moc_lacznie_w > 0 for u in INWENTARZ)
