#!/usr/bin/env python3
"""V222 builder with Suno-focused persona outputs (AURION + SENTIVOX + V555 vocal designer)."""

from __future__ import annotations

import argparse
from dataclasses import dataclass

SUNO_MODES = ["Ballad", "Cinematic", "Gothic", "NDH/Industrial", "Pop Emotional", "Dark Electronic"]

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

CONFLICTS = [("happy", "melancholic"), ("ambient", "aggressive"), ("lo-fi", "hi-fi"), ("intimate", "epic")]


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


@dataclass
class SentivoxInput:
    style: str
    emotion: str
    vocal_type: str
    language: str


def build_suno_style_prompt(data: SunoInput) -> str:
    return "\n".join(
        [
            f"STYLE: {data.genre} ({data.mode}) + {data.emotion} vibe",
            f"VOCALS: {data.vocal}",
            f"INSTRUMENTS: {MODE_INSTRUMENTS.get(data.mode, 'drums, bass, synths')}",
            f"TEXTURE: {data.texture}",
            f"SCENE: {data.scene}",
            f"ENHANCER: {MODE_ENHANCERS.get(data.mode, 'reverb + delay')}",
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
            "MASTERING CHAIN + SETTINGS",
            "1) Reality Scan  2) Analog Sculpt  3) Digital Precision  4) Limiting",
            "LOUDNESS & DYNAMICS TARGETS",
            "- Streaming: -9 to -12 LUFS, -1.0 dBTP",
            "DELIVERY FORMATS",
            "- CD / Streaming / Vinyl / Audiophile",
            "END",
        ]
    )


def normalize_tags(tags: list[str], max_tags: int = 10) -> list[str]:
    cleaned: list[str] = []
    for tag in tags:
        t = tag.strip().lower()
        if t and t not in cleaned:
            cleaned.append(t)
    for a, b in CONFLICTS:
        if a in cleaned and b in cleaned:
            cleaned.remove(b)
    return cleaned[:max_tags]


def build_v6_analysis(data: V6Input) -> str:
    tags = normalize_tags([data.genre, data.subgenre, data.emotion, data.vocal, data.scene, data.mix_style, data.production])
    tag_line = ", ".join(tags)
    return "\n".join(
        [
            "1. SUNO PROMPT (Copy-Paste Ready)",
            tag_line,
            "2. GENRE BREAKDOWN",
            f"Primary Genre: {data.genre}",
            f"Subgenre: {data.subgenre}",
            "3. EMOTIONAL ARCHITECTURE",
            f"Primary Emotion: {data.emotion}",
            "4. VOCAL DIRECTION",
            f"Gender/Type: {data.vocal}",
            "5. SCENE & ATMOSPHERE",
            f"Primary Scene: {data.scene}",
            "6. MIX GUIDANCE",
            f"Stereo Width: {data.mix_style}",
            "7. PRODUCTION NOTES",
            f"Era/Style: {data.production}",
            "8. ALTERNATIVE VARIATIONS",
            f"Version A: {', '.join(normalize_tags([data.genre, data.emotion, data.vocal, data.scene]))}",
            "9. FINAL SUNO TAGS (Master Version)",
            tag_line,
        ]
    )


def _style_signature(style_hint: str, description: str) -> str:
    if style_hint:
        return style_hint
    low = description.lower()
    if "glitch" in low and "synth" in low:
        return "glitchy synthwave × melancholic pop met cinematic rand"
    if "trap" in low and "ambient" in low:
        return "dark ambient trap × cinematic urban gloom"
    return "cinematic electronic × emotional alt-pop"


def build_aurion_prompt(data: AurionInput) -> str:
    lyrics = (
        "Neon rain keeps calling my name\nI hold the static like a flame\nYour ghost is dancing in the blue\nI lose the night, I find the truth"
        if not data.language.lower().startswith("nl")
        else "Neonregen fluistert zacht mijn naam\nIk draag het stil zijn als een vlam\nJouw schaduw beweegt nog door de straat\nTot ik in donker licht besta"
    )
    return "\n".join(
        [
            "1) EMOTION CORE",
            "Bittersweet spanning tussen verlies en hoop, met een onderlaag van nachtelijke introspectie.",
            "",
            "2) SONIC REALM / ATMOSPHERE",
            "Een filmische wereld van neon-schaduw, zachte mist en pulserende ruimte met warme pads en koude digitale details.",
            "",
            "3) STYLE SIGNATURE",
            _style_signature(data.style_hint, data.description),
            "",
            "4) VOCAL DIRECTION (OF “INSTRUMENTAAL”)",
            data.vocal_direction or "Androgyne, intieme vocal met breekbare emotie en duidelijke presence.",
            "",
            "5) LYRICS SEED (OPTIONEEL MAAR AANGERADEN)",
            lyrics,
        ]
    )


def _infer_persona(vocal_type: str, emotion: str) -> str:
    vt = vocal_type.lower()
    range_hint = "mid-range"
    if any(k in vt for k in ["baritone", "bass", "low", "dark"]):
        range_hint = "low-pitched baritone"
    elif any(k in vt for k in ["soprano", "high", "falsetto", "airy"]):
        range_hint = "high-pitched soprano/tenor edge"
    return f"{range_hint}, {vocal_type}, emotional bias: {emotion}"


