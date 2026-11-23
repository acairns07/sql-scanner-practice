# Which parcel scan wins?

A 10–15 minute SQLite exercise. A warehouse view needs the current state of each parcel. Scanners sometimes submit several events at the same timestamp, so the latest timestamp alone can return more than one row.

## Your task

Write one query over `scans` (see `fixture.sql`). Return exactly one row per `parcel_ref` with columns `parcel_ref`, `scan_id`, `scan_state`, sorted by `parcel_ref`. Pick the greatest `scanned_at`; if timestamps tie for a parcel, pick the greatest `scan_id`. IDs are unique and are only a tie-breaker, not a reliable substitute for event time. Timestamps in this exercise are fixed-width UTC strings, so text sort gives chronological order.

| parcel_ref | scan_id | scan_state |
| --- | ---: | --- |
| P-101 | 42 | routed |
| P-102 | 17 | received |
| P-103 | 62 | received |
| P-104 | 72 | held |

Save your query as `attempt.sql` and run `python3 check.py attempt.sql`. Run `python3 check.py` to test the reference answer. No dependencies beyond Python 3 with SQLite 3.25+ and its standard-library `sqlite3` module.

## Walkthrough (after trying it)

`solution.sql` partitions events by parcel and ranks by timestamp, then ID, both descending. `ROW_NUMBER()` returns one first row even when timestamps tie. Put the window expression in a CTE so you can filter on its result. `MAX(scanned_at)` joined back to `scans` would return both P-101 rows at 09:20. Picking `MAX(scan_id)` would return the older scan for P-102. The final `ORDER BY` sorts the output, not the events within a parcel.

---

Optional: the publisher of this free exercise also sells a separate PDF interview kit, [The Locker Feed (£8)](https://payhip.com/b/mNALJ). You can read the [free no-spoiler preview](https://payhip.com/preview/mNALJ) first. This exercise is complete on its own.
