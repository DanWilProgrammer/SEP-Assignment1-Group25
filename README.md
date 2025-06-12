# Report for Assignment 1

## Project

Description: A command-line-based Expense Tracker that allows users to register/login, manage their expenses, set monthly budgets, and view budget charts. It uses file-based JSON storage and supports category breakdowns

Programming language: Python

## Initial tests

### Tests

*test_register_and_login:*

![image](https://github.com/user-attachments/assets/77c033c7-edd9-4eeb-b3bc-178e41187efe)

TODO: Add their code here

### Coverage of initial tests

Tool Used: coverage.py

Command Used:

- coverage run -m pytest
- coverage report -m

Initial Test Coverage (so far just Daniel at this point)
![image](https://github.com/user-attachments/assets/19d39f32-20af-44b5-95e8-d812e2613c8c)

## Coverage improvement

### Individual tests

TODO: The following is supposed to be repeated for each group member

Daniel

TODO: Test 1

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

TODO: Provide a screenshot of the new coverage results

TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

Romina

TODO: Test 1

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

TODO: Provide a screenshot of the new coverage results

TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

Adrianna

TODO: Test 1

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

TODO: Provide a screenshot of the new coverage results

TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

Elena

TODO: Test 1

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

TODO: Provide a screenshot of the new coverage results

TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

Repeat for other tests...

### Overall

TODO: Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)

TODO: Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group

## 👥 Statement of Individual Contributions

| Member              | Three functions (with links to the code)                                                                                                                                             | Initial Test                        | Other Tests                                            |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|--------------------------------------------------------|
| Elena Toderascu     | [`login`](src/main.py#L82), [`left_to_spend`](src/monthly_budget.py#L12), [`view_log_file`](src/monthly_budget.py#L76)                                                                          | `test_expense_save_and_load`        | `test_view_expenses_no_user`, `test_add_expense_flow` |
| Adriana Voinescu    | [`add_category`](src/monthly_budget.py#L142), [`total_expenses_per_category`](src/expense.py#L69), [`remove_monthly_budget`](src/monthly_budget.py#L132)                    | `test_view_budget_log_file`         | `test_remove_budget`, `test_update_budget_negative`   |
| Romina Asgari       | [`total_expenses`](src/expense.py#L48), [`average_monthly_expenses`](src/expense.py#L53), [`input_expense`](src/main.py#L100)                                                | `test_output_chart_invalid_choice`  | `test_add_duplicate_category`, `test_chart_missing_user` |
| Daniel Williamson   | [`register`](src/main.py#L73), [`login`](src/main.py#L94), [`_generate_id`](src/main.py#L69)                                                                                         | `test_register_and_login`           | `test_duplicate_registration`, `test_login_fail_case`  |
