"""Entry program: writes the one-star Moon review to /output/entry.txt."""
import os

ENTRY = "★☆☆☆☆ Changes shape every night and expects me to just accept that. Pick a phase and commit."

# Gate (sealed scorer): entry.txt must be UTF-8 text of 1 to 120 characters,
# not only white space. Fail loudly here instead of shipping an invalid entry.
assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} outside gate 1-120"
assert ENTRY.strip(), "entry must not be only white space"

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
