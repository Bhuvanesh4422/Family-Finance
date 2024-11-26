from flask import Flask, request, jsonify
from scoring_model import calculate_financial_score

app = Flask(__name__)

@app.route('/calculate_score', methods=['POST'])
def calculate_score():
    """
    API endpoint to calculate the financial score for a family.
    """
    try:
        # Parse input JSON data
        input_data = request.json
        if not input_data:
            return jsonify({"error": "Invalid input. Please provide proper family financial data."}), 400
        
        # Calculate financial score and insights
        score, insights = calculate_financial_score(input_data)
        
        # Return the results
        response = {
            "Financial Score": round(score, 2),
            "Insights": insights
        }
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
