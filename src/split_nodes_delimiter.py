from textnode import TextNode, TextType
from pprint import pprint

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for old in old_nodes:
        if old.text.count(delimiter) == 0:
            new_nodes.append(old)
        elif old.text.count(delimiter)%2 == 0:
            pieces = old.text.split(delimiter)
            for n, piece in enumerate(pieces):
                if n%2 == 0:
                    new_nodes.append(TextNode(piece, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(piece, text_type))
        else:
            # print(f"Problem text: {old.text}")
            raise Exception("Text must contain exactly two instances of the delimiter")
    return new_nodes

if __name__ == "__main__":
    test_nodes = [
        TextNode("This contains plain text", TextType.TEXT),
        TextNode("This contains **bold** text", TextType.TEXT),
        TextNode("This contains _italic_ text", TextType.TEXT),
        TextNode("This contains `code` text", TextType.TEXT),
        TextNode("This contains `two` valid `code` fragments", TextType.TEXT),
        TextNode("This contains invalid **bold text", TextType.TEXT),
        TextNode("This contains invalid _italic text", TextType.TEXT),
        TextNode("This contains invalid `code text", TextType.TEXT),
        TextNode("This _contains **nested** bold_ text", TextType.TEXT),
    ]

    first_output = split_nodes_delimiter(test_nodes[:4], "**", TextType.BOLD)
    second_output = split_nodes_delimiter(first_output, "_", TextType.ITALIC)
    final_output = split_nodes_delimiter(second_output, "`", TextType.CODE)

    from pprint import pprint
    pprint(final_output)