def grade(vars):
    score = 0
    total = 2
    feedback = {}

    # Q1: function test
    try:
        if callable(vars.get('square')) and vars['square'](2) == 4:
            score += 1
            feedback['Q1'] = "✅ Correct"
        else:
            feedback['Q1'] = "❌ Incorrect result for square(2)"
    except Exception as e:
        feedback['Q1'] = f"❌ Error: {e}"

    # Q2: simple text match
    ans2 = str(vars.get('answer_q2', '')).strip().lower()
    if "list" in ans2:
        score += 1
        feedback['Q2'] = "✅ Correct"
    else:
        feedback['Q2'] = "❌ Expected 'list'"

    percent = (score / total) * 100
    return {"score": score, "total": total, "percent": percent, "feedback": feedback}
