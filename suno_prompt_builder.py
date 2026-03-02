#!/usr/bin/env python3
"""V222 Suno Ultimate Style Prompt Builder + Bob Ludwig V5 report generator."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


SUNO_MODES = [
    "Ballad",
    "Cinematic",
    "Gothic",
    "NDH/Industrial",
    "Pop Emotional",
    "Dark Electronic",
]

MODE_INSTRUMENTS = {
    "Ballad": "piano, soft strings, subtle pads",
    "Cinematic": "orchestral drums, strings, brass swells",
    "Gothic": "dark synths, reverb guitars, deep bass",
    "NDH/Industrial": "heavy guitars, industrial drums, metallic synths",
    "Pop Emotional": "modern drums, bright synths, atmospheric guitars",
    "Dark Electronic": "analog bass, arps, punchy electronic drums",
}

MODE_ENHANCERS = {
    "Ballad": "plate reverb + subtle delay",
    "Cinematic": "hall reverb + stereo delay",
    "Gothic": "long reverb + dark delay",
    "NDH/Industrial": "distortion + short room reverb",
    "Pop Emotional": "wide reverb + slap delay",
    "Dark Electronic": "tempo delay + saturation",
}


@dataclass
class SunoInput:
    emotion: str
    genre: str
    vocal: str
    scene: str
    texture: str
    mode: str


def build_suno_style_prompt(data: SunoInput) -> str:
    instruments = MODE_INSTRUMENTS.get(data.mode, "drums, bass, synths")
    enhancer = MODE_ENHANCERS.get(data.mode, "reverb + delay")

    return "\n".join(
        [
            f"STYLE: {data.genre} ({data.mode}) + {data.emotion} vibe",
            f"VOCALS: {data.vocal}",
            f"INSTRUMENTS: {instruments}",
            f"TEXTURE: {data.texture}",
            f"SCENE: {data.scene}",
            f"ENHANCER: {enhancer}",
        ]
    )


def build_mastering_report(track_desc: str, style_hint: str) -> str:
    return "\n".join(
        [
            "MASTERING REPORT",
            "DETECTION MAP",
            f"- Source description: {track_desc}",
            "- Micro scan: transients, phase, resonance, stereo drift",
            "BAND/STYLE DNA",
            f"- Style hint: {style_hint}",
            "- Emotion curve: intensity, darkness/brightness, vocal focus",
            "MASTERING CHAIN + SETTINGS",
            "1) Reality Scan: LUFS/RMS/crest + phase/spectrum",
            "2) Analog Sculpt: broad EQ + gentle glue compression",
            "3) Digital Precision: dynamic EQ + de-ess + M/S control",
            "4) Limiting: target loudness with true-peak safety",
            "LOUDNESS & DYNAMICS TARGETS",
            "- Streaming: -9 to -12 LUFS, -1.0 dBTP",
            "- Club: -4 to -6 LUFS, punch-focused",
            "- Radio: -9 to -11 LUFS, broadcast-safe",
            "DELIVERY FORMATS",
            "- CD 44.1k/16-bit (dither)",
            "- Streaming 48k/24-bit",
            "- Vinyl 96k/24-bit (high dynamics)",
            "- Audiophile 96k/24-bit",
            "END",
        ]
    )


def ask(question: str, default: str) -> str:
    raw = input(f"{question} [{default}]: ").strip()
    return raw or default


def interactive_suno() -> SunoInput:
    print("\nV222 SUNO — ULTIMATE STYLE PROMPT BUILDER\n")
    mode = ask("Mode (Ballad/Cinematic/Gothic/NDH/Industrial/Pop Emotional/Dark Electronic)", "Cinematic")
    return SunoInput(
        emotion=ask("Emotion", "melancholic but powerful"),
        genre=ask("Genre", "dark cinematic electronic"),
        vocal=ask("Vocal", "female airy lead, emotional intensity"),
        scene=ask("Scene", "night city rooftop in rain"),
        texture=ask("Texture", "cold, wide, analog-filmic"),
        mode=mode,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="V222 Suno Builder + Bob Ludwig V5 report mode")
    sub = parser.add_subparsers(dest="command")

    suno = sub.add_parser("suno", help="Generate short Suno-friendly style prompt")
    suno.add_argument("--emotion")
    suno.add_argument("--genre")
    suno.add_argument("--vocal")
    suno.add_argument("--scene")
    suno.add_argument("--texture")
    suno.add_argument("--mode", choices=SUNO_MODES)

    master = sub.add_parser("mastering", help="Generate Bob Ludwig V5-style mastering report")
    master.add_argument("--track", default="User-described track")
    master.add_argument("--style", default="Hybrid modern")

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.command == "mastering":
        print("\nBOB LUDWIG MASTERING ENGINE — V5 'UNIVERSE MODE'\n")
        print(build_mastering_report(args.track, args.style))
        return

    if args.command == "suno":
        payload = SunoInput(
            emotion=args.emotion or "melancholic but powerful",
            genre=args.genre or "dark cinematic electronic",
            vocal=args.vocal or "female airy lead, emotional intensity",
            scene=args.scene or "night city rooftop in rain",
            texture=args.texture or "cold, wide, analog-filmic",
            mode=args.mode or "Cinematic",
        )
    else:
        payload = interactive_suno()

    print("\nOUTPUT (SHORT, SUNO-FRIENDLY):\n")
    print(build_suno_style_prompt(payload))


if __name__ == "__main__":
    main()
