#!/bin/sh
# 페이지 문구를 바꾼 뒤 실행: 쓰는 글자만 남긴 글꼴을 site/fonts 에 다시 만든다 (pip install fonttools brotli)
cd "$(dirname "$0")/.." || exit 1
T=$(mktemp -d)
python -X utf8 fonts-src/chars.py "$T"
S="python -m fontTools.subset --flavor=woff2 --layout-features=*"
$S fonts-src/PretendardVariable.woff2 --text-file="$T/page.txt" --output-file=site/fonts/pretendard-page.woff2
$S fonts-src/PretendardVariable.woff2 --text-file="$T/full.txt" --output-file=site/fonts/pretendard-ks.woff2
$S fonts-src/GmarketSansBold.woff --text-file="$T/head.txt" --output-file=site/fonts/gmarket-bold.woff2
$S fonts-src/GmarketSansMedium.woff --text-file="$T/head.txt" --output-file=site/fonts/gmarket-medium.woff2
rm -r "$T"
ls -l site/fonts
