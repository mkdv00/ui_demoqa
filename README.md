## Проект UI автотестов demoqa.com

<!-- Технологии -->

### Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="resources/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="resources/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="resources/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="resources/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="resources/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="resources/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="resources/logo/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="resources/logo/docker.png"></code>
  <code><img width="5%" title="Selenoid" src="resources/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="resources/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="resources/logo/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="resources/logo/jira.png"></code>
  <code><img width="5%" title="Telegram" src="resources/logo/tg.png"></code>
</p>


<!-- Тест кейсы -->

### Что проверяем
* Отправка формы и проверка данных всей заполненной формы
* Отправка формы и проверка данных только с заполнением главных полей
* Отправка пустой формы
* Валидация поля номера телефона
* Валидация поля Email


<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="resources/logo/jenkins.png"> Запуск проекта в Jenkins

### [Job](https://jenkins.autotests.cloud/job/UI_demoqa_qa_guru_python_2/)

##### При нажатии на "Собрать сейчас" начнется сборка тестов и их прохождение, через виртуальную машину в Selenide.
![This is an image](resources/screenshots/jenkins.png)


<!-- Allure report -->

### <img width="3%" title="Allure Report" src="resources/logo/allure_report.png"> Allure report

##### После прохождения тестов, результаты можно посмотреть в Allure отчете, где так же содержится ссылка на Jenkins
![This is an image](resources/screenshots/allure_dashboard.png)

##### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.
![This is an image](resources/screenshots/allure_graphs.png)

##### Во вкладке Suites находятся собранные тест кейсы, у которых описаны шаги и приложены логи, скриншот и видео о прохождении теста
![This is an image](resources/screenshots/allure_suites.png)

##### Видео прохождение теста
![This is an image](resources/screenshots/tests_ui.gif)


<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="resources/logo/allure_testops.png"> Интеграция с Allure TestOps

### [Dashboard](https://allure.autotests.cloud/project/1720/dashboards)

##### Так же вся отчетность сохраняется в Allure TestOps, где строятся аналогичные графики.
![This is an image](resources/screenshots/allure_testops_dashboard.png)

#### Во вкладке со сьютами, мы можем:
- Управлять всеми тест-кейсами или с каждым отдельно
- Перезапускать каждый тест отдельно от всех тестов
- Настроить интеграцию с Jira
- Добавлять ручные тесты и т.д

![This is an image](resources/screenshots/allure_testops_suites.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="resources/logo/jira.png"> Интеграция с Jira
##### Настроив через Allure TestOps интеграцию с Jira, в тикет можно пробросить результат прохождение тестов и список тест-кейсов из Allure

![This is an image](resources/screenshots/jira.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="resources/logo/tg.png"> Интеграция с Telegram
##### После прохождения тестов, в Telegram bot приходит сообщение с графиком и небольшой информацией о тестах.

![This is an image](resources/screenshots/tg_bot.png)
