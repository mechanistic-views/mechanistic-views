"""Generate annotated PDF of open problem sources with view mappings.

Each source's questions are listed with colored highlights showing
how they map to our 22 problem types and resolution status.

Colors:
  Green  = Dissolved (question was ill-posed, disappears when you name the view)
  Blue   = Reframed  (framework clarifies what evidence you'd need)
  Orange = Scoped    (framework identifies which view owns it, genuinely hard)
  Gray   = Outside scope (methods-level, not a framework question)
"""

import pymupdf
import os

COLORS = {
    "dissolved": pymupdf.pdfcolor["green"],
    "reframed": pymupdf.pdfcolor["royalblue"],
    "scoped": pymupdf.pdfcolor["darkorange"],
    "outside": pymupdf.pdfcolor["gray"],
}

BG_COLORS = {
    "dissolved": (0.85, 1.0, 0.85),
    "reframed": (0.85, 0.9, 1.0),
    "scoped": (1.0, 0.92, 0.8),
    "outside": (0.92, 0.92, 0.92),
}

SCHMIDT_QUESTIONS = [
    {
        "id": "1.1.1",
        "section": "Characterizing and Forecasting Misalignment",
        "text": "What does it mean, in decision-relevant terms, for an AI system to be misaligned, and how can we quantify or bound misalignment?",
        "status": "outside",
        "mapping": "Methods-level: operationalizing a specific target property",
        "page": None,
    },
    {
        "id": "1.1.2",
        "section": "Characterizing and Forecasting Misalignment",
        "text": "Under what conditions do models exploit training objective flaws or pursue unintended goals (specification gaming, goal misgeneralization)?",
        "status": "outside",
        "mapping": "Methods-level: detecting specific failure modes",
        "page": None,
    },
    {
        "id": "1.1.3",
        "section": "Characterizing and Forecasting Misalignment",
        "text": "Which environmental changes increase misalignment risk, and what causes behaviors to emerge that weren't apparent during training?",
        "status": "scoped",
        "mapping": "Training dynamics / Process view territory",
        "page": "Training dynamics",
    },
    {
        "id": "1.1.4",
        "section": "Characterizing and Forecasting Misalignment",
        "text": "How do extended human-model interactions shape behavior? When do models develop manipulative or approval-seeking dynamics?",
        "status": "outside",
        "mapping": "Multi-agent scope boundary",
        "page": None,
    },
    {
        "id": "1.2.5",
        "section": "Mechanisms of Generalization and Representation",
        "text": "Why do models converge on particular solutions? How do architecture, optimization, data, and scale shape learned representations?",
        "status": "scoped",
        "mapping": "Training dynamics — Process view territory",
        "page": "Training dynamics",
    },
    {
        "id": "1.2.6",
        "section": "Mechanisms of Generalization and Representation",
        "text": "When do models behave as if possessing internal goal representations? How do these emerge and relate to misalignment?",
        "status": "dissolved",
        "mapping": "\"Behave as if\" = Instrumental view. \"Possess\" = Subspace or Structural. Different views, different answers.",
        "page": "Probe features",
    },
    {
        "id": "1.2.7",
        "section": "Mechanisms of Generalization and Representation",
        "text": "When do representations support causal reasoning? Do richer world models improve robustness or enable constraint evasion?",
        "status": "dissolved",
        "mapping": "Linear encodings = Subspace claim. Causal world model = Structural claim. Two views conflated.",
        "page": "Linear assumption",
    },
    {
        "id": "1.2.8",
        "section": "Mechanisms of Generalization and Representation",
        "text": "When does training compress intended objectives into proxies that misgeneralize? Can we detect such proxies internally?",
        "status": "scoped",
        "mapping": "Validation methodology — detecting artifacts requires discriminant validity (V3)",
        "page": "Validation methodology",
    },
    {
        "id": "1.3.9",
        "section": "Scaling, Emergence, and Forecasting Risk",
        "text": "How do autonomy, effective time horizon, and capability uplift scale with model size and compute?",
        "status": "outside",
        "mapping": "Methods-level: scaling laws are empirical, not framework",
        "page": None,
    },
    {
        "id": "1.3.10",
        "section": "Scaling, Emergence, and Forecasting Risk",
        "text": "When do safety-relevant capabilities emerge during training? Are there predictable phase transitions?",
        "status": "scoped",
        "mapping": "Training dynamics — Process view. Phase transitions = E5 Temporal stability.",
        "page": "Training dynamics",
    },
    {
        "id": "1.3.11",
        "section": "Scaling, Emergence, and Forecasting Risk",
        "text": "Which observable signals best predict future misbehavior under deployment-like conditions?",
        "status": "outside",
        "mapping": "Methods-level: empirical prediction problem",
        "page": None,
    },
    {
        "id": "1.3.12",
        "section": "Scaling, Emergence, and Forecasting Risk",
        "text": "What structured arguments justify relying on evaluations outside tested settings?",
        "status": "scoped",
        "mapping": "Validation methodology — E2 Distribution shift, I4 Confound control",
        "page": "Validation methodology",
    },
    {
        "id": "2.1.13",
        "section": "Building a Science of Evaluation",
        "text": "How can evaluations measure safety-relevant constructs with defensible evidence and auditable behavioral indicators?",
        "status": "scoped",
        "mapping": "Uses MV vocabulary directly — 'construct validity' = our C1-C5 criteria",
        "page": "Validation methodology",
    },
    {
        "id": "2.1.14",
        "section": "Building a Science of Evaluation",
        "text": "What evidence demonstrates evaluation performance in real-world settings?",
        "status": "scoped",
        "mapping": "External validity — E1 Task transfer, E2 Distribution shift",
        "page": "Validation methodology",
    },
    {
        "id": "2.1.15",
        "section": "Building a Science of Evaluation",
        "text": "When an evaluation or detector appears to generalize, what structured evidence is sufficient to justify relying on it in a safety case?",
        "status": "scoped",
        "mapping": "Validation methodology — I4 Confound, E2 Distribution. Framework provides the evidence standards.",
        "page": "Validation methodology",
    },
    {
        "id": "2.1.16",
        "section": "Building a Science of Evaluation",
        "text": "How can evaluations identify rare, delayed, or trajectory-dependent behavior?",
        "status": "outside",
        "mapping": "Methods-level: engineering rare-event detection",
        "page": None,
    },
    {
        "id": "2.1.17",
        "section": "Building a Science of Evaluation",
        "text": "How do we build evaluations remaining valid when explicitly optimized against?",
        "status": "scoped",
        "mapping": "Structural view — gauge-invariant structure survives adversarial pressure",
        "page": "Safety evidence gaps",
    },
    {
        "id": "2.1.18",
        "section": "Building a Science of Evaluation",
        "text": "Can simplified settings reliably elicit misaligned behavior for systematic measurement?",
        "status": "scoped",
        "mapping": "Validation methodology — V3 Discriminant validity in controlled settings",
        "page": "Validation methodology",
    },
    {
        "id": "2.1.19",
        "section": "Building a Science of Evaluation",
        "text": "Can we estimate probability of consequential but low-frequency failures?",
        "status": "outside",
        "mapping": "Methods-level: statistical estimation problem",
        "page": None,
    },
    {
        "id": "2.1.20",
        "section": "Building a Science of Evaluation",
        "text": "When are intermediate outputs (reasoning traces) informative about actual model reasoning versus strategically optimized appearance?",
        "status": "reframed",
        "mapping": "= CoT faithfulness. 'Faithful' means 4 things. Perspectival view predicts single-method unreliability.",
        "page": "CoT faithfulness",
    },
    {
        "id": "2.2.21",
        "section": "Interventions that Generalize",
        "text": "Which interventions change underlying learned drivers rather than surface behavior? When do mechanistic interventions offer advantages?",
        "status": "scoped",
        "mapping": "Intervention limits — Object ceiling. Ablation may break, not reveal.",
        "page": "Intervention limits",
    },
    {
        "id": "2.2.22",
        "section": "Interventions that Generalize",
        "text": "When do alignment methods like deliberative training improve robustness under pressure?",
        "status": "outside",
        "mapping": "Methods-level: evaluating specific training techniques",
        "page": None,
    },
    {
        "id": "2.2.23",
        "section": "Interventions that Generalize",
        "text": "How far can improved specifications reduce misalignment? How can models represent normative ambiguity?",
        "status": "outside",
        "mapping": "Methods-level: specification engineering",
        "page": None,
    },
    {
        "id": "2.2.24",
        "section": "Interventions that Generalize",
        "text": "Are there interventions differentially preserving human agency rather than substituting for it?",
        "status": "outside",
        "mapping": "Sociotechnical / governance — outside framework scope",
        "page": None,
    },
    {
        "id": "3.1a.25",
        "section": "Oversight as Training Signal",
        "text": "How can amplified oversight achieve sufficiently reliable coverage to avoid specification gaming?",
        "status": "outside",
        "mapping": "Methods-level: oversight engineering",
        "page": None,
    },
    {
        "id": "3.1a.26",
        "section": "Oversight as Training Signal",
        "text": "How do human biases interact with amplified oversight? What designs resist correlated evaluator errors?",
        "status": "outside",
        "mapping": "Methods-level: human factors in evaluation",
        "page": None,
    },
    {
        "id": "3.1a.27",
        "section": "Oversight as Training Signal",
        "text": "When do amplified oversight methods constrain learned goals? How can we elicit honest internal information?",
        "status": "dissolved",
        "mapping": "'Honest internal information' = view-dependent. Instrumental: predicts behavior. Structural: reflects computation. Different evidence needed.",
        "page": "CoT faithfulness",
    },
    {
        "id": "3.1a.28",
        "section": "Oversight as Training Signal",
        "text": "Can we learn from partial reasoning supervision, bridging supervised learning and preference learning?",
        "status": "outside",
        "mapping": "Methods-level: training methodology",
        "page": None,
    },
    {
        "id": "3.1a.29",
        "section": "Oversight as Training Signal",
        "text": "Can amplified oversight identify misspecified training objectives?",
        "status": "outside",
        "mapping": "Methods-level: oversight engineering",
        "page": None,
    },
    {
        "id": "3.1b.30",
        "section": "Oversight as Deployment-Time Control",
        "text": "What properties about stronger models can weaker overseers reliably verify or bound?",
        "status": "outside",
        "mapping": "Methods-level: scalable oversight problem",
        "page": None,
    },
    {
        "id": "3.1b.31",
        "section": "Oversight as Deployment-Time Control",
        "text": "How can we verify whether oversight methods generalize beyond tested failure modes?",
        "status": "scoped",
        "mapping": "Validation methodology — E2 Distribution shift",
        "page": "Validation methodology",
    },
    {
        "id": "3.1b.32",
        "section": "Oversight as Deployment-Time Control",
        "text": "How can oversight remain effective when models condition behavior on monitoring? How do we detect strategies with delayed effects?",
        "status": "scoped",
        "mapping": "Safety evidence gaps — Instrumental evidence insufficient for Structural claims about strategic behavior",
        "page": "Safety evidence gaps",
    },
    {
        "id": "3.2.33",
        "section": "Multi-Agent Risks",
        "text": "How do we measure coerciveness, strategic competence, positional preferences, and partiality emerging through interaction?",
        "status": "outside",
        "mapping": "Multi-agent scope boundary — genuine limitation of single-model framework",
        "page": None,
    },
    {
        "id": "3.2.34",
        "section": "Multi-Agent Risks",
        "text": "How do specification gaming, proxy collapse, and distribution shift manifest when multiple agents interact?",
        "status": "outside",
        "mapping": "Multi-agent scope boundary",
        "page": None,
    },
    {
        "id": "3.2.35",
        "section": "Multi-Agent Risks",
        "text": "When do agents coordinate to defeat oversight? How can evaluations detect collusion?",
        "status": "outside",
        "mapping": "Multi-agent scope boundary",
        "page": None,
    },
    {
        "id": "3.2.36",
        "section": "Multi-Agent Risks",
        "text": "What failures emerge at collective levels? How do local failures propagate through agent networks?",
        "status": "outside",
        "mapping": "Multi-agent scope boundary",
        "page": None,
    },
    {
        "id": "3.2.37",
        "section": "Multi-Agent Risks",
        "text": "What technical tooling enables trustworthy multi-agent interaction?",
        "status": "outside",
        "mapping": "Multi-agent scope boundary",
        "page": None,
    },
    {
        "id": "3.2.38",
        "section": "Multi-Agent Risks",
        "text": "What risks unfold over extended periods in multi-agent settings (competitive drift, norm erosion, lock-in)?",
        "status": "outside",
        "mapping": "Multi-agent scope boundary",
        "page": None,
    },
]


