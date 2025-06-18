import sys
from dataclasses import dataclass


W: int = 1000
H: int = 1000 

W_R: int = 300
H_R: int = 100


@dataclass
class Element:
    color: str
    text: str
    x: int
    y: int


def data_parser(file: str) -> list[Element] | int:
    elements: list[Element] = []
    current_y: int = 100
    last = 0

    with open(file, "r") as f:
        for line in f.readlines():
            end_sq_b = line.find("]")

            text = line[end_sq_b + 1 :].strip()
            prop = line[1:end_sq_b].split("-")

            if current_y > H:
                raise Exception("Too many rec")

            el = Element(
                prop[0],
                text,
                200,
                current_y,
            )
            current_y += 200
            elements.append(el)
            last += 1

    return elements, last


def crafter(elements: list[Element], last: int) -> str:
    data: list[str] = []
    current: int = 0
    current_y_1: int = 200
    current_y_2: int = 100
    current_text_y: int = 140

    for element in elements:
        data.append(
            f'<rect width={W_R} height={H_R} x={element.x} y={element.y} rx="20" ry="20" fill={element.color} />\n'
        )
        data.append(
            f'<text x=345 y={current_text_y} font-family="Arial" font-size="20" fill="white" text-anchor="middle" alignment-baseline="middle"> {element.text}</text>\n'
        )
        current_text_y += 200

        if current + 1 != last:
            y_1 = current_y_1
            y_2 = current_y_2 + 200
            data.append(
                f'<line x1=345 y1={y_1} x2=345 y2={y_2} style="stroke:white;stroke-width:1" />\n'
            )

            current_y_1: int = current_y_1 * 2
            current_y_2: int = current_y_2 + 200
            current += 1

    return f"<svg height={H} width={W}>\n{"".join(data)}</svg>" + "><style>body {background-color: black;}</style>"

def main() -> None:
    file: str = sys.argv[1]

    elements, last = data_parser(file)
    result = crafter(elements, last)
    with open("result.html", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
