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