class HTMLNode:
    def __init__(
            self,
            tag: str = None,
            value: str = None,
            children: list[HTMLNode] = None,
            props: dict[str, str] = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        else:
            return "".join([f' {k}="{v}"' for k, v in self.props.items()])

    def __repr__(self):
        return f"HTMLNode\n{self.tag}\n{self.value}\n{self.children}\n{self.props_to_html()}"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        elif self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"HTMLNode\n{self.tag}\n{self.value}\n{self.props_to_html()}"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        elif not self.children:
            raise ValueError("ParentNode must have children")
        else:
            if isinstance(self.children, list):
                htmls = []
                for child in self.children:
                    if not isinstance(child, HTMLNode):
                        raise ValueError("ParentNode children must be HTMLNode")
                    child_html = child.to_html()
                    htmls.append(child_html)
                all_children = "".join(htmls)
                return f"<{self.tag}>{all_children}</{self.tag}>"
            elif isinstance(self.children, HTMLNode):
                return f"<{self.tag}>{self.children.to_html()}</{self.tag}>"
            else:
                raise ValueError("ParentNode children must be a list or a LeafNode")
