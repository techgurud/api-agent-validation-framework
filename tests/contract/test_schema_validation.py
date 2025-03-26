import json
from helpers.api_utils import compare_responses

def evaluate_json_response(expected_response, actual_response):
    """
    Evaluates the JSON response by comparing the expected and actual responses.

    Args:
        expected_response (dict): The expected JSON response.
        actual_response (dict): The actual JSON response.

    Returns:
        dict: A dictionary containing the comparison result and any differences.
    """
    try:
        # Perform the comparison using the utility function
        comparison_result = compare_responses(expected_response, actual_response)

        # Return the result
        return {
            "success": comparison_result["success"],
            "differences": comparison_result.get("differences", [])
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }