import os
import narrator

from narrator import Checkpoint
from inventory.Item import BoxSpec

class FragileBox(BoxSpec):

    def __init__(self):
        super().__init__(__file__)

def main():
    
    n = narrator.Narrator()
    n.path.change({"act": 1, "scene": 0})
    n.narrate()
    
    q = narrator.YesNoQuestion({
        "question": "Open the box?",
        "outcomes": [{"act": 1, "scene": 1}, {"act": 1, "scene": 8}]
    })
    
    n.path.change(q.ask())

    n.narrate()

    if n.path.scene == 9:
        return
    
    q = narrator.Question({
        "question": "Where will you place the `Printer.py`?",
        "responses": [
            {"choice": "living-room", "outcome": {"act": 1, "scene": 2}},
            {"choice": "dining-room", "outcome": {"act": 1, "scene": 3}},
            {"choice": "kitchen", "outcome": {"act": 1, "scene": 4}},
            {"choice": "hallway", "outcome": {"act": 1, "scene": 5}},
            {"choice": "bedroom", "outcome": {"act": 1, "scene": 6}},
            {"choice": "office", "outcome": {"act": 1, "scene": 7}}
        ]
    })

    n.path.change(q.ask())

    n.narrate()

    cwd = Checkpoint.check_flag("cwd")
    location = Checkpoint.check_flag(q.choice)

    box = FragileBox()
    box.use(action="unpack",items="Printer.py")

    os.rename(
        "Printer.py",
        f"{cwd}/{location}/Printer.py"
    )

    Checkpoint.set_flag("printer", f"{cwd}/{location}")

    print(f"🖶 >-MOVED-> {q.choice}")
    boxes_unpacked = Checkpoint.check_flag("unpacked")
    Checkpoint.set_flag("unpacked", boxes_unpacked + 1)


if __name__ == "__main__":
    main()
