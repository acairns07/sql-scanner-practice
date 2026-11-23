from pathlib import Path
import sqlite3
import sys
import unittest

HERE = Path(__file__).resolve().parent
QUERY = Path(sys.argv.pop(1)).read_text() if len(sys.argv) > 1 else (HERE / 'solution.sql').read_text()
FIXTURE = (HERE / 'fixture.sql').read_text()
EXPECTED = [('P-101', 42, 'routed'), ('P-102', 17, 'received'),
            ('P-103', 62, 'received'), ('P-104', 72, 'held')]


class ScanCheck(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(':memory:')
        self.addCleanup(self.db.close)
        self.db.executescript(FIXTURE)

    def test_fixture(self):
        self.assertEqual(self.db.execute(QUERY).fetchall(), EXPECTED)

    def test_extra_tie_and_late_id(self):
        self.db.executemany('INSERT INTO scans VALUES (?, ?, ?, ?)', [
            (90, 'P-101', '2026-04-07T09:05:00Z', 'replayed'),
            (91, 'P-104', '2026-04-07T09:18:00Z', 'cleared'),
        ])
        self.assertEqual(self.db.execute(QUERY).fetchall(),
                         EXPECTED[:3] + [('P-104', 91, 'cleared')])

    def test_no_scans(self):
        self.db.execute('DELETE FROM scans')
        self.assertEqual(self.db.execute(QUERY).fetchall(), [])


if __name__ == '__main__':
    unittest.main(verbosity=2)
