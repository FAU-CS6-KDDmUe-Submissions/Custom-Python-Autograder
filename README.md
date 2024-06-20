## Custom Python Autograder
### Overview
**Custom Python Autograder** is a plugin for GitHub Classroom's Autograder. It is an alternative to  https://github.com/education/autograding-python-grader which failed in many of our submissions due to many test cases being present. This implementation does not report any test codes or test outputs to the autograding reporter and is therefore able to handle much more test cases.

### Key Features
- **Automatic Grading**: Evaluate student code submissions and provide immediate feedback.
- **Customizable Test Setup**: Define pre-test setup commands and specify custom test paths.
- **Timeout Control**: Limit the runtime of tests to prevent excessive resource usage, with a maximum duration of 6 hours.
- **Scoring System**: Assign a maximum score for tests, awarding points upon successful test completion.

### Inputs

| Input Name      | Description                                                                                                     | Required |
|-----------------|-----------------------------------------------------------------------------------------------------------------|----------|
| `timeout`       | Duration (in minutes) before the test is terminated. Defaults to 10 minutes with a maximum limit of 6 hours.    | Yes      |
| `max-score`     | Points to be awarded if the test passes.                                                                        | Yes       |
| `setup-command`         | Command to execute prior to the test, typically for environment setup or dependency installation.                                                                | No       |
| `test-path`         | Only execute pytests at a specific path                                                                | No       |


### Outputs

| Output Name | Description                        |
|-------------|------------------------------------|
| `result`    | Outputs the result of the grader, indicating the success or failure of the test.  |

### Usage

1. Add the GitHub Classroom Python Grader action to your workflow.

```
name: Autograding Tests

on:
  push

jobs:
  run-tests:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout code
      uses: actions/checkout@v4
    - name: Grading
      id: grading
      uses: FAU-CS6-KDDmUe-Submissions/Custom-Python-Autograder@v1
      with:
        timeout: '15'
        max-score: '100'
        setup-command: 'pip install -r requirements.txt'
        test-path: 'tests/my_special_test.py'
    - name: Autograding Reporter
      uses: classroom-resources/autograding-grading-reporter@v1
      env:
        GRADING_RESULTS: "${{steps.grading.outputs.result}}"
      with:
        runners: grading
```