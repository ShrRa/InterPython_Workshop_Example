"""Tests for the Patient model."""


def test_create_patient():
    from lightcurves.models import Patient

    name = 'Alice'
    p = Patient(name=name)

    assert p.name == name
