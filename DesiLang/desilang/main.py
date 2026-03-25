# main.py
import sys
import os
from .interpreter import execute_desi
 
def main():
    if len(sys.argv) < 2:
        print("❌ Galti: File ka naam toh batao!")
        print("Usage: desilang <filename.desi>")
        return
 
    filename = sys.argv[1]
 
    if not os.path.exists(filename):
        print(f"❌ Error: '{filename}' naam ki file nahi mili.")
        return
 
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
        execute_desi(code)  # ← filepath nahi, code pass karo
    except Exception as e:
        print(f"❌ Kuch gadbad ho gayi: {e}")
 
if __name__ == "__main__":
    main()
