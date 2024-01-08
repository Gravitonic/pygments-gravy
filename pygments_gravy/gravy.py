"""Personal Pygments style."""

from pygments.style import Style
from pygments.token import Token


class GravyStyle(Style):
    """Personal Pygments style."""

    background_color = "#fff"

    styles = {
        Token.Comment: "italic #A8A8B3",  # "italic #3D7B7B",
        Token.Comment.Preproc: "#E98816",  # "noitalic #9C6500",
        Token.Keyword: "bold #7E53CF",  # "bold #008000",
        Token.Keyword.Pseudo: "nobold",  # "nobold",
        Token.Keyword.Type: "nobold #EB7ABA",  # "nobold #B00040",
        Token.Name.Builtin.Pseudo: "bold #EB7ABA",
        Token.Name.Function: "bold #0E5DE4",  # "#0000FF",
        Token.Name.Class: "bold #0E5DE4",  # "bold #0000FF",
        Token.Name.Exception: "#EB7ABA",  # "bold #CB3F38",
        Token.Name.Variable: "#292933",  # "#19177C",
        Token.Name.Constant: "#E98816",  # "#880000",
        Token.Name.Entity: "#757580",  # "bold #717171",
        Token.Name.Attribute: "#21B5CC",  # "#687822",
        Token.Name.Tag: "#DC2430",  # "bold #008000",
        Token.Name.Decorator: "#0E5DE4",  # "#AA22FF",
        Token.String: "#19A964",  # "#BA2121",
        Token.String.Interpol: "#0E5DE4",  # "bold #A45A77",
        Token.String.Escape: "#757580",  # "bold #AA5D1F",
        Token.String.Symbol: "bold #EB7ABA",
        Token.String.Affix: "#E98816",
        Token.Number: "#E98816",  # "#666666",
        Token.Operator: "#757580",
        Token.Operator.Word: "bold #7E53CF",
        Token.Punctuation: "#292933",
        Token.Punctuation.Marker: "#E98816",
        Token.Generic.Heading: "#0E5DE4",  # "bold #000080",
        Token.Generic.Subheading: "#0E5DE4",  # "bold #800080",
        Token.Generic.Deleted: "#DC2430",  # "#A00000",
        Token.Generic.Inserted: "#19A964",  # "#008400",
        Token.Generic.Error: "bold #DC2430",  # "#E40000",
        Token.Generic.Emph: "italic",  # "italic",
        Token.Generic.Strong: "bold",  # "bold",
        Token.Generic.EmphStrong: "bold italic",  # "bold italic",
        Token.Generic.Prompt: "bold #0E5DE4",  # "bold #000080",
        Token.Generic.Output: "#292933",  # "#717171",
        Token.Generic.Traceback: "#757580",  # "#04D",
        Token.Error: "border:#DC2430",  # "border:#FF0000",
    }
