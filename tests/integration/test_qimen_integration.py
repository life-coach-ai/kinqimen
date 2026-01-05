# -*- coding: utf-8 -*-
"""
Integration tests for kinqimen package.

Tests cross-module behavior and complete workflows.
"""

import pytest
from datetime import datetime


class TestQimenEndToEnd:
    """End-to-end integration tests."""

    def test_import_from_package(self):
        """Test that we can import Qimen from the package."""
        from kinqimen import Qimen, QiMen

        assert Qimen is not None
        assert QiMen is not None
        assert Qimen is QiMen  # They should be the same class

    def test_complete_chart_calculation_workflow(self):
        """Test complete workflow from instantiation to chart calculation."""
        from kinqimen import Qimen

        # Create instance
        qm = Qimen(2024, 1, 14, 23, 20)

        # Calculate hour chart (時家奇門)
        hour_chart = qm.pan(1)
        assert isinstance(hour_chart, dict)
        assert "天盤" in hour_chart
        assert "地盤" in hour_chart
        assert "門" in hour_chart
        assert "星" in hour_chart

        # Calculate day chart (日家奇門/金函玉鏡)
        day_chart = qm.gpan()
        assert isinstance(day_chart, dict)
        assert "局" in day_chart
        assert "星" in day_chart
        assert "門" in day_chart

        # Calculate minute chart (刻家奇門)
        minute_chart = qm.pan_minute(1)
        assert isinstance(minute_chart, dict)
        assert "天盤" in minute_chart
        assert "地盤" in minute_chart

    def test_overall_workflow(self):
        """Test the overall() method that combines all chart types."""
        from kinqimen import Qimen

        qm = Qimen(2024, 6, 21, 12, 0)  # Summer solstice
        overall = qm.overall(1)

        # Verify all three chart types are present
        assert "金函玉鏡(日家奇門)" in overall
        assert "時家奇門" in overall
        assert "刻家奇門" in overall

        # Verify each chart type has expected structure
        day_chart = overall["金函玉鏡(日家奇門)"]
        assert "局" in day_chart

        hour_chart = overall["時家奇門"]
        assert "天盤" in hour_chart
        assert "地盤" in hour_chart

        minute_chart = overall["刻家奇門"]
        assert "天盤" in minute_chart
        assert "地盤" in minute_chart

    def test_different_chart_options(self):
        """Test that different calculation options produce different results."""
        from kinqimen import Qimen

        qm = Qimen(2024, 3, 21, 6, 0)  # Spring equinox

        # Calculate with option 1 (拆補)
        chart1 = qm.pan(1)

        # Calculate with option 2 (置閏)
        chart2 = qm.pan(2)

        # They should use different methods
        assert chart1["排盤方式"] == "拆補"
        assert chart2["排盤方式"] == "置閏"

        # The results should differ
        assert chart1 != chart2

    def test_multiple_instances_independent(self):
        """Test that multiple Qimen instances are independent."""
        from kinqimen import Qimen

        # Create two instances with different dates
        qm1 = Qimen(2024, 1, 1, 0, 0)
        qm2 = Qimen(2024, 12, 31, 23, 59)

        # Calculate charts
        chart1 = qm1.pan(1)
        chart2 = qm2.pan(1)

        # They should be different
        assert chart1["干支"] != chart2["干支"]

    def test_seasonal_variations(self):
        """Test that charts reflect seasonal variations."""
        from kinqimen import Qimen

        # Winter solstice
        winter = Qimen(2024, 12, 21, 12, 0)
        winter_day_chart = winter.gpan()

        # Summer solstice
        summer = Qimen(2024, 6, 21, 12, 0)
        summer_day_chart = summer.gpan()

        # Day charts should have different 局 (bureaus) for different seasons
        assert "局" in winter_day_chart
        assert "局" in summer_day_chart
        assert winter_day_chart["局"] != summer_day_chart["局"]


class TestQimenReproducibility:
    """Test that calculations are reproducible."""

    def test_same_datetime_produces_same_chart(self):
        """Test that the same datetime always produces the same chart."""
        from kinqimen import Qimen

        # Create two instances with identical datetime
        qm1 = Qimen(2024, 5, 15, 14, 30)
        qm2 = Qimen(2024, 5, 15, 14, 30)

        # Calculate charts with same option
        chart1 = qm1.pan(1)
        chart2 = qm2.pan(1)

        # They should be identical
        assert chart1["干支"] == chart2["干支"]
        assert chart1["旬首"] == chart2["旬首"]
        assert chart1["局日"] == chart2["局日"]
        assert chart1["排局"] == chart2["排局"]
