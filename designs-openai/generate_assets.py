"""Generate CurationsLA Holiday Guide 2025 illustration SVG assets."""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Sequence, Tuple
import xml.etree.ElementTree as ET

PALETTE: Dict[str, str] = {
    "lime": "#D4FF5B",
    "purple": "#A078FF",
    "hot_pink": "#FF6B9D",
    "sky_blue": "#74B9FF",
    "sunshine": "#FFE66D",
    "winter_blue": "#5AC8FA",
    "frost_mint": "#B8F8E3",
    "black": "#000000",
    "off_white": "#F8F5EC",
}

STROKE_WIDTH = 8
FONT = "Helvetica, Arial, sans-serif"


def svg_root(width: int, height: int) -> ET.Element:
    svg = ET.Element(
        "svg",
        {
            "xmlns": "http://www.w3.org/2000/svg",
            "width": str(width),
            "height": str(height),
            "viewBox": f"0 0 {width} {height}",
            "style": f"background:{PALETTE['off_white']}",
        },
    )
    return svg


def add_rect(
    parent: ET.Element,
    x: float,
    y: float,
    width: float,
    height: float,
    *,
    fill: str,
    stroke: str = PALETTE["black"],
    stroke_width: float = STROKE_WIDTH,
    rx: float | None = None,
    ry: float | None = None,
) -> ET.Element:
    attrib = {
        "x": f"{x}",
        "y": f"{y}",
        "width": f"{width}",
        "height": f"{height}",
        "fill": fill,
        "stroke": stroke,
        "stroke-width": f"{stroke_width}",
        "stroke-linejoin": "miter",
    }
    if rx is not None:
        attrib["rx"] = f"{rx}"
    if ry is not None:
        attrib["ry"] = f"{ry}"
    return ET.SubElement(parent, "rect", attrib)


def add_circle(
    parent: ET.Element,
    cx: float,
    cy: float,
    r: float,
    *,
    fill: str,
    stroke: str = PALETTE["black"],
    stroke_width: float = STROKE_WIDTH,
) -> ET.Element:
    return ET.SubElement(
        parent,
        "circle",
        {
            "cx": f"{cx}",
            "cy": f"{cy}",
            "r": f"{r}",
            "fill": fill,
            "stroke": stroke,
            "stroke-width": f"{stroke_width}",
        },
    )


def add_line(
    parent: ET.Element,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    *,
    stroke: str = PALETTE["black"],
    stroke_width: float = STROKE_WIDTH,
) -> ET.Element:
    return ET.SubElement(
        parent,
        "line",
        {
            "x1": f"{x1}",
            "y1": f"{y1}",
            "x2": f"{x2}",
            "y2": f"{y2}",
            "stroke": stroke,
            "stroke-width": f"{stroke_width}",
        },
    )


def add_polygon(
    parent: ET.Element,
    points: Sequence[Tuple[float, float]],
    *,
    fill: str,
    stroke: str = PALETTE["black"],
    stroke_width: float = STROKE_WIDTH,
) -> ET.Element:
    return ET.SubElement(
        parent,
        "polygon",
        {
            "points": " ".join(f"{x},{y}" for x, y in points),
            "fill": fill,
            "stroke": stroke,
            "stroke-width": f"{stroke_width}",
        },
    )


def add_text(
    parent: ET.Element,
    text: str,
    x: float,
    y: float,
    *,
    size: float,
    fill: str = PALETTE["black"],
    anchor: str = "middle",
    weight: str = "700",
) -> ET.Element:
    elem = ET.SubElement(
        parent,
        "text",
        {
            "x": f"{x}",
            "y": f"{y}",
            "fill": fill,
            "font-size": f"{size}",
            "font-family": FONT,
            "font-weight": weight,
            "text-anchor": anchor,
            "dominant-baseline": "central",
        },
    )
    elem.text = text
    return elem


def add_group(parent: ET.Element, *, translate: Tuple[float, float] | None = None) -> ET.Element:
    attrib: Dict[str, str] = {}
    if translate:
        attrib["transform"] = f"translate({translate[0]},{translate[1]})"
    return ET.SubElement(parent, "g", attrib)


def write_svg(path: Path, svg: ET.Element) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    xml = ET.tostring(svg, encoding="unicode")
    path.write_text("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" + xml, encoding="utf-8")


