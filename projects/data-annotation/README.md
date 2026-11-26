# Data annotation quality

This fictional calibration example uses labels Supported, Unsupported and Ambiguous.

| Record | Reviewer A | Reviewer B | Action |
|---|---|---|---|
| 1 | Supported | Supported | Accept |
| 2 | Unsupported | Unsupported | Accept |
| 3 | Ambiguous | Supported | Adjudicate |
| 4 | Ambiguous | Ambiguous | Retain ambiguity |
| 5 | Supported | Supported | Accept |

Raw agreement is 4/5 = 80%. This tiny synthetic sample is an illustration, not a production benchmark.

## Review workflow

- Define label meanings and boundary cases.
- Independently double-label a calibration sample.
- Record disagreement reasons and adjudicate.
- Update guidance without silently overwriting the original labels.
- Recheck samples after rubric changes.

**Next evidence to add:** authorized anonymized examples and real agreement metrics.
