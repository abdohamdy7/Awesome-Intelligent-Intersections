# Contributing

Thank you for improving Awesome Intelligent Intersections. Contributions may add a resource, correct a record, verify an implementation, or improve the taxonomy and documentation.

## Before opening a pull request

1. Confirm that the resource directly supports intersection-level planning, control, coordination, evaluation, or deployment.
2. Add or edit the appropriate CSV file in [`data/`](data/); do not edit generated index pages by hand.
3. Use the existing vocabulary and a stable kebab-case `id`.
4. Set `last_verified` to the date on which you checked the links and metadata.
5. Run:

   ```bash
   python scripts/build_pages.py
   python scripts/build_pages.py --check
   python scripts/validate_repository.py
   ```

## Verifying paper and code links

A code repository should be linked only when its relationship to the paper is supported by at least one of these signals:

- the paper or project page links to the repository;
- the repository explicitly names/cites the paper and is owned by an author, laboratory, or project;
- an author-controlled profile links the paper and repository;
- for a third-party reproduction, the repository clearly identifies the reproduced method.

Use `official`, `author-released`, or `third-party` accordingly. If none can be verified, leave `code_url` blank and use `not-found`. Do not substitute a similarly named repository or a general framework.

## Required paper fields

Provide the title, year, venue, intersection context, traffic context, method family, coordination architecture, evidence level, stable paper URL when available, BibTeX key, and verification date. A BibTeX key should correspond to the survey bibliography or be added to it in a coordinated paper update.

## Evidence and claims

- Report the demonstrated environment, not an inferred deployment level.
- Distinguish offline data evaluation from closed-loop simulation.
- Do not treat a 100% CAV study as mixed-traffic evidence.
- For foundation-model work, distinguish direct, enabling, and adjacent roles.
- Preserve stated limitations and commercial/license constraints for resources.

Use the issue forms for proposed additions or corrections when a pull request is not ready.
