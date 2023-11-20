# Проект по тестированию сайта <a target="_blank" href="https://protei.ru/">"НТЦ Протей" </a> 

![main page screenshot](./pictures/protei_main_page.png)

----

### Список проверок, реализованных в автотестах

- [x] Доступ к Главной странице
- [x] Переход с Главной к странице Мобильных операторов
- [x] Заполнение формы для заявки мобильных операторов
- [x] Переход с Главной к странице ПРОТЕЙ-Юником
- [x] Заполнение формы для заявки на корпоративный мессенджер

----
### Используемый стэк
<img title="Python" src="./pictures/icons/python-original.svg" height="40" width="40"/> <img title="Pytest" src="./pictures/icons/pytest.png" height="40" width="40"/> <img title="Pycharm" src="./pictures/icons/intellij_pycharm.png" height="40" width="40"/> <img title="Selenium" src="./pictures/icons/selenium.png" height="40" width="40"/> <img title="Selene" src="./pictures/icons/selene.png" height="40" width="40"/> <img title="GitHub" src="./pictures/icons/github-original.svg" height="40" width="40"/> <img title="Allure Report" src="./pictures/icons/allure_report.png" height="40" width="40"/> <img title="Allure TestOps" src="./pictures/icons/allure_testops.png" height="40" width="40"/><img title="Telegram" src="./pictures/icons/tg.png" height="40" width="40"/><img title="Jenkins" src="./pictures/icons/jenkins.png" height="40" width="40"/>

----
### Локальный запуск автотестов

#### Выполнить в cli:
> [!NOTE]
> Ключ выбора версии `--browser-version` не обязателен
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest . --browser-version=100
```
#### Получение отчёта:
```bash
allure serve tests/allure-results
```

----
### Проект в Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/protei_project///">Ссылка</a>

#### Параметры сборки


* environment - параметр определяет окружение для запуска тестов
* browser version - параметр для настройки версии браузера для запуска тестов

#### Запуск автотестов в Jenkins
1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/protei_project">проект</a>
2. Нажать "Build with Parameters"
3. Из списка "ENVIRONMENT" выбрать: PROD
4. В поле "BROWSER_VERSION" ввести предпочитаемую версию браузера
5. Нажать "Build"

----
### Allure отчет
#### Общие результаты

![allure_report_overview](./pictures/allure_full_report.png)
#### Список тест кейсов
![allure_reports_behaviors](./pictures/allure_test_cases.png)
#### Отчет прохождения теста

![allure_reports_graphs](./pictures/allure_test_case.png)

----
### Интеграция с Allure TestOps
> <a target="_blank" href="https://allure.autotests.cloud/launch/32414">Ссылка на проект</a>

#### Информация с общими показателями тестовых прогонов

![allure_test_ops_dashboards](./pictures/allure_testops_full.png)

#### Дерево тест-кейсов

![allure_testops_suites](./pictures/testops_test_cases.png)

----
### Оповещения в Telegram

![telegram_allert](./pictures/tg_notification.png)

----
### Видео прохождения автотеста

![autotest_gif](./pictures/video.gif)

----
