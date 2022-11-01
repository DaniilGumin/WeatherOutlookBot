# Отчёт

***
### Team Members:

- **Daniil Gumin**
- **Andrew Zmushko**
- **Ivan Hryakow**

***

[Ссылка на доску](https://trello.com/invite/b/MpeIYfJi/ATTIa54f793ae698601655214faf4c70e516F75EBF7C/aid)

***

#### 1. В качестве системы ведения проектов выбрали Trello, так как наш проект небольшой и нам не нужны продвинутые инструменты для организации работы. Функционала Trello достаточно для ведения проектов таких размеров.
#### 2. Доска у нас состоит из 6 столбцов. 
##### - Первый столбец - Backlog - в него помещаются задачи с указанием их срочности, дедлайна, типа и критичности. 
##### - Второй столбец - To Do - туда карточка попадает после распределения задач, когда участник команды берёт соответствующую задачу на себя. 
##### - Третий столбец - Doing - когда участник приступает к выполнению, он перемещает задачу в этот столбец, создаёт ветку для её выполнения на GitHub и привязывает к карточке. 
##### - Четвёртый столбец - Testing - он используется для задач, которые связаны с кодом и требуют проверки работоспособности. Сюда попадают задачи, находящиеся на тестировании. 
##### - Пятый столбец - Done - сюда попадает карточка с выполненной работой и привязанным к ней Pull Request, если дан апрув, то задача остается в Done и помечается, как выполненная и закрытая. В случае, если она требует доработки, то отправляется обратно в Doing. 
##### - Последний столбец - Deployed - сюда попадают карточки из Done, которые были отмечены как закрытые и задеплоиные на сервер.
#### 3. Интеграция с GitHub происходит с помощью добавления на доску "улучшения" GitHub. После этого на каждой карточке становится доступна кнопка, с помощью которой можно привязать к карточке ветку, проблему, коммит или pull-запрос. Также, при привязке pull-запроса отображается его статус, если ветка вмёрджена будет написано "объеденино", в противном случае никакой надписи не будет. Стоит отдельно отметить, что при прикреплении pull-запроса показывается успешно прошли или нет проверки GitHub. 
#### 4. Систему ведения документации выбрали GitBook ввиду её простоты. Документацию для публичной страницы мы подтягиваем с репозитория на GitHub, для приватной пишем самостоятельно. [Ссылка на публичную документацию](https://aid.gitbook.io/project-documentation/)
#### 5. Генератор документации по коду pdoc. Для установки необходимо выполнить `pip install pdoc3`. После этого в терминале необходимо запустить команду ` pdoc --output-dir=название_директории  название_файла.py` и библиотека сгенерирует *.md файл, в котором будут docstring описания методов. [Ссылка на библиотеку](https://pdoc3.github.io/pdoc/)