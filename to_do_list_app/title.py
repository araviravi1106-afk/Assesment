def print_title():
    patterns = {
        "T": ["*****", "  *  ", "  *  ", "  *  ", "  *  "],
        "O": [" *** ", "*   *", "*   *", "*   *", " *** "],
        "-": ["     ", "     ", " *** ", "     ", "     "],
        "D": ["**** ", "*   *", "*   *", "*   *", "**** "],
    }

    for row in range(5):
        print("  ".join(patterns[ch][row] for ch in "TO-DO"))

