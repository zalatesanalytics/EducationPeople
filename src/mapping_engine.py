"""
AI-style indicator mapping engine.

For now uses text similarity (SequenceMatcher).
Later you can plug in OpenAI / other LLMs here.
"""

from difflib import SequenceMatcher
from typing import List, Dict, Tuple, Optional


def _similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def map_indicator_to_org(
    indicator_text: str,
    org_catalog: List[Dict],
    threshold: float = 0.45,
) -> Tuple[Optional[str], float]:
    """
    Map a single project indicator to the closest organizational indicator.

    Returns (org_indicator_id, similarity_score).
    If no match above threshold, returns (None, best_score).
    """
    indicator_text = (indicator_text or "").strip()
    if not indicator_text:
        return None, 0.0

    best_match = None
    best_score = 0.0

    key_words = ["student", "school", "teacher", "book", "classroom", "household", "learner"]

    for org_ind in org_catalog:
        name = org_ind.get("name", "")
        score = _similarity(indicator_text, name)

        for kw in key_words:
            if kw in indicator_text.lower() and kw in name.lower():
                score += 0.05

        if score > best_score:
            best_score = score
            best_match = org_ind

    if best_match and best_score >= threshold:
        return best_match["org_indicator_id"], round(best_score, 3)

    return None, round(best_score, 3)