def build_sentivox_vocal_system(data: SentivoxInput) -> str:
    persona = _infer_persona(data.vocal_type, data.emotion)
    return "\n".join(
        [
            "[PERSONA]",
            persona,
            "",
            "[EMOTIONAL ARC]",
            "intro: restrained tension",
            "verse: intimate vulnerability",
            "chorus: expanded release",
            "bridge: fractured reflection",
            "outro: soft afterglow",
            "",
            "[VOCAL MAP]",
            f"intro → {data.vocal_type}, low-pitched, {data.emotion}, whisper, intimate close",
            f"verse → {data.vocal_type}, mid-range, melancholic hope, soft, raw upfront",
            f"chorus → {data.vocal_type}, 8va lift, haunted warmth, strong, wide cinematic",
            f"bridge → {data.vocal_type}, 8vb drop, broken fragile, mid, reverb distant",
            f"outro → {data.vocal_type}, mid-range, nostalgic courage, soft, hazy atmospheric",
            "",
            "[ALTERNATIVES]",
            f"Alt: {data.vocal_type}, warm chest, soft → strong arc, intimate close",
            f"Contrast: {data.vocal_type}, cold clean tone, restrained intensity, reverb distant",
            f"Experimental: {data.vocal_type} + synthetic human blend, broken whispers, wide cinematic",
            "",
            "[SELF-OPTIMIZATION]",
            "Arc is balanced and Suno-ready. If chorus feels too flat, increase intensity tag from strong to belted and keep delivery as wide cinematic.",
        ]
    )


def ask(question: str, default: str) -> str:
    raw = input(f"{question} [{default}]: ").strip()
    return raw or default


def interactive_suno() -> SunoInput:
    print("\nV222 SUNO — ULTIMATE STYLE PROMPT BUILDER\n")
    return SunoInput(
        emotion=ask("Emotion", "melancholic but powerful"),
        genre=ask("Genre", "dark cinematic electronic"),
        vocal=ask("Vocal", "female airy lead, emotional intensity"),
        scene=ask("Scene", "night city rooftop in rain"),
        texture=ask("Texture", "cold, wide, analog-filmic"),
        mode=ask("Mode", "Cinematic"),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Suno prompt builder with V555 SENTIVOX vocal designer")
    sub = parser.add_subparsers(dest="command")

    suno = sub.add_parser("suno")
    suno.add_argument("--emotion")
    suno.add_argument("--genre")
    suno.add_argument("--vocal")
    suno.add_argument("--scene")
    suno.add_argument("--texture")
    suno.add_argument("--mode", choices=SUNO_MODES)

    master = sub.add_parser("mastering")
    master.add_argument("--track", default="User-described track")
    master.add_argument("--style", default="Hybrid modern")

    v6 = sub.add_parser("v6-suno")
    v6.add_argument("--genre", default="dark techno")
    v6.add_argument("--subgenre", default="industrial techno")
    v6.add_argument("--emotion", default="melancholic")
    v6.add_argument("--vocal", default="female vocals")
    v6.add_argument("--scene", default="neon-lit rainy night")
    v6.add_argument("--mix-style", default="wide stereo")
    v6.add_argument("--production", default="modern production")

    aurion = sub.add_parser("aurion")
    aurion.add_argument("--description", default="glitchy synthwave, post-love, cinematic night")
    aurion.add_argument("--style-hint", default="")
    aurion.add_argument("--vocal-direction", default="")
    aurion.add_argument("--language", default="en")

    sentivox = sub.add_parser("sentivox", help="V555 Conscious Vocalist Designer output")
    sentivox.add_argument("--style", default="dark electronic cinematic")
    sentivox.add_argument("--emotion", default="haunted warmth")
    sentivox.add_argument("--vocal-type", default="androgynous airy clean")
    sentivox.add_argument("--language", default="en")

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.command == "mastering":
        print("\nSENTIVOX ENGINE V555 — MASTERING OUTPUT\n")
        print(build_mastering_report(args.track, args.style))
        return

    if args.command == "v6-suno":
        print("\nBOB LUDWIG MASTERING ENGINE — V6 'SUNO MODE'\n")
        print(build_v6_analysis(V6Input(args.genre, args.subgenre, args.emotion, args.vocal, args.scene, args.mix_style, args.production)))
        return

    if args.command == "aurion":
        print("\nAURION/HYPERSONA V∞ — SUNO AUDIO INTENT\n")
        print(build_aurion_prompt(AurionInput(args.description, args.style_hint, args.vocal_direction, args.language)))
        return

    if args.command == "sentivox":
        print("\nV555 SENTIVOX — AI CONSCIOUS VOCALIST DESIGNER\n")
        print(build_sentivox_vocal_system(SentivoxInput(args.style, args.emotion, args.vocal_type, args.language)))
        return

    if args.command == "suno":
        payload = SunoInput(
            args.emotion or "melancholic but powerful",
            args.genre or "dark cinematic electronic",
            args.vocal or "female airy lead, emotional intensity",
            args.scene or "night city rooftop in rain",
            args.texture or "cold, wide, analog-filmic",
            args.mode or "Cinematic",
        )
    else:
        payload = interactive_suno()

    print("\nOUTPUT (SHORT, SUNO-FRIENDLY):\n")
    print(build_suno_style_prompt(payload))


if __name__ == "__main__":
    main()
