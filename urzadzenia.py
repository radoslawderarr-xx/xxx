"""Inwentarz urzadzen pracujacych w trybie ciaglym (24/7).

Pole `zrodlo` mowi, skad pochodzi wartosc mocy:
  "typowa"   - wartosc orientacyjna dla tej klasy urzadzen, do zastapienia pomiarem
  "zmierzona" - odczyt z gniazdka z pomiarem mocy albo z Home Assistant
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Urzadzenie:
    nazwa: str
    moc_w: float
    sztuk: int = 1
    zrodlo: str = "typowa"

    @property
    def moc_lacznie_w(self) -> float:
        return self.moc_w * self.sztuk


# Sprzet pracujacy non-stop. Moce typowe - podmien na zmierzone, gdy je poznasz.
INWENTARZ = [
    Urzadzenie("Mini PC Lenovo M710q (OMV + Home Assistant, idle)", 18.0),
    Urzadzenie("Router", 9.0),
    Urzadzenie("Hue Bridge", 1.8),
    Urzadzenie("Strong Leap S3 (serwer dzwieku, LAN)", 3.5),
    Urzadzenie("Google Streamer / Chromecast (czuwanie)", 2.0),
    Urzadzenie("Drukarka HP M1132 (czuwanie)", 1.5),
    Urzadzenie("Termostat WiFi 230V", 1.0),
    Urzadzenie("Wtyczki i przekazniki WiFi (czuwanie)", 0.9, sztuk=7),
    Urzadzenie("Wtyczki i kontrolery Zigbee (czuwanie)", 0.4, sztuk=3),
    Urzadzenie("Zarowki Hue E27 (zgaszone, pod napieciem)", 0.4, sztuk=5),
    Urzadzenie("Hue Play (czuwanie)", 0.5, sztuk=2),
    Urzadzenie("Hue Lightstrip 10m (czuwanie)", 0.5),
    Urzadzenie("Zarowka WOOX E27 (czuwanie)", 0.4),
]
