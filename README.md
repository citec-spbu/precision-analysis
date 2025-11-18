# Robot Calibration

Приложение для сравнения классических методов решения задач **AX = XB** и **AX = YB**. Вход - файлы в формате `id, X, Y, Z, RZ, RY, RX` (мм и градусы, углы в порядке ZYX). 

* Используемые методы: `tsai-lenz`, `park-martin`, `daniilidis`, `li-wang-wu`, `shah`.
* Метрики: `mean, median, rmse, p95, max`.

---

Запуск:
```
python .\src\app.py
```
