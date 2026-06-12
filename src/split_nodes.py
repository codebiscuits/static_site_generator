from textnode import TextNode, TextType
from extract_markdown import *
from pprint import pprint

def split_nodes_image(nodes: list[TextNode]) -> list[TextNode]:
    # print("\ncalling split image\n")
    new_nodes = []
    if not nodes:
        return nodes
    for node in nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        elif node.text == "":
            new_nodes.append(node)
        else:
            # print(f"node text: {node.text}")
            img_matches = extract_markdown_images(node.text)
            if not img_matches:
                new_nodes.append(node)
                continue
            match = img_matches[0]
            split_str = f"![{match[0]}]({match[1]})"
            sections = node.text.split(split_str, maxsplit=1)
            sections = [s for s in sections if s]
            if sections:
                new_nodes.extend(
                    (
                        TextNode(sections[0], TextType.TEXT),
                        TextNode(match[0], TextType.IMAGE, match[1]),
                    )
                )
            else:
                new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            if len(sections) > 1:
                if len(img_matches) > 1:
                    new_nodes.extend(split_nodes_image([TextNode(sections[1], TextType.TEXT)]))
                else:
                    new_nodes.append(TextNode(sections[1], TextType.TEXT))

    return new_nodes


def split_nodes_link(nodes: list[TextNode]) -> list[TextNode]:
    # print("\ncalling split link\n")
    new_nodes = []
    if not nodes:
        return nodes
    for node in nodes:
        if node.text_type != TextType.TEXT or node.text == "":
            new_nodes.append(node)
        else:
            link_matches = extract_markdown_links(node.text)
            if not link_matches:
                new_nodes.append(node)
                continue
            # print(f"split_nodes_link processing {node.text}")
            match = link_matches[0]
            split_str = f"[{match[0]}]({match[1]})"
            sections = node.text.split(split_str, maxsplit=1)
            sections = [s for s in sections if s]
            if sections:
                new_nodes.extend(
                    (
                        TextNode(sections[0], TextType.TEXT),
                        TextNode(match[0], TextType.LINK, match[1]),
                    )
                )
            else:
                new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            if len(sections) > 1:
                if len(link_matches) > 1:
                    new_nodes.extend(split_nodes_link([TextNode(sections[1], TextType.TEXT)]))
                else:
                    new_nodes.append(TextNode(sections[1], TextType.TEXT))

    return new_nodes

if __name__ == "__main__":
    from pprint import pprint

    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png), this is text with a link [to boot dev](https://www.boot.dev) and another ![second image](https://i.imgur.com/3elNhQu.png) and [to youtube](https://www.youtube.com/@bootdotdev)",
        TextType.TEXT,
    )
    print("Calling Split Image")
    split_1 = split_nodes_image([node])
    print("Split Image call complete")
    pprint(split_1)
    print("Calling Split Link")
    split_2 = split_nodes_link(split_1)
    print("Split Link call complete")
    pprint(split_2)
    print("\nCorrect answer below:")
    pprint([
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(", this is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and another ", TextType.TEXT),
            TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ])
