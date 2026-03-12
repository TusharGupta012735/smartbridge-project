import re

def split_advice_sections(advice_text):
    """
    Splits the general AI financial advice into a dictionary of sections.
    It looks for lines ending with a colon (:) which we instructed Gemini to use as headers.
    """
    sections = {}
    current_header = "Executive Summary"
    current_content = []

    if not advice_text or "API Error" in advice_text:
        return {"Error": advice_text}

    lines = advice_text.split('\n')
    for line in lines:
        stripped_line = line.strip()
        if not stripped_line:
            continue
        
        # Identify headers: lines ending with a colon and reasonably short
        if stripped_line.endswith(':') and len(stripped_line) < 60:
            # Save the previous section before starting a new one
            if current_content:
                sections[current_header] = '\n'.join(current_content).strip()
            
            # Set the new header (removing the colon for a cleaner look)
            current_header = stripped_line[:-1]
            current_content = []
        else:
            current_content.append(line)
            
    # Don't forget to save the very last section
    if current_content:
        sections[current_header] = '\n'.join(current_content).strip()
        
    return sections

def split_goal_sections(goal_text):
    """
    Splits the goal-oriented AI plan into a dictionary.
    Since we instructed Gemini to use the same colon-header format for goals,
    we can utilize the same robust parsing logic.
    """
    return split_advice_sections(goal_text)