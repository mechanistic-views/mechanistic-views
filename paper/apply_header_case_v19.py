"""Views subsection headers to sentence case, plus two renames.

Sentence case is the convention at TMLR and in the author's other papers; v19 was
uniformly Title Case. Proper nouns keep their capitals. Any \\label inside a
heading's braces is preserved. Backup at mechviews_v19_preheaders.tex.
"""
import pathlib
import re

P = pathlib.Path(__file__).resolve().parent / "mechviews_v19.tex"

RENAMES = {
    "What a Mechanistic View Is": "What a mechanistic view is",
    "The Five Axes": "The five axes",
    "Object View": "Object view",
    "Role View": "Role view",
    "Subspace View": "Subspace view",
    "Structural View": "Structural view",
    "Process View": "Process view",
    "Stratified View": "Stratified view",
    "Perspectival View": "Perspectival view",
    "Instrumental View": "Instrumental view",
    "Contrastive View": "Contrastive view",
    "The Determination Chain": "The determination chain",
    "View Families and Ontological Commitment": "View families and ontological commitment",
    "Methods Mapping": "Methods mapping",
    "Indirect Object Identification": "Indirect object identification",
    "Induction Heads": "Induction heads",
    "Localized vs.\\ Distributed": "Localized vs.\\ distributed",
    "Object vs.\\ Role": "Object vs.\\ role",
    "Single vs.\\ Triangulated Evidence": "Single vs.\\ triangulated evidence",
    "Static vs.\\ Process": "Static vs.\\ process",
    "Subspace vs.\\ Structural": "Subspace vs.\\ structural",
    "Behavioral vs.\\ Mechanistic": "Behavioral vs.\\ mechanistic",
    "The View Declaration Template": "The view declaration template",
    "Common Coherence Violations": "Common coherence violations",
    "Independent Convergence": "Independent convergence",
    "Clarified Problems": "Clarified problems",
    "Reframed Problems": "Reframed problems",
    "Scoped Problems": "Scoped problems",
    "Resolution Summary": "Resolution summary",
    "SAE Features: Decomposition or Projection?": "SAE features: decomposition or projection?",
    "Gender Bias Circuits": "Gender bias circuits",
    "Factual Recall and Knowledge Editing": "Factual recall and knowledge editing",
    "World Models": "World models",
    "Circuit Disagreements": "Circuit disagreements",
    "Decomposition Identity": "Decomposition identity",
    "Cross-Model Identity and Circuit Universality":
        "Cross-model identity and circuit universality",
    "Chain-of-Thought Faithfulness": "Chain-of-thought faithfulness",
    "Deceptive Alignment": "Deceptive alignment",
    "Safety Evidence Gaps": "Safety evidence gaps",
    "Validation Methodology": "Validation methodology",
    # --- the two that were making a claim in the heading ---
    # "Dissolved" states the section's conclusion; every sibling case study is a
    # plain label, so this one is brought into line.
    "Probe Features: The Probing Wars Dissolved": "Probe features",
    # "Research programme" is Lakatos's technical object (hard core, protective
    # belt, progressive or degenerating). The section actually distinguishes views
    # that organise existing practice from views that call for methods that do not
    # yet exist.
    "Views as Research Programs": "Descriptive and generative views",
}

text = P.read_text()
hits, missed = 0, []


def fix(match):
    global hits
    inner = match.group(1)
    # split off a trailing \label{...} so it survives the rename
    m = re.match(r"^(.*?)(\\label\{[^}]*\}\s*)?$", inner, re.S)
    title, label = m.group(1).rstrip(), m.group(2) or ""
    if title in RENAMES:
        hits += 1
        return "\\subsection{%s%s}" % (RENAMES[title], label)
    return match.group(0)


text = re.sub(r"\\subsection\{([^}]*(?:\{[^}]*\}[^}]*)*)\}", fix, text)

present = set(re.findall(r"\\subsection\{([^}]*)\}", text))
for old in RENAMES:
    if any(old in p for p in present):
        missed.append(old)

P.write_text(text)
print(f"{hits} subsection headers rewritten")
if missed:
    print("still present, check by hand:", missed)
