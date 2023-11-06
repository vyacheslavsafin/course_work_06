## Структура проекта и работа с git:

+Проект на github
+Разработка велась в нескольких ветвях
+Есть gitignore
+Есть список зависимостей
+Секретные данные вынесены в переменные окружения
+Проект разбит по приложениям
+Есть readme
+Есть env.sample
+Нет лишних файлов и папок в репозитории

## Сущности:

+Верно описана модель рассылки
+Верно описана модель клиент сервиса
+Верно описана модель сообщение для рассылки
+Верно описана модель лога
+Верно описана модель пользователя, email определен как поле для авторизации 
+Верно описана модель блога

## Интерфейс:

+Реализован CRUD для рассылок
+Реализован CRUD для клиентов
+Реализован CRUD для сообщений
+Для логина и авторизации есть свои страницы, регистрация производится с верификацией почты
+Есть раздел блогов
+На главной странице отображается необходимая информация

## Права доступа:

+Реализован функционал менеджера
+Пользователи могут взаимодействовать только со своими сущностями

## Кеширование:

+Использовано кеширование

## Логика работы системы:

+Письма уходят по расписанию
+После попытки отправки письма создается запись лога