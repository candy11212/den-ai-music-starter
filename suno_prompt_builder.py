#!/usr/bin/env python3
"""Suno style prompt builder met AI-achtige band analyse.

Gebruik:
  python suno_prompt_builder.py --band "Daft Punk"

Als geen argumenten worden gegeven, start een interactieve modus.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from difflib import get_close_matches


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


BAND_PROFILES: dict[str, dict[str, str]] = {
    "linkin park": {
        "genre": "alternative rock / nu metal",
        "mood": "dark but hopeful",
        "energy": "high",
        "pace": "driving",
        "key": "F# minor",
        "octave": "low-mid (2-4)",
        "vocals": "powerful male lead with emotional grit and layered harmonies",
        "language": "English",
        "theme": "inner struggle, resilience, and release",
        "production": "punchy drums, distorted guitars, cinematic synth layers",
    },
    "coldplay": {
        "genre": "anthemic pop-rock",
        "mood": "uplifting and emotional",
        "energy": "medium-high",
        "pace": "steady and driving",
        "key": "E major",
        "octave": "mid-high (3-5)",
        "vocals": "warm expressive male lead with atmospheric backing vocals",
        "language": "English",
        "theme": "hope, connection, and wonder",
        "production": "big drums, shimmering guitars, wide ambient synth pads",
    },
    "rammstein": {
        "genre": "industrial metal",
        "mood": "dark and aggressive",
        "energy": "high",
        "pace": "march-like and heavy",
        "key": "E minor",
        "octave": "low-mid (2-4)",
        "vocals": "deep commanding male vocal",
        "language": "German",
        "theme": "power, conflict, and intensity",
        "production": "massive drums, distorted synths, heavy guitar wall",
    },
    "daft punk": {
        "genre": "electro-funk / house",
        "mood": "futuristic and groovy",
        "energy": "medium-high",
        "pace": "danceable",
        "key": "A minor",
        "octave": "mid (3-4)",
        "vocals": "processed robotic lead with catchy toplines",
        "language": "English",
        "theme": "nightlife, motion, and euphoria",
        "production": "tight disco drums, analog synth bass, glossy retro textures",
    },
}


def infer_profile_from_band(band: str) -> dict[str, str]:
    normalized = band.strip().lower()
    if normalized in BAND_PROFILES:
        return BAND_PROFILES[normalized]

    close = get_close_matches(normalized, BAND_PROFILES.keys(), n=1, cutoff=0.65)
    if close:
        return BAND_PROFILES[close[0]]

    return {
        "genre": "anthemic pop-rock",
        "mood": "uplifting and emotional",
        "energy": "medium-high",
        "pace": "steady and driving",
        "key": "E minor",
        "octave": "mid-to-high (3-5)",
        "vocals": "powerful lead with layered harmonies",
        "language": "English",
        "theme": "overcoming setbacks and rising stronger",
        "production": "big drums, wide synth pads, shimmering guitars",
    }


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
    band = ask("Band/groep als referentie", "Coldplay")
    inferred = infer_profile_from_band(band)

    return PromptInput(
        band=band,
        genre=ask("Genre", inferred["genre"]),
        mood=ask("Sfeer", inferred["mood"]),
        energy=ask("Energy", inferred["energy"]),
        pace=ask("Pace/snelheid", inferred["pace"]),
        key=ask("Key/toonsoort", inferred["key"]),
        octave=ask("Octave focus", inferred["octave"]),
        vocals=ask("Type vocals", inferred["vocals"]),
        language=ask("Taal", inferred["language"]),
        theme=ask("Thema/boodschap", inferred["theme"]),
        production=ask("Productie stijl", inferred["production"]),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build een professionele AI style prompt voor Suno.ai")
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
        inferred = infer_profile_from_band(args.band)
        payload = PromptInput(
            band=args.band,
            genre=args.genre or inferred["genre"],
            mood=args.mood or inferred["mood"],
            energy=args.energy or inferred["energy"],
            pace=args.pace or inferred["pace"],
            key=getattr(args, "key") or inferred["key"],
            octave=args.octave or inferred["octave"],
            vocals=args.vocals or inferred["vocals"],
            language=args.language or inferred["language"],
            theme=args.theme or inferred["theme"],
            production=args.production or inferred["production"],
        )

    print("\n✨ Jouw Suno style prompt:\n")
    print(build_style_prompt(payload))


if __name__ == "__main__":
    main()
