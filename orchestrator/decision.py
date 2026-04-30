def decide_mode(eval_data):
    avg = (
        eval_data["clarity"]
        + eval_data["depth"]
        + eval_data["correctness"]
        + eval_data["communication"]
    ) / 4

    if eval_data["followup_needed"]:
        return "followup"
    elif avg > 7:
        return "increase_difficulty"
    else:
        return "normal"
