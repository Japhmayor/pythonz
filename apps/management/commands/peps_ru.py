from django.core.management.base import BaseCommand

from ...models import PEP


ru = {
1: 'О назначении PEP и руководство по созданию',
2: 'Процесс добавления новых модулей',
3: 'Руководство по обработке отчётов об ошибках',
4: 'Процесс исключения стандартных модулей',
5: 'Руководство по эволюции языка',
6: 'Выпуск версий с исправлениями',
7: 'Руководство по оформлению кода на Си',
8: 'Руководство по оформлению кода на Питоне',
9: 'Шаблон для PEP. Простой текст',
10: 'Руководство по голосованию',
11: 'Отказ от поддержки малоиспользуемых платформ',
12: 'Шаблон для PEP. Формат reStructuredText',
20: 'Дзен Питона',
42: 'Запросы о нововведениях',
100: 'Интеграция Unicode',
101: 'Вводный курс по созданию выпусков Питона',
102: 'О микро-релизах Питона',
103: 'Подборка информации о Git',
160: 'График выпуска Python 1.6',
200: 'График выпуска Python 2.0',
201: 'Слаженное итерирование',
202: 'Компоновка списков',
203: 'Дополняющие присвоения',
204: 'Литералы диапазонов',
205: 'Слабые ссылки',
206: 'Расширенная библиотека Питона',
207: '«Богатые» сравнения',
208: 'Переработка системы приведения типов',
209: 'Многомерные массивы',
210: 'Уменьшение связанности в цикле интерпретатора',
211: 'Добавление оператора векторного произведения',
212: 'Итерирование со счётчиком цикла',
213: 'Обработчики доступа к атрибутам',
214: 'Расширенная инструкция print',
215: 'Интерполяция строк',
216: 'Формат строк документации',
217: 'Хук для вывода в интерактивном режиме',
218: 'Добавление встроенного типа «множество»',
219: 'Исключение стека Питона',
220: 'Сопрограммы, генераторы, возобновления',
221: 'import as',
222: 'Улучшения библиотеки для Web',
223: 'Смена значения \\x-последовательностей',
224: 'Документирование атрибутов',
225: 'Поэлементные/пообъектные операторы',
226: 'График выпуска Python 2.1',
227: 'Статически вложенные области видимости',
228: 'Пересмотр числовой модели Питона',
229: 'Использование distutils для сборок Питона',
230: 'Каркас предупреждений — warnings',
231: '__findattr__()',
232: 'Атрибуты функций',
233: 'Внешняя справка для Питона',
234: 'Итераторы',
235: 'Импорт на платформах не различающих регистр',
236: 'Назад в __future__',
237: 'Унификация длинных целых и целых',
238: 'Изменения для оператора деления',
239: 'Добавления типа рациональных чисел',
240: 'Добавление литералов для рациональных чисел',
241: 'Метаданные для пакетов приложений',
242: 'Численные виды',
243: 'Механизм выгрузки в репозиторий модулей',
244: 'Инструкция `directive`',
245: 'Синтаксис для интерфейсов в Питоне',
246: 'Адаптация объектов',
247: 'API для криптографических функций',
248: 'Спецификация для работы с БД v1.0',
249: 'Спецификация для работы с БД v2.0',
250: 'Использование site-packages на Windows',
251: 'График выпуска Python 2.2',
252: 'Чтобы типы были больше похожи на классы',
253: 'Наследование от встроенных типов',
254: 'Чтобы классы были больше похожи на типы',
255: 'Простые генераторы',
256: 'Система обработки строк документации',
257: 'Соглашения по строкам документации',
258: 'Спецификация docutils',
259: 'Не начинать новую строку после новой строки',
260: 'Упрощение xrange()',
261: 'Поддержка «широких» символов Unicode',
262: 'БД установленных пакетов',
263: 'Обозначение кодировки в исходном коде',
264: 'Инструкции future в эмулируемых оболочках',
265: 'Сортировка словарей по значению',
266: 'Оптимизация доступа к глобальным меременным/атрибутам',
267: 'Оптимизация доступа к пространству имён модуля',
268: 'Расширение функциональности HTTP и WebDAV',
269: 'Модуль pgen',
270: 'Метод uniq для списков',
271: 'Дополнение sys.path из командной строки',
272: 'API для блочных алгоритмов шифрования v1.0',
273: 'Импорт модулей из zip-архивов',
274: 'Компоновка словарей',
275: 'Переключение (switch) для множественных значений',
276: 'Простор итератор для целых',
277: 'Поддержка Unicode в именах файлов на Windows NT',
278: 'Поддержка универсальных переносов строк',
279: 'Встроенная функция enumerate()',
280: 'Оптимизация доступа к глобальным переменным',
281: 'Итерирование со счётчиком для range и xrange',
282: 'Система журналирования',
283: 'График выпуска Python 2.3',
284: 'Циклы for для целых',
285: 'Добавление типа bool',
286: 'Улучшение для кортежей аргументов',
287: 'Формат reStructuredText для документирования',
288: 'Атрибуты и исключения для генераторов',
289: 'Генераторные выражения',
290: 'Миграция и модернизация кода',
291: 'Обратная совместимость для стандартной библиотеки Python 2',
292: 'Упрощённая замена строк',
293: 'Обратные вызовы при обработке ошибок кодеков',
294: 'Имена типов в модуле types',
295: 'Интерпретация многострочных констант',
296: 'Добавление типа bytes',
297: 'Поддержка обновлений системы',
298: 'Интерфейс блокированных буферов',
299: 'Специальная функция __main__() для модулей',
301: 'Индекс пакета и метаданные для distutils',
302: 'Новые хуки импорта',
303: 'Расширение divmod() для нескольких делителей',
304: 'Контроль генерирования файлов с байткодом',
305: 'API для CSV файлов',
306: 'Как менять грамматику Питона',
307: 'Расширения для протокола консервирования "pickle"',
308: 'Условные выражения',
309: 'Применение функции partial',
310: 'Надежные пары захват/освобождение',
311: 'Упрощённый захват глобальной блокировки интерпретатора для расширений',
312: 'Простая подразумеваемая lambda',
313: 'Литералы римских числительных',
314: 'Метаданные для программ на Питоне v1.1',
315: 'Улучшенный цикл while',
316: 'Контрактное программирование в Питоне',
317: 'Устранение неявного создания объектов исключений',
318: 'Декораторы для функций и методов',
319: 'Блок synchronize/asynchronize',
320: 'График выпуска Python 2.4',
321: 'Разбор и форматирование даты/времени',
322: 'Обратное итерирование',
323: 'Итераторы, поддерживающие копирование',
324: 'Новый модуль для работы с процессами — subprocess',
325: 'Поддержка освобождения ресурсов для генераторов',
326: 'Поддержка крайних (верхнего и нижнего) значений',
327: 'Типа данных decimal',
328: 'Импорты: многострочные и абсолютные/относительные',
329: 'Встроенные сущности стандартной библиотеки как константы',
330: 'Проверка байткода Питона',
331: 'Независящие от локали преобразования чисел с плавающей запятой / строка',
332: 'Векторы байтов и унификация строка/Юникод',
333: 'Интерфейс шлюза веб-сервера (WSGI) v1.0',
334: 'Простые сопрограммы при помощи SuspendIteration',
335: 'Перегружаемые булевы-операторы',
336: 'Поддержка вызова для None',
337: 'Использование logging в стандартной библиотеке',
338: 'Выполнение модулей как скриптов',
339: 'Конструкция компилятора CPython',
340: 'Инструкции анонимных блоков',
341: 'Унификация try-except и try-finally',
342: 'Сопрограммы при помощи улучшенных генераторов',
343: 'Инструкция "with"',
344: 'Цепочка исключений и встроенные трассировки',
345: 'Метаданные для программ на Питоне v1.2',
346: 'Пользовательские инструкции "with"',
347: 'Миграция Питона с CVS на Subversion',
348: 'Реорганизация исключений для Питона 3.0',
349: 'Позволить str() возвращать Юникод-строки',
350: 'Теги в коде - codetags',
351: 'Протокол заморозки',
352: 'Базовый класс для всех исключений',
353: 'Использование ssize_t в качестве типа индекса',
354: 'Перечисления в Питоне',
355: 'path — объектно-ориентированный подход к путям в файловых системах',
356: 'График выпуска Python 2.5',
357: 'Дозволить использование любых объектов для построения срезов',
358: 'Объект "bytes"',
359: 'Инструкция "make"',
360: 'Пакеты со внешней поддержкой',
361: 'Графики выпуска Python 2.6 и 3.0',
362: 'Объект сигнатуры функции',
363: 'Синтаксис для динамического доступа к атрибутам',
364: 'Переход стандартной библиотеки на Py3K',
365: 'Добавление модуля pkg_resources',
366: 'Явные относительные импорта главного модуля',
367: 'Новая super',
368: 'Стандартный протокол и класс для изображений',
369: 'Хуки после import',
370: 'Директория site-packages для каждого пользователя',
371: 'Добавление пакета multiprocessing в стандартную библиотеку',
372: 'Добавление в collections упорядоченного словаря',
373: 'График выпуска Python 2.7',
374: 'Выбор распределенной VCS для Питона',
375: 'График выпуска Python 3.1',
376: 'База данных с установленными дистрибутивами Питона',
377: 'Позволить методам __enter__() пропускать инструкции из тела with',
378: 'Спецификатор формата для разделителя тысяч',
379: 'Добавление выражений присвоения',
380: 'Синтаксис делегирования подгенератору',
381: 'Зеркало для инфраструктуры PyPI',
382: 'Пакеты-пространства-имён',
383: 'Недекодируемые байты в интерфейсах ОС для работы с символами',
384: 'Определение стабильного ABI',
385: 'Миграция с Subversion на Mercurial',
386: 'Изменение модуля сравнения версий в distutils',
387: 'Политика обратной совместимости',
389: 'Новый модуль для разбора командной строки — argparse',
390: 'Статичные метаданные для distutils',
391: 'Конфигурирование logging при помощи словарей',
392: 'График выпуска Python 3.2',
393: 'Гибкие представления строк',
394: 'Команда "python" в Unix-подобных системах',
395: 'Полные имена для модулей',
396: 'Нумерация версий модулей',
397: 'Средство запуска Питона для Windows',
398: 'График выпуска Python 3.3',
399: 'Требования совместимости для модулей на чистом Питоне и на Си',
400: 'Считать устаревшими codecs.StreamReader codecs.StreamWriter',
401: 'Уход в отставку BDFL',
402: 'Упрощение архитектуры пакетов и их разбиения',
403: 'Декоратор общего назначения (aka "@in")',
404: 'График невыпуска Python 2.8',
405: 'Виртуальные окружения Питона',
406: 'Улучшение инкапсуляции состояния импорта',
407: 'Новый цикл выпусков и представление версий с длительной поддержкой',
408: 'Пакет __preview__ стандартной библиотеки',
409: 'Подавление контекста исключения',
410: 'Использование decimal.Decimal для временных меток',
411: 'Предварительные пакеты в стандартной библиотеке Питона',
412: 'Словарь с разделяемыми ключами',
413: 'Более быстрая эволюция стандартной библиотеки Питона',
414: 'Явный литерал для Юникода в Python 3.3',
415: 'Реализация подавления контекста при помощи атрибутов исключений',
416: 'Добавление встроенного типа frozendict',
417: 'Включение модуля mock в стандартную библиотеку',
418: 'Добавление функций монотонного времени, счётчика производительности и времени процесса',
419: 'Защита финализации от прерываний',
420: 'Неявные пакеты-пространства-имён',
421: 'Добавление sys.implementation',
422: 'Упрощение модификаций процесса создания классов',
423: 'Рецепты по созданию пакетов и соглашения об их именовании',
424: 'Метод для предоставления подсказки о длине',
425: 'Метки совместимости для сборки дистрибутивов',
426: 'Метаданные для программ на Питоне v2.0',
427: 'Формат двоичных пакетов wheel v1.0',
428: 'Модуль pathlib — объектно-ориентированный подход к путям в файловых системах',
429: 'График выпуска Python 3.4',
430: 'Миграция веб-справки по умолчанию на Питон 3',
431: 'Улучшения для работы с временными зонами',
432: 'Упрощение последовательности запуска CPython',
433: 'Упрощённая отмена наследования файловых дескрипторов',
434: 'Исключение для улучшений в IDLE для всех веток',
435: 'Добавление типа Enum в стандартную библиотеку',
436: 'Предментно-ориентированный язык «Клиника аргументов»',
437: 'Предментно-ориентированный язык для сигнатур, аннотаций и преобразователей аргументов',
438: 'Переход на хостинг пакетов на PyPI',
439: 'Включение в установку Питона скрытой установки pip',
440: 'Идентификация версии и спецификация зависимостей',
441: 'Улучшение поддержки Питон-приложений в zip',
442: 'Безопасная финализация объектов',
443: 'Централизованная обработка для функций общего назначения',
444: 'Интерфейс Web3 для Питона',
445: 'Добавление новых API для управления выделением памяти в Питоне',
446: 'Сделать создаваемые файловые дескрипторы ненаследуемыми',
447: 'Добавить для метаклассов метод __getdescriptor__',
448: 'Дополнительные общие правила распаковки',
449: 'Устранение автоматического обнаружения зеркал PyPI и схемы наименований',
450: 'Добавление модуля statistics в стандартную библиотеку',
451: 'Тип ModuleSpec для системы импорта',
452: 'API для криптографических функций v2.0',
453: 'Включение в установку Питона явной установки pip',
454: 'Добавление нового модуля tracemalloc трассировок управления памятью',
455: 'Добавление в collections словаря с трансформируемыми ключами',
456: 'Безопасный и адаптируемый алгоритм хеширования',
457: 'Синтаксис для «только-позиционных» аргументов',
458: 'Жизнь после компрометации PyPI',
459: 'Расширение стандартных метаданных для пакетов',
460: 'Добавление интерполяции и форматирования для двоичных данных',
461: 'Добавление форматирования при помощи % для byte и bytearray',
462: 'Автоматизация процесса разработки ядра CPython',
463: 'Выражения для отлова исключений',
464: 'Устранение API аутентификации для зеркал PyPI',
465: 'Отдельный инфиксный оператор для перемножения матриц',
466: 'Улучшения сетевой безопасности для Python 2.7.x',
467: 'Мелкие улучшения API для двоичных последовательностей',
468: 'Сохранение порядка **kwargs для функций.',
469: 'Перевод кода прохода по словарю на Python 3',
470: 'Устранение поддержки внешнего хостинга для PyPI',
471: 'Функция os.scandir() — улучшенный и ускоренный итератор для директорий',
472: 'Поддержка индексации именованными аргументами',
473: 'Добавление структурированных данных во встроенные исключения',
474: 'Создание forge.python.org',
475: 'Повторное выполнение системных вызовов при помощи EINTR',
476: 'Включение по умолчанию проверки сертификатов http-клиентов в стандартной библиотеке',
477: 'Обратное портирование ensurepip (PEP 453) для Python 2.7',
478: 'График выпуска Python 3.5',
479: 'Изменение обработки StopIteration внутри генераторов',
480: 'Жизнь после компрометации PyPI: максимально безопасная модель',
481: 'Переход CPython на Git, Github и Phabricator',
482: 'Литературный обзор указаний типов',
483: 'Теория указаний типов',
484: 'Указание типов',
485: 'Функция проверки на примерное равенство',
486: 'Познакомить средство запуска Питона с виртуальными окружениями',
487: 'Упрощение модификаций процесса создания классов',
488: 'Устранение pyo файлов',
489: 'Многофазовая инициализация расширений',
490: 'Обработка исключений по цепочке на уровне Си',
491: 'Формат двоичных пакетов wheel v1.9',
492: 'Сопрограммы при помощи async и await',
493: 'Инструменты миграции проверок HTTPS для Python 2.7',
494: 'График выпуска Python 3.6',
495: 'Устранение неоднозначности для локального времени',
496: 'Маркеры окружений',
497: 'Стандартный механизм обратной совместимости',
498: 'Интерполяция для литералов строк',
499: '"python -m foo" должен оказаться в "sys.modules[`foo`]" и в "sys.modules[`__main__`]"',
500: 'Протокол делегирования методов datetime реализациям с tzinfo',
501: 'Интерполяция общего назначения для строк',
502: 'Интерполяция строк — расширенное обсуждение',
503: 'Простой API для репозиториев',
504: 'Использование системного генератора случайных чисел по умолчанию',
505: 'Поддержка None в операторах',
506: 'Добавление модуля secrets в стандартную библиотеку',
507: 'Переход CPython на Git и GitLab',
508: 'Указание зависимостей для пакетов',
509: 'Добавление версии в словарь',
510: 'Специализация функций при помощи защиты',
511: 'API для преобразователей кода',
512: 'Переход с hg.python.org на GitHub',
513: 'Метка платформы для портируемых дистрибутивов Питона в Linux',
514: 'Занесение Питона в реестр Windows',
515: 'Подчеркивания в литералах чисел',
516: 'Построение абстракций для pip/conda и пр.',
517: 'Формат топологии исходного кода, независящий от систем сборки',
518: 'Указание минимальный требований для сборки проектов на Питоне',
519: 'Добавление протокола для путей в файловых системах',
520: 'Сохранение порядка определений атрибутов в классе',
521: 'Управление глобальным контекстом при помощи `with` в генераторах и сопрограммах',
522: 'Использование BlockingIOError в API, нуждающихся в безопасности',
523: 'Добавление в CPython API для исполнения фреймов',
524: 'Сделать os.urandom() блокирующим на Linux',
525: 'Асинхронные генераторы',
526: 'Синтаксис для аннотаций переменных',
527: 'Удаление с PyPI неиспользуемых и малоиспользуемых типов файлов',
528: 'Смена кодировки в консоли Windows на UTF-8',
529: 'Смена кодировки для файловой системы Windows на UTF-8',
530: 'Асинхронные компоновки',
628: 'Добавление "math.tau"',
666: 'Не поддерживать дурацкие отступы',
754: 'IEEE 754 специальные значения для чисел с плавающей запятой',
3000: 'Python 3000',
3001: 'Процедура обзора и улучшения для модулей стандартной библиотеки',
3002: 'Процедура для изменений без обратной совместимости',
3003: 'Мораторий на язык Python',
3099: 'Что не изменится в Python 3000',
3100: 'Прочие планы на Python 3.0',
3101: 'Усовершенствованное форматирование строк',
3102: 'Только-именованные аргументы',
3103: 'Инструкция switch/case',
3104: 'Доступ к именам во внешних областях видимости',
3105: 'Сделать print функцией',
3106: 'Пересмотр dict.keys(), .values() и .items()',
3107: 'Аннотации функций',
3108: 'Реорганизация стандартной библиотеки',
3109: 'Подъём исключений в Python 3000',
3110: 'Перехват исключений в Python 3000',
3111: 'Простая встроенная input в Python 3000',
3112: 'Литералы для байтов в Python 3000',
3113: 'Устранение распаковки кортежа параметров',
3114: 'Переименование iterator.next() в iterator.__next__()',
3115: 'Метаклассы в Python 3000',
3116: 'Новый ввод-вывод',
3117: 'Постфиксные объявления типов',
3118: 'Корректировки для протокола буфера',
3119: 'Внесение абстрактных базовых классов',
3120: 'Использование UTF-8 в качестве кодировки исходного кода по умолчанию',
3121: 'Инициализация и финализация расширений',
3122: 'Определение главного модуля',
3123: 'Приведение PyObject_HEAD к стандартному Си',
3124: 'Перегрузка, общие функции, интерфейсы и адаптация',
3125: 'Устранение обратного слеша как символа продолжения строки',
3126: 'Устранение возможности неявного склеивания строк',
3127: 'Поддержка и синтаксис литералов целых',
3128: 'BList: более быстрый спископодобный тип',
3129: 'Декораторы классов',
3130: 'Доступ к текущему модулю/классу/функции',
3131: 'Поддержка не-ASCII идентификаторов',
3132: 'Расширенная распаковка для типов, поддерживающих итерирование',
3133: 'Внедрение ролей',
3134: 'Цепочка исключений и встроенные трассировки',
3135: 'Новая super',
3136: 'Маркировка для break и continue',
3137: 'Неизменяемые bytes и изменяемый буфер',
3138: 'Представление строк в Python 3000',
3139: 'Чистка sys и новый модуль "interpreter"',
3140: 'str(контейнер) должен вызывать str(элемент), а не repr(элемент)',
3141: 'Иерархия типов для чисел',
3142: 'Добавить "while" в генераторные выражения',
3143: 'Модуль для создания процессов-демонов в стандартной библиотеке',
3144: 'Модуль для работы с IP-адресами для стандартной библиотеки',
3145: 'Асинхронный ввод-вывод для subprocess.Popen',
3146: 'Слияние Unladen Swallow в CPython',
3147: 'Директории-репозитории для PYC',
3148: 'futures для запуска асинхронных вычислений',
3149: '.so файлы с указанием версии ABI',
3150: 'Локальная область видимости для инструкций (aka "given")',
3151: 'Переработка иерархии исключений ОС и ввода-вывода',
3152: 'Кофункции',
3153: 'Поддержка асинхронного ввода-вывода',
3154: 'Протокол консервирования pickle, версия 4',
3155: 'Полные имена для классов и функций',
3156: 'Поддержка асинхронного ввода-вывода заново: модуль "asyncio"',
3333: 'Интерфейс шлюза веб-сервера (WSGI) v1.0.1',
}


class Command(BaseCommand):

    help = 'Puts Russian traslation for PEPs'

    def handle(self, *realm_names, **options):

        self.stdout.write('Starting PEP loco update ...\n')

        for pep in PEP.objects.all():
            tr = ru.get(pep.num)
            if tr:
                pep.title = tr
                pep.save()

        self.stdout.write('PEP loco update is done.\n')