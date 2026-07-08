import pytest
from task import add_task, show_tasks


@pytest.fixture
def empty_plan():
    """Fixture to provide an empty list for tests."""
    return []


def test_add_task(monkeypatch):
    """Test adding a task by mocking user input."""
    plan = []
    # Mock inputs: first time, then description
    inputs = iter(['10:00', 'Morning workout'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    add_task(plan)

    assert len(plan) == 1
    assert plan[0] == {"time": "10:00", "task": "Morning workout"}


def test_show_tasks_empty(capsys):
    """Test output when the task list is empty."""
    show_tasks([])
    captured = capsys.readouterr()
    assert "Your plan for today is currently empty." in captured.out


def test_show_tasks_sorting(capsys):
    """Test that tasks are sorted by time."""
    plan = [
        {"time": "14:00", "task": "Meeting"},
        {"time": "09:00", "task": "Breakfast"}
    ]
    show_tasks(plan)
    captured = capsys.readouterr()

    # Verify chronological order in output
    output = captured.out
    assert output.find("09:00") < output.find("14:00")
