# -*- coding: utf-8 -*-
"""
Unit tests for kinqimen.py module.

Following 1:1 mapping: kinqimen.py → tests/unit/test_kinqimen.py
"""

import pytest
from datetime import datetime


class TestQimenInstantiation:
    """Test Qimen class instantiation."""

    def test_qimen_init(self, sample_date_components):
        """Test that Qimen instance can be created with valid parameters."""
        from kinqimen import Qimen

        qm = Qimen(
            sample_date_components["year"],
            sample_date_components["month"],
            sample_date_components["day"],
            sample_date_components["hour"],
            sample_date_components["minute"]
        )

        assert qm.year == sample_date_components["year"]
        assert qm.month == sample_date_components["month"]
        assert qm.day == sample_date_components["day"]
        assert qm.hour == sample_date_components["hour"]
        assert qm.minute == sample_date_components["minute"]

    def test_qimen_alias(self, sample_date_components):
        """Test that QiMen alias works correctly."""
        from kinqimen import QiMen

        qm = QiMen(
            sample_date_components["year"],
            sample_date_components["month"],
            sample_date_components["day"],
            sample_date_components["hour"],
            sample_date_components["minute"]
        )

        assert qm is not None
        assert hasattr(qm, 'year')


class TestQimenChartMethods:
    """Test Qimen chart calculation methods."""

    def test_pan_method_exists(self, qimen_instance):
        """Test that pan() method exists and is callable."""
        assert hasattr(qimen_instance, 'pan')
        assert callable(qimen_instance.pan)

    def test_pan_returns_dict(self, qimen_instance):
        """Test that pan() returns a dictionary."""
        result = qimen_instance.pan(1)
        assert isinstance(result, dict)

    def test_pan_contains_expected_keys(self, qimen_instance):
        """Test that pan() result contains expected keys."""
        result = qimen_instance.pan(1)

        # Check for essential keys
        expected_keys = ["排盤方式", "干支", "旬首", "旬空", "局日", "排局", "節氣"]
        for key in expected_keys:
            assert key in result, f"Expected key '{key}' not found in result"

    def test_pan_option_1_vs_2(self, qimen_instance):
        """Test that pan(1) and pan(2) produce different results."""
        result1 = qimen_instance.pan(1)
        result2 = qimen_instance.pan(2)

        assert result1["排盤方式"] == "拆補"
        assert result2["排盤方式"] == "置閏"

    def test_gpan_method_exists(self, qimen_instance):
        """Test that gpan() method exists and is callable."""
        assert hasattr(qimen_instance, 'gpan')
        assert callable(qimen_instance.gpan)

    def test_gpan_returns_dict(self, qimen_instance):
        """Test that gpan() returns a dictionary."""
        result = qimen_instance.gpan()
        assert isinstance(result, dict)

    def test_pan_minute_method_exists(self, qimen_instance):
        """Test that pan_minute() method exists and is callable."""
        assert hasattr(qimen_instance, 'pan_minute')
        assert callable(qimen_instance.pan_minute)

    def test_pan_minute_returns_dict(self, qimen_instance):
        """Test that pan_minute() returns a dictionary."""
        result = qimen_instance.pan_minute(1)
        assert isinstance(result, dict)


class TestQimenHelperMethods:
    """Test Qimen helper methods."""

    def test_year_yuen_exists(self, qimen_instance):
        """Test that year_yuen() method exists."""
        assert hasattr(qimen_instance, 'year_yuen')
        assert callable(qimen_instance.year_yuen)

    def test_qimen_ju_day_exists(self, qimen_instance):
        """Test that qimen_ju_day() method exists."""
        assert hasattr(qimen_instance, 'qimen_ju_day')
        assert callable(qimen_instance.qimen_ju_day)

    def test_qimen_ju_day_returns_string(self, qimen_instance):
        """Test that qimen_ju_day() returns a string."""
        result = qimen_instance.qimen_ju_day()
        assert isinstance(result, str)

    def test_tianyi_exists(self, qimen_instance):
        """Test that tianyi() method exists."""
        assert hasattr(qimen_instance, 'tianyi')
        assert callable(qimen_instance.tianyi)


class TestQimenOverall:
    """Test overall() method that combines all chart types."""

    def test_overall_method_exists(self, qimen_instance):
        """Test that overall() method exists and is callable."""
        assert hasattr(qimen_instance, 'overall')
        assert callable(qimen_instance.overall)

    def test_overall_returns_dict(self, qimen_instance):
        """Test that overall() returns a dictionary."""
        result = qimen_instance.overall(1)
        assert isinstance(result, dict)

    def test_overall_contains_all_chart_types(self, qimen_instance):
        """Test that overall() contains all three chart types."""
        result = qimen_instance.overall(1)

        expected_keys = ["金函玉鏡(日家奇門)", "時家奇門", "刻家奇門"]
        for key in expected_keys:
            assert key in result, f"Expected key '{key}' not found in overall() result"


class TestQimenEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_qimen_with_current_datetime(self):
        """Test Qimen with current datetime components."""
        from kinqimen import Qimen
        now = datetime.now()

        qm = Qimen(now.year, now.month, now.day, now.hour, now.minute)
        assert qm is not None

        # Should be able to calculate a chart
        result = qm.pan(1)
        assert isinstance(result, dict)

    def test_qimen_with_historical_date(self):
        """Test Qimen with a historical date."""
        from kinqimen import Qimen

        # Test with a date from year 2000
        qm = Qimen(2000, 6, 15, 12, 30)
        assert qm is not None

        result = qm.pan(1)
        assert isinstance(result, dict)

    def test_qimen_with_future_date(self):
        """Test Qimen with a future date."""
        from kinqimen import Qimen

        # Test with a date in year 2030
        qm = Qimen(2030, 12, 31, 23, 59)
        assert qm is not None

        result = qm.pan(1)
        assert isinstance(result, dict)
