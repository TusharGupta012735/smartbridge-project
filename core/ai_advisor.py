import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables and configure Gemini API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if api_key:
    genai.configure(api_key=api_key)
    # Using Gemini 2.0 Flash as per your project specifications
    model = genai.GenerativeModel('gemini-2.0-flash') 
else:
    model = None

# 1. AI Reasoning Module
def generate_financial_advice(user_data, analysis_data):
    if user_data.get('profile') == "Student":
        profile_prompt = "Focus on building good habits, minimizing student debt, and starting early investments."
    elif user_data.get('profile') == "Professional":
        profile_prompt = "Focus on tax optimization, wealth accumulation, and aggressive debt reduction."
    else:
        profile_prompt = "Focus on capital preservation, safe withdrawals, and risk management."

    prompt = f"""
    You are an expert financial advisor. Generate a sectioned, structured, and actionable personal finance plan.

    {profile_prompt}

    User Data:
    - Profile Type: {user_data.get('profile', 'N/A')}
    - Monthly Income: ₹{user_data.get('income', 0)}
    - Monthly Expenses: ₹{user_data.get('expenses', 0)}
    - Total Debts: ₹{user_data.get('debts', 0)}
    - Existing Savings & Investments: ₹{user_data.get('existing_savings', 0)}
    - Estimated Monthly Savings: ₹{analysis_data.get('savings', 0)}
    - Total Net Worth: ₹{analysis_data.get('total_net_worth', 0)}
    - Debt-to-Income Ratio: {analysis_data.get('debt_to_income_ratio', 0)*100:.1f}%
    - Savings Ratio: {analysis_data.get('savings_ratio', 0)*100:.2f}%
    - Financial Goals: {', '.join(user_data.get('goals', []))}
    - Risk Tolerance: {user_data.get('risk_tolerance', 'medium')}
    - Recommended Investment Allocation: {analysis_data.get('recommended_investment_allocation', {})}

    Important: The user already has ₹{user_data.get('existing_savings', 0)} in existing savings and investments.
    Consider how to best utilize these existing funds alongside new monthly savings.

    Instructions:
    - Use sections with clear headers and : (e.g., Existing Savings Utilization:, Monthly Savings Strategy:, Debt Plan:, Investment Advice:, Goal Guidance:, Budgeting & ...)
    - Include specific advice on how to utilize existing savings
    - Consider if existing savings should be used for debt repayment, emergency fund completion, or goal acceleration
    - Include short, actionable bullet points in each section
    - Tailor advice to the user's profile and risk tolerance
    - Keep tone professional and easy to follow
    - Avoid long paragraphs and executive summaries
    - Do not use markdown, tables, or bold formatting

    Output:
    - Ready-to-read actionable plan that incorporates existing savings
    """
    try:
        if model is None:
            return "Gemini model not configured. Set GEMINI_API_KEY to use AI responses."
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini API Error: {e}"

