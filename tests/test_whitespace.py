# coding: utf-8
"""A few simple tests for normalization of whitespace."""
# pylint: disable=protected-access,too-many-public-methods,no-self-use,too-few-public-methods,redefined-outer-name
from __future__ import unicode_literals

import pytest

from cleanliness import normalize_whitespace


class TestWhitespace(object):
    """Test class for whitespace normalization."""

    @pytest.mark.parametrize("test_input,expected", [
        ("This\ntext\ncontains\nmultiple\n\nnewlines", "This\ntext\ncontains\nmultiple\nnewlines"),
        ("This\ttext\tcontains\ttabs.", "This text contains tabs."),
        ("This\ntext\tcontains  odd\n\t whitespace.", "This\ntext contains odd\nwhitespace.")
    ])
    def test_rules(self, test_input, expected):
        """Test splitting of full form to prefix and suffix."""
        actual = normalize_whitespace(test_input)
        assert actual == expected
