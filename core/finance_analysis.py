# Finance Analysis Module

def analyze_finances(user_data):
    # Core Financial Calculations
    savings = max(0, user_data['income'] - user_data['expenses'])
    
    # Ratios
    debt_to_income_ratio = user_data['debts'] / user_data['income'] if user_data['income'] > 0 else 0
    savings_ratio = savings / user_data['income'] if user_data['income'] > 0 else 0
    expense_ratio = user_data['expenses'] / user_data['income'] if user_data['income'] > 0 else 0
    debt_to_savings_ratio = user_data['debts'] / savings if savings > 0 else 0
    
    # Capacity and Net Worth
    investment_capacity = savings * 0.5
    total_net_worth = user_data['existing_savings'] + savings - user_data['debts']
    
    # Emergency Fund Logic
    emergency_fund_target = user_data['expenses'] * 6
    emergency_fund_shortfall = max(0, emergency_fund_target - user_data['existing_savings'])
    emergency_fund_monthly = emergency_fund_shortfall / 18 # Targeted over 1.5 years
    
    # Risk-based Investment Allocation
    risk = user_data.get('risk_tolerance', 'medium').lower()
    
    if risk == "low":
        investment_allocation = {
            "High-Interest Savings / RD": investment_capacity * 0.4,
            "Debt Mutual Funds / Bonds": investment_capacity * 0.4,
            "ETFs / Balanced Funds": investment_capacity * 0.2
        }
    elif risk == "medium":
        investment_allocation = {
            "Stocks / Equity Funds": investment_capacity * 0.3,
            "ETFs / Balanced Funds": investment_capacity * 0.4,
            "Debt Mutual Funds / Bonds": investment_capacity * 0.3
        }
    elif risk == "high":
        investment_allocation = {
            "Stocks / Equity Funds": investment_capacity * 0.5,
            "ETFs / Balanced Funds": investment_capacity * 0.3,
            "Debt Mutual Funds / Bonds": investment_capacity * 0.2
        }
    else: # Default Fallback
        investment_allocation = {
            "Stocks / Equity Funds": investment_capacity * 0.3,
            "ETFs / Balanced Funds": investment_capacity * 0.4,
            "Debt Mutual Funds / Bonds": investment_capacity * 0.3
        }

    # High Debt Alert
    high_debt_alert = debt_to_income_ratio > 0.4

    return {
        "savings": savings,
        "debt_to_income_ratio": debt_to_income_ratio,
        "savings_ratio": savings_ratio,
        "expense_ratio": expense_ratio,
        "debt_to_savings_ratio": debt_to_savings_ratio,
        "investment_capacity": investment_capacity,
        "emergency_fund_target": emergency_fund_target,
        "emergency_fund_shortfall": emergency_fund_shortfall,
        "emergency_fund_monthly": emergency_fund_monthly,
        "total_net_worth": total_net_worth,
        "existing_savings": user_data['existing_savings'],
        "recommended_investment_allocation": investment_allocation,
        "high_debt_alert": high_debt_alert
    }