## Сервис управления рассылками

### Необходимые требования

- Выполните клон репозитория
- Создайте виртуальное окружение, активируйте его
- Установите зависимости ```pip install -r requirements.txt```
- Заполните файл .env.sample в корне проекта своими данными:
  (секретный ключ, настройки подключения к базе данных, настройки отправки email сообщений, настройки кеширования)
- Переименуйте .env.sample в .env
- Создайте и примените миграции
- Запустите командой в терминале ```python3 manage.py runserver```
- Создайте суперпользователя ```python3 manage.py csu```
- Зарегистрируйте на сайте модератора и присвойте ему статус персонала через панель администрирования
- Модератор может просматривать сущность 'рассылка' и 'пользователь', отключать любую рассылку и деактивировать
  пользователя. Редактирование, удаление пользователей, рассылок и писем модератору недоступны.
- Незарегистрированный пользователь может просматривать только раздел Блоги

### Логика работы:

- После создания новой рассылки, если текущее время больше времени начала и меньше времени окончания, то должны быть
  выбраны из справочника все клиенты, которые указаны в настройках рассылки, и запущена отправка для всех этих клиентов.
- Если создается рассылка со временем старта в будущем, то отправка должна стартовать автоматически по наступлению этого
  времени без дополнительных действий со стороны пользователя системы.
- По ходу отправки сообщений должна собираться статистика (см. описание сущности «сообщение» и «логи» выше) по каждому
  сообщению для последующего формирования отчетов.