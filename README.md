# V222 + SENTIVOX + AURION Suno Prompt Builder

Deze tool ondersteunt nu **4 modes**:

1. `suno` → korte Suno-vriendelijke prompt (STYLE/VOCALS/INSTRUMENTS/TEXTURE/SCENE/ENHANCER)
2. `mastering` → SENTIVOX/V5 mastering report
3. `v6-suno` → uitgebreide V6 Suno-analyse met 9 vaste outputsecties
4. `aurion` → AURION/HYPERSONA V∞ output in exact 5-delig format

## Nieuwe mode: aurion

`aurion` volgt exact deze structuur:
1) EMOTION CORE
2) SONIC REALM / ATMOSPHERE
3) STYLE SIGNATURE
4) VOCAL DIRECTION (OF “INSTRUMENTAAL”)
5) LYRICS SEED (OPTIONEEL MAAR AANGERADEN)

Deze mode blijft creatief en Suno-gericht, zonder technische masteringtermen.

### Voorbeeld

```bash
python suno_prompt_builder.py aurion \
  --description "female vocal, glitchy synthwave, post-love, cinematic night" \
  --style-hint "glitchy synthwave × melancholic pop met cinematic rand" \
  --vocal-direction "Breathy, intieme female vocal met zachte melancholie" \
  --language "en"
```

## v6-suno mode

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

## korte suno mode

```bash
python suno_prompt_builder.py suno \
  --emotion "angry" \
  --genre "industrial metal" \
  --vocal "male deep aggressive" \
  --scene "abandoned factory at night" \
  --texture "cold, metallic, wide" \
  --mode "NDH/Industrial"
```

## mastering mode

```bash
python suno_prompt_builder.py mastering \
  --track "Dark electronic rock with female lead and heavy sub" \
  --style "Gothic / Dark Electronic"
```
