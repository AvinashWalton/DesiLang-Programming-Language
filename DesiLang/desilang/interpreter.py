import sys
import os
import time
import random
import math
import csv

# Structures import (Data Science features)
try:
    from .structures import Table, Ladi, kholo, Sikhao, rishta, jodo, ausat, Khali
    STRUCTURES_AVAILABLE = True
except ImportError:
    try:
        from structures import Table, Ladi, kholo, Sikhao, rishta, jodo, ausat, Khali
        STRUCTURES_AVAILABLE = True
    except ImportError:
        STRUCTURES_AVAILABLE = False


# ============================================================
#   DesiLang v1.2.0 — Ab Functions (kaam) Support ke saath!
#   Created by: Avinash Walton
#   GitHub: github.com/AvinashWalton/DesiLang
# ============================================================

def execute_desi(code, _variables=None, _functions=None, _output_collector=None):
    """
    DesiLang Interpreter — Main Engine
    
    Features:
    - bolo / bol       → Print
    - mano             → Variable
    - agar / warna     → If / Else
    - jab tak / khatam → While Loop
    - kaam / wapas     → Function define & return  ← NEW v1.2.0
    - pooch            → User Input
    - safai            → Clear Screen
    - ruko             → Sleep
    - Data Analysis    → kholo, chano, jodo, ausat, gino
    """

    # --- GLOBAL STATE ---
    variables = _variables if _variables is not None else {}
    functions = _functions if _functions is not None else {}

    # Output collector: None = direct print, list = collect karo (playground ke liye)
    def desi_output(text):
        if _output_collector is not None:
            _output_collector.append(str(text))
        else:
            print(text)

    # --- BASE DATA FUNCTIONS ---
    def _jodo_col(data, col):
        total = 0
        if isinstance(data, list):
            for row in data:
                try: total += float(row.get(col, 0))
                except: pass
        elif STRUCTURES_AVAILABLE and isinstance(data, Table):
            return data[col].sum()
        return total

    def _ausat_col(data, col):
        total = _jodo_col(data, col)
        count = len(data) if hasattr(data, '__len__') else 0
        return round(total / count, 2) if count else 0

    def _filter_data(data, cond):
        if STRUCTURES_AVAILABLE and isinstance(data, Table):
            try: return data.query(cond)
            except: pass
        filtered = []
        if isinstance(data, list):
            for row in data:
                try:
                    if eval(cond, {}, row): filtered.append(row)
                except: pass
        return filtered

    def _kholo_csv(filepath):
        if STRUCTURES_AVAILABLE:
            return kholo(filepath)
        # Fallback: plain CSV reader
        try:
            with open(filepath, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                data = []
                for row in reader:
                    new_row = {}
                    for k, v in row.items():
                        k = k.strip()
                        if v is None: v = ""
                        try: new_row[k] = int(v.strip())
                        except:
                            try: new_row[k] = float(v.strip())
                            except: new_row[k] = v.strip()
                    data.append(new_row)
                return data
        except FileNotFoundError:
            desi_output(f"❌ Error: File nahi mili: {filepath}")
            return []

    def _print_data(val):
        if isinstance(val, list) and val and isinstance(val[0], dict):
            headers = list(val[0].keys())
            desi_output(f"\n📊 DATA TABLE ({len(val)} rows)")
            desi_output(" | ".join(f"{h:<12}" for h in headers))
            desi_output("─" * (len(headers) * 15))
            for row in val[:15]:
                desi_output(" | ".join(f"{str(row.get(h,'')):<12}" for h in headers))
            if len(val) > 15:
                desi_output(f"  ... aur {len(val)-15} rows hain.")
            desi_output("")
        elif STRUCTURES_AVAILABLE and isinstance(val, (Table, Ladi)):
            desi_output(str(val))
        else:
            desi_output(str(val))

    # --- EVAL CONTEXT ---
    EVAL_CTX = {
        "random": random, "math": math, "time": time,
        "len": len, "range": range, "int": int, "float": float,
        "str": str, "abs": abs, "round": round, "print": desi_output,
        "kholo": _kholo_csv,
        "jodo": _jodo_col,
        "ausat": _ausat_col,
        "chano": _filter_data, "chhano": _filter_data,
        "gin": len, "gino": len,
        "sahi": True, "galat": False,
    }
    if STRUCTURES_AVAILABLE:
        EVAL_CTX.update({
            "Table": Table, "Ladi": Ladi,
            "Sikhao": Sikhao, "rishta": rishta, "Khali": Khali,
        })

    def get_full_ctx():
        return {**variables, **EVAL_CTX, **{
            name: make_callable(name, fn)
            for name, fn in functions.items()
        }}

    # ============================================================
    #   FUNCTION CALL ENGINE
    # ============================================================
    def make_callable(func_name, func_def):
        """DesiLang function ko Python callable mein badlo"""
        def callable_func(*args):
            return call_kaam(func_name, list(args))
        return callable_func

    def call_kaam(func_name, args):
        """kaam (function) ko chalao aur wapas (return) value do"""
        if func_name not in functions:
            desi_output(f"❌ Error: '{func_name}' naam ka kaam nahi mila!")
            return None

        func_def = functions[func_name]
        params   = func_def["params"]
        body     = func_def["body"]

        # Local scope banao
        local_vars = dict(variables)
        for p, a in zip(params, args):
            local_vars[p] = a

        # Body run karo (recursive call with local scope)
        return_val = [None]
        returned   = [False]

        def local_output(text):
            desi_output(text)

        # Body ke lines run karo
        result = execute_desi(
            "\n".join(body),
            _variables=local_vars,
            _functions=functions,
            _output_collector=_output_collector
        )
        return result  # wapas value yahan aayegi

    # ============================================================
    #   PASS 1 — Saare 'kaam' (functions) collect karo
    # ============================================================
    lines = code.split('\n')
    i = 0
    skip_lines = set()  # Function definition lines skip hongi main loop mein

    while i < len(lines):
        line = lines[i].strip()

        if line.startswith("kaam "):
            func_start = i
            # Header parse karo: "kaam greet(naam, saal):"
            header = line[5:].strip().rstrip(":")

            if "(" in header and ")" in header:
                func_name  = header[:header.index("(")].strip()
                params_str = header[header.index("(")+1 : header.index(")")].strip()
                params     = [p.strip() for p in params_str.split(",") if p.strip()]
            else:
                func_name = header.strip()
                params    = []

            # Body collect karo (khatam tak)
            body_lines = []
            skip_lines.add(i)  # kaam header line skip
            i += 1

            nest = 0
            while i < len(lines):
                curr = lines[i].strip()
                skip_lines.add(i)

                if curr.startswith("kaam "):
                    nest += 1
                if curr == "khatam":
                    if nest == 0:
                        break
                    nest -= 1

                body_lines.append(lines[i])
                i += 1

            skip_lines.add(i)  # khatam line skip

            # Function save karo
            functions[func_name] = {
                "params": params,
                "body": body_lines,
                "start_line": func_start,
            }

        i += 1

    # ============================================================
    #   PASS 2 — Main Code Run karo (functions skip karke)
    # ============================================================
    def parse_val(v):
        try: return int(v)
        except:
            try: return float(v)
            except: return v

    # Special: wapas (return) ke liye
    RETURN_SIGNAL = object()
    return_value  = [None]

    i = 0
    while i < len(lines):

        # Function definition lines skip karo
        if i in skip_lines:
            i += 1
            continue

        raw  = lines[i]
        line = raw.strip()

        # Khali lines aur comments skip
        if not line or line.startswith("#"):
            i += 1
            continue

        full_ctx = get_full_ctx()

        # ----------------------------------------------------------
        # bolo / bol → Print
        # ----------------------------------------------------------
        if line.startswith("bolo ") or line.startswith("bol "):
            expr = line[5:].strip() if line.startswith("bolo ") else line[4:].strip()

            if expr.startswith('"') and expr.endswith('"') and expr.count('"') == 2:
                desi_output(expr[1:-1])
            elif expr == '" "' or expr == "' '":
                desi_output(" ")
            else:
                try:
                    result = eval(expr, {}, full_ctx)
                    _print_data(result)
                except Exception as e:
                    desi_output(f"⚠️ bolo error: {expr} → {e}")
            i += 1

        # ----------------------------------------------------------
        # mano → Variable assign
        # ----------------------------------------------------------
        elif line.startswith("mano "):
            parts = line[5:].split("=", 1)
            if len(parts) < 2:
                desi_output(f"❌ Line {i+1}: '=' nahi mila 'mano' ke baad")
                i += 1
                continue

            var_name = parts[0].strip()
            expr     = parts[1].strip()

            if expr.startswith("pooch "):
                prompt = expr[6:].strip().strip('"')
                try:
                    val = input(prompt + " ")
                    variables[var_name] = parse_val(val)
                except EOFError:
                    variables[var_name] = ""
            else:
                try:
                    variables[var_name] = eval(expr, {}, full_ctx)
                except Exception as e:
                    desi_output(f"❌ mano error '{var_name}': {e}")
            i += 1

        # ----------------------------------------------------------
        # wapas → Return (function ke andar)
        # ----------------------------------------------------------
        elif line.startswith("wapas "):
            expr = line[6:].strip()
            try:
                return_value[0] = eval(expr, {}, full_ctx)
            except Exception as e:
                desi_output(f"❌ wapas error: {e}")
                return_value[0] = None
            return return_value[0]  # ← Seedha return karo

        # ----------------------------------------------------------
        # agar → If
        # ----------------------------------------------------------
        elif line.startswith("agar "):
            cond = line[5:].strip()
            try: result = eval(cond, {}, full_ctx)
            except: result = False

            if result:
                i += 1
            else:
                nest = 0
                while i < len(lines):
                    i += 1
                    if i >= len(lines): break
                    curr = lines[i].strip()
                    if curr.startswith("agar "): nest += 1
                    if curr == "bas":
                        if nest == 0: break
                        nest -= 1
                    if curr == "warna" and nest == 0: break

        # ----------------------------------------------------------
        # warna → Else
        # ----------------------------------------------------------
        elif line == "warna":
            nest = 0
            while i < len(lines):
                i += 1
                if i >= len(lines): break
                curr = lines[i].strip()
                if curr.startswith("agar "): nest += 1
                if curr == "bas":
                    if nest == 0: break
                    nest -= 1
            i += 1

        elif line == "bas":
            i += 1

        # ----------------------------------------------------------
        # jab tak → While Loop
        # ----------------------------------------------------------
        elif line.startswith("jab tak "):
            cond = line[8:].strip()
            full_ctx = get_full_ctx()
            try:
                if eval(cond, {}, full_ctx): i += 1
                else:
                    nest = 0
                    while i < len(lines):
                        i += 1
                        if i >= len(lines): break
                        curr = lines[i].strip()
                        if curr.startswith("jab tak "): nest += 1
                        if curr == "khatam":
                            if nest == 0: break
                            nest -= 1
                    i += 1
            except:
                i += 1

        # ----------------------------------------------------------
        # khatam → End Loop
        # ----------------------------------------------------------
        elif line == "khatam":
            scan = i
            nest = 0
            while scan >= 0:
                temp = lines[scan].strip()
                if temp == "khatam": nest += 1
                elif temp.startswith("jab tak "):
                    if nest == 1: i = scan; break
                    else: nest -= 1
                scan -= 1
            if scan < 0: i += 1

        # ----------------------------------------------------------
        # safai → Clear Screen
        # ----------------------------------------------------------
        elif line == "safai":
            if _output_collector is None:
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                desi_output("🧹 [Screen saaf]")
            i += 1

        # ----------------------------------------------------------
        # ruko → Sleep
        # ----------------------------------------------------------
        elif line.startswith("ruko "):
            try:
                secs = float(line[5:].strip())
                if _output_collector is None:
                    time.sleep(secs)
                else:
                    desi_output(f"⏳ ruko {secs} sec...")
            except: pass
            i += 1

        # ----------------------------------------------------------
        # Direct function call: greet("Avinash") ya koi expression
        # ----------------------------------------------------------
        else:
            try:
                eval(line, {}, full_ctx)
            except Exception as e:
                desi_output(f"❌ Line {i+1}: Samajh nahi aaya → '{line}' ({e})")
            i += 1

    return return_value[0]


# ============================================================
#   FILE RUNNER
# ============================================================
def run_desilang(filepath):
    """DesiLang .desi file chalao"""
    if not os.path.exists(filepath):
        print(f"❌ Error: File '{filepath}' nahi mili.")
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        execute_desi(code)
    except Exception as e:
        print(f"❌ File Read Error: {e}")


# ============================================================
#   DIRECT RUN
# ============================================================
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Usage: python -m desilang.interpreter <file.desi>")
    else:
        run_desilang(sys.argv[1])
