#!/usr/bin/env python3
"""Suno style prompt builder.

Gebruik:
  python suno_prompt_builder.py --band "Daft Punk"

Als geen argumenten worden gegeven, start een interactieve modus.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass
class PromptInput:
    band: str
    genre: str
    mood: str
    energy: str
    pace: str
    key: str
    octave: str
    vocals: str
    language: str
    theme: str
    production: str


HIGH_CLASS_ADJECTIVES = [
    "cinematic",
    "premium studio polish",
    "emotionally rich",
    "radio-ready",
    "world-class arrangement",
    "luxury sonic texture",
]


def build_style_prompt(data: PromptInput) -> str:
    return "\n".join(
        [
            f"AI STYLE BRIEF (Suno) — Inspired by {data.band}.",
            f"Genre & vibe: {data.genre}; mood: {data.mood}; energy: {data.energy}; pace: {data.pace}.",
            f"Musical center: key {data.key}; octave focus: {data.octave}.",
            f"Vocals: {data.vocals}. Language: {data.language}. Theme: {data.theme}.",
            f"Production direction: {data.production}; {', '.join(HIGH_CLASS_ADJECTIVES)}.",
            "Write a complete song with strong hook, memorable chorus, dynamic build-up, and premium finish.",
            "Avoid muddy mix, weak drums, repetitive melody, flat dynamics, amateur mastering, and generic lyrics.",
        ]
    )


def ask(question: str, default: str) -> str:
    raw = input(f"{question} [{default}]: ").strip()
    return raw or default


def interactive() -> PromptInput:
    print("\n🎼 Suno.ai High-Class Style Prompt Builder\n")
    return PromptInput(
        band=ask("Band/groep als referentie", "Coldplay"),
        genre=ask("Genre", "anthemic pop-rock"),
        mood=ask("Sfeer", "uplifting and emotional"),
        energy=ask("Energy", "medium-high"),
        pace=ask("Pace/snelheid", "steady and driving"),
        key=ask("Key/toonsoort", "E minor"),
        octave=ask("Octave focus", "mid-to-high (3-5)"),
        vocals=ask("Type vocals", "powerful lead with layered harmonies"),
        language=ask("Taal", "English"),
        theme=ask("Thema/boodschap", "overcoming setbacks and rising stronger"),
        production=ask("Productie stijl", "big drums, wide synth pads, shimmering guitars"),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build een professionele style prompt voor Suno.ai")
    parser.add_argument("--band")
    parser.add_argument("--genre")
    parser.add_argument("--mood")
    parser.add_argument("--energy")
    parser.add_argument("--pace")
    parser.add_argument("--key")
    parser.add_argument("--octave")
    parser.add_argument("--vocals")
    parser.add_argument("--language")
    parser.add_argument("--theme")
    parser.add_argument("--production")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.band:
        payload = interactive()
    else:
        payload = PromptInput(
            band=args.band,
            genre=args.genre or "anthemic pop-rock",
            mood=args.mood or "uplifting and emotional",
            energy=args.energy or "medium-high",
            pace=args.pace or "steady and driving",
            key=getattr(args, "key") or "E minor",
            octave=args.octave or "mid-to-high (3-5)",
            vocals=args.vocals or "powerful lead with layered harmonies",
            language=args.language or "English",
            theme=args.theme or "overcoming setbacks and rising stronger",
            production=args.production or "big drums, wide synth pads, shimmering guitars",
        )

    print("\n✨ Jouw Suno style prompt:\n")
    print(build_style_prompt(payload))


if __name__ == "__main__":
    main()
