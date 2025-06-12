# Report for Assignment 1

## Project

Description: A command-line-based Expense Tracker that allows users to register/login, manage their expenses, set monthly budgets, and view budget charts. It uses file-based JSON storage and supports category breakdowns

Programming language: Python

## Initial tests

### Tests

*test_register_and_login: (daniel)*

[![image](https://github.com/user-attachments/assets/77c033c7-edd9-4eeb-b3bc-178e41187efe)](tests/test_main.py#L20)

*ttest_total_expenses: (Romina)*

![image](https://github.com/user-attachments/assets/f0bb743e-5e0a-4c15-a29d-1573d78e49ab)


*test_left_to_spend: (Elena)*

![image](https://github.com/user-attachments/assets/d60fb46d-3eef-42ce-8e0d-9b87c1a2dd87)

*test_total_expenses_per_category_basic_calculation: (Adriana)*
![image](https://github.com/user-attachments/assets/2f5cfdab-93a5-415d-b74a-26362cd6665a)

### Coverage of initial tests

Tool Used: coverage.py

Commands Used:

- coverage run -m pytest
- coverage report -m

Initial Test Coverage (This should be the last image as this is after the inital test from Adriana)
![Afbeelding van WhatsApp op 2025-06-12 om 21 59 54_82666882](https://github.com/user-attachments/assets/2e85ee15-1892-4613-9034-90497c7ca631)



## Coverage improvement

### Individual tests

TODO: The following is supposed to be repeated for each group member

Daniel

**Test 1:** `test_expense_save_and_load`

[![image](https://github.com/user-attachments/assets/67baca08-8f86-4616-843f-b3bc201c8e5a)](https://github.com/DanWilProgrammer/SEP-Assignment1-Group25/commit/2d1be7ca42bad5cb70354ca21d37f16535fd2fbd)

*click images to go to commit with respective test*

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

![image](https://github.com/user-attachments/assets/19d39f32-20af-44b5-95e8-d812e2613c8c)

TODO: Provide a screenshot of the new coverage results

![image](https://github.com/user-attachments/assets/49940e0e-f703-413e-b253-952ea8066b16)

TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

**Test 2:** `test_duplicate_registration`

[![image](https://github.com/user-attachments/assets/3d518a1f-26fc-4d57-80a1-2f3c3368e048)](https://github.com/DanWilProgrammer/SEP-Assignment1-Group25/commit/310f2e4b5f1e2307fbb7f15bf045fdff80ea102d)

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

![image](https://github.com/user-attachments/assets/49940e0e-f703-413e-b253-952ea8066b16)

TODO: Provide a screenshot of the new coverage results

![image](https://github.com/user-attachments/assets/d6c8dda3-5629-4105-9909-0c5df5285876)

Romina

TODO:
**Test 1:** `total_expenses`

<img width="668" alt="Screenshot 2025-06-12 at 18 07 34" src="https://github.com/user-attachments/assets/d50a0f0b-c7d2-4674-87f7-81a9b37d7a81" />


TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

![image](https://github.com/user-attachments/assets/07e4ed37-f2a8-4c56-aef4-bc814e6c8b7e)


TODO: Provide a screenshot of the new coverage results

<img width="660" alt="Screenshot 2025-06-12 at 18 07 42" src="https://github.com/user-attachments/assets/fb095ad5-652f-403d-bc15-fd38358ea754" />

TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

**Test 2:** `input_expenses`

 <img width="737" alt="Screenshot 2025-06-12 at 19 18 15" src="https://github.com/user-attachments/assets/4a0cd644-5138-4a3f-a9b9-ed0daee29d75" />

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)


<img width="660" alt="Screenshot 2025-06-12 at 18 07 42" src="https://github.com/user-attachments/assets/fb095ad5-652f-403d-bc15-fd38358ea754" />


TODO: Provide a screenshot of the new coverage results


<img width="552" alt="Screenshot 2025-06-12 at 20 15 23" src="https://github.com/user-attachments/assets/799a0a8d-2e8e-493f-87fa-52bdd8136686" />


Adriana

TODO: `test_RemoveMonthlyBudget_BudgetExists_BudgetIsZero`
![image](https://github.com/user-attachments/assets/17e0ebc1-9890-4b26-96a9-184f067f5a3b)




TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)
![image](https://github.com/user-attachments/assets/f2389064-81c7-4026-973e-5e4087e24808)


TODO: Provide a screenshot of the new coverage results
![image](https://github.com/user-attachments/assets/f73ae108-860a-4b4c-a98f-263ce672c6c0)


TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

Elena

TODO: `test_view_log_file`

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

![Afbeelding van WhatsApp op 2025-06-12 om 20 21 31_83b6500c](https://github.com/user-attachments/assets/b9828f07-237d-4c53-8fa5-86af5d05cbde)

TODO: Provide a screenshot of the new coverage results

![Afbeelding van WhatsApp op 2025-06-12 om 21 47 33_0ea1d671](https://github.com/user-attachments/assets/f78e6ec3-581d-438b-a118-c119552f2835)

TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

TODO: `test_monthly_budget`

TODO: Show a patch (diff) or a link to a commit made in your repository that shows the new test

TODO: Provide a screenshot of the old coverage results (the same as you already showed above)

![Afbeelding van WhatsApp op 2025-06-12 om 21 47 33_0ea1d671](https://github.com/user-attachments/assets/f78e6ec3-581d-438b-a118-c119552f2835)

TODO: Provide a screenshot of the new coverage results

![image](https://github.com/user-attachments/assets/5838a404-5839-4d1d-bd28-52e511a977f7)

TODO: State the coverage improvement with a number and elaborate on why the coverage is improved

Repeat for other tests...

### Overall

TODO: Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)

TODO: Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group

## 👥 Statement of Individual Contributions

| Member              | Three functions (with links to the code)                                                                                                                                             | Initial Test                        | Other Tests                                            |
|---------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------|--------------------------------------------------------|
| Elena Toderascu     | [`login`](src/main.py#L82), [`left_to_spend`](src/monthly_budget.py#L12), [`view_log_file`](src/monthly_budget.py#L76)                                                                          | `test_left_to_spend`        | `test_view_log_file`, `test_monthly_budget_functions` |
| Adriana Voinescu    | [`add_category`](src/monthly_budget.py#L142), [`total_expenses_per_category`](src/expense.py#L69), [`remove_monthly_budget`](src/monthly_budget.py#L132)                    | `test_total_expenses_per_category_basic_calculation`         | `test_total_expenses_per_category_single_new_category`, `test_RemoveMonthlyBudget_BudgetExists_BudgetIsZero`   |
| Romina Asgari       | [`total_expenses`](src/expense.py#L48), [`average_monthly_expenses`](src/expense.py#L53), [`input_expense`](src/main.py#L100)                                                | `test_average_monthly_expenses`  | `test_total_expenses`, `test_input_expenses` |
| Daniel Williamson   | [`output_chart`](src/monthly_budget.py#L159), [`set_monthly_budget`](src/monthly_budget.py#L98), [`update_monthly_budget`](src/monthly_budget.py#L118)                                                                                         | `test_register_and_login`           | `test_expense_save_and_load`, `test_duplicate_registration`  |
