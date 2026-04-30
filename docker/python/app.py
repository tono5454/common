# app.py

import openai
import time

def main():
    print("Package versions:")
    print(f"openai: {openai.__version__}")
    while True:
       time.sleep (30)

if __name__ == "__main__":
    main()
