USER_PROMPT_TEMPLATE = """
Usability Criterion ID: {criterion_id}

Usability Criterion: {criterion}

Evaluation Instructions:
Evaluate the interface for the criterion listed above. Follow these steps:
1. Identify any usability issues related to the criterion and explain each issue.
2. Provide a practical, actionable recommendation to fix each issue.
3. Assign severity using this exact scale:
    - 1: Cosmetic problem only
    - 2: Minor usability problem
    - 3: Major usability problem
    - 4: Usability catastrophe

Response Guideline:
Keep each issue’s analysis and recommendation concise (1–3 sentences).
Avoid restating the criterion definition.
Return only valid JSON (no markdown, no commentary) using this exact shape:
{{"issues": [{{"description": "...", "recommendation": "...", "severity": 2}}]}}
Each issue object must include all keys: description, recommendation, severity.
Severity must be an integer in [1, 4].
If no issues are found, return exactly: {{"issues": []}}
Before finalizing, verify no issue object is missing any required key.
""".strip()


def get_user_prompt(criterion_id: str, criterion: str) -> str:
    """Get the user prompts with included variables.

    Args:
        criterion_id: The criterion ID
        criterion: The criterion description

    Returns:
        user_prompt
    """
    user_prompt = USER_PROMPT_TEMPLATE.format(
        criterion_id=criterion_id,
        criterion=criterion,
    )
    return user_prompt
