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


@dataclass
class ProducerInput:
    texture: str
    instruments: str
    energy_curve: str
    mix_direction: str


@dataclass
class SongwriterInput:
    emotion: str
    scene: str
    vocal: str
    theme: str
    language: str


@dataclass
class OmegaInput:
    mood: str
    emotion: str
    vocal: str
    style: str
    tempo: str
    image: str
    export_goal: str
    language: str


def build_songwriter_report(data: SongwriterInput) -> str:
    lyrics_en = """[Verse 1]
In the rain-lit glass I hear your name
Neon halos burn, but not the same
I keep the pieces where the streetlights fade
Learning how to hold the mess we made

[Pre-Chorus]
If the night breaks open, I will stay
With a fragile fire that won’t decay

[Chorus]
I rise through the dark with a trembling spark
Melancholic hope in a city of scars
You were the wound, now you’re the sign
I lost your hand, but I found my light

[Verse 2]
Cathedral echoes in the underpass
Old ghosts flicker in a mirror’s glass
Every silence taught me how to breathe
Every ending gave me room to be

[Bridge]
No perfect halo, no clean goodbye
Just human thunder under midnight sky

[Final Chorus]
I rise through the dark with a trembling spark
Melancholic hope in a city of scars
You were the wound, now you’re the sign
I lost your hand, but I found my light"""

    lyrics_nl = """[Verse 1]
In natte ramen hoor ik nog je naam
Neon brandt, maar nooit meer hetzelfde raam
Ik draag de scherven waar de straat stil wordt
En leer te leven met wat ooit kapot was

[Pre-Chorus]
Als de nacht me breekt, blijf ik nog staan
Met een kleine vlam die niet wil gaan

[Chorus]
Ik stijg uit het donker met een trillend hart
Melancholische hoop in een stad vol barst
Jij was de wond, nu ben je het teken
Ik liet je los, maar ik ben niet gebroken

[Verse 2]
Kerkklanken dwalen door beton en mist
Oude schaduwen in een raam dat wist
Elke stilte leerde mij weer adem
Elke val gaf ruimte om te dragen

[Bridge]
Geen heilige lijn, geen nette pijn
Alleen menselijk onweer onder maanlicht schijn

[Final Chorus]
Ik stijg uit het donker met een trillend hart
Melancholische hoop in een stad vol barst
Jij was de wond, nu ben je het teken
Ik liet je los, maar ik ben niet gebroken"""

    lyrics = lyrics_nl if data.language.lower().startswith('nl') else lyrics_en

    return "\n".join([
        "1. SONG CREATION REPORT",
        f"Theme: {data.theme}",
        "2. Emotional Genesis",
        f"Primary: {data.emotion}; Secondary: melancholic hope; Hidden: quiet resilience",
        "3. Scene & Atmosphere",
        f"Scene: {data.scene}; tone: cinematic, intimate, night-driven",
        "4. Vocal Direction",
        f"Vocal narrative DNA: {data.vocal}; performance arc: soft -> strong -> broken -> release",
        "5. Symbolic Motifs",
        "rain, neon, shadows, heart-fire, echo, night-city",
        "6. Full Lyrics (Suno-ready)",
        lyrics,
        "7. V222 Style Prompt (max 1–3 regels)",
        f"cinematic emotional pop, {data.emotion}, {data.vocal}, {data.scene}, symbolic rain-and-neon imagery",
        "8. Meta-Story Summary",
        "A love-wound transforms into identity: the narrator moves from fracture to grounded hope without losing emotional depth.",
    ])


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
            "SENTIVOX MASTERPLAN",
            "🎛 Chain settings",
            "- EQ: gentle tonal sculpt based on emotion target",
            "- Compression: glue + vocal-presence control",
            "- Limiting: controlled loudness with preserved transients",
            "💓 Emotion map",
            "- Lows: grounded weight",
            "- Mids: narrative/intimacy focus",
            "- Highs: air and emotional lift",
            "🧬 Profile match",
            f"- Source description: {track_desc}",
            f"- Style hint: {style_hint}",
            "📦 Export presets",
            "- Streaming: balanced loudness + true-peak safety",
            "- Vinyl: wider dynamics, softer limiting",
            "- TikTok/Shorts: forward mids + clear hook presence",
            "- AI-feed stems: clean separated print for reuse",
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
            "Output is Suno-ready and sectioned. If chorus feels too flat, change 'strong' to 'belted'; if too harsh, replace 'raw upfront' with 'intimate close'.",
        ]
    )


