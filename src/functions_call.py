import numpy as np

from utils import load_poses_csv, df_to_Ts, summarize_errors
from tsai_lenz import tsai_lenz
from park_martin import park_martin
from daniilidis import daniilidis
from li_wang_wu import li_wang_wu
from shah import shah


DEFAULT_A = "data/calibF/MeasuredPositionsLeica.txt"
DEFAULT_B = "data/calibF/MeasuredPositionsTS_ModelLines.txt"

def run_method(name, As, Bs):
    if name == "tsai-lenz":
        X, Y = tsai_lenz(As, Bs)
    elif name == "park-martin":
        X, Y = park_martin(As, Bs)
    elif name == "daniilidis":
        X, Y = daniilidis(As, Bs)
    elif name == "li-wang-wu":
        X, Y = li_wang_wu(As, Bs)
    elif name == "shah":
        X, Y = shah(As, Bs)
    else:
        raise ValueError(f"Неизвестный метод: {name}")

    t_stats, r_stats = summarize_errors(As, Bs, X, Y)
    return X, Y, t_stats, r_stats


def load_inputs(file_A, file_B):
    dfA = load_poses_csv(file_A)
    dfB = load_poses_csv(file_B)

    As = df_to_Ts(dfA)
    Bs = df_to_Ts(dfB)
    return As, Bs


def print_table(rows, headers):
    widths = [len(h) for h in headers]
    for r in rows:
        for i, cell in enumerate(r):
            widths[i] = max(widths[i], len(cell))

    sep = "+".join("-" * (w + 2) for w in widths)
    line_sep = f"+{sep}+"

    def fmt_row(values):
        return "|" + "|".join(f" {v:<{w}} " for v, w in zip(values, widths)) + "|"

    print(line_sep)
    print(fmt_row(headers))
    print(line_sep)
    for r in rows:
        print(fmt_row(r))
    print(line_sep)


def get_error_data(methods, file_a, file_b):
    As, Bs = load_inputs(file_a, file_b)
    t_rows = {}
    r_rows = {}
    for name in methods:
            try:
                _, _, t_stats, r_stats = run_method(name, As, Bs)
                t_rows[name] = t_stats
                r_rows[name] = r_stats
            except Exception:
                t_rows[name] = {
                    "mean": "ERR",
                    "median": "ERR",
                    "rmse": "ERR",
                    "p95": "ERR",
                    "max": "ERR"
                    }
                r_rows[name] = {
                    "mean": "ERR",
                    "median": "ERR",
                    "rmse": "ERR",
                    "p95": "ERR",
                    "max": "ERR"
                    }
    return t_rows, r_rows

if __name__ == "__main__":
    one, two = get_error_data(["shah"], "1.txt", "2.txt")
    print(one)
    print(two)