"""Smoke tests for suno_prompt_builder CLI functions."""
import pytest

from suno_prompt_builder import (
    OmegaInput,
    SentivoxInput,
    build_omega_system_output,
    build_sentivox_vocal_system,
)


def make_omega(**kwargs) -> OmegaInput:
    defaults = dict(
        mood="neon rain city",
        emotion="melancholic hope",
        vocal="androgynous intimate whisper",
        style="glitchy synthwave cinematic",
        tempo="mid-slow pulse",
        image="time-fracture skyline in rain",
        export_goal="streaming + storytelling",
        language="en",
    )
    defaults.update(kwargs)
    return OmegaInput(**defaults)


def make_sentivox(**kwargs) -> SentivoxInput:
    defaults = dict(
        style="dark electronic cinematic",
        emotion="haunted warmth",
        vocal_type="androgynous airy clean",
        language="en",
    )
    defaults.update(kwargs)
    return SentivoxInput(**defaults)


# ---------------------------------------------------------------------------
# omega --tempo
# ---------------------------------------------------------------------------

def test_omega_output_includes_tempo():
    out = build_omega_system_output(make_omega(tempo="mid-slow pulse"))
    assert "mid-slow pulse" in out


def test_omega_different_tempos_produce_different_output():
    out_slow = build_omega_system_output(make_omega(tempo="slow, 70 BPM"))
    out_fast = build_omega_system_output(make_omega(tempo="fast, 150 BPM"))
    assert out_slow != out_fast
    assert "slow, 70 BPM" in out_slow
    assert "fast, 150 BPM" in out_fast


# ---------------------------------------------------------------------------
# omega meta_truth localization
# ---------------------------------------------------------------------------

def test_omega_meta_truth_english_when_language_en():
    out = build_omega_system_output(make_omega(language="en"))
    assert "The song is about healing" in out
    # Must NOT contain Dutch-only meta_truth
    assert "Het lied gaat over helen" not in out


def test_omega_meta_truth_dutch_when_language_nl():
    out = build_omega_system_output(make_omega(language="nl"))
    assert "Het lied gaat over helen" in out


def test_omega_meta_truth_german_when_language_de():
    out = build_omega_system_output(make_omega(language="de"))
    assert "Das Lied handelt vom Heilen" in out


# ---------------------------------------------------------------------------
# sentivox --style
# ---------------------------------------------------------------------------

def test_sentivox_output_includes_style():
    out = build_sentivox_vocal_system(make_sentivox(style="dark electronic cinematic"))
    assert "dark electronic cinematic" in out


def test_sentivox_different_styles_produce_different_output():
    out_dark = build_sentivox_vocal_system(make_sentivox(style="dark industrial metal"))
    out_pop = build_sentivox_vocal_system(make_sentivox(style="bright pop ballad"))
    assert out_dark != out_pop
    assert "dark industrial metal" in out_dark
    assert "bright pop ballad" in out_pop
