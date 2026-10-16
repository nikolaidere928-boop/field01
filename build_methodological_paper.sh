#!/bin/sh
set -eu

cd "$(dirname "$0")"

export SOURCE_DATE_EPOCH=1792108800
export TZ=UTC

paper=reading_past_label_vs_updating_surface_record_en
(
    cd articles
    latexmk -C "$paper.tex"
    latexmk -pdf -interaction=nonstopmode -halt-on-error "$paper.tex"
)

sha256sum \
    ./ABSTRACTS_EN.md \
    ./EDITION_2026_10_16.md \
    ./README.md \
    "./articles/$paper.tex" \
    "./articles/${paper}_refs.tex" \
    "./articles/$paper.pdf" \
    > ./SHA256SUMS_2026_10_16.txt

sha256sum -c ./SHA256SUMS_2026_10_16.txt