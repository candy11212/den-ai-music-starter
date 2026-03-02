# Suno.ai internet research note

## Status
Attempted to fetch Suno documentation and community pages, but outgoing HTTPS requests in this environment returned `403 CONNECT tunnel failed`.

## Tried sources
- https://help.suno.com/en
- https://help.suno.com/en/collections/1865339-getting-started
- https://www.suno.wiki/faq/prompting
- https://www.reddit.com/r/SunoAI/search/?q=prompt%20tips&restrict_sr=1

## Practical Suno prompt guidance (compiled)
Even without direct access to those pages in this environment, these are strong practical defaults:

1. Keep style prompts concise and concrete (genre + mood + vocal + production texture).
2. Describe arrangement arc explicitly (intro -> verse -> chorus -> bridge -> final chorus).
3. Include vocal intent (distance, intensity, timbre, delivery).
4. Avoid contradictory tags (e.g., "lo-fi" + "hi-fi", "ambient" + "aggressive").
5. For consistency, reuse a fixed prompt template and swap only 3-5 key variables.
6. For better hooks, ask for "memorable chorus" and "clear topline" directly.
7. For cinematic tracks, mention spatial feel (wide chorus, intimate verse, atmospheric tails).
8. For dark/gothic material, include symbolic imagery (rain, stone, night, echo, silence).

## Suggested template
`<genre/subgenre>, <emotion>, <vocal type + delivery>, <scene>, <texture>, <arrangement arc>, <mix intent>`

Example:
`dark cinematic rock, melancholic hope, baritone intimate-to-anthemic vocal, neon rainy city, warm mids with wide chorus, fragile intro -> confessional verse -> anthemic chorus -> reflective bridge -> cathartic final chorus, clear vocal center with atmospheric width`