def crowd_strip(parent: ET.Element, width: float, y: float, height: float) -> None:
    add_rect(parent, 60, y, width - 120, height, fill=PALETTE["black"], stroke=PALETTE["black"], stroke_width=0)
    spacing = 36
    for idx in range(int((width - 120) // spacing) + 2):
        add_circle(parent, 60 + spacing / 2 + idx * spacing, y + height / 2, spacing / 3, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 2)


def nutcracker(parent: ET.Element, x: float, y: float, scale: float, colors: Sequence[str]) -> None:
    torso = add_rect(parent, x - 40 * scale, y - 80 * scale, 80 * scale, 120 * scale, fill=PALETTE[colors[0]])
    add_rect(parent, x - 50 * scale, y - 120 * scale, 100 * scale, 40 * scale, fill=PALETTE[colors[1]])
    add_rect(parent, x - 30 * scale, y - 160 * scale, 60 * scale, 40 * scale, fill=PALETTE[colors[2]])
    add_rect(parent, x - 25 * scale, y + 40 * scale, 50 * scale, 70 * scale, fill=PALETTE[colors[1]])
    add_rect(parent, x - 40 * scale, y + 110 * scale, 30 * scale, 70 * scale, fill=PALETTE[colors[2]])
    add_rect(parent, x + 10 * scale, y + 110 * scale, 30 * scale, 70 * scale, fill=PALETTE[colors[2]])
    add_circle(parent, x, y - 40 * scale, 24 * scale, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 1.5)
    add_line(parent, x - 12 * scale, y - 35 * scale, x + 12 * scale, y - 35 * scale, stroke_width=STROKE_WIDTH / 2)
    add_line(parent, x - 8 * scale, y - 20 * scale, x - 2 * scale, y - 15 * scale, stroke_width=STROKE_WIDTH / 2)
    add_line(parent, x + 8 * scale, y - 20 * scale, x + 2 * scale, y - 15 * scale, stroke_width=STROKE_WIDTH / 2)


def palm_tree(parent: ET.Element, x: float, y: float, height: float, colors: Sequence[str]) -> None:
    band = height / 5
    for idx in range(5):
        add_rect(parent, x - 10, y - band * (idx + 1), 20, band, fill=PALETTE[colors[idx % len(colors)]])
    for angle in (-50, -20, 20, 50):
        rad = math.radians(angle)
        length = 80
        points = [
            (x, y - height),
            (x + math.cos(rad) * length, y - height - math.sin(rad) * length * 0.3),
            (x + math.cos(rad) * length * 0.8, y - height - math.sin(rad) * length * 0.7),
        ]
        add_polygon(parent, points, fill=PALETTE["winter_blue"] if angle % 2 else PALETTE["lime"], stroke_width=STROKE_WIDTH / 2)


def ornament_strand(parent: ET.Element, x: float, y: float, width: float, bulbs: int) -> None:
    add_line(parent, x, y, x + width, y, stroke_width=STROKE_WIDTH / 2)
    colors = ["hot_pink", "sky_blue", "sunshine", "lime", "purple"]
    spacing = width / (bulbs - 1)
    for idx in range(bulbs):
        add_circle(parent, x + spacing * idx, y + 20, 14, fill=PALETTE[colors[idx % len(colors)]], stroke_width=STROKE_WIDTH / 2)


@dataclass
class Neighborhood:
    slug: str
    name: str
    street_label: str
    skyline_landmark: str
    shopping_icons: List[Tuple[str, str]]
    eats_icons: List[str]
    events: Dict[int, str]
    map_shopping: List[str]
    map_landmarks: List[str]
    map_parking: List[str]
    map_restrooms: List[str]
    landmark_icons: List[str]


NEIGHBORHOODS: List[Neighborhood] = [
    Neighborhood(
        slug="beverly-hills",
        name="Beverly Hills",
        street_label="RODEO DRIVE",
        skyline_landmark="Palm Lined Luxury",
        shopping_icons=[
            ("FASHION BOUTIQUE", "fashion"),
            ("JEWELRY HOUSE", "jewelry"),
            ("DESIGN OBJECTS", "design"),
            ("BEAUTY BAR", "beauty"),
            ("ART GALLERY", "gallery"),
            ("TOY EMPORIUM", "toy"),
        ],
        eats_icons=["HOT COCOA", "FINE DINING", "TAKEOUT", "HOLIDAY COOKIE", "COCKTAIL", "BAKERY PASTRY"],
        events={1: "Boulevard Lighting", 8: "Luxury Walk", 15: "Nutcracker Pop-Up", 22: "Midnight Stroll"},
        map_shopping=["Luxury Row", "Designer Alley"],
        map_landmarks=["Palm Atrium"],
        map_parking=["P1", "P2"],
        map_restrooms=["R"],
        landmark_icons=["Rodeo Palm", "Gift Stack", "Boutique Arch", "Holiday Star"],
    ),
    Neighborhood(
        slug="old-pasadena",
        name="Old Pasadena",
        street_label="COLORADO BOULEVARD",
        skyline_landmark="Pasadena City Hall",
        shopping_icons=[
            ("INDIE BOOKSTORE", "book"),
            ("ARTISAN MARKET", "market"),
            ("DESIGN STUDIO", "design"),
            ("VINTAGE SHOP", "vintage"),
            ("GALLERY STORE", "gallery"),
            ("TOY SHOP", "toy"),
        ],
        eats_icons=["HOT COCOA", "FINE DINING", "TAKEOUT", "HOLIDAY COOKIE", "COCKTAIL", "BAKERY PASTRY"],
        events={3: "Tree Lighting", 10: "Book Fair", 17: "Art Walk", 23: "Midnight Choir"},
        map_shopping=["Mercado Row", "Gallery Walk"],
        map_landmarks=["City Hall"],
        map_parking=["P"],
        map_restrooms=["R"],
        landmark_icons=["City Hall Dome", "Book Stack", "Ornament Tower", "Gift Bag"],
    ),
    Neighborhood(
        slug="long-beach",
        name="Long Beach",
        street_label="PINE AVENUE",
        skyline_landmark="Queen Mary Silhouette",
        shopping_icons=[
            ("SURF SHOP", "surf"),
            ("NAUTICAL GIFTS", "nautical"),
            ("RECORD SHOP", "record"),
            ("ART MARKET", "gallery"),
            ("FASHION BOUTIQUE", "fashion"),
            ("HOME GOODS", "home"),
        ],
        eats_icons=["HOT COCOA", "SEAFOOD DINING", "TAKEOUT", "HOLIDAY COOKIE", "COCKTAIL", "BAKERY PASTRY"],
        events={4: "Harbor Lights", 11: "Ship Tours", 18: "Pier Concert", 24: "Eve Fireworks"},
        map_shopping=["Pier Market", "Pine Boutiques"],
        map_landmarks=["Queen Mary", "Aquarium"],
        map_parking=["P1"],
        map_restrooms=["R1"],
        landmark_icons=["Queen Mary", "Wave Icon", "Pine Sign", "Gift Buoy"],
    ),
    Neighborhood(
        slug="griffith-park-los-feliz",
        name="Griffith Park",
        street_label="LOS FELIZ VILLAGE",
        skyline_landmark="Observatory Glow",
        shopping_icons=[
            ("BOOK & VINYL", "record"),
            ("WELLNESS SHOP", "wellness"),
            ("ART PRINTS", "gallery"),
            ("CAFÉ MARKET", "market"),
            ("TOY STORE", "toy"),
            ("FLORAL BAR", "floral"),
        ],
        eats_icons=["HOT COCOA", "FINE DINING", "TAKEOUT", "HOLIDAY COOKIE", "COCKTAIL", "BAKERY PASTRY"],
        events={2: "Observatory Illumination", 9: "Story Hour", 16: "Village Market", 21: "Solstice Jam"},
        map_shopping=["Village Row"],
        map_landmarks=["Observatory", "Hill Trail"],
        map_parking=["P"],
        map_restrooms=["R"],
        landmark_icons=["Observatory", "Palm Crest", "Village Sign", "Starburst"],
    ),
    Neighborhood(
        slug="culver-city",
        name="Culver City",
        street_label="CULVER BOULEVARD",
        skyline_landmark="Creative Campus",
        shopping_icons=[
            ("DESIGN HUB", "design"),
            ("INDIE BOOKS", "book"),
            ("TECH GIFTS", "tech"),
            ("ART GALLERY", "gallery"),
            ("TOY LAB", "toy"),
            ("WELLNESS SHOP", "wellness"),
        ],
        eats_icons=["HOT COCOA", "FINE DINING", "TAKEOUT", "HOLIDAY COOKIE", "COCKTAIL", "BAKERY PASTRY"],
        events={5: "Studio Lighting", 12: "Design Night", 19: "Maker Fair", 26: "Finale DJ"},
        map_shopping=["Steps Plaza", "Gallery Lane"],
        map_landmarks=["Tower"],
        map_parking=["P1", "P2"],
        map_restrooms=["R1"],
        landmark_icons=["Culver Steps", "Film Reel", "Palm Pair", "Gift Stack"],
    ),
    Neighborhood(
        slug="downtown-burbank",
        name="Downtown Burbank",
        street_label="MEDIA DISTRICT",
        skyline_landmark="Studio Skyline",
        shopping_icons=[
            ("ANIMATION SHOP", "toy"),
            ("BOOK & ART", "book"),
            ("COLLECTIBLES", "vintage"),
            ("FASHION", "fashion"),
            ("HOME GOODS", "home"),
            ("GALLERY", "gallery"),
        ],
        eats_icons=["HOT COCOA", "FINE DINING", "TAKEOUT", "HOLIDAY COOKIE", "COCKTAIL", "BAKERY PASTRY"],
        events={6: "Studio Lighting", 13: "Animator Meetup", 20: "Caroling Night", 27: "Closing Show"},
        map_shopping=["Collector Row", "Artist Walk"],
        map_landmarks=["Media Tower"],
        map_parking=["P", "P2"],
        map_restrooms=["R"],
        landmark_icons=["Film Tower", "Clapper", "Studio Palm", "Gift Reel"],
    ),
    Neighborhood(
        slug="glendale",
        name="Glendale",
        street_label="BRAND BOULEVARD",
        skyline_landmark="Americana Tower",
        shopping_icons=[
            ("GALLERIA FINDS", "shopping_bag"),
            ("HOLIDAY FASHION", "fashion"),
            ("HOME GOODS", "home"),
            ("BEAUTY BAR", "beauty"),
            ("TOY BOUTIQUE", "toy"),
            ("ART PRINTS", "gallery"),
        ],
        eats_icons=["HOT COCOA", "FINE DINING", "TAKEOUT", "HOLIDAY COOKIE", "COCKTAIL", "BAKERY PASTRY"],
        events={2: "Tree Lighting", 9: "Skate Night", 16: "Market", 23: "Eve Concert"},
        map_shopping=["Americana", "Galleria"],
        map_landmarks=["Fountain"],
        map_parking=["P1", "P2"],
        map_restrooms=["R1"],
        landmark_icons=["Americana Tower", "Galleria Bag", "Fountain", "Gift Lights"],
    ),
    Neighborhood(
        slug="west-hollywood",
        name="West Hollywood",
        street_label="SUNSET STRIP",
        skyline_landmark="Strip Skyline",
        shopping_icons=[
            ("DESIGNER FASHION", "fashion"),
            ("RECORD SHOP", "record"),
            ("GALLERY", "gallery"),
            ("BEAUTY LAB", "beauty"),
            ("VINTAGE FINDS", "vintage"),
            ("ART BOOKS", "book"),
        ],
        eats_icons=["HOT COCOA", "FINE DINING", "TAKEOUT", "HOLIDAY COOKIE", "COCKTAIL", "BAKERY PASTRY"],
        events={7: "Opening Night", 14: "Music Crawl", 21: "Drag Brunch", 28: "NYE Countdown"},
        map_shopping=["Boutique Row", "Record Alley"],
        map_landmarks=["Sunset Tower"],
        map_parking=["P"],
        map_restrooms=["R"],
        landmark_icons=["Sunset Tower", "Neon Star", "Record", "Gift Marquee"],
    ),
    Neighborhood(
        slug="venice-beach",
        name="Venice Beach",
        street_label="ABBOT KINNEY BOULEVARD",
        skyline_landmark="Windward Columns",
        shopping_icons=[
            ("SURF SHOP", "surf"),
            ("ARTISAN MARKET", "market"),
            ("DESIGN GOODS", "design"),
            ("VINTAGE SHOP", "vintage"),
            ("WELLNESS STUDIO", "wellness"),
            ("BOOK & CAFÉ", "book"),
        ],
        eats_icons=["HOT COCOA", "FINE DINING", "TAKEOUT", "HOLIDAY COOKIE", "COCKTAIL", "BAKERY PASTRY"],
        events={3: "Sunset Lighting", 10: "Maker Market", 17: "Boardwalk Beats", 24: "Eve Drum Circle"},
        map_shopping=["Windward", "Abbot Kinney"],
        map_landmarks=["Columns", "Skate Park"],
        map_parking=["P"],
        map_restrooms=["R"],
        landmark_icons=["Windward Columns", "Surfboard", "Gift Wave", "Venice Sign"],
    ),
    Neighborhood(
        slug="santa-monica",
        name="Santa Monica",
        street_label="THIRD STREET PROMENADE",
        skyline_landmark="Pacific Wheel",
        shopping_icons=[
            ("COASTAL FASHION", "fashion"),
            ("TECH HUB", "tech"),
            ("TOY SHOP", "toy"),
            ("BOOKSTORE", "book"),
            ("BEAUTY BAR", "beauty"),
            ("HOME GOODS", "home"),
        ],
        eats_icons=["HOT COCOA", "FINE DINING", "TAKEOUT", "HOLIDAY COOKIE", "COCKTAIL", "BAKERY PASTRY"],
        events={2: "Pier Lighting", 9: "Skate Night", 16: "Maker Market", 23: "Sunset Concert"},
        map_shopping=["Promenade", "Pier"],
        map_landmarks=["Wheel", "Arch"],
        map_parking=["P1", "P2"],
        map_restrooms=["R1"],
        landmark_icons=["Ferris Wheel", "Pier Arch", "Gift Wave", "Palm Duo"],
    ),
    Neighborhood(
        slug="downtown-los-angeles",
        name="Downtown Los Angeles",
        street_label="SKYLINE CELEBRATION",
        skyline_landmark="Skyline Celebration",
        shopping_icons=[
            ("DESIGN DISTRICT", "design"),
            ("BOOK & ART", "book"),
            ("FASHION", "fashion"),
            ("TECH MARKET", "tech"),
            ("JEWELRY", "jewelry"),
            ("HOME GOODS", "home"),
        ],
        eats_icons=["HOT COCOA", "FINE DINING", "TAKEOUT", "HOLIDAY COOKIE", "COCKTAIL", "BAKERY PASTRY"],
        events={5: "Skyline Lighting", 12: "Design Fair", 19: "Grand Parade", 31: "Midnight Lights"},
        map_shopping=["Historic Core", "Arts District"],
        map_landmarks=["Skyline", "Union Station"],
        map_parking=["P1", "P2", "P3"],
        map_restrooms=["R1", "R2"],
        landmark_icons=["US Bank Tower", "Grand Park", "Streetcar", "Gift Skyline"],
    ),
]

ICON_COLOR_ROTATION = ["lime", "hot_pink", "sky_blue", "sunshine", "winter_blue", "purple"]


def icon_background(parent: ET.Element, x: float, y: float, size: float, index: int) -> None:
    color = PALETTE[ICON_COLOR_ROTATION[index % len(ICON_COLOR_ROTATION)]]
    add_rect(parent, x, y, size, size, fill=color)


def icon_shape(parent: ET.Element, icon_type: str, center: Tuple[float, float], size: float) -> None:
    cx, cy = center
    half = size / 2
    if icon_type == "fashion":
        add_polygon(parent, [(cx, cy - half), (cx - half * 0.6, cy + half), (cx, cy + half * 0.5), (cx + half * 0.6, cy + half)], fill=PALETTE["hot_pink"], stroke_width=STROKE_WIDTH / 1.5)
        add_rect(parent, cx - half * 0.15, cy - half * 0.5, half * 0.3, half * 0.6, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 2)
    elif icon_type == "jewelry":
        add_polygon(parent, [(cx, cy - half), (cx - half * 0.7, cy), (cx, cy + half), (cx + half * 0.7, cy)], fill=PALETTE["sunshine"], stroke_width=STROKE_WIDTH / 1.5)
        add_circle(parent, cx, cy, half * 0.3, fill=PALETTE["purple"], stroke_width=STROKE_WIDTH / 2)
    elif icon_type == "design":
        add_rect(parent, cx - half * 0.8, cy - half * 0.8, half * 1.6, half * 1.6, fill=PALETTE["sky_blue"], stroke_width=STROKE_WIDTH / 1.5)
        add_rect(parent, cx - half * 0.4, cy - half * 0.4, half * 0.8, half * 0.8, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 2)
    elif icon_type == "beauty":
        add_rect(parent, cx - half * 0.3, cy - half * 0.8, half * 0.6, half * 1.4, fill=PALETTE["purple"], stroke_width=STROKE_WIDTH / 1.5)
        add_circle(parent, cx, cy + half * 0.8, half * 0.4, fill=PALETTE["hot_pink"], stroke_width=STROKE_WIDTH / 2)
    elif icon_type == "gallery":
        add_rect(parent, cx - half * 0.7, cy - half * 0.7, half * 1.4, half * 1.4, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 1.5)
        add_polygon(parent, [(cx - half * 0.6, cy + half * 0.5), (cx, cy - half * 0.4), (cx + half * 0.6, cy + half * 0.5)], fill=PALETTE["winter_blue"], stroke_width=STROKE_WIDTH / 2)
    elif icon_type == "toy":
        add_rect(parent, cx - half * 0.8, cy + half * 0.1, half * 1.6, half * 0.8, fill=PALETTE["sunshine"], stroke_width=STROKE_WIDTH / 1.5)
        add_circle(parent, cx - half * 0.4, cy + half * 0.8, half * 0.3, fill=PALETTE["sky_blue"], stroke_width=STROKE_WIDTH / 2)
        add_circle(parent, cx + half * 0.4, cy + half * 0.8, half * 0.3, fill=PALETTE["sky_blue"], stroke_width=STROKE_WIDTH / 2)
    elif icon_type == "book":
        add_rect(parent, cx - half * 0.8, cy - half * 0.7, half * 0.6, half * 1.4, fill=PALETTE["frost_mint"], stroke_width=STROKE_WIDTH / 1.5)
        add_rect(parent, cx - half * 0.2, cy - half * 0.7, half * 0.6, half * 1.4, fill=PALETTE["sky_blue"], stroke_width=STROKE_WIDTH / 1.5)
    elif icon_type == "market":
        add_rect(parent, cx - half * 0.9, cy - half * 0.6, half * 1.8, half * 0.7, fill=PALETTE["sunshine"], stroke_width=STROKE_WIDTH / 1.5)
        add_rect(parent, cx - half * 0.5, cy, half, half * 0.9, fill=PALETTE["lime"], stroke_width=STROKE_WIDTH / 1.5)
    elif icon_type == "vintage":
        add_circle(parent, cx, cy, half * 0.9, fill=PALETTE["purple"], stroke_width=STROKE_WIDTH / 1.5)
        add_circle(parent, cx, cy, half * 0.4, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 2)
    elif icon_type == "surf":
        add_polygon(parent, [(cx - half * 0.3, cy - half), (cx + half * 0.4, cy), (cx - half * 0.3, cy + half)], fill=PALETTE["winter_blue"], stroke_width=STROKE_WIDTH / 1.5)
    elif icon_type == "nautical":
        add_circle(parent, cx, cy, half * 0.8, fill=PALETTE["sky_blue"], stroke_width=STROKE_WIDTH / 1.5)
        add_line(parent, cx, cy - half * 0.8, cx, cy + half * 0.8, stroke_width=STROKE_WIDTH / 1.5)
        add_line(parent, cx - half * 0.6, cy, cx + half * 0.6, cy, stroke_width=STROKE_WIDTH / 1.5)
    elif icon_type == "home":
        add_polygon(parent, [(cx - half * 0.8, cy + half * 0.4), (cx, cy - half), (cx + half * 0.8, cy + half * 0.4)], fill=PALETTE["frost_mint"], stroke_width=STROKE_WIDTH / 1.5)
        add_rect(parent, cx - half * 0.3, cy + half * 0.4, half * 0.6, half * 0.6, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 2)
    elif icon_type == "wellness":
        add_circle(parent, cx, cy, half * 0.7, fill=PALETTE["frost_mint"], stroke_width=STROKE_WIDTH / 1.5)
        add_polygon(parent, [(cx, cy - half * 0.6), (cx - half * 0.4, cy + half * 0.6), (cx + half * 0.4, cy + half * 0.6)], fill=PALETTE["lime"], stroke_width=STROKE_WIDTH / 1.5)
    elif icon_type == "floral":
        for idx in range(5):
            angle = math.radians(idx * 72)
            add_circle(parent, cx + math.cos(angle) * half * 0.5, cy + math.sin(angle) * half * 0.5, half * 0.35, fill=PALETTE["hot_pink"], stroke_width=STROKE_WIDTH / 2)
        add_circle(parent, cx, cy, half * 0.25, fill=PALETTE["sunshine"], stroke_width=STROKE_WIDTH / 2)
    elif icon_type == "tech":
        add_rect(parent, cx - half * 0.8, cy - half * 0.6, half * 1.6, half * 1.2, fill=PALETTE["winter_blue"], stroke_width=STROKE_WIDTH / 1.5, rx=12, ry=12)
        add_rect(parent, cx - half * 0.5, cy + half * 0.3, half, half * 0.2, fill=PALETTE["black"], stroke_width=STROKE_WIDTH / 2)
    elif icon_type == "shopping_bag":
        add_rect(parent, cx - half * 0.7, cy - half * 0.2, half * 1.4, half * 0.9, fill=PALETTE["hot_pink"], stroke_width=STROKE_WIDTH / 1.5)
        add_line(parent, cx - half * 0.4, cy - half * 0.2, cx - half * 0.2, cy - half * 0.6, stroke_width=STROKE_WIDTH / 1.5)
        add_line(parent, cx + half * 0.4, cy - half * 0.2, cx + half * 0.2, cy - half * 0.6, stroke_width=STROKE_WIDTH / 1.5)
    elif icon_type == "record":
        add_circle(parent, cx, cy, half * 0.8, fill=PALETTE["purple"], stroke_width=STROKE_WIDTH / 1.5)
        add_circle(parent, cx, cy, half * 0.2, fill=PALETTE["hot_pink"], stroke_width=STROKE_WIDTH / 2)
    else:
        add_rect(parent, cx - half * 0.6, cy - half * 0.6, half * 1.2, half * 1.2, fill=PALETTE["sky_blue"], stroke_width=STROKE_WIDTH / 1.5)


def icon_labels(parent: ET.Element, text: str, x: float, y: float) -> None:
    add_text(parent, text, x, y, size=28, fill=PALETTE["black"], anchor="middle")


def make_icon_panel(neighborhood: Neighborhood, title: str, entries: Sequence[Tuple[str, str]]) -> ET.Element:
    svg = svg_root(1200, 900)
    add_rect(svg, 40, 40, 1120, 820, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_rect(svg, 40, 40, 1120, 120, fill=PALETTE["black"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, f"{neighborhood.name.upper()} {title}", 600, 100, size=52, fill=PALETTE["off_white"])
    origin_x, origin_y = 120, 220
    cell = 320
    for idx, (label, icon_key) in enumerate(entries):
        col = idx % 3
        row = idx // 3
        x = origin_x + col * cell
        y = origin_y + row * cell
        icon_background(svg, x, y, 240, idx)
        icon_shape(svg, icon_key, (x + 120, y + 120), 180)
        icon_labels(svg, label, x + 120, y + 240 + 40)
    return svg


def skyline_block(parent: ET.Element, x: float, base: float, width: float, height: float, color: str) -> None:
    add_rect(parent, x, base - height, width, height, fill=PALETTE[color])
    add_rect(parent, x + width * 0.2, base - height + 40, width * 0.2, 32, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 2)
    add_rect(parent, x + width * 0.6, base - height + 80, width * 0.2, 32, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 2)


def generate_skyline(neighborhood: Neighborhood) -> ET.Element:
    svg = svg_root(900, 1400)
    add_rect(svg, 30, 30, 840, 1340, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_rect(svg, 60, 60, 780, 80, fill=PALETTE["black"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, f"CURATIONSLA × {neighborhood.name.upper()} HOLIDAY 2025", 450, 100, size=44, fill=PALETTE["off_white"])
    ornament_strand(svg, 140, 200, 620, 10)
    group = add_group(svg, translate=(120, 320))
    skyline_block(group, 0, 640, 140, 320, "sky_blue")
    skyline_block(group, 180, 640, 180, 360, "winter_blue")
    skyline_block(group, 400, 640, 120, 280, "purple")
    add_rect(group, 240, 420, 160, 220, fill=PALETTE["sunshine"])
    add_text(group, neighborhood.skyline_landmark.upper(), 320, 520, size=28, fill=PALETTE["black"])
    palm_tree(svg, 200, 1100, 240, ["hot_pink", "lime"])
    palm_tree(svg, 700, 1100, 240, ["sky_blue", "sunshine"])
    nutcracker(svg, 220, 1020, 0.6, ["hot_pink", "sunshine", "lime"])
    nutcracker(svg, 680, 1020, 0.6, ["sky_blue", "purple", "winter_blue"])
    add_rect(svg, 420, 1080, 80, 80, fill=PALETTE["hot_pink"])
    add_rect(svg, 500, 1100, 100, 100, fill=PALETTE["lime"])
    add_line(svg, 420, 1120, 500, 1120, stroke_width=STROKE_WIDTH / 2)
    add_line(svg, 550, 1100, 550, 1200, stroke_width=STROKE_WIDTH / 2)
    crowd_strip(svg, 840, 1200, 80)
    add_rect(svg, 60, 1260, 780, 80, fill=PALETTE["black"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, neighborhood.street_label, 450, 1300, size=48, fill=PALETTE["off_white"])
    return svg


def month_grid(parent: ET.Element, x: float, y: float, cols: int, rows: int, cell: float) -> None:
    add_rect(parent, x, y, cols * cell, rows * cell, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 2)
    for c in range(cols + 1):
        add_line(parent, x + c * cell, y, x + c * cell, y + rows * cell, stroke_width=STROKE_WIDTH / 2)
    for r in range(rows + 1):
        add_line(parent, x, y + r * cell, x + cols * cell, y + r * cell, stroke_width=STROKE_WIDTH / 2)


def generate_calendar(neighborhood: Neighborhood) -> ET.Element:
    svg = svg_root(1100, 1400)
    add_rect(svg, 40, 40, 1020, 1320, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_rect(svg, 40, 40, 1020, 120, fill=PALETTE["black"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, f"{neighborhood.name.upper()} HOLIDAY EVENTS", 550, 100, size=52, fill=PALETTE["off_white"])
    skyline = add_group(svg, translate=(80, 220))
    skyline_block(skyline, 0, 220, 160, 180, "winter_blue")
    skyline_block(skyline, 200, 220, 140, 160, "sky_blue")
    skyline_block(skyline, 360, 220, 100, 140, "purple")
    add_rect(skyline, 160, 160, 140, 80, fill=PALETTE["sunshine"])
    add_text(skyline, neighborhood.skyline_landmark.upper(), 230, 200, size=20, fill=PALETTE["black"])
    month_grid(svg, 120, 360, 7, 6, 120)
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    for idx, day in enumerate(days):
        add_text(svg, day, 120 + idx * 120 + 60, 340, size=28, fill=PALETTE["black"], weight="600")
    start_offset = 1  # December 2025 starts on Monday, offset 1 when Sunday-first grid
    day = 1
    color_index = 0
    for row in range(6):
        for col in range(7):
            cell_index = row * 7 + col
            if cell_index < start_offset:
                continue
            if day > 31:
                break
            cx = 120 + col * 120 + 60
            cy = 360 + row * 120 + 60
            if day in neighborhood.events:
                color = PALETTE[ICON_COLOR_ROTATION[color_index % len(ICON_COLOR_ROTATION)]]
                add_circle(svg, cx, cy, 40, fill=color, stroke_width=STROKE_WIDTH / 2)
                add_text(svg, str(day), cx, cy, size=30, fill=PALETTE["black"])
                add_text(svg, neighborhood.events[day], cx, cy + 48, size=20, fill=PALETTE["black"], anchor="middle", weight="600")
                color_index += 1
            else:
                add_text(svg, str(day), cx, cy, size=30, fill=PALETTE["black"])
            day += 1
        if day > 31:
            break
    return svg


def generate_map(neighborhood: Neighborhood) -> ET.Element:
    svg = svg_root(1200, 900)
    add_rect(svg, 60, 60, 1080, 780, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, f"WALKABLE MINI MAP – {neighborhood.name.upper()}", 600, 140, size=48, fill=PALETTE["black"])
    for row in range(3):
        for col in range(4):
            add_rect(svg, 160 + col * 200, 220 + row * 200, 160, 160, fill=PALETTE["frost_mint"], stroke_width=STROKE_WIDTH / 2)
    add_rect(svg, 160, 400, 800, 50, fill=PALETTE["hot_pink"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, neighborhood.street_label, 560, 425, size=36, fill=PALETTE["off_white"])
    for idx, name in enumerate(neighborhood.map_shopping):
        add_rect(svg, 200 + idx * 220, 260, 140, 120, fill=PALETTE["sunshine"], stroke_width=STROKE_WIDTH / 2)
        add_text(svg, name.upper(), 270 + idx * 220, 320, size=20, fill=PALETTE["black"])
    for idx, name in enumerate(neighborhood.map_landmarks):
        add_rect(svg, 220 + idx * 240, 520, 120, 120, fill=PALETTE["sky_blue"], stroke_width=STROKE_WIDTH / 2)
        add_text(svg, name.upper(), 280 + idx * 240, 580, size=20, fill=PALETTE["black"])
    for idx, name in enumerate(neighborhood.map_parking):
        add_rect(svg, 1040, 240 + idx * 120, 80, 80, fill=PALETTE["lime"], stroke_width=STROKE_WIDTH / 2)
        add_text(svg, name, 1080, 280 + idx * 120, size=28, fill=PALETTE["black"])
    for idx, name in enumerate(neighborhood.map_restrooms):
        add_rect(svg, 1040, 480 + idx * 120, 80, 80, fill=PALETTE["purple"], stroke_width=STROKE_WIDTH / 2)
        add_text(svg, name, 1080, 520 + idx * 120, size=28, fill=PALETTE["off_white"])
    add_text(svg, "STAY WALKABLE", 600, 780, size=42, fill=PALETTE["black"])
    return svg


def generate_transport(neighborhood: Neighborhood) -> ET.Element:
    svg = svg_root(1200, 600)
    add_rect(svg, 40, 40, 1120, 520, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_rect(svg, 40, 40, 1120, 100, fill=PALETTE["black"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, f"{neighborhood.name.upper()} TRANSPORTATION", 600, 90, size=48, fill=PALETTE["off_white"])
    labels = ["P", "CAR", "TRANSIT", "WALK", "BIKE"]
    for idx, label in enumerate(labels):
        x = 120 + idx * 210
        icon_background(svg, x, 200, 180, idx)
        cx, cy = x + 90, 290
        if label == "P":
            add_rect(svg, cx - 60, cy - 60, 120, 120, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 1.5)
            add_text(svg, "P", cx, cy, size=72, fill=PALETTE["black"])
        elif label == "CAR":
            add_rect(svg, cx - 70, cy - 30, 140, 80, fill=PALETTE["sunshine"], stroke_width=STROKE_WIDTH / 1.5)
            add_circle(svg, cx - 40, cy + 50, 22, fill=PALETTE["black"], stroke_width=STROKE_WIDTH / 2)
            add_circle(svg, cx + 40, cy + 50, 22, fill=PALETTE["black"], stroke_width=STROKE_WIDTH / 2)
        elif label == "TRANSIT":
            add_rect(svg, cx - 60, cy - 60, 120, 140, fill=PALETTE["winter_blue"], stroke_width=STROKE_WIDTH / 1.5)
            add_rect(svg, cx - 40, cy + 40, 80, 40, fill=PALETTE["black"], stroke_width=STROKE_WIDTH / 2)
            add_circle(svg, cx - 30, cy + 80, 16, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 2)
            add_circle(svg, cx + 30, cy + 80, 16, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 2)
        elif label == "WALK":
            add_line(svg, cx, cy - 60, cx, cy - 10, stroke_width=STROKE_WIDTH / 1.2)
            add_circle(svg, cx, cy - 80, 20, fill=PALETTE["hot_pink"], stroke_width=STROKE_WIDTH / 2)
            add_line(svg, cx, cy - 10, cx - 30, cy + 60, stroke_width=STROKE_WIDTH / 1.2)
            add_line(svg, cx, cy - 10, cx + 30, cy + 60, stroke_width=STROKE_WIDTH / 1.2)
        elif label == "BIKE":
            add_circle(svg, cx - 40, cy + 40, 28, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 1.5)
            add_circle(svg, cx + 40, cy + 40, 28, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 1.5)
            add_line(svg, cx - 40, cy + 40, cx, cy, stroke_width=STROKE_WIDTH / 1.2)
            add_line(svg, cx, cy, cx + 40, cy + 40, stroke_width=STROKE_WIDTH / 1.2)
            add_line(svg, cx, cy, cx, cy - 60, stroke_width=STROKE_WIDTH / 1.2)
        add_text(svg, label, cx, 420, size=30, fill=PALETTE["black"])
    return svg


def generate_weather(neighborhood: Neighborhood) -> ET.Element:
    svg = svg_root(1200, 600)
    add_rect(svg, 40, 40, 1120, 520, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_rect(svg, 40, 40, 1120, 100, fill=PALETTE["black"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, f"WEATHER – {neighborhood.name.upper()}", 600, 90, size=48, fill=PALETTE["off_white"])
    labels = ["SUNNY", "PARTLY CLOUDY", "CLOUDY", "LIGHT RAIN", "FESTIVE FLAKE"]
    for idx, label in enumerate(labels):
        x = 120 + idx * 210
        icon_background(svg, x, 200, 180, idx)
        cx, cy = x + 90, 280
        if label == "SUNNY":
            add_circle(svg, cx, cy, 50, fill=PALETTE["sunshine"], stroke_width=STROKE_WIDTH / 1.5)
            for angle in range(0, 360, 45):
                rad = math.radians(angle)
                add_line(svg, cx + math.cos(rad) * 70, cy + math.sin(rad) * 70, cx + math.cos(rad) * 100, cy + math.sin(rad) * 100, stroke_width=STROKE_WIDTH / 2)
        elif label == "PARTLY CLOUDY":
            add_circle(svg, cx - 20, cy - 10, 40, fill=PALETTE["sunshine"], stroke_width=STROKE_WIDTH / 1.5)
            add_circle(svg, cx + 20, cy + 10, 40, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 1.5)
            add_circle(svg, cx - 40, cy + 20, 40, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 1.5)
        elif label == "CLOUDY":
            add_circle(svg, cx - 30, cy, 40, fill=PALETTE["frost_mint"], stroke_width=STROKE_WIDTH / 1.5)
            add_circle(svg, cx + 30, cy, 40, fill=PALETTE["frost_mint"], stroke_width=STROKE_WIDTH / 1.5)
            add_circle(svg, cx, cy - 20, 40, fill=PALETTE["frost_mint"], stroke_width=STROKE_WIDTH / 1.5)
        elif label == "LIGHT RAIN":
            add_circle(svg, cx - 20, cy - 20, 40, fill=PALETTE["winter_blue"], stroke_width=STROKE_WIDTH / 1.5)
            for drop in range(3):
                add_line(svg, cx - 40 + drop * 40, cy + 20, cx - 40 + drop * 40, cy + 80, stroke=PALETTE["hot_pink"], stroke_width=STROKE_WIDTH / 2)
        elif label == "FESTIVE FLAKE":
            for angle in range(0, 360, 60):
                rad = math.radians(angle)
                add_line(svg, cx, cy, cx + math.cos(rad) * 60, cy + math.sin(rad) * 60, stroke=PALETTE["sky_blue"], stroke_width=STROKE_WIDTH / 1.2)
                add_line(svg, cx, cy, cx + math.cos(rad + math.pi / 6) * 40, cy + math.sin(rad + math.pi / 6) * 40, stroke=PALETTE["sky_blue"], stroke_width=STROKE_WIDTH / 1.2)
        add_text(svg, label, cx, 420, size=24, fill=PALETTE["black"])
    return svg


def generate_gift_guide(neighborhood: Neighborhood) -> ET.Element:
    categories = [
        ("FASHION", "fashion"),
        ("TECH", "tech"),
        ("BEAUTY", "beauty"),
        ("BOOKS", "book"),
        ("JEWELRY", "jewelry"),
        ("HOME", "home"),
    ]
    svg = make_icon_panel(neighborhood, "HOLIDAY GIFT GUIDE", categories)
    add_text(svg, f"HOLIDAY GIFT GUIDE – {neighborhood.name.upper()}", 600, 840, size=36, fill=PALETTE["black"])
    return svg


def generate_landmark_sheet(neighborhood: Neighborhood) -> ET.Element:
    svg = svg_root(1000, 1000)
    add_rect(svg, 60, 60, 880, 880, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, f"{neighborhood.name.upper()} LANDMARK ICONS", 500, 140, size=48, fill=PALETTE["black"])
    for row in range(2):
        for col in range(2):
            add_rect(svg, 160 + col * 300, 220 + row * 300, 240, 240, fill=PALETTE["frost_mint"], stroke_width=STROKE_WIDTH / 2)
    for idx, label in enumerate(neighborhood.landmark_icons):
        col = idx % 2
        row = idx // 2
        cx = 160 + col * 300 + 120
        cy = 220 + row * 300 + 120
        icon_shape(svg, "design", (cx, cy), 160)
        add_text(svg, label.upper(), cx, cy + 120, size=24, fill=PALETTE["black"])
    return svg


def generate_pattern_pack(neighborhood: Neighborhood) -> ET.Element:
    svg = svg_root(1600, 900)
    add_rect(svg, 40, 40, 1520, 820, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, f"{neighborhood.name.upper()} HOLIDAY PATTERN PACK", 800, 110, size=48, fill=PALETTE["black"])
    for idx in range(4):
        add_rect(svg, 120 + idx * 360, 180, 320, 640, fill=PALETTE["off_white"], stroke_width=STROKE_WIDTH / 2)
    # pattern 1 – palms
    palm_group = add_group(svg, translate=(120, 180))
    add_rect(palm_group, 0, 0, 320, 640, fill=PALETTE["sunshine"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH / 2)
    for row in range(4):
        palm_tree(palm_group, 80 + (row % 2) * 120, 120 + row * 150, 120, ["lime", "hot_pink"])
    # pattern 2 – nutcrackers
    nut_group = add_group(svg, translate=(480, 180))
    add_rect(nut_group, 0, 0, 320, 640, fill=PALETTE["frost_mint"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH / 2)
    for row in range(3):
        nutcracker(nut_group, 80, 150 + row * 200, 0.4, ["hot_pink", "sunshine", "lime"])
        nutcracker(nut_group, 240, 150 + row * 200, 0.4, ["sky_blue", "purple", "winter_blue"])
    # pattern 3 – gifts
    gift_group = add_group(svg, translate=(840, 180))
    add_rect(gift_group, 0, 0, 320, 640, fill=PALETTE["lime"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH / 2)
    for row in range(4):
        for col in range(2):
            add_rect(gift_group, 40 + col * 140, 60 + row * 140, 100, 100, fill=PALETTE[ICON_COLOR_ROTATION[(row + col) % len(ICON_COLOR_ROTATION)]], stroke_width=STROKE_WIDTH / 2)
            add_line(gift_group, 40 + col * 140 + 50, 60 + row * 140, 40 + col * 140 + 50, 160 + row * 140, stroke_width=STROKE_WIDTH / 2)
            add_line(gift_group, 40 + col * 140, 60 + row * 140 + 50, 140 + col * 140, 60 + row * 140 + 50, stroke_width=STROKE_WIDTH / 2)
    # pattern 4 – abstract blocks
    abstract_group = add_group(svg, translate=(1200, 180))
    add_rect(abstract_group, 0, 0, 320, 640, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH / 2)
    for row in range(4):
        for col in range(2):
            add_rect(abstract_group, 20 + col * 150, 20 + row * 150, 120, 120, fill=PALETTE[ICON_COLOR_ROTATION[(row + col) % len(ICON_COLOR_ROTATION)]], stroke_width=STROKE_WIDTH / 2)
            add_circle(abstract_group, 80 + col * 150, 80 + row * 150, 30, fill=PALETTE["black"], stroke_width=STROKE_WIDTH / 2)
    add_text(abstract_group, "CURATIONSLA", 160, 600, size=36, fill=PALETTE["black"])
    return svg


def generate_social(neighborhood: Neighborhood) -> ET.Element:
    svg = svg_root(2400, 1800)
    add_rect(svg, 40, 40, 2320, 1720, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, f"{neighborhood.name.upper()} SOCIAL CAROUSEL", 1200, 140, size=60, fill=PALETTE["black"])
    for idx in range(6):
        add_rect(svg, 120 + idx * 360, 220, 320, 1400, fill=PALETTE[ICON_COLOR_ROTATION[idx % len(ICON_COLOR_ROTATION)]], stroke_width=STROKE_WIDTH / 2)
        add_text(svg, f"CARD {idx + 1}", 280 + idx * 360, 340, size=36, fill=PALETTE["black"])
    return svg


def generate_banners(neighborhood: Neighborhood) -> ET.Element:
    svg = svg_root(2000, 1000)
    add_rect(svg, 40, 40, 1920, 920, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, f"{neighborhood.name.upper()} WEBSITE BANNERS", 1000, 140, size=56, fill=PALETTE["black"])
    add_rect(svg, 120, 220, 1760, 220, fill=PALETTE["black"], stroke_width=STROKE_WIDTH / 2)
    add_text(svg, "HERO BANNER", 1000, 330, size=48, fill=PALETTE["off_white"])
    add_rect(svg, 120, 480, 1760, 200, fill=PALETTE["sunshine"], stroke_width=STROKE_WIDTH / 2)
    ornament_strand(svg, 160, 560, 1680, 10)
    add_rect(svg, 120, 720, 1760, 160, fill=PALETTE["hot_pink"], stroke_width=STROKE_WIDTH / 2)
    add_text(svg, "FOOTER LIGHTS", 1000, 800, size=44, fill=PALETTE["black"])
    return svg


def generate_stickers(neighborhood: Neighborhood) -> ET.Element:
    svg = svg_root(1400, 1400)
    add_rect(svg, 40, 40, 1320, 1320, fill=PALETTE["off_white"], stroke=PALETTE["black"], stroke_width=STROKE_WIDTH)
    add_text(svg, f"{neighborhood.name.upper()} STICKER SHEET", 700, 140, size=56, fill=PALETTE["black"])
    for row in range(3):
        for col in range(4):
            idx = row * 4 + col
            add_circle(svg, 200 + col * 300, 260 + row * 320, 120, fill=PALETTE[ICON_COLOR_ROTATION[idx % len(ICON_COLOR_ROTATION)]], stroke_width=STROKE_WIDTH / 2)
            add_text(svg, f"STICKER {idx + 1}", 200 + col * 300, 420 + row * 320, size=28, fill=PALETTE["black"])
    return svg


def generate_assets() -> None:
    output_root = Path("designs-openai/assets")
    for neighborhood in NEIGHBORHOODS:
        base = output_root / neighborhood.slug
        write_svg(base / f"curationsla_{neighborhood.slug}_skyline_celebration_poster.svg", generate_skyline(neighborhood))
        write_svg(base / f"curationsla_{neighborhood.slug}_shopping_icons.svg", make_icon_panel(neighborhood, "SHOPPING GUIDE", neighborhood.shopping_icons))
        eats = [(label, "design") for label in neighborhood.eats_icons]
        write_svg(base / f"curationsla_{neighborhood.slug}_holiday_eats.svg", make_icon_panel(neighborhood, "HOLIDAY EATS", eats))
        write_svg(base / f"curationsla_{neighborhood.slug}_events_calendar.svg", generate_calendar(neighborhood))
        write_svg(base / f"curationsla_{neighborhood.slug}_walkable_map.svg", generate_map(neighborhood))
        write_svg(base / f"curationsla_{neighborhood.slug}_transportation.svg", generate_transport(neighborhood))
        write_svg(base / f"curationsla_{neighborhood.slug}_weather.svg", generate_weather(neighborhood))
        write_svg(base / f"curationsla_{neighborhood.slug}_gift_guide.svg", generate_gift_guide(neighborhood))
        write_svg(base / f"curationsla_{neighborhood.slug}_landmark_icons.svg", generate_landmark_sheet(neighborhood))
        write_svg(base / f"curationsla_{neighborhood.slug}_pattern_pack.svg", generate_pattern_pack(neighborhood))
        write_svg(base / f"curationsla_{neighborhood.slug}_social_suite.svg", generate_social(neighborhood))
        write_svg(base / f"curationsla_{neighborhood.slug}_website_banners.svg", generate_banners(neighborhood))
        write_svg(base / f"curationsla_{neighborhood.slug}_sticker_sheet.svg", generate_stickers(neighborhood))


if __name__ == "__main__":
    generate_assets()
