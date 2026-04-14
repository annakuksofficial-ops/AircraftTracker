from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
import requests


class BaseAPIClient(ABC):
    """Абстрактный класс для работы с API"""

    def __init__(self, base_url: str):
        """Инициализация базового API клиента"""
        self._base_url = base_url
        self._session = requests.Session()

    def _send_request(self, url: str, params: Optional[Dict] = None) -> Dict[str, Any]:
        """Приватный метод для отправки запроса"""
        response = self._session.get(url, params=params)
        response.raise_for_status()  # Проверка статус-кода
        return response.json()

    @abstractmethod
    def get_data(self, **kwargs) -> Any:
        """Абстрактный метод для получения данных"""
        pass


class OpenSkyClient(BaseAPIClient):
    """Клиент для работы с OpenSky API"""

    def __init__(self):
        super().__init__("https://opensky-network.org/api")

    def get_data(self, lamin: float, lamax: float, lomin: float, lomax: float) -> Dict:
        """Получение данных о самолётах по координатам"""
        params = {
            'lamin': lamin,
            'lamax': lamax,
            'lomin': lomin,
            'lomax': lomax
        }
        url = f"{self._base_url}/states/all"
        return self._send_request(url, params)


class NominatimClient(BaseAPIClient):
    """Клиент для работы с Nominatim API"""

    def __init__(self):
        super().__init__("https://nominatim.openstreetmap.org")

    def get_data(self, country: str) -> Dict:
        """Получение координат страны"""
        params = {
            'country': country,
            'format': 'json',
            'limit': 1
        }
        headers = {'User-Agent': 'course-work/1.0'}
        url = f"{self._base_url}/search"
        response = self._session.get(url, params=params, headers=headers)
        response.raise_for_status()
        data = response.json()
        if not data:
            raise ValueError(f"Страна '{country}' не найдена")
        return data[0]
