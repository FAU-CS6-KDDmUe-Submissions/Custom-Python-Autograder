# Custom grading script implemented as the default GitHub Classroom action currently has a bug
import os
import json

# Set the maximum number of points
max_points = int(os.environ["MAX_SCORE"])
print(max_points)

# Open the report.json
with open("/autograding_output/report.json", "r") as file:
    data = json.load(file)

# Get the total amount of tests that have been executed
total_tests = data.get("summary").get("total")

# If no tests have been executed, we have to create a custom results.json
if total_tests == 0:
    with open("/autograding_output/results.json", "w") as file:
        json.dump(
            {
                "version": 1,
                "status": "fail",
                "tests": [
                    {
                        "name": "Tests could not be executed",
                        "status": "fail",
                        "message": "",
                        "test_code": "pytest",
                        "task_id": 0,
                        "filename": "",
                        "line_no": 0,
                        "duration": 0,
                        "score": 0,
                    }
                ],
                "max_score": max_points,
            },
            file,
            indent=4,
        )
    exit(0)

# Compute the amount of points per test
points_per_test = max_points / total_tests

# Create a new list of results to be used in the results.json
test_results = []

# Count the total points and tests
points = 0
test_count = 0

# Access the single test results
for test in data.get("tests", []):
    # Read the important info
    nodeid = test.get("nodeid")
    outcome = test.get("outcome")

    # Increase the test count
    test_count += 1

    # Create an entry for test_results
    test_results.append(
        {
            "name": "Test " + str(test_count) + " (" + outcome + ")",
            "status": "pass" if outcome == "passed" else "fail",
            "message": outcome,
            "test_code": "pytest " + nodeid,
            "task_id": 0,
            "filename": "",
            "line_no": 0,
            "duration": 0,
            "score": points_per_test if outcome == "passed" else 0,
        }
    )

    # Add the points if passed
    if outcome == "passed":
        points += points_per_test

# Get the exitcode
exit_code = data.get("exitcode")

# Create the results.json
results = {
    "version": 1,
    "status": "pass" if exit_code == 0 else "fail",
    "tests": test_results,
    "max_score": max_points,
}

# Print the amount of points reached
print("Points: " + str(points) + "/" + str(max_points))

with open("/autograding_output/results.json", "w") as file:
    json.dump(results, file, indent=4)
