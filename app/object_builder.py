#!/usr/bin/env python3
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
