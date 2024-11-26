import pandas as pd
import numpy as np

def calculate_financial_score(data):
    """
    Calculate the financial score for a family based on input data.
    Args:
        data (dict): Dictionary containing financial metrics for a family.
    Returns:
        tuple: Financial score (float) and key insights (str).
    """
    income = data.get('Income', 1)  # Avoid division by zero
    savings = data.get('Savings', 0)
    expenses = data.get('Expenses', 0)
    loan_payments = data.get('Loan_Payments', 0)
    credit_card_trend = data.get('Credit_Card_Spending_Trend', 0)
    travel_entertainment_spending = data.get('Travel_Entertainment_Spending', 0)
    financial_goals_met = data.get('Financial_Goals_Met', 0)

    # Individual metrics
    savings_ratio = (savings / income) * 100
    expenses_ratio = (expenses / income) * 100
    loan_ratio = (loan_payments / income) * 100
    credit_card_penalty = abs(credit_card_trend)  # Higher deviation = penalty
    travel_penalty = max(0, (travel_entertainment_spending / income) * 100 - 20)

    # Score calculation (weighted)
    score = (
        0.3 * savings_ratio +
        0.25 * max(0, 100 - expenses_ratio) +
        0.2 * max(0, 100 - loan_ratio) +
        0.1 * max(0, 100 - credit_card_penalty) +
        0.1 * max(0, 100 - travel_penalty) +
        0.05 * financial_goals_met
    )
    score = min(max(score, 0), 100)  # Clamp score between 0 and 100

    # Generate insights
    insights = []
    if savings_ratio < 20:
        insights.append(f"Savings are low ({savings_ratio:.1f}% of income), affecting your score by 10 points.")
    if expenses_ratio > 50:
        insights.append(f"Expenses are high ({expenses_ratio:.1f}% of income), reducing your score by 15 points.")
    if loan_ratio > 30:
        insights.append(f"Loan payments are significant ({loan_ratio:.1f}% of income), impacting your score.")
    if travel_penalty > 0:
        insights.append(f"Excessive travel/entertainment spending penalizes your score by {travel_penalty:.1f} points.")
    if not insights:
        insights.append("Your financial health looks good!")

    return score, " ".join(insights)
