import agent.performance as performance

def test_get_cpu_usage(monkeypatch):
    def fake_cpu_percent(interval):
        assert interval == 1
        return 42.5

    monkeypatch.setattr(
        performance.psutil,
        "cpu_percent",
        fake_cpu_percent
    )

    result = performance.get_cpu_usage()

    assert isinstance(result, float)
    assert 0 <= result <= 100
    assert result == 42.5