import pytest
from energia import zuzycie_roczne_kwh, koszt_roczny


def test_zuzycie_7w():
    # 7 W * 8760 h = 61320 Wh = 61.32 kWh
    assert zuzycie_roczne_kwh(7) == pytest.approx(61.32, abs=0.01)


def test_koszt_7w():
    # 61.32 kWh * 0.90 zl = 55.19 zl
    assert koszt_roczny(7, 0.90) == pytest.approx(55.19, abs=0.01)


def test_zuzycie_zerowe():
    assert zuzycie_roczne_kwh(0) == 0
