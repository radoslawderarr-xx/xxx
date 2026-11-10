"""Liczenie kosztu energii dla urzadzen pracujacych w trybie ciaglym."""

GODZIN_W_ROKU = 24 * 365


def zuzycie_roczne_kwh(moc_w: float) -> float:
    """Zuzycie energii w kWh dla urzadzenia o mocy `moc_w` watow pracujacego caly rok."""
    return moc_w * GODZIN_W_ROKU / 1000  # Wh -> kWh


def koszt_roczny(moc_w: float, cena_kwh: float) -> float:
    """Roczny koszt pracy urzadzenia w zlotowkach."""
    return zuzycie_roczne_kwh(moc_w) * cena_kwh
