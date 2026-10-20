#!/usr/bin/env python3
"""Compatibility entry point for the canonical, non-destructive niche populator.

The former implementation generated flat TOP_*.md files with legacy question
semantics. All generation now uses the taxonomy and CONFIG_SCHEMA.json.
"""
from populate_niches import main


if __name__ == "__main__":
    main()
