from pprint import pprint

def markdown_to_blocks(md):
    blocks = md.split("\n\n")
    return [block.strip("\n").strip() for block in blocks if block]

if __name__ == "__main__":
    input = "first block\n\nsecond block  \n\n\nthird block"
    output = markdown_to_blocks(input)

    print("My output:")
    pprint(output)
    print("Correct answer:")
    pprint(["first block", "second block", "third block"])