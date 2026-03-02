#!/usr/bin/env python3
"""V222 builder with Suno-focused persona outputs (AURION + SENTIVOX)."""

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

CONFLICTS = [
    ("happy", "melancholic"),
    ("ambient", "aggressive"),
    ("lo-fi", "hi-fi"),
    ("intimate", "epic"),
    ("calm", "intense"),
]


@dataclass
class SunoInput:
    emotion: str
    genre: str
    vocal: str
    scene: str
    texture: str
    mode: str


@dataclass
class V6Input:
    genre: str
    subgenre: str
    emotion: str
    vocal: str
    scene: str
    mix_style: str
    production: str


@dataclass
class AurionInput:
    description: str
    style_hint: str
    vocal_direction: str
    language: str


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


def normalize_tags(tags: list[str], max_tags: int = 10) -> list[str]:
    seen: set[str] = set()
    cleaned: list[str] = []
    for tag in tags:
        t = tag.strip().lower()
        if not t or t in seen:
            continue
        seen.add(t)
        cleaned.append(t)

    for a, b in CONFLICTS:
        if a in cleaned and b in cleaned:
            cleaned.remove(b)

    return cleaned[:max_tags]


def build_v6_analysis(data: V6Input) -> str:
    tags = normalize_tags(
        [
            data.genre,
            data.subgenre,
            data.emotion,
            data.vocal,
            data.scene,
            data.mix_style,
            data.production,
        ],
        max_tags=10,
    )
    tag_line = ", ".join(tags)
    primary_genre = tags[0] if tags else data.genre
    return "\n".join(
        [
            "1. SUNO PROMPT (Copy-Paste Ready)",
            tag_line,
            "2. GENRE BREAKDOWN",
            f"Primary Genre: {primary_genre}",
            f"Subgenre: {data.subgenre}",
            f"Influences: {data.mix_style}",
            f"Era: {data.production}",
            "3. EMOTIONAL ARCHITECTURE",
            f"Primary Emotion: {data.emotion}",
            "Secondary Emotion: cinematic tension",
            "Intensity: 7/10",
            "Emotional Arc: intro tension -> melodic lift -> emotional release",
            "4. VOCAL DIRECTION",
            f"Gender/Type: {data.vocal}",
            "Timbre: dark/airy (as requested)",
            "Delivery: emotional",
            "Register: mixed",
            "Emotional Quality: intimate but powerful",
            "5. SCENE & ATMOSPHERE",
            f"Primary Scene: {data.scene}",
            "Mood: immersive and visual",
            "Spatial Characteristics: controlled depth, clear center",
            "Visual Elements: cinematic light/shadow contrast",
            "Temporal Setting: night",
            "6. MIX GUIDANCE",
            f"Stereo Width: {data.mix_style}",
            "Reverb/Depth: scene-matched",
            "Texture: balanced clarity + character",
            "Energy Level: moderate to intense",
            "Density: layered but readable",
            "7. PRODUCTION NOTES",
            f"Era/Style: {data.production}",
            "Key Elements: strong hook + clear vocal identity",
            "Technical Focus: low-end control, vocal clarity, top-end polish",
            "Avoid: conflicting tags, overloading beyond 12 tags",
            "8. ALTERNATIVE VARIATIONS",
            f"Version A: {', '.join(normalize_tags([data.genre, data.emotion, data.vocal, data.scene, 'reverb-heavy']))}",
            f"Version B: {', '.join(normalize_tags([data.genre, data.subgenre, data.vocal, data.mix_style, data.production]))}",
            f"Version C: {', '.join(normalize_tags([data.genre, data.emotion, data.vocal, data.scene]))}",
            "9. FINAL SUNO TAGS (Master Version)",
            tag_line,
        ]
    )


def _style_signature(style_hint: str, description: str) -> str:
    if style_hint:
        return style_hint
    text = description.lower()
    if "glitch" in text and "synth" in text:
        return "glitchy synthwave × melancholic pop met cinematic rand"
    if "trap" in text and "ambient" in text:
        return "dark ambient trap × cinematic urban gloom"
    return "cinematic electronic × emotional alt-pop"


