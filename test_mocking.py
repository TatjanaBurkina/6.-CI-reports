import allure
from loguru import logger
import responses
import requests

@allure.feature("API тестирование")
@allure.story("Проверка работы мокированного запроса")
@allure.severity(allure.severity_level.CRITICAL)
@responses.activate
def test_mock_request():
    logger.info("Запрос к мокированному API начат")

    with allure.step("Добавление мок-ответа"):
        responses.add(
            responses.GET, 
            "https://api.accuweather.com/weather",
            json={"weather": "sunny"}, 
            status=200
        )

    with allure.step("Отправка запроса"):
        response = requests.get("https://api.accuweather.com/weather")
    
    with allure.step("Проверка статуса ответа"):
        assert response.status_code == 200
    
    with allure.step("Проверка содержимого ответа"):
        assert response.json() == {"weather": "sunny"}

    logger.success("Тест прошёл успешно!")

import pytest
import allure
import requests

API_KEY = "ft636sbc6xTE3spOQyLTX3k8dZucd6hw"

@allure.feature("API Testing")
def test_status_code():
    url = f"https://dataservice.accuweather.com/currentconditions/v1/1?apikey={API_KEY}"
    response = requests.get(url)
    assert response.status_code == 200, f"Ошибка: код ответа {response.status_code}"
