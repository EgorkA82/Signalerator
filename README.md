# Signalerator

[![Build](https://github.com/EgorkA82/Signalerator/actions/workflows/main.yml/badge.svg)](https://github.com/EgorkA82/Signalerator/actions/workflows/main.yml)
![GitHub](https://img.shields.io/github/languages/code-size/EgorkA82/Signalerator)
![GitHub](https://img.shields.io/github/license/EgorkA82/Signalerator)
![GitHub commit activity (branch)](https://img.shields.io/github/commit-activity/m/EgorkA82/Signalerator)

## Введение

---

## Теоретическая часть

---

Генератор сигналов может создавать различные сигналы, необходимые пользователю. Это может быть:

* прямоугольный сигнал (имеющий только два значения – 1 или 0),
* треугольный сигнал (изменяющийся от одного значения к другому),
* синусоида (имеющий форму синусоиды),
* произвольный сигнал (значение описывается формулой, введённой пользователем).

## Практическая часть

---

Разработка началась с создания внешнего вида приложения в **Qt Designer** - программы для разметки расположения кнопок, переключателей и т.д.\
Изначальный результат визуально сильно отличался от переработанного: все цвета приложения были градациями серого, разделение на логические блоки отсутствовало. В результате редизайна приложение, получившее к этому моменту название **Signalerator** (от англ. **Signal** Gen**erator** - генератор сигналов), стало соответствовать современным стандартам визуального оформления:

* появились два основных цвета - белый и светло-голубой
* были выделены 4 логических блока (подключение, настройка, выбор формы сигнала и отображение данных в реальном времени)
* блоки получили скругление углов, добавив приложению привлекательности и "дружелюбности"

Были добавленые базовые реакции на действия пользователя: при наведении и нажатии на кнопку подключения к генератору сигналов её цвет меняется; при переключении на режим произвольного сигнала становится возможным ввод функции в поле ввода; при установке максимального напряжения ниже минимального, минимальное автоматически корректируется, чтобы не превышать максимальное.

---

Следующим изменением стало добавление возможности запуска программы в тест-режиме: программа запускается, подключает необходимые библиотеки, создаёт библиотеки и переменные, а после закрывается. Данная функция необходима для автоматической проверки работоспособности программы при её публикации на **GitHub** - крупнейшего веб-сервиса для хостинга IT-проектов и их совместной разработки. Система проверяет данный проект, запусткая программу на данных конфигурациях:

* Операционная система: `Windows 11`
* Среда исполнения:
  - `Python 3.10.1`
  - `Python 3.10.2`

Если при запуске возникали какие-либо ошибки и приложение не запускается, на электронную почту автоматически отправляется сообщение об ошибке запуска.

Это также может быть полезным другим пользователям: при просмотре страницы проекта они сразу видят, работоспособна ли последняя версия приложения.

Для запуска приложения в тест-режиме необходимо в консоли добавить флаг `--test`. Пример такого запуска через командную строку выглядит так:

```python main.py --test```

По умолчанию программа запускается в релиз-режиме.

---

Следующим шагом стало добавление работы с *потоками*. Изначально программа работает в одном потоке: функции исполняются друг за другом, по очереди. Однако в данной программе было необходимо совершать несколько действий почти одновременно:

* Реагировать на действия пользователя,
* Обновлять список доступных для подключения устройств,
* Отправлять значения сигнала на контроллер.
  
Если в данный момент программе не нужно реагировать на пользовательские действия, она автоматически переключается на выполнение других задач, на обновление списка доступных устройств и отправление данных. Из-за того, что переключение между задачами происходит очень быстро, складывается впечатление, что функции выполняются параллельно.

Однако важно не создавать чрезмерно большое число потоков, в противном случает программа может начать работать медленно или вообще зависнуть.

---

После этого в программе была реализована автоматическая проверка на отсутствие необходимых библиотек. В случае отсутствия библиотеки программа устанавливает её, а не завершает работу. Благодаря такому функционалу нет необходимости предварительно устанавливать какие-либо библиотеки: при первом запуске программ установит всё, что необходимо для её работы.

---

Так как иногда пользователю необходимо быстро отключить устройство, в программу была добавлена возможность "горячего отключения" - отключения устройства без предварительного отключения в программе. Как только программа обнаруживает, что контроллер был отключен, весь интерфейс изменяется:

* сигнал переводится в режим "отключено",
* отключается возможность настройки сигнала,
* зелёная надпись "подключено" заменяется на красную "не подключено".

При подключении устройства обратно достаточно нажать кнопку "Подключиться" и выбрать форму сигнала. Настройки останутся те же, что были при отключении.

---

После того, как программа стала готова к первому подключению, необходимо было написать программу для микроконтроллера. В данном проекте используется микроконтроллер `Arduino Nano`, его средняя рыночная стоимость по состоянию на апрель 2022 года состовляет 200-500 рублей. Контреллер не большой мощностью, однако он полностью подходит для задач данного проекта. Основным требованием к программе являлась быстрота её испольнения, программа должна успевать считать необходимое значение сигнала и установить быстрее, чем за 40мс: человеческому взляду необходимо измененние изображения не менее 25 кадров в секунду, чтобы изменение казалось плавным, соответственно каждый кадр должен обновляться не реже, чем через 40мс.

Для возможности изменения напряжения в микроконтреллере, который может выдавать только 0В или 5В применяется ШИМ. **ШИМ** (**Ш**иротно-**и**мпульсная  **м**одуляция) подразумевает очень быстрое переключение состояний "вкл"/"выкл". Так, чтобы из 5В выдать 2.5В, устройство устанавливает продолжительность открытия и закрытия транзистора в соотношении 1 к 1. Таким образом, подключенный к выводу светодиод очень быстро включается и отключается, а человеку кажется, будто светодиод горит в половину своей максимальной яркости.

---

Самым важным обновлением программы стало добавление полноценной генерации сигнала. В программе ведётся "статус" сигнала - число от 0 до 1, обозначающее прогресс сигнала в данном периоде. Если прогресс равен 0.5, то половина периода сигнала прошла. Используя эту переменную (обозначим её как `x`), мы можем определить значение сигнала:

* Прямоугольный - ![](https://render.githubusercontent.com/render/math?math=(x%20%5Clt%200.5%20%5CRightarrow%200)%20%5Ciff%20(x%20%5Cgeq%200.5%20%5CRightarrow%201))
* Треугольный - ![](https://render.githubusercontent.com/render/math?math=(x%20%5Clt%200.5%20%5CRightarrow%202x)%20%5Ciff%20(x%20%5Cgeq%200.5%20%5CRightarrow%202(-x%20%2b%201)))
* Синусоида - ![](https://render.githubusercontent.com/render/math?math=%5Csin(2%20%5Cpi%20x%20%2b%201))
* Произвольный - ![](https://render.githubusercontent.com/render/math?math=%5Cint_%7B0%7D%5E%7B1%7D%20f(x))

В поле произвольной функции можно использовать множество математических функций:

| Функция | Описание |
| :- | :- |
| `acos(x)` | Арккосинус `x` |
| `asin(x)` | Арксинус `x` |
| `atan(x)` | Арктангенс `x` |
| `atan2(x)` | Обратный гиперболический тангенс `x` |
| `ceil(x)` | Округление `x` вверх до целого |
| `cos(x)` | Косинус `x` |
| `cosh(x)` | Гиперболический косинус `x` |
| `degrees(x)` | Перевод `x` из радиан в градусы |
| `e` | Число Эйлера |
| `exp(x)` | Экспонента `x` |
| `fabs(x)` | Модуль `x` |
| `floor(x)` | Округление `x` вниз до целого |
| `fmod(x, y)` | Остаток от деления `x` на `y` |
| `hypot(*coordinates)` | Гипотенуза |
| `log(x, y)` | Логарифм `x` по основанию `y` |
| `log10(x)` | Логарифм `x` по основанию 10 |
| `pi` | Число Пи |
| `pow(x, y)` | Возведение `x` в степень `y` |
| `radians(x)` | Перевод `x` из градусов в радианы |
| `round(x)` | Округление `x` до целого |
| `sin(x)` | Синус `x` |
| `sinh(x)` | Гиперболический синус `x` |
| `sqrt(x)` | Квадратный корень `x` |
| `tan(x)` | Тангенс `x` |
| `tanh(x)` | Гиперболический тангенс `x` |

---

Последнее обновление являлось, по большей мере, оптимизацией кода программы. Так как при изменении атрибутов элементов интерфейса их стили не обновляются автоматически, их необходимо применять к элементу заново. До обновления стили, которые было необходимо применить, были прописаны прямо в программе. После обновления стили элементов стали браться у самих элементов. Благодаря этому обновлению пропала необходимость измениять стили в программе при их изменении в файле стилей.

## Источники

---

<https://qna.habr.com>

<https://stackoverflow.com>

<https://forum.qt.io>

<https://www.youtube.com>

<https://doc.qt.io>

<https://alexgyver.ru/lessons/pwm-signal/>

<https://docs.python.org/3/library/math.html>
