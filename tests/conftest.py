# -*- coding: utf-8 -*-
"""
Shared pytest fixtures and configuration.
"""

import pytest
from datetime import datetime


@pytest.fixture
def sample_datetime():
    """Sample datetime for testing."""
    return datetime(2024, 1, 14, 23, 20)


@pytest.fixture
def sample_date_components():
    """Sample date components as separate values."""
    return {
        "year": 2024,
        "month": 1,
        "day": 14,
        "hour": 23,
        "minute": 20
    }


@pytest.fixture
def qimen_instance(sample_date_components):
    """Create a Qimen instance for testing."""
    from kinqimen import Qimen
    return Qimen(
        sample_date_components["year"],
        sample_date_components["month"],
        sample_date_components["day"],
        sample_date_components["hour"],
        sample_date_components["minute"]
    )
