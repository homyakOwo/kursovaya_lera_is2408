import unittest
from notes import Note, add_note, complete_note, pending_titles, summary


class NotesTests(unittest.TestCase):
    def test_add_to_empty(self):
        self.assertEqual(add_note((), "Учебная задача")[0].identifier, 1)

    def test_add_trims_whitespace(self):
        self.assertEqual(add_note((), "  Задача  ")[0].title, "Задача")

    def test_add_rejects_empty(self):
        with self.assertRaises(ValueError):
            add_note((), "")

    def test_add_rejects_blank(self):
        with self.assertRaises(ValueError):
            add_note((), "  ")

    def test_identifiers_increase(self):
        existing = (Note(4, "A"), Note(9, "B"))
        self.assertEqual(add_note(existing, "C")[-1].identifier, 10)

    def test_complete_marks_note(self):
        self.assertTrue(complete_note((Note(1, "A"),), 1)[0].completed)

    def test_complete_rejects_missing(self):
        with self.assertRaises(ValueError):
            complete_note((Note(1, "A"),), 5)

    def test_original_note_not_mutated(self):
        original = (Note(1, "A"),)
        complete_note(original, 1)
        self.assertFalse(original[0].completed)

    def test_pending_titles(self):
        self.assertEqual(pending_titles((Note(1, "A"), Note(2, "B", True))), ["A"])

    def test_summary(self):
        self.assertEqual(summary((Note(1, "A"), Note(2, "B", True))), "Всего: 2, выполнено: 1")


if __name__ == "__main__":
    unittest.main()
