# Suno.ai Prompt Builder

Een professionele **AI prompt builder** voor Suno.ai.

## Wat is nu echt “AI” aan deze builder?

Deze versie doet meer dan een vaste template:
- Je geeft alleen een **band/groep** op.
- De builder gebruikt een **band-profiel analyse** om automatisch stijlvoorstellen te doen (genre, mood, energy, pace, key, octave, vocals, language, theme, production).
- Je kunt alles nog handmatig overschrijven met flags.

Dus: eerst slimme suggestie op basis van band, daarna controle door jou.

## Gebruik

### 1) Alleen band (AI-suggesties)

```bash
python suno_prompt_builder.py --band "Linkin Park"
```

### 2) Band + eigen overrides

```bash
python suno_prompt_builder.py \
  --band "Imagine Dragons" \
  --mood "epic and uplifting" \
  --key "D minor" \
  --octave "mid-to-high (3-5)"
```

### 3) Interactief

```bash
python suno_prompt_builder.py
```

Plak de output direct in Suno.ai als style prompt.
