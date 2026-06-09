from pprint import pprint

def markdown_to_blocks(md: str) -> list[str]:
    blocks = md.split("\n\n")
    # print(f"md_to_blocks 1: {len(blocks)} blocks")
    # if len(blocks) == 1:
    #     # remove newlines by splitting on them and joining back together
    #     return [" ".join(blocks[0].split("\n")).strip()]
    # # remove newlines for each block in the list
    # return [" ".join(block.split("\n")).strip() for block in blocks if block]
    return [block.strip(" ").strip("\n") for block in blocks if block]

# if __name__ == "__main__":
#     input = "first block\n\nsecond block  \n\n\nthird block"
#     output = markdown_to_blocks(input)
#
#     print("My output:")
#     pprint(output)
#     print("Correct answer:")
#     pprint(["first block", "second block", "third block"])