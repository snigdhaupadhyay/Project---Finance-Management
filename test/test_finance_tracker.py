import unittest
from unittest.mock import MagicMock, patch

import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from FinanceTracker import FinanceTracker

class TestFinanceTracker(unittest.TestCase):

    def setUp(self):
        # Create instance of FinanceTracker
        self.tracker = FinanceTracker()

        # Mock the MongoDB collections
        self.mock_expenses_collection = MagicMock()
        self.mock_budget_collection = MagicMock()

        # Replace the real collections with mocks
        self.tracker.expenses_collection = self.mock_expenses_collection
        self.tracker.budget_collection = self.mock_budget_collection


    def test_log_expense(self):
        expense = {"amount": 100, "category": "Food", "date": "2024-11-14"}
        self.tracker.log_expense(expense)
        self.mock_expenses_collection.insert_one.assert_called_once_with(expense)


    def test_set_budget_new(self):
        category = "Food"
        limit = 500

        # Simulate no existing budget
        self.mock_budget_collection.find_one.return_value = None

        self.tracker.set_budget(category, limit)
        self.mock_budget_collection.insert_one.assert_called_once_with({"category": category, "limit": limit})


    def test_set_budget_existing(self):
        category = "Food"
        limit = 500

        # Simulate an existing budget
        self.mock_budget_collection.find_one.return_value = {"category": category, "limit": 300}

        self.tracker.set_budget(category, limit)
        self.mock_budget_collection.update_one.assert_called_once_with(
            {"category": category}, {"$set": {"limit": limit}}
        )

    def test_show_summary(self):
        # Mock aggregation pipeline result
        mock_summary = [{"_id": "Food", "total_amount": 100}]
        self.mock_expenses_collection.aggregate.return_value = mock_summary

        summary = self.tracker.show_summary()

        self.mock_expenses_collection.aggregate.assert_called_once()
        self.assertEqual(list(summary), mock_summary)  # Verify the summary matches the mocked result

    def test_show_summarybymonth(self):
        month = "November"
        mock_summary = [{"_id": "Food", "total_amount": 100}]
        self.mock_expenses_collection.aggregate.return_value = mock_summary

        summary = self.tracker.show_summarybymonth(month)

        self.mock_expenses_collection.aggregate.assert_called_once()
        self.assertEqual(list(summary), mock_summary)


if __name__ == "__main__":
     unittest.main()
