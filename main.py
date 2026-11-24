"""Ridiculous at First Glance, Real by the Second — entry for make.fun.

Writes one sentence to /output/entry.txt.
The sentence is one startup pitch, under 200 characters, bizarre at first glance and sound on the second.
"""
import os

LINE = "We rent out professional line-standers for sold-out sneaker drops, so hypebeasts pay $40 an hour to never queue again — and the queue is the product."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
