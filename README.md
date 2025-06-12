# Report for Assignment 1

## Project

Description: A command-line-based Expense Tracker that allows users to register/login, manage their expenses, set monthly budgets, and view budget charts. It uses file-based JSON storage and supports category breakdowns

Programming language: Python

## Initial tests

### Tests

*test_register_and_login: (daniel)*

[![image](https://github.com/user-attachments/assets/77c033c7-edd9-4eeb-b3bc-178e41187efe)](tests/test_main.py#L20)

TODO: Add their code here



*test_average_monthly_expenses: (Romina)*

<img width="1249" alt="Screenshot 2025-06-12 at 17 14 01" src="https://github.com/user-attachments/assets/4faca02f-8654-4c0d-adfc-935f95ae3928" />


### Coverage of initial tests

Tool Used: coverage.py

Commands Used:

- coverage run -m pytest
- coverage report -m

Initial Test Coverage (so far just Daniel at this point)
![image](https://github.com/user-attachments/assets/19d39f32-20af-44b5-95e8-d812e2613c8c)


*Initial Test Coverage (Romina)*

![image](https://github.com/user-attachments/assets/2bc9c7ea-9c36-471b-9cc1-1a7d9724540b)



## Coverage improvement

### Individual tests

TODO: The following is supposed to be repeated for each group member

Daniel

**Test:** `test_expense_save_and_load`

[![image](https://github.com/user-attachments/assets/67baca08-8f86-4616-843f-b3bc201c8e5a)](https://github.com/DanWilProgrammer/SEP-Assignment1-Group25/commit/2d1be7ca42bad5cb70354ca21d37f16535fd2fbd)

*click images to go to commit with respective test*

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

![image](https://github.com/user-attachments/assets/19d39f32-20af-44b5-95e8-d812e2613c8c)

TODO: Provide a screenshot of the new coverage results

![image](https://github.com/user-attachments/assets/49940e0e-f703-413e-b253-952ea8066b16)

TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

**Test:** `test_duplicate_registration`

[![image](https://github.com/user-attachments/assets/3d518a1f-26fc-4d57-80a1-2f3c3368e048)](https://github.com/DanWilProgrammer/SEP-Assignment1-Group25/commit/310f2e4b5f1e2307fbb7f15bf045fdff80ea102d)

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

![image](https://github.com/user-attachments/assets/49940e0e-f703-413e-b253-952ea8066b16)

TODO: Provide a screenshot of the new coverage results

![image](https://github.com/user-attachments/assets/d6c8dda3-5629-4105-9909-0c5df5285876)

Romina

TODO:
**Test:** `total_expenses`

<img width="668" alt="Screenshot 2025-06-12 at 18 07 34" src="https://github.com/user-attachments/assets/d50a0f0b-c7d2-4674-87f7-81a9b37d7a81" />


TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

<img width="660" alt="Screenshot 2025-06-12 at 18 07 42" src="https://github.com/user-attachments/assets/fb095ad5-652f-403d-bc15-fd38358ea754" />

TODO: Provide a screenshot of the new coverage results

TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

Adriana

TODO: `test_total_expenses_per_category_basic_calculation`
![image](https://github.com/user-attachments/assets/00069df2-cb96-46d7-a950-8b9b792b42db)


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
| Elena Toderascu     | [`login`](src/main.py#L82), [`left_to_spend`](src/monthly_budget.py#L12), [`view_log_file`](src/monthly_budget.py#L76)                                                                          | `TEST_TO_BE_WRITTEN`        | `TEST_TO_BE_WRITTEN`, `TEST_TO_BE_WRITTEN` |
| Adriana Voinescu    | [`add_category`](src/monthly_budget.py#L142), [`total_expenses_per_category`](src/expense.py#L69), [`remove_monthly_budget`](src/monthly_budget.py#L132)                    | `TEST_TO_BE_WRITTEN`         | `TEST_TO_BE_WRITTEN`, `TEST_TO_BE_WRITTEN`   |
| Romina Asgari       | [`total_expenses`](src/expense.py#L48), [`average_monthly_expenses`](src/expense.py#L53), [`input_expense`](src/main.py#L100)                                                | `TEST_TO_BE_WRITTEN`  | `TEST_TO_BE_WRITTEN`, `TEST_TO_BE_WRITTEN` |
| Daniel Williamson   | [`output_chart`](src/monthly_budget.py#L159), [`set_monthly_budget`](src/monthly_budget.py#L98), [`update_monthly_budget`](src/monthly_budget.py#L118)                                                                                         | `TEST_TO_BE_WRITTEN`           | `TEST_TO_BE_WRITTEN`, `TEST_TO_BE_WRITTEN`  |
