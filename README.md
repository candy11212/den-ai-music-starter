# V222 Suno Ultimate Style Prompt Builder

Deze tool heeft nu **2 modi**:

1. **Suno mode**: korte, Suno-vriendelijke style prompt met exact jouw gewenste output-structuur.
2. **Mastering mode**: Bob Ludwig V5 “Universe Mode”-achtige mastering report template.

## Suno mode (kort & direct)

Verplichte input-logica:
- emotion
- genre
- vocal
- scene
- texture

Output is altijd kort:
- STYLE
- VOCALS
- INSTRUMENTS
- TEXTURE
- SCENE
- ENHANCER

### Builder modes
- Ballad
- Cinematic
- Gothic
- NDH/Industrial
- Pop Emotional
- Dark Electronic

### Voorbeeld

```bash
python suno_prompt_builder.py suno \
  --emotion "angry" \
  --genre "industrial metal" \
  --vocal "male deep aggressive" \
  --scene "abandoned factory at night" \
  --texture "cold, metallic, wide" \
  --mode "NDH/Industrial"
```

## Mastering mode (V5 report)

Genereert een gestructureerde output met:
- MASTERING REPORT
- DETECTION MAP
- BAND/STYLE DNA
- MASTERING CHAIN + SETTINGS
- LOUDNESS & DYNAMICS TARGETS
- DELIVERY FORMATS
- END

### Voorbeeld

```bash
python suno_prompt_builder.py mastering \
  --track "Dark electronic rock with female lead and heavy sub" \
  --style "Gothic / Dark Electronic"
```

## Interactief

```bash
python suno_prompt_builder.py
```