def build_aurion_prompt(data: AurionInput) -> str:
    signature = _style_signature(data.style_hint, data.description)
    emotion_core = "Bittersweet spanning tussen verlies en hoop, met een onderlaag van nachtelijke introspectie."
    sonic = (
        "Een filmische wereld van neon-schaduw, zachte mist en pulserende ruimte. "
        "Warme pads botsen met koude digitale details zodat het tegelijk menselijk en futuristisch voelt. "
        "De track moet bewegen als een verhaal: rustig begin, oplopende spanning, emotionele release."
    )
    vocal = data.vocal_direction or "Androgyne, intieme vocal met breekbare emotie en duidelijke presence."
    lyrics_en = "Neon rain keeps calling my name\nI hold the static like a flame\nYour ghost is dancing in the blue\nI lose the night, I find the truth"
    lyrics_nl = "Neonregen fluistert zacht mijn naam\nIk draag het stil zijn als een vlam\nJouw schaduw beweegt nog door de straat\nTot ik in donker licht besta"
    lyrics = lyrics_nl if data.language.lower().startswith("nl") else lyrics_en

    return "\n".join(
        [
            "1) EMOTION CORE",
            emotion_core,
            "",
            "2) SONIC REALM / ATMOSPHERE",
            sonic,
            "",
            "3) STYLE SIGNATURE",
            signature,
            "",
            "4) VOCAL DIRECTION (OF “INSTRUMENTAAL”)",
            vocal,
            "",
            "5) LYRICS SEED (OPTIONEEL MAAR AANGERADEN)",
            lyrics,
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
    parser = argparse.ArgumentParser(description="V222 builder with AURION/HYPERSONA and SENTIVOX modes")
    sub = parser.add_subparsers(dest="command")

    suno = sub.add_parser("suno", help="Generate short Suno-friendly style prompt")
    suno.add_argument("--emotion")
    suno.add_argument("--genre")
    suno.add_argument("--vocal")
    suno.add_argument("--scene")
    suno.add_argument("--texture")
    suno.add_argument("--mode", choices=SUNO_MODES)

    master = sub.add_parser("mastering", help="Generate SENTIVOX/V5-style mastering report")
    master.add_argument("--track", default="User-described track")
    master.add_argument("--style", default="Hybrid modern")

    v6 = sub.add_parser("v6-suno", help="Generate full V6 Suno analysis output")
    v6.add_argument("--genre", default="dark techno")
    v6.add_argument("--subgenre", default="industrial techno")
    v6.add_argument("--emotion", default="melancholic")
    v6.add_argument("--vocal", default="female vocals")
    v6.add_argument("--scene", default="neon-lit rainy night")
    v6.add_argument("--mix-style", default="wide stereo")
    v6.add_argument("--production", default="modern production")

    aurion = sub.add_parser("aurion", help="Generate AURION/HYPERSONA V∞ Suno intent output")
    aurion.add_argument("--description", default="glitchy synthwave, post-love, cinematic night")
    aurion.add_argument("--style-hint", default="")
    aurion.add_argument("--vocal-direction", default="")
    aurion.add_argument("--language", default="en")

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.command == "mastering":
        print("\nSENTIVOX ENGINE V555 — MASTERING OUTPUT\n")
        print(build_mastering_report(args.track, args.style))
        return

    if args.command == "v6-suno":
        payload = V6Input(
            genre=args.genre,
            subgenre=args.subgenre,
            emotion=args.emotion,
            vocal=args.vocal,
            scene=args.scene,
            mix_style=args.mix_style,
            production=args.production,
        )
        print("\nBOB LUDWIG MASTERING ENGINE — V6 'SUNO MODE'\n")
        print(build_v6_analysis(payload))
        return

    if args.command == "aurion":
        payload = AurionInput(
            description=args.description,
            style_hint=args.style_hint,
            vocal_direction=args.vocal_direction,
            language=args.language,
        )
        print("\nAURION/HYPERSONA V∞ — SUNO AUDIO INTENT\n")
        print(build_aurion_prompt(payload))
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
