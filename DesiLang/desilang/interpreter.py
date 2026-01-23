import sys
import time
import random
import os
import csv
import math

def run_desilang(code):
    variables = {}
    
    # --- DATA ANALYST TOOLKIT ---
    
    def kholo_csv(filename):
        try:
            if not os.path.exists(filename):
                return f"❌ Error: File '{filename}' nahi mili."
            
            with open(filename, 'r', encoding='utf-8-sig') as f:
                reader = csv.DictReader(f)
                data = list(reader)
                
                cleaned_data = []
                for row in data:
                    new_row = {}
                    for k, v in row.items():
                        k = k.strip()
                        if v is None: v = ""
                        try: new_row[k] = int(v)
                        except:
                            try: new_row[k] = float(v)
                            except: new_row[k] = v.strip()
                    cleaned_data.append(new_row)
                return cleaned_data
        except Exception as e:
            return f"❌ Error: {e}"

    def jodo_column(data, column):
        total = 0
        if isinstance(data, list):
            for row in data:
                val = row.get(column, 0)
                try: total += float(val)
                except: pass
        return total

    def ausat_column(data, column):
        total = jodo_column(data, column)
        count = len(data) if isinstance(data, list) else 0
        if count > 0:
            return round(total / count, 2)
        return 0

    def filter_logic(data, condition_str):
        filtered = []
        if isinstance(data, list):
            for row in data:
                try:
                    if eval(condition_str, {}, row):
                        filtered.append(row)
                except: pass
        return filtered

    # --- CONTEXT SETTINGS ---
    eval_context = {
        "random": random,
        "time": time,
        "math": math,
        "kholo": kholo_csv,
        "jodo": jodo_column,
        "ausat": ausat_column,
        "chano": filter_logic,
        "chhano": filter_logic, # Dono spelling chalegi
        "gin": len,             # Option 1
        "gino": len             # Option 2 (New Feature)
    }

    lines = code.split('\n')
    i = 0 

    def parse_value(val):
        try: return int(val)
        except:
            try: return float(val)
            except: return val

    # --- MAIN LOOP ---
    while i < len(lines):
        line = lines[i].strip()
        
        if not line or line.startswith('#'):
            i += 1
            continue

        # COMMAND: "bol" YA "bolo"
        if line.startswith("bol ") or line.startswith("bolo "):
            if line.startswith("bolo "):
                expr = line[5:].strip()
            else:
                expr = line[4:].strip()

            if expr.startswith('"'):
                print(expr.strip('"'))
            else:
                try:
                    full_context = {**variables, **eval_context}
                    result = eval(expr, {}, full_context)
                    
                    if isinstance(result, list) and len(result) > 0 and isinstance(result[0], dict):
                        print(f"\n📊 DATA REPORT ({len(result)} rows)")
                        headers = list(result[0].keys())
                        print(" | ".join(f"{h:<10}" for h in headers)) 
                        print("-" * (len(headers) * 13))
                        for row in result[:10]:
                            print(" | ".join(f"{str(row.get(h, '')):<10}" for h in headers))
                        if len(result) > 10: 
                            print(f"... aur {len(result)-10} rows hain.")
                        print("-" * (len(headers) * 13) + "\n")
                    else:
                        print(result)
                except Exception as e:
                    print(f"⚠️ Error: {expr} ({e})")
            i += 1

        # COMMAND: "mano"
        elif line.startswith("mano "):
            parts = line[5:].split('=', 1) # Fix for filters with '=='
            
            if len(parts) < 2:
                print(f"❌ Syntax Error Line {i+1}: 'mano' ke baad '=' lagana bhool gaye?")
                i += 1
                continue

            var_name = parts[0].strip()
            expr = parts[1].strip()

            if expr.startswith("pooch "):
                prompt = expr[6:].strip().strip('"')
                val = input(prompt + " ")
                variables[var_name] = parse_value(val)
            else:
                full_context = {**variables, **eval_context}
                try:
                    variables[var_name] = eval(expr, {}, full_context)
                except Exception as e:
                    print(f"❌ Error in mano: {e}")
            i += 1

        # Logic Blocks (agar, warna, bas, jab tak, khatam, safai, ruko)
        elif line.startswith("agar "):
            condition = line[5:].strip()
            full_context = {**variables, **eval_context}
            try: result = eval(condition, {}, full_context)
            except: result = False
            if result: i += 1
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

        elif line == "bas": i += 1

        elif line.startswith("jab tak "):
            condition = line[8:].strip()
            full_context = {**variables, **eval_context}
            try:
                if eval(condition, {}, full_context): i += 1
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
            except: i += 1

        elif line == "khatam":
            scan = i
            nest = 0
            while scan >= 0:
                temp = lines[scan].strip()
                if temp == "khatam": nest += 1
                elif temp.startswith("jab tak "):
                    if nest == 1:
                        i = scan
                        break
                    else: nest -= 1
                scan -= 1
            if scan < 0: i += 1

        elif line == "safai":
            os.system('cls' if os.name == 'nt' else 'clear')
            i += 1
            
        elif line.startswith("ruko "):
            try: time.sleep(float(line[5:].strip()))
            except: pass
            i += 1
            
        else:
            i += 1