from textnode import TextNode, TextType
from split_nodes import *
from split_nodes_delimiter import split_nodes_delimiter

def text_to_textnodes(text):
    if not text:
        return []

    start = TextNode(text, TextType.TEXT)
    first_output = split_nodes_delimiter([start], "**", TextType.BOLD)
    print(f"first output: {first_output}")
    second_output = split_nodes_delimiter(first_output, "_", TextType.ITALIC)
    print(f"second output: {second_output}")
    third_output = split_nodes_delimiter(second_output, "`", TextType.CODE)
    print(f"third output: {third_output}")
    fourth_output = split_nodes_image(third_output)
    print(f"fourth output: {fourth_output}")
    return split_nodes_link(fourth_output)



if __name__ == "__main__":
    text_in = ""

    out = text_to_textnodes(text_in)

    print("Output:")
    pprint(out)
    print("Correct answer:")
    pprint(
        []
    )

