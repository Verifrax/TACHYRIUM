from __future__ import annotations

def build_object(
    *,
    kind: str,
    source_surface: str,
    target_surface: str,
    status: str,
    summary: str,
    payload: dict,
    notes: list[str],
) -> dict:
    return {
        "kind": kind,
        "source_surface": source_surface,
        "target_surface": target_surface,
        "status": status,
        "summary": summary,
        "payload": payload,
        "notes": notes,
    }


CLASS_MAP = {
    "host-copy": "projection",
    "readme-draft": "projection",
    "docs-draft": "projection",
    "topology-summary": "topology",
    "evidence-summary": "analysis",
    "authority-clarification": "analysis",
    "execution-clarification": "analysis",
    "verification-guidance": "routing",
    "proof-organization": "routing",
    "status-summary": "analysis",
}

ROUTE_MAP = {
    "host-copy": "VERIFRAX-SURFACE",
    "readme-draft": "VERIFRAX",
    "evidence-summary": "VERIFRAX",
    "authority-clarification": "AUCTORISEAL",
    "execution-clarification": "CORPIFORM",
    "verification-guidance": "VERIFRAX-verify",
    "proof-organization": "proof",
    "docs-draft": "VERIFRAX-DOCS",
    "status-summary": "VERIFRAX-STATUS",
    "topology-summary": "ARCHITECTURE",
}


def classify_subject_value(subject: str) -> str:
    return CLASS_MAP.get(subject, "analysis")


def route_subject_value(subject: str) -> str:
    return ROUTE_MAP.get(subject, "TACHYRIUM")


def classify_subject(subject: str) -> dict:
    classification = classify_subject_value(subject)
    return build_object(
        kind="summary",
        source_surface="TACHYRIUM",
        target_surface="TACHYRIUM",
        status="bounded",
        summary=f"Subject {subject} classified for bounded cognition handling.",
        payload={
            "subject": subject,
            "classification": classification,
            "scope": "bounded",
        },
        notes=[
            "review allowed",
            "non-authoritative",
        ],
    )


def route_candidate(subject: str, summary: str) -> dict:
    return build_object(
        kind="candidate",
        source_surface="TACHYRIUM",
        target_surface=route_subject_value(subject),
        status="subordinate",
        summary=summary,
        payload={
            "subject": subject,
            "intent": "route",
            "scope": "bounded",
        },
        notes=[
            "review required",
            "non-authoritative",
        ],
    )


def generate_candidate(subject: str, target_surface: str, summary: str) -> dict:
    return build_object(
        kind="candidate",
        source_surface="TACHYRIUM",
        target_surface=target_surface,
        status="subordinate",
        summary=summary,
        payload={
            "subject": subject,
            "intent": "draft",
            "scope": "bounded",
        },
        notes=[
            "review required",
            "non-authoritative",
        ],
    )


def pipeline_result(subject: str) -> dict:
    classification = classify_subject_value(subject)
    target_surface = route_subject_value(subject)
    return build_object(
        kind="briefing",
        source_surface="TACHYRIUM",
        target_surface="TACHYRIUM",
        status="bounded",
        summary=f"Bounded pipeline briefing prepared for {subject}.",
        payload={
            "subject": subject,
            "classification": classification,
            "target_surface": target_surface,
            "pipeline": ["classify", "route", "briefing"],
            "scope": "bounded",
        },
        notes=[
            "review required",
            "non-authoritative",
        ],
    )
