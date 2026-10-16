from cloudscope.incident import HealthState

def test_health_states():
    # Test that HEALTHY equals "healthy"
    assert HealthState.HEALTHY.value == "healthy"

    # Test that DEGRADED equals "degraded"
    assert HealthState.DEGRADING.value == "degraded"

    # Test that UNHEALTHY equals "unhealthy"
    assert HealthState.UNHEALTHY.value == "unhealthy"

    # Test that RECOVERING equals "recovering"
    assert HealthState.RECOVERING.value == "recovering"

    # Test that the enum contains exactly four members
    assert len(list(HealthState)) == 4