def build_voicebrain(data: SentivoxInput) -> str:
    return "\n".join(["[PERSONA]", _infer_persona(data.vocal_type, data.emotion)])


def build_arcify(data: SentivoxInput) -> str:
    return "\n".join(
        [
            "[EMOTIONAL ARC]",
            "intro: fragile",
            "verse: confessional",
            "chorus: strong release",
            "bridge: haunted break",
            "outro: reflective fade",
        ]
    )


def build_lyricmatch(data: SentivoxInput, lyrics: str) -> str:
    return "\n".join(
        [
            "[VOCAL MAP]",
            f"lyric intent: {lyrics.strip() or 'no lyrics supplied'}",
            f"delivery: {data.vocal_type}, mid-range, {data.emotion}, intimate close",
            "hook delivery: 8va lift, strong, wide cinematic",
        ]
    )


def build_abtest(data: SentivoxInput, variant_a: str, variant_b: str) -> str:
    return "\n".join(
        [
            "[ALTERNATIVES]",
            f"Alt A: {variant_a or (data.vocal_type + ', intimate close, soft')}",
            f"Alt B: {variant_b or (data.vocal_type + ', reverb distant, haunted')}",
            "Experimental: synthetic human blend + broken whispers + 8vb bridge",
            "",
            "[SELF-OPTIMIZATION]",
            "Pick A for clarity and lyric focus; pick B for atmosphere and distance.",
        ]
    )


def build_producer_direction(data: ProducerInput) -> str:
    return "\n".join(
        [
            "V222 PRODUCER DIRECTION",
            "ARRANGEMENT:",
            "intro airy setup -> verse detail -> pre-chorus lift -> wide chorus -> bridge contrast -> final release",
            "SOUND DESIGN:",
            data.instruments,
            "ENERGY CURVE:",
            data.energy_curve,
            "TEXTURE & TONE:",
            data.texture,
            "PRODUCTION:",
            f"{data.texture}, {data.instruments}, {data.energy_curve}, {data.mix_direction}",
        ]
    )




