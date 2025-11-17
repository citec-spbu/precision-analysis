# Robot Calibration

Консольное приложение для сравнения классических методов решения задач **AX = XB** и **AX = YB**. Вход - файлы в формате `id, X, Y, Z, RZ, RY, RX` (мм и градусы, углы в порядке ZYX). 

* Используемые методы: `tsai-lenz`, `park-martin`, `daniilidis`, `li-wang-wu`, `shah`.
* Метрики: `mean, median, rmse, p95, max`.

---

Запуск:
```
uv run src/main.py [-h] [--method METHOD] [--file-a FILE_A] [--file-b FILE_B] [--print-xy]
```

Параметры:
```
options:
  -h, --help            show this help message and exit
  --method METHOD, -m METHOD
                        Метод: tsai-lenz | park-martin | daniilidis | li-wang-wu | shah | all (по умолчанию   
                        all)
  --file-a FILE_A, -a FILE_A
                        Путь к файлу A (по умолчанию data/calibF/MeasuredPositionsLeica.txt)
  --file-b FILE_B, -b FILE_B
                        Путь к файлу B (по умолчанию data/calibF/MeasuredPositionsTS_ModelLines.txt)
  --print-xy            Печатать матриц X и Y(Z) для выбранного метода
```

Пример вывода:
``` 
Translation errors (mm):
+-------------+--------+--------+--------+--------+--------+
| method      | mean   | median | rmse   | p95    | max    |
+-------------+--------+--------+--------+--------+--------+
| tsai-lenz   | 0.2935 | 0.2105 | 0.4022 | 0.4932 | 1.3859 |
| park-martin | 0.3652 | 0.3285 | 0.4470 | 0.6014 | 1.3231 |
| daniilidis  | 0.3098 | 0.2923 | 0.4103 | 0.5739 | 1.3185 |
| li-wang-wu  | 0.5409 | 0.4950 | 0.5700 | 0.8125 | 1.1459 |
| shah        | 0.3455 | 0.2838 | 0.4666 | 0.6250 | 1.6023 |
+-------------+--------+--------+--------+--------+--------+

Rotation errors (deg):
+-------------+--------+--------+--------+--------+--------+
| method      | mean   | median | rmse   | p95    | max    |
+-------------+--------+--------+--------+--------+--------+
| tsai-lenz   | 0.0470 | 0.0257 | 0.0976 | 0.0966 | 0.4067 |
| park-martin | 0.0515 | 0.0299 | 0.0972 | 0.1144 | 0.3942 |
| daniilidis  | 0.0461 | 0.0236 | 0.0997 | 0.0859 | 0.4196 |
| li-wang-wu  | 0.0466 | 0.0254 | 0.0996 | 0.0809 | 0.4192 |
| shah        | 0.0508 | 0.0289 | 0.0969 | 0.1095 | 0.3950 |
+-------------+--------+--------+--------+--------+--------+
```
