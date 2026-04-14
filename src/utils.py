from typing import List
from src.aeroplane import Aeroplane


def filter_by_country(
    aeroplanes: List[Aeroplane], countries: List[str]
) -> List[Aeroplane]:
    """Фильтрует самолёты по стране регистрации"""
    if not countries:
        return aeroplanes
    return [a for a in aeroplanes if a.origin_country in countries]


def filter_by_altitude(
    aeroplanes: List[Aeroplane], min_alt: float, max_alt: float
) -> List[Aeroplane]:
    """Фильтрует самолёты по диапазону высот"""
    return [a for a in aeroplanes if min_alt <= a.altitude <= max_alt]


def get_top_n_by_altitude(aeroplanes: List[Aeroplane], n: int) -> List[Aeroplane]:
    """Возвращает топ N самолётов по высоте"""
    sorted_aeroplanes = sorted(aeroplanes, key=lambda x: x.altitude, reverse=True)
    return sorted_aeroplanes[:n]


def sort_by_velocity(
    aeroplanes: List[Aeroplane], reverse: bool = True
) -> List[Aeroplane]:
    """Сортирует самолёты по скорости"""
    return sorted(aeroplanes, key=lambda x: x.velocity, reverse=reverse)
