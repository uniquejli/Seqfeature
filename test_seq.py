import bioinfo_dicts
import seq
import pytest

def test_n_neg_for_single_E_or_D():
    """Perform unit tests on n_neg."""

    assert seq.n_neg('E') == 1
    assert seq.n_neg('D') == 1

def test_n_neg_for_empty_sequence():
    assert seq.n_neg('') == 0

def test_n_neg_for_longer_sequences():
    assert seq.n_neg('ACKLWTTAE') == 1
    assert seq.n_neg('DDDDEEEE') == 8

def test_n_neg_for_lower_case_sequences():
    assert seq.n_neg('acklwttae') == 1

def test_n_neg_for_invalid_amino_acid():
    with pytest.raises(RuntimeError) as excinfo:
        seq.n_neg('Z')
    excinfo.match("Z is not a valid amino acid")
