# main.py

import sys
import os
from interpreter import run_desilang

def main():
    # Step 1: Check karo ki user ne file ka naam diya hai ya nahi
    if len(sys.argv) < 2:
        print("❌ Galti: File ka naam toh batao!")
        print("Usage: python main.py <filename.desi>")
        return

    filename = sys.argv[1]

    # Step 2: Check karo file exist karti hai ya nahi
    if not os.path.exists(filename):
        print(f"❌ Error: '{filename}' naam ki file nahi mili.")
        return

    # Step 3: File ko padho
    try:
        with open(filename, 'r') as f:
            code = f.read()
        
        # Step 4: Interpreter ko code run karne ko bolo
        run_desilang(code)
        
    except Exception as e:
        print(f"Kuch gadbad ho gayi file padhne me: {e}")

if __name__ == "__main__":
    main()