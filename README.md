## Пакет парсеров (пока только карт)

## Структура проекта

- bs - парсинг через bs4
  - maps - для карт
    - base_parser - базовый парсинг - класс.
    - gis 
    - google 
    - yandex
- geckodriver - исходный файл geckodriver
  - geckodriver - driver for firefox
- output - вывод. Поддерживается в html, json
  - html
    - maps - Вывод для всех одинаков. Рендерит файл из /tmp
  - json
    - maps
    - work_json_file - утилитка для работы с json файлами
- results - Результаты парсинга
  - maps - По картам. В двух форматах
    - html
    - json
- src - Исходники
  - ajax_handling - Обработка ajax
  - base_driver - Базовый драйвер
  - base_reviews - Базовый класс отзывов по картам
  - const - константы
  - middlewares - декораторы
  - mixins - примеси
  - my_driver - Сам драйвер
  - scroll - Скролл-практики. Класс привязан к ajax обработке. Но может использоваться и напрямую
  - search_methods - поисковые методы
  - web_search - Веб-поиск. Вбив в поле поиска с результатами поиска
- tmp - Директория временных файлов
  - maps - Карты
    - rendering - Для рендеринга
      - base_reviews
    - source - Исходный код страницы после обработки 
- web - Сама работа с вебом
  - maps - Карты
    - gis - 
    - google
    - interface - Общий интерфейс
    - yandex