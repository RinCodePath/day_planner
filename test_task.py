import pytest
from task import add_task, show_tasks, Task, parse_time, save_plan, load_plan


def test_parse_time_valid():
    assert parse_time("09:00") == "09:00"
    assert parse_time("23:59") == "23:59"


def test_parse_time_invalid():
    with pytest.raises(ValueError):
        parse_time("99:99")
    with pytest.raises(ValueError):
        parse_time("not-a-time")


def test_save_and_load(tmp_path):
    tasks = [Task(time="09:00", task="Breakfast"), Task(time="13:30", task="Meeting")]
    path = tmp_path / "plan.json"
    save_plan(str(path), tasks)

    loaded = load_plan(str(path))
    assert loaded == tasks


def test_add_task(monkeypatch):
    plan = []
    inputs = iter(["10:00", "Morning workout"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    add_task(plan)

    assert len(plan) == 1
    assert plan[0] == Task(time="10:00", task="Morning workout")


def test_show_tasks_empty(capsys):
    show_tasks([])
    captured = capsys.readouterr()
    assert "Your plan for today is currently empty." in captured.out


def test_show_tasks_sorting(capsys):
    plan = [Task(time="14:00", task="Meeting"), Task(time="09:00", task="Breakfast")]
    show_tasks(plan)
    captured = capsys.readouterr()
    output = captured.out
    assert output.find("09:00") < output.find("14:00")