def build_omega_system_output(data: OmegaInput) -> str:
    aurion = build_aurion_prompt(
        AurionInput(
            description=f"{data.mood}, {data.style}, {data.image}",
            style_hint=f"{data.style} met {data.emotion} emotionele kern",
            vocal_direction=f"{data.vocal}, emotie: {data.emotion}, tempo-feel: {data.tempo}",
            language=data.language,
        )
    )
    mixboard = "\n".join(
        [
            "V∞ OMEGA MIXBOARD",
            f"Celestial: shine layer shaped by {data.mood}",
            f"Heartline: mid emotional core driven by {data.emotion}",
            f"Sub Foundation: bass gravity matched to {data.tempo}",
            f"Vocal Shape: {data.vocal}",
            f"Texture Direction: {data.style}",
            f"Image Translation: {data.image}",
        ]
    )
    sentivox = build_mastering_report(
        track_desc=f"{data.style} / {data.mood} / {data.emotion}",
        style_hint=f"Export intent: {data.export_goal}",
    )
    return "\n".join(
        [
            "OMEGA MUSIC SYSTEM — COMPLETE OUTPUT",
            "1) AURION WORLD + LYRICS",
            aurion,
            "",
            "2) OMEGA MIXBOARD ARCHITECTURE",
            mixboard,
            "",
            "3) SENTIVOX CONCEPTUAL MASTERING",
            sentivox,
            "",
            "4) OMEGA SUMMARY",
            f"Mood: {data.mood}",
            f"Emotion Curve: Shadow -> Glow ({data.emotion})",
            f"Style: {data.style}",
            f"Vocal Soul: {data.vocal}",
            f"Visual Frame: {data.image}",
            f"Export Goal: {data.export_goal}",
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

    sentivox = sub.add_parser("sentivox", help="/sentivox full vocal system generation")
    sentivox.add_argument("--style", default="dark electronic cinematic")
    sentivox.add_argument("--emotion", default="haunted warmth")
    sentivox.add_argument("--vocal-type", default="androgynous airy clean")
    sentivox.add_argument("--language", default="en")

    voicebrain = sub.add_parser("voicebrain", help="/voicebrain persona creation")
    voicebrain.add_argument("--emotion", default="haunted warmth")
    voicebrain.add_argument("--vocal-type", default="androgynous airy clean")

    arcify = sub.add_parser("arcify", help="/arcify emotional arc")
    arcify.add_argument("--emotion", default="haunted warmth")
    arcify.add_argument("--vocal-type", default="androgynous airy clean")

    lyricmatch = sub.add_parser("lyricmatch", help="/lyricmatch interpret lyrics into delivery")
    lyricmatch.add_argument("--emotion", default="haunted warmth")
    lyricmatch.add_argument("--vocal-type", default="androgynous airy clean")
    lyricmatch.add_argument("--lyrics", default="")

    abtest = sub.add_parser("abtest", help="/abtest compare two vocal approaches")
    abtest.add_argument("--emotion", default="haunted warmth")
    abtest.add_argument("--vocal-type", default="androgynous airy clean")
    abtest.add_argument("--a", default="")
    abtest.add_argument("--b", default="")

    producer = sub.add_parser("producer", help="V222 producer direction output")
    producer.add_argument("--texture", default="warm velvet + fog atmosphere")
    producer.add_argument("--instruments", default="warm analog keys, deep bass, emotional pads, soft piano")
    producer.add_argument("--energy-curve", default="slow emotional rise with cinematic peak")
    producer.add_argument("--mix-direction", default="wide cinematic mix, vocal-forward center")


    songwriter = sub.add_parser("songwriter", help="V222 songwriter full reality-architect output")
    songwriter.add_argument("--emotion", default="melancholic hope")
    songwriter.add_argument("--scene", default="neon rainy city")
    songwriter.add_argument("--vocal", default="androgynous intimate lead")
    songwriter.add_argument("--theme", default="post-love recovery")
    songwriter.add_argument("--language", default="en")


    omega = sub.add_parser("omega", help="OMEGA system: aurion + mixboard + sentivox")
    omega.add_argument("--mood", default="neon rain city")
    omega.add_argument("--emotion", default="melancholic hope")
    omega.add_argument("--vocal", default="androgynous intimate whisper")
    omega.add_argument("--style", default="glitchy synthwave cinematic")
    omega.add_argument("--tempo", default="mid-slow pulse")
    omega.add_argument("--image", default="time-fracture skyline in rain")
    omega.add_argument("--export-goal", default="streaming + storytelling")
    omega.add_argument("--language", default="en")

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

    if args.command == "voicebrain":
        print(build_voicebrain(SentivoxInput("", args.emotion, args.vocal_type, "en")))
        return

    if args.command == "arcify":
        print(build_arcify(SentivoxInput("", args.emotion, args.vocal_type, "en")))
        return

    if args.command == "lyricmatch":
        print(build_lyricmatch(SentivoxInput("", args.emotion, args.vocal_type, "en"), args.lyrics))
        return

    if args.command == "abtest":
        print(build_abtest(SentivoxInput("", args.emotion, args.vocal_type, "en"), args.a, args.b))
        return

    if args.command == "producer":
        print(build_producer_direction(ProducerInput(args.texture, args.instruments, args.energy_curve, args.mix_direction)))
        return


    if args.command == "songwriter":
        print(build_songwriter_report(SongwriterInput(args.emotion, args.scene, args.vocal, args.theme, args.language)))
        return


    if args.command == "omega":
        print(
            build_omega_system_output(
                OmegaInput(
                    mood=args.mood,
                    emotion=args.emotion,
                    vocal=args.vocal,
                    style=args.style,
                    tempo=args.tempo,
                    image=args.image,
                    export_goal=args.export_goal,
                    language=args.language,
                )
            )
        )
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
