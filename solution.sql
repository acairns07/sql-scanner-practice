WITH ranked AS (
    SELECT *, ROW_NUMBER() OVER (
        PARTITION BY parcel_ref
        ORDER BY scanned_at DESC, scan_id DESC
    ) AS position
    FROM scans
)
SELECT parcel_ref, scan_id, scan_state
FROM ranked
WHERE position = 1
ORDER BY parcel_ref;