# 2. Advanced Goal Oriented plan with User Instructions
def generate_goal_plan(user_data, analysis_data, user_instructions=""):
    prompt = f"""
    You are a highly experienced and practical financial advisor. Generate a structured, actionable, and goal-specific financial plan that PRIORITIZES and STRICTLY FOLLOWS the user's specific instructions above all other considerations.

    USER'S SPECIFIC INSTRUCTIONS (MUST FOLLOW STRICTLY):
    {user_instructions}

    CRITICAL: The user's instructions above are NON-NEGOTIABLE and must be the PRIMARY FOCUS of this plan. All other financial advice must work AROUND these instructions.

    User Goal: {', '.join(user_data.get('goals', []))}
    Profile Type: {user_data.get('profile', 'N/A')}
    Monthly Income: ₹{user_data.get('income', 0)}
    Monthly Expenses: ₹{user_data.get('expenses', 0)}
    Total Debts: ₹{user_data.get('debts', 0)}
    Existing Savings & Investments: ₹{user_data.get('existing_savings', 0)}
    Estimated Monthly Savings: ₹{analysis_data.get('savings', 0)}
    Total Net Worth: ₹{analysis_data.get('total_net_worth', 0)}
    Debt-to-Income Ratio: {analysis_data.get('debt_to_income_ratio', 0)*100:.1f}%
    Savings Ratio: {analysis_data.get('savings_ratio', 0)*100:.2f}%
    Risk Tolerance: {user_data.get('risk_tolerance', 'medium')}
    Recommended Investment Allocation: {analysis_data.get('recommended_investment_allocation', {})}

    Existing Savings Available: ₹{user_data.get('existing_savings', 0)}

    MANDATORY INSTRUCTION FOLLOWING FRAMEWORK:
    1. FIRST AND FOREMOST: Implement the user's specific instruction exactly as requested
    2. SECOND: Build the entire financial plan around supporting this instruction
    3. THIRD: Adjust all other financial aspects to accommodate the instruction
    4. FOURTH: Ensure the instruction doesn't compromise basic financial security

    Instructions For Advanced Planning:
    - THE USER'S INSTRUCTION IS YOUR TOP PRIORITY - everything else is secondary
    - Create a mathematically sound plan that implements the user's instruction while maintaining financial stability
    - Calculate exact timelines, amounts, and milestones based on the instruction
    - Show how the instruction accelerates or modifies the original goal achievement
    - Provide contingency plans for potential risks introduced by the instruction
    - Be brutally honest about trade-offs and compromises required

    ORGANIZE OUTPUT INTO THESE EXACT SECTIONS WITH COLONS:

    Instruction Implementation Strategy:
    Detail exactly how the user's specific instruction will be executed step by step

    Financial Impact Analysis:
    Show how this instruction affects all aspects of finances with before/after comparisons

    Revised Goal Timeline:
    Provide exact timeline calculations showing new completion dates and milestones

    Monthly Action Plan:
    Break down monthly financial actions with specific ₹ amounts and allocations

    Resource Allocation Strategy:
    Show how existing savings and monthly income will be distributed to support the instruction

    Risk Assessment & Mitigation:
    Identify potential risks from following this instruction and provide mitigation strategies

    Progress Tracking Framework:
    Define clear metrics and checkpoints to monitor progress

    Contingency Planning:
    Provide alternative scenarios if circumstances change or challenges arise

    Key Success Metrics:
    List the specific numbers and targets that define success

    Next Immediate Actions:
    Provide the first 3-5 actions the user should take immediately

    Output Requirements:
    - Use exactly the section headers provided above with colons
    - Each section must have 3-5 clear, actionable points
    - Include specific calculations and ₹ amounts in every relevant section
    - Show mathematical formulas used for timeline calculations
    - Provide monthly breakdowns with exact dates and amounts
    - Be realistic about challenges while maintaining focus on the user's instruction
    - Use simple, direct language without financial jargon
    - Start each section immediately after the header without blank lines
    - Do not use numbering the points just bullet points
    """
    try:
        if model is None:
            return "Gemini model not configured. Set GEMINI_API_KEY to use AI responses."
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini API Error: {e}"

# 3. Chatbot Module for Any Query
def finance_chatbot_response(user_data, analysis_data, user_query):
    prompt = f"""
    You are a professional, highly knowledgeable, and practical financial advisor. Respond to the user's question with clear, actionable, and personalized advice based on their financial details.

    User Profile Details:
    - Profile Type: {user_data.get('profile', 'N/A')}
    - Monthly Income: ₹{user_data.get('income', 0)}
    - Monthly Expenses: ₹{user_data.get('expenses', 0)}
    - Total Debts: ₹{user_data.get('debts', 0)}
    - Existing Savings & Investments: ₹{user_data.get('existing_savings', 0)}
    - Estimated Monthly Savings: ₹{analysis_data.get('savings', 0)}
    - Total Net Worth: ₹{analysis_data.get('total_net_worth', 0)}
    - Debt-to-Income Ratio: {analysis_data.get('debt_to_income_ratio', 0):.2f}
    - Savings Ratio: {analysis_data.get('savings_ratio', 0):.2f}
    - Risk Tolerance: {user_data.get('risk_tolerance', 'medium')}
    - Recommended Investment Allocation: {analysis_data.get('recommended_investment_allocation', {})}
    - Financial Goals: {', '.join(user_data.get('goals', []))}

    User Question: {user_query}

    Instructions for response:
    - First, determine if the question is related to finance, budgeting, savings, debts, investments, or financial goals.
      - If unrelated, respond politely: "I'm a financial advisor, so I can best answer questions about budgeting, savings, debts, investments, and financial planning."
    - Just answer the question don not add any extra info.
    - Tailor the response specifically to the user's financial profile, risk tolerance, and goals.
    - If the question includes a financial term or abbreviation (e.g., SIP, ROI), briefly define it and explain how it may relate to the user's financial situation.
    - Provide 3-5 actionable points tailored to the user's profile and goals.
    - Include numeric suggestions whenever relevant (e.g., amounts to save, invest, or allocate).
    - Consider how existing savings can be utilized in the response
    - Keep the tone professional, friendly, and concise.
    - Use bullet points or numbered steps; avoid long paragraphs.
    - Reference the user's profile, savings, risk tolerance, and goals only if it adds value.
    - Make the answer practical, easy to follow, and directly helpful for financial decision-making.
    - Don not use BOLD words, any markdown formatting along with tables, long paragraphs, and special characters(e.g. _, -, +, *).

    Output:
    - Clear, actionable, and personalized financial advice.
    """
    try:
        if model is None:
            return "Gemini model not configured. Set GEMINI_API_KEY to use AI responses."
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Gemini API Error: {e}"