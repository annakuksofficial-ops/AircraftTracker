from typing import Optional


class Aeroplane:
    """Класс для работы с информацией о самолёте"""

    __slots__ = ('_icao24', '_callsign', '_origin_country',
                 '_velocity', '_altitude', '_longitude', '_latitude')

    def __init__(self, icao24: str, callsign: Optional[str], origin_country: str,
                 velocity: Optional[float], altitude: Optional[float],
                 longitude: Optional[float], latitude: Optional[float]):
        """Инициализация самолёта с валидацией"""
        self._icao24 = self._validate_string(icao24, "ICAO24")
        self._callsign = callsign
        self._origin_country = self._validate_string(origin_country, "Страна")
        self._velocity = self._validate_float(velocity, "Скорость")
        self._altitude = self._validate_float(altitude, "Высота")
        self._longitude = self._validate_float(longitude, "Долгота")
        self._latitude = self._validate_float(latitude, "Широта")

    def _validate_string(self, value: str, field_name: str) -> str:
        """Приватная валидация строковых значений"""
        if not value:
            return "Неизвестно"
        return str(value)

    def _validate_float(self,
                        value: Optional[float], field_name: str) -> float:
        """Приватная валидация числовых значений"""
        if value is None:
            return 0.0
        return float(value)

    @property
    def icao24(self) -> str:
        return self._icao24

    @property
    def callsign(self) -> Optional[str]:
        return self._callsign

    @property
    def origin_country(self) -> str:
        return self._origin_country

    @property
    def velocity(self) -> float:
        return self._velocity

    @property
    def altitude(self) -> float:
        return self._altitude

    @property
    def longitude(self) -> float:
        return self._longitude

    @property
    def latitude(self) -> float:
        return self._latitude

    def __lt__(self, other: 'Aeroplane') -> bool:
        """Сравнение по высоте (меньше)"""
        return self.altitude < other.altitude

    def __gt__(self, other: 'Aeroplane') -> bool:
        """Сравнение по высоте (больше)"""
        return self.altitude > other.altitude

    def __eq__(self, other: 'Aeroplane') -> bool:
        """Сравнение по высоте (равно)"""
        return self.altitude == other.altitude

    def __str__(self) -> str:
        return (f"Самолёт {self.callsign or self.icao24}: "
                f"страна={self.origin_country}, "
                f"высота={self.altitude:.1f}м, "
                f"скорость={self.velocity:.1f}м/с")

    @classmethod
    def from_state_vector(cls, state: list) -> 'Aeroplane':
        """Создание объекта из списка от OpenSky API"""
        return cls(
            icao24=state[0],
            callsign=state[1].strip() if state[1] else None,
            origin_country=state[2],
            velocity=state[9],
            altitude=state[7],
            longitude=state[5],
            latitude=state[6]
        )
