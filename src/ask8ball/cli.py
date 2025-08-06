import random
import sys
import importlib.resources  # <-- The new, professional way to read package files

def main():
    if len(sys.argv) < 2:
        print("Oops! You forgot to ask a question.")
        print("Usage: 8ball \"<your question here>\"") # <-- Updated usage text
        sys.exit(1)

    # This 'with' block is the only part that changes.
    with importlib.resources.open_text("ask8ball", "answers.txt") as f:
        answers = f.readlines()

    chosen_answer = random.choice(answers).strip()
    print(chosen_answer)

if __name__ == "__main__":
    main()