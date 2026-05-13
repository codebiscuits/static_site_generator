from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old in old_nodes:
        if old.text.count(delimiter) == 0:
            new_nodes.append(old)
        elif old.text.count(delimiter) != 2:
            raise Exception("Text must contain exactly two instances of the delimiter")
        else:
            pieces = old.text.split(delimiter)
            new_nodes.extend(
                (
                    TextNode(pieces[0], TextType.TEXT),
                    TextNode(pieces[1], text_type),
                    TextNode(pieces[2], TextType.TEXT),
                )
            )
    return new_nodes

if __name__ == "__main__":
    test_nodes = [
        TextNode("This contains plain text", TextType.TEXT),
        TextNode("This contains **bold** text", TextType.TEXT),
        TextNode("This contains _italic_ text", TextType.TEXT),
        TextNode("This contains `code` text", TextType.TEXT),
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