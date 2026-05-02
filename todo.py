import json
from pathlib import Path

DATA_FILE = Path("tasks.json")


def load_tasks() -> list[dict]:
    """Load tasks from the JSON file."""
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return []


def save_tasks(tasks: list[dict]) -> None:
    """Save tasks to the JSON file."""
    DATA_FILE.write_text(json.dumps(tasks, indent=2))


def add_task(description: str) -> None:
    """Add a new task."""
    tasks = load_tasks()
    tasks.append({"description": description, "done": False})
    save_tasks(tasks)
    print(f"✅ Added: {description}")


def list_tasks() -> None:
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet. Add one with: python todo.py add 'Your task'")
        return

    print("\n📋 Your Tasks:\n")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["done"] else "○"
        print(f"  {i}. [{status}] {task['description']}")
    print()


def complete_task(index: int) -> None:
    """Mark a task as completed."""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        tasks[index - 1]["done"] = True
        save_tasks(tasks)
        print(f"✅ Completed: {tasks[index - 1]['description']}")
    else:
        print(f"❌ Invalid task number: {index}")


def delete_task(index: int) -> None:
    """Delete a task."""
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"🗑️  Deleted: {removed['description']}")
    else:
        print(f"❌ Invalid task number: {index}")


def main() -> None:
    import sys

    if len(sys.argv) < 2:
        list_tasks()
        return

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) >= 3:
        add_task(" ".join(sys.argv[2:]))
    elif command == "list":
        list_tasks()
    elif command == "done" and len(sys.argv) == 3:
        complete_task(int(sys.argv[2]))
    elif command == "delete" and len(sys.argv) == 3:
        delete_task(int(sys.argv[2]))
    else:
        print("Usage:")
        print("  python todo.py              - List all tasks")
        print("  python todo.py add <task>   - Add a task")
        print("  python todo.py done <num>   - Mark task as done")
        print("  python todo.py delete <num> - Delete a task")


if __name__ == "__main__":
    main()
