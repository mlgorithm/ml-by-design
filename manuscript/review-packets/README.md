# Review Packets

This directory documents the reviewer-specific chapter bundles that can be generated from `book.pdf`.

Use the packet builder:

```bash
manuscript/build_review_packets.sh
```

Default output:

```text
/tmp/ai-book-review-packets
```

You can also choose a custom output directory:

```bash
manuscript/build_review_packets.sh /custom/output/path
```

## Packet Definitions

### ML Expert

- output file: `ml-expert-review.pdf`
- chapter bundle: Chapters 1, 2, 3, and 10
- page ranges in current compiled PDF: `15-58,147-158`

### Systems Or Reliability Reviewer

- output file: `systems-review.pdf`
- chapter bundle: Chapters 8, 9, 10, 11, and 12
- page ranges in current compiled PDF: `120-183`

### Instructor Or Target Reader

- output file: `instructor-review.pdf`
- chapter bundle: Chapters 1, 2, 8, and 12
- page ranges in current compiled PDF: `15-42,120-133,169-183`

## Notes

- The page ranges are based on the current compiled `book.pdf`.
- If the manuscript is edited substantially and pagination changes, regenerate the packets after rebuilding the book.
- The current builder writes a `manifest.txt` file next to the generated PDFs so each outreach packet can record the source commit and chapter bundle.
