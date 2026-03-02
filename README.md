# V222 + BOB LUDWIG V6 Suno Prompt Builder

Deze tool ondersteunt nu **3 modes**:

1. `suno` → korte Suno-vriendelijke prompt (STYLE/VOCALS/INSTRUMENTS/TEXTURE/SCENE/ENHANCER)
2. `mastering` → V5 mastering report
3. `v6-suno` → uitgebreide V6 Suno-analyse met 9 vaste outputsecties

## Nieuwe mode: v6-suno

De `v6-suno` mode volgt je notecardstructuur:
1. SUNO PROMPT (Copy-Paste Ready)
2. GENRE BREAKDOWN
3. EMOTIONAL ARCHITECTURE
4. VOCAL DIRECTION
5. SCENE & ATMOSPHERE
6. MIX GUIDANCE
7. PRODUCTION NOTES
8. ALTERNATIVE VARIATIONS
9. FINAL SUNO TAGS (Master Version)

Daarnaast wordt basis conflict-filtering toegepast (bijv. `happy` + `melancholic`, `lo-fi` + `hi-fi`) en tag-reductie naar max 10 tags.

### Voorbeeld

```bash
python suno_prompt_builder.py v6-suno \
  --genre "dark techno" \
  --subgenre "industrial techno" \
  --emotion "melancholic" \
  --vocal "ethereal female vocals" \
  --scene "neon-lit rainy night" \
  --mix-style "wide stereo" \
  --production "modern production"
```

## Bestaande korte Suno mode

```bash
python suno_prompt_builder.py suno \
  --emotion "angry" \
  --genre "industrial metal" \
  --vocal "male deep aggressive" \
  --scene "abandoned factory at night" \
  --texture "cold, metallic, wide" \
  --mode "NDH/Industrial"
```

## Mastering mode

```bash
python suno_prompt_builder.py mastering \
  --track "Dark electronic rock with female lead and heavy sub" \
  --style "Gothic / Dark Electronic"
```
