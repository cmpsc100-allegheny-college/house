import narrator
from narrator import Checkpoint
import os

n = narrator.Narrator()

def main():
    unpacked = Checkpoint.check_flag("boxes_unpacked")
    lease_printed = bool(Checkpoint.check_flag("lease_printed"))
    
    if unpacked == 5:
        n.path.change({"act": 0, "scene": 6})
        n.narrate()
        q = narrator.YesNoQuestion({
            "prompt":"Throw away the note", 
            "outcomes":[{"act": 0, "scene": 7}, {"act": 0, "scene": 8}]
        })
        n.path.change(q.ask())
        if n.path.scene == 0.7:
            os.remove("Note.py")
        n.narrate()
        return

    if bool(Checkpoint.check_flag("note_read")):
        n.path.change({"act": 0, "scene": 8})
        n.narrate()
        q = narrator.Question({
            "question": "Is there a certain section you want to read",
            "responses": [
                {"choice": "unpacking", "outcome": {"act": 0, "scene": 1}},
                {"choice": "lease", "outcome": {"act": 0, "scene": 2}},
                {"choice": "conclusion", "outcome": {"act": 0, "scene": 3}},
                {"choice": "don't read", "outcome": {"act": 0, "scene": 4}}
            ]
        })
        n.path.change(q.ask())
        n.narrate()
        return
    
    n.narrate()
    q = narrator.YesNoQuestion({
        "question": "Read the note",
        "outcomes": [{"act": 0, "scene": 1}, {"act": 0, "scene": 4}]
    })
    n.path.change(q.ask())
    n.narrate()
    if n.path.scene == 5:
        return
    while n.path.scene < 6:
        q = narrator.YesNoQuestion({
            "question": "Continue reading",
            "outcomes": [{"act": 0, "scene": n.path.scene}, {"act": 0, "scene": 4}]
        })
        n.path.change(q.ask())
        n.narrate()
        if n.path.scene == 3:
            n.narrate()
            Checkpoint.set_flag("note_read", True)
            n.narrate()
            return
        if n.path.scene == 5:
            return

if __name__ == "__main__":
    main()