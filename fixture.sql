CREATE TABLE scans (
    scan_id INTEGER PRIMARY KEY,
    parcel_ref TEXT NOT NULL,
    scanned_at TEXT NOT NULL,
    scan_state TEXT NOT NULL
);

-- Timestamps are UTC, with a fixed-width ISO 8601 representation.
INSERT INTO scans VALUES
    (42, 'P-101', '2026-04-07T09:20:00Z', 'routed'),
    (17, 'P-102', '2026-04-07T09:18:00Z', 'received'),
    (11, 'P-101', '2026-04-07T09:10:00Z', 'received'),
    (61, 'P-103', '2026-04-07T08:00:00Z', 'received'),
    (41, 'P-101', '2026-04-07T09:20:00Z', 'labelled'),
    (33, 'P-102', '2026-04-07T09:15:00Z', 'labelled'),
    (62, 'P-103', '2026-04-07T08:00:00Z', 'received'),
    (72, 'P-104', '2026-04-07T09:18:00Z', 'held');
