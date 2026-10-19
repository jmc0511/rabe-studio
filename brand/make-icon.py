# 디스코드 서버 아이콘 (512x512). 사이트 히어로의 16x16 까마귀를 그대로 키운다. 디스코드가 원으로 자르니 까마귀는 가운데 원 안에.
from PIL import Image, ImageDraw
RAVEN = [
    "................",
    "......rrrr......",
    ".....rrrrrr.....",
    "...bbrerrrrr....",
    "..bbbrrrrrrr....",
    ".....rrrrrrrr...",
    ".....rrrfrrrrr..",
    "....rrrrffrrrrr.",
    "....rrrrrffrrrrr",
    ".....rrrrrfffrrr",
    "......rrrrrrrrrr",
    ".......rrrrrrr.r",
    "........l..l....",
    "........l..l....",
    ".......ll.ll....",
    "................",
]
C = {"r": "#14171e", "f": "#34598a", "b": "#d99a2b", "e": "#f6f7fa", "l": "#586072"}
S, CELL = 512, 22
im = Image.new("RGB", (S, S), "#e9ecf1")
d = ImageDraw.Draw(im)
for g in range(0, S, 32):  # 사이트 배경 같은 옅은 청크 격자
    d.line([(g, 0), (g, S)], fill="#dde2ea"); d.line([(0, g), (S, g)], fill="#dde2ea")
xs = [x for row in RAVEN for x, ch in enumerate(row) if ch != "."]
ys = [y for y, row in enumerate(RAVEN) for ch in row if ch != "."]
w, h = (max(xs) - min(xs) + 1) * CELL, (max(ys) - min(ys) + 1) * CELL
ox, oy = (S - w) // 2 - min(xs) * CELL, (S - h) // 2 - min(ys) * CELL + 6
# 그림자 (사이트 버튼처럼 청색으로 살짝 밀린 그림자)
for y, row in enumerate(RAVEN):
    for x, ch in enumerate(row):
        if ch != ".":
            d.rectangle([ox + x*CELL + 10, oy + y*CELL + 10, ox + (x+1)*CELL + 9, oy + (y+1)*CELL + 9], fill="#c7d3e6")
for y, row in enumerate(RAVEN):
    for x, ch in enumerate(row):
        if ch != ".":
            d.rectangle([ox + x*CELL, oy + y*CELL, ox + (x+1)*CELL - 1, oy + (y+1)*CELL - 1], fill=C[ch])
im.save("brand/discord-icon.png")
# 원 마스크 미리보기
pv = Image.new("RGB", (S, S), "#1e1f22"); m = Image.new("L", (S, S), 0); ImageDraw.Draw(m).ellipse([0, 0, S-1, S-1], fill=255)
pv.paste(im, (0, 0), m); pv.save("brand/discord-icon-preview.png")
print("ok")
