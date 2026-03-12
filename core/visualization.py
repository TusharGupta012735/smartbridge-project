import matplotlib.pyplot as plt
import seaborn as sns

# Visualization: Detailed Advised Financial Health
def plot_advised_financial_overview(user_data, analysis_data):
    
    # Extract calculated values
    expenses = user_data.get("expenses", 0)
    savings = analysis_data.get("savings", 0)
    emergency_fund_monthly = analysis_data.get("emergency_fund_monthly", 0)
    
    investment_allocation = analysis_data.get("recommended_investment_allocation", {})
    high_interest = investment_allocation.get("High-Interest Savings / RD", 0)
    stocks = investment_allocation.get("Stocks / Equity Funds", 0)
    etfs = investment_allocation.get("ETFs / Balanced Funds", 0)
    risk_free = investment_allocation.get("Debt Mutual Funds / Bonds", 0)
    
    total_investments = high_interest + stocks + etfs + risk_free
    remaining_savings = max(0, savings - (emergency_fund_monthly + total_investments))
    
    # Setup Labels and Values, filtering out zero amounts for cleaner charts
    all_labels = ["Expenses", "Emergency Fund", "High-Interest / RD", "Stocks / Equity", "ETFs / Balanced", "Debt / Bonds", "Unallocated Savings"]
    all_values = [expenses, emergency_fund_monthly, high_interest, stocks, etfs, risk_free, remaining_savings]
    
    labels = [l for l, v in zip(all_labels, all_values) if v > 0]
    values = [v for l, v in zip(all_labels, all_values) if v > 0]
    
    # Styling setup
    colors = sns.color_palette("pastel", len(values))
    fig, ax = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor("#F9FAFB")
    
    # 1. Pie Chart: Savings & Investment Distribution
    wedges, texts, autotexts = ax[0].pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
    ax[0].set_title("Savings & Investment Distribution", pad=35, fontweight="bold", fontsize=11, color="#222222")
    
    # 2. Bar Chart: Component-wise Financial Impact
    sns.set_style("whitegrid")
    sns.barplot(x=labels, y=values, ax=ax[1], palette="pastel", hue=labels, legend=False)
    ax[1].set_facecolor("#FFFFFF")
    ax[1].grid(axis="y", linestyle="--", alpha=0.5)
    ax[1].set_ylabel("Amount (₹)", fontsize=10, fontweight="bold", color="#222222")
    ax[1].tick_params(axis="x", rotation=45, labelsize=9)
    ax[1].set_title("Component-wise Financial Impact", pad=35, fontweight="bold", fontsize=11, color="#222222")
    
    # Add text numbers on top of the bars
    for i, value in enumerate(values):
        ax[1].text(i, value + (max(values)*0.02), f"₹{int(value)}", ha='center', va='bottom', fontsize=9, color="#222222")
        
    plt.tight_layout(rect=[0.05, 0.1, 0.95, 0.95])
    plt.subplots_adjust(wspace=0.4)
    
    return fig