from abc import ABC, abstractmethod
import json
import os
from typing import List
from src.aeroplane import Aeroplane


class BaseFileSaver(ABC):
    """Абстрактный класс для работы с файлами"""

    @abstractmethod
    def add_aeroplane(self, aeroplane: Aeroplane) -> None:
        pass

    @abstractmethod
    def get_aeroplanes(self) -> List[Aeroplane]:
        pass

    @abstractmethod
    def delete_aeroplane(self, aeroplane: Aeroplane) -> None:
        pass


class JSONSaver(BaseFileSaver):
    """Класс для сохранения данных в JSON файл"""

    def __init__(self, filename: str = "data/aeroplanes.json"):
        self._filename = filename
        self._ensure_file_exists()

    def _ensure_file_exists(self) -> None:
        """Создаёт файл если его нет"""
        if not os.path.exists(self._filename):
            os.makedirs(os.path.dirname(self._filename), exist_ok=True)
            with open(self._filename, 'w', encoding='utf-8') as f:
                json.dump([], f)

    def _load_data(self) -> List[dict]:
        """Загружает данные из файла"""
        with open(self._filename, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _save_data(self, data: List[dict]) -> None:
        """Сохраняет данные в файл"""
        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_aeroplane(self, aeroplane: Aeroplane) -> None:
        """Добавляет самолёт в файл (без дубликатов)"""
        data = self._load_data()

        existing = [item for item in data if item.get('icao24') == aeroplane.icao24]
        if existing:
            return

        data.append({
            'icao24': aeroplane.icao24,
            'callsign': aeroplane.callsign,
            'origin_country': aeroplane.origin_country,
            'velocity': aeroplane.velocity,
            'altitude': aeroplane.altitude,
            'longitude': aeroplane.longitude,
            'latitude': aeroplane.latitude
        })
        self._save_data(data)

    def get_aeroplanes(self) -> List[Aeroplane]:
        """Возвращает список всех самолётов из файла"""
        data = self._load_data()
        aeroplanes = []
        for item in data:
            aeroplane = Aeroplane(
                icao24=item['icao24'],
                callsign=item.get('callsign'),
                origin_country=item['origin_country'],
                velocity=item['velocity'],
                altitude=item['altitude'],
                longitude=item['longitude'],
                latitude=item['latitude']
            )
            aeroplanes.append(aeroplane)
        return aeroplanes

    def delete_aeroplane(self, aeroplane: Aeroplane) -> None:
        """Удаляет самолёт из файла"""
        data = self._load_data()
        data = [item for item in data if item.get('icao24') != aeroplane.icao24]
        self._save_data(data)