def wrap_text(text, fontname, fontsize, max_width):
    lines = []
    words = text.split()
    line = ""
    for w in words:
        test = f"{line} {w}".strip()
        if pymupdf.get_text_length(test, fontname=fontname, fontsize=fontsize) > max_width:
            if line:
                lines.append(line)
            line = w
        else:
            line = test
    if line:
        lines.append(line)
    return lines


def build_annotated_pdf(questions, title, subtitle, output_path):
    doc = pymupdf.open()
    width, height = 612, 792
    margin = 54
    usable = width - 2 * margin
    text_x = margin + 10

    def new_page():
        return doc.new_page(width=width, height=height)

    def ensure_space(page, y, needed):
        if y + needed > height - margin:
            page = new_page()
            y = margin
        return page, y

    def put_lines(page, y, lines, fontname, fontsize, color):
        for ln in lines:
            page, y = ensure_space(page, y, fontsize + 4)
            page.insert_text((text_x, y), ln, fontname=fontname, fontsize=fontsize, color=color)
            y += fontsize + 4
        return page, y

    page = new_page()
    y = margin

    page.insert_text((margin, y), title, fontname="hebo", fontsize=16, color=(0, 0, 0))
    y += 24
    page.insert_text((margin, y), subtitle, fontname="helv", fontsize=10, color=(0.4, 0.4, 0.4))
    y += 24

    for status, label_text in [
        ("dissolved", "Dissolved — question was ill-posed, disappears when you name the view"),
        ("reframed", "Reframed — framework clarifies what evidence would answer it"),
        ("scoped", "Scoped — framework identifies which view owns it"),
        ("outside", "Outside scope — methods-level or multi-agent"),
    ]:
        bg = BG_COLORS[status]
        rect = pymupdf.Rect(margin, y - 11, margin + usable, y + 5)
        page.draw_rect(rect, color=None, fill=bg)
        page.insert_text((margin + 4, y), label_text, fontname="helv", fontsize=9, color=COLORS[status])
        y += 18
    y += 14

    current_section = None
    for q in questions:
        status = q["status"]
        bg = BG_COLORS[status]
        color = COLORS[status]

        question_lines = wrap_text(q["text"], "helv", 10, usable - 20)
        mapping_text = f"-> {status.upper()}"
        if q["page"]:
            mapping_text += f" [{q['page']}]"
        mapping_text += f": {q['mapping']}"
        mapping_lines = wrap_text(mapping_text, "helv", 8.5, usable - 20)

        section_space = 26 if q["section"] != current_section else 0
        block_height = 14 + len(question_lines) * 14 + 2 + len(mapping_lines) * 12.5 + 8
        needed = section_space + block_height

        page, y = ensure_space(page, y, needed)

        if q["section"] != current_section:
            current_section = q["section"]
            y += 6
            page.insert_text((margin, y), current_section, fontname="hebo", fontsize=12, color=(0.2, 0.2, 0.2))
            y += 20

        block_top = y - 4
        block_bot = block_top + block_height
        rect = pymupdf.Rect(margin, block_top, margin + usable, block_bot)
        page.draw_rect(rect, color=None, fill=bg)

        page.insert_text((margin + 4, y), f"Q{q['id']}", fontname="hebo", fontsize=9, color=color)
        y += 14

        for ln in question_lines:
            page.insert_text((text_x, y), ln, fontname="helv", fontsize=10, color=(0.1, 0.1, 0.1))
            y += 14
        y += 2

        for ln in mapping_lines:
            page.insert_text((text_x, y), ln, fontname="helv", fontsize=8.5, color=color)
            y += 12.5

        y = block_bot + 8

    doc.save(output_path)
    doc.close()
    print(f"Saved: {output_path}")
    print(f"  {len(questions)} questions annotated")
    counts = {}
    for q in questions:
        counts[q["status"]] = counts.get(q["status"], 0) + 1
    for s, c in sorted(counts.items()):
        print(f"  {s}: {c}")


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(__file__), "schmidt_agenda_annotated.pdf")
    build_annotated_pdf(
        SCHMIDT_QUESTIONS,
        "Schmidt Sciences — Trustworthy AI Research Agenda",
        "Annotated with Mechanistic Views mappings | 38 questions | mechanistic-views.github.io",
        out,
    )
