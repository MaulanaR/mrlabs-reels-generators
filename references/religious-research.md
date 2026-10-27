# Religious research and claim/source ledger

Read before writing religious assertions or selecting a story. This is an editorial sourcing workflow, not an automated fatwa service. Follow the user's selected baseline: Quran with Indonesian Kemenag translation/tafsir, and traceable sahih/hasan hadith with grading authority. Do not assume a preferred school of jurisprudence from the account name.

## Trace the actual claim

1. Identify the exact claim, whether it is a direct quotation, translation, tafsir, hadith, historical statement or the narrator's reflection, and which scene uses it.
2. For Quran, use [Quran Kemenag](https://quran.kemenag.go.id/) or [Bimas Islam Quran](https://bimasislam.kemenag.go.id/al-quran). Record surah name/number, verse range, verified Arabic when used, exact translation edition/source and relevant surrounding context. Consult tafsir before deriving a conclusion not stated directly in the verse. Do not assume an API is public/authorized merely because a documentation link exists.
3. For hadith, record collection, actual reference number plus edition/numbering system, quoted text or identified paraphrase, grade, and who graded it. A searchable publisher such as [Sunnah.com](https://sunnah.com/) can help locate text and grading; check the actual entry and attribution, not a search snippet or a grade invented from the collection name. A different numbering system is not automatically a different hadith. For the Sahih collections, record collection authentication/edition as the basis rather than inventing an entry-level grader.
4. Use verified sahih/hasan evidence for asserted teachings. Reject fabricated material; unresolved, weak or disputed authenticity is not silently upgraded. If an assessment materially differs between authorities, identify the difference and avoid presenting a disputed conclusion as consensus. Resolve uncertainty before production of the affected claim; rewrite or omit it, keeping the revised reviewed package consistent.
5. Distinguish historical detail established by evidence from illustrative setting. Do not invent a prophet's speech, motivation, physical appearance or unseen details to make a scene dramatic. A quotation attributed to a prophet requires actual source support. TTS remains a narrator describing meaning, never voice impersonation or AI tilawah.
6. New current-world facts need their own primary sources. A stock disaster clip is not evidence that a particular event was divine punishment. Do not add unsupported reward, punishment, medical benefit, end-time date or engagement promise.

Save `01_research.md` as readable notes and `01_religious_references.json` as the ledger. Mirror its status/claims/review_notes in `production.json.religious_references`; the guard checks consistency. Fields below are local production records, not a provider API schema.

## Ledger fields

- Root: `status` (`pending` or `verified`), `claims`, and `review_notes` with actual context/uncertainties. No claims means there are no religious assertions requiring a citation; explain this honestly in `review_notes`, not as an escape from research.
- Each claim: stable `id`, actual `claim`, `kind` (`quran`, `hadith`, `tafsir`, `history`, or `reflection`), `status`, `source_url`, and `context`. Only a genuinely examined claim may be marked `verified`.
- `quran`: add `surah`, `verses`, and `translation_source`; exact Arabic/translation and edition, when displayed, belong in the research/review artifact as well.
- `hadith`: add `collection`, `number`, `numbering_edition`, `grade` (`sahih` or `hasan`) and `grading_authority`. Add grading source/link when distinct from `source_url`; name the actual authority/basis, not an assumed one.
- Other types: identify the source and the distinction between sourced explanation and personal reflection. Do not relabel a religious assertion `reflection` to avoid verification.

The ledger, script, storyboard and DESIGN.md are part of the hashed review package. Production may not start with pending or unverified claims. The guard checks recorded completeness and consistency; it cannot authenticate a scholar's judgment, browser lookup, or human approval. Read the sources and show important citations/qualifications to the user.

## Arabic and narration

Preserve exact verified spelling, diacritics, verse boundaries and RTL shaping. Use an appropriate font such as Noto Naskh Arabic/Amiri and inspect actual rendered line wrapping/harakat. Do not generate Quran calligraphy or prophet names inside raster imagery, truncate a verse into a misleading statement, or guess a missing word. Keep verse, translation, source label and explanatory captions distinct.

Google narrates Indonesian meaning/explanation. Default honorific wording is respectful and consistent with the approved script. Do not send Arabic verse text for AI recitation; the user's selected policy excludes AI tilawah. An optional supplied licensed recording requires its own explicit request and review; it does not authorize changing the current default automatically.
