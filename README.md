# 📊 Assignment 1 Report
**Software Engineering Practices - Group 25**

---

## 🚀 Project Overview

> **Expense Tracker** - A comprehensive command-line application for personal finance management

| Aspect | Details |
|--------|---------|
| **Description** | Command-line-based Expense Tracker with user authentication, expense management, budget tracking, and visual analytics |
| **Language** | Python |
| **Storage** | File-based JSON storage |
| **Features** | User registration/login, expense categorization, monthly budgets, budget visualization |

---

## 🧪 Initial Test Suite

### Core Test Functions

#### 🔐 **Authentication Testing** *(Daniel)*
**Test:** `test_register_and_login`

[![Test Implementation](https://img.shields.io/badge/View%20Code-GitHub-blue?style=for-the-badge&logo=github)](tests/test_main.py#L20)

![Test Screenshot](https://github.com/user-attachments/assets/77c033c7-edd9-4eeb-b3bc-178e41187efe)

#### 💰 **Expense Calculation Testing** *(Romina)*
**Test:** `test_total_expenses`

![Test Screenshot](https://github.com/user-attachments/assets/f0bb743e-5e0a-4c15-a29d-1573d78e49ab)

#### 📈 **Budget Analysis Testing** *(Elena)*
**Test:** `test_left_to_spend`

![Test Screenshot](https://github.com/user-attachments/assets/d60fb46d-3eef-42ce-8e0d-9b87c1a2dd87)

#### 📊 **Category Analytics Testing** *(Adriana)*
**Test:** `test_total_expenses_per_category_basic_calculation`

![Test Screenshot](https://github.com/user-attachments/assets/2f5cfdab-93a5-415d-b74a-26362cd6665a)

### 📋 Initial Coverage Analysis

**Tool:** `coverage.py`

**Commands:**
```bash
coverage run -m pytest
coverage report -m
```

**Baseline Coverage Results:**

![Before](https://github.com/user-attachments/assets/19d39f32-20af-44b5-95e8-d812e2613c8c)
---

## 📈 Coverage Improvement Analysis

### 👨‍💻 Daniel Williamson

#### ✅ **Test 1:** `test_expense_save_and_load`

[![View Commit](https://img.shields.io/badge/View%20Commit-GitHub-green?style=flat-square&logo=github)](https://github.com/DanWilProgrammer/SEP-Assignment1-Group25/commit/2d1be7ca42bad5cb70354ca21d37f16535fd2fbd)

**Before Coverage:**
![Before](https://github.com/user-attachments/assets/19d39f32-20af-44b5-95e8-d812e2613c8c)

**After Coverage:**
![After](https://github.com/user-attachments/assets/49940e0e-f703-413e-b253-952ea8066b16)

**Coverage Improvement:** *[Percentage to be calculated]*
- Enhanced testing of file I/O operations for expense data persistence

#### ✅ **Test 2:** `test_duplicate_registration`

[![View Commit](https://img.shields.io/badge/View%20Commit-GitHub-green?style=flat-square&logo=github)](https://github.com/DanWilProgrammer/SEP-Assignment1-Group25/commit/310f2e4b5f1e2307fbb7f15bf045fdff80ea102d)

**Before Coverage:**
![Before](https://github.com/user-attachments/assets/49940e0e-f703-413e-b253-952ea8066b16)

**After Coverage:**
![After](https://github.com/user-attachments/assets/d6c8dda3-5629-4105-9909-0c5df5285876)

**Coverage Improvement:** *[Percentage to be calculated]*
- Improved validation testing for user registration edge cases

---

### 👩‍💻 Romina Asgari

#### ✅ **Test 1:** `test_average_monthly_expenses`

![Test Implementation](https://github.com/user-attachments/assets/22c53da5-755b-4049-aa19-04c69b637ee8)

**Before Coverage:**
![Before](https://github.com/user-attachments/assets/f97f3b83-8726-450f-b81f-8ae9b666a649)

**After Coverage:**
![After](https://github.com/user-attachments/assets/4bde0b98-d3ac-4955-be38-b38edb0d601d)

**Coverage Improvement:** *[Percentage to be calculated]*
- Enhanced testing of monthly expense calculation algorithms

#### ✅ **Test 2:** `test_input_expenses`

![Test Implementation](https://github.com/user-attachments/assets/c84b1ff1-f735-4593-b60a-0a8d431906d6)

**Before Coverage:**
![Before](https://github.com/user-attachments/assets/69510d0b-c03d-4b54-8d36-b4111132cdb1)

**After Coverage:**
![After](https://github.com/user-attachments/assets/799a0a8d-2e8e-493f-87fa-52bdd8136686)

**Coverage Improvement:** *[Percentage to be calculated]*
- Improved testing of expense input validation and processing

---

### 👩‍💻 Adriana Voinescu

#### ✅ **Test 1:** `test_RemoveMonthlyBudget_BudgetExists_BudgetIsZero`

![Test Implementation](https://github.com/user-attachments/assets/17e0ebc1-9890-4b26-96a9-184f067f5a3b)

**Before Coverage:**
![Before](https://github.com/user-attachments/assets/f2389064-81c7-4026-973e-5e4087e24808)

**After Coverage:**
![After](https://github.com/user-attachments/assets/f73ae108-860a-4b4c-a98f-263ce672c6c0)

**Coverage Improvement:** *[Percentage to be calculated]*
- Enhanced testing of budget removal functionality and edge cases

#### ✅ **Test 2:** `test_total_expenses_per_category_single_new_category`

![Test Implementation](https://github.com/user-attachments/assets/a7964086-f8ea-427d-a866-d632b81598cc)

**Before Coverage:**
![After](https://github.com/user-attachments/assets/f73ae108-860a-4b4c-a98f-263ce672c6c0)

**After Coverage:**
![image](https://github.com/user-attachments/assets/d15daea2-daf2-4d82-a368-23eacbd4edbf)

**Coverage Improvement:** *[Percentage to be calculated]*
- Improved testing of category-based expense analysis

---

### 👩‍💻 Elena Toderascu

#### ✅ **Test 1:** `test_view_log_file`

**Before Coverage:**
![Before](https://github.com/user-attachments/assets/b9828f07-237d-4c53-8fa5-86af5d05cbde)

**After Coverage:**
![After](https://github.com/user-attachments/assets/f78e6ec3-581d-438b-a118-c119552f2835)

**Coverage Improvement:** *[Percentage to be calculated]*
- Enhanced testing of log file viewing and data retrieval functionality

#### ✅ **Test 2:** `test_monthly_budget`

**Before Coverage:**
![Before](https://github.com/user-attachments/assets/f78e6ec3-581d-438b-a118-c119552f2835)

**After Coverage:**
![After](https://github.com/user-attachments/assets/5838a404-5839-4d1d-bd28-52e511a977f7)

**Coverage Improvement:** *[Percentage to be calculated]*
- Improved testing of monthly budget management features

---

## 📊 Overall Coverage Summary

### Before vs After Comparison

| Metric | Initial Coverage | Final Coverage | Improvement |
|--------|------------------|----------------|-------------|
| **Line Coverage** | *[To be filled]* | *[To be filled]* | *[To be calculated]* |
| **Branch Coverage** | *[To be filled]* | *[To be filled]* | *[To be calculated]* |
| **Function Coverage** | *[To be filled]* | *[To be filled]* | *[To be calculated]* |

**Final Coverage Screenshot:**
*[Comprehensive coverage report to be added]*

---

## 👥 Individual Contributions

<table>
<thead>
<tr>
<th>👤 Team Member</th>
<th>🔧 Functions Implemented</th>
<th>🧪 Initial Test</th>
<th>✅ Additional Tests</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Elena Toderascu</strong></td>
<td>
• <a href="src/main.py#L82"><code>login</code></a><br>
• <a href="src/monthly_budget.py#L12"><code>left_to_spend</code></a><br>
• <a href="src/monthly_budget.py#L76"><code>view_log_file</code></a>
</td>
<td><code>test_left_to_spend</code></td>
<td>
• <code>test_view_log_file</code><br>
• <code>test_monthly_budget_functions</code>
</td>
</tr>
<tr>
<td><strong>Adriana Voinescu</strong></td>
<td>
• <a href="src/monthly_budget.py#L142"><code>add_category</code></a><br>
• <a href="src/expense.py#L69"><code>total_expenses_per_category</code></a><br>
• <a href="src/monthly_budget.py#L132"><code>remove_monthly_budget</code></a>
</td>
<td><code>test_total_expenses_per_category_basic_calculation</code></td>
<td>
• <code>test_total_expenses_per_category_single_new_category</code><br>
• <code>test_RemoveMonthlyBudget_BudgetExists_BudgetIsZero</code>
</td>
</tr>
<tr>
<td><strong>Romina Asgari</strong></td>
<td>
• <a href="src/expense.py#L48"><code>total_expenses</code></a><br>
• <a href="src/expense.py#L53"><code>average_monthly_expenses</code></a><br>
• <a href="src/main.py#L100"><code>input_expense</code></a>
</td>
<td><code>test_average_monthly_expenses</code></td>
<td>
• <code>test_total_expenses</code><br>
• <code>test_input_expenses</code>
</td>
</tr>
<tr>
<td><strong>Daniel Williamson</strong></td>
<td>
• <a href="src/monthly_budget.py#L159"><code>output_chart</code></a><br>
• <a href="src/monthly_budget.py#L98"><code>set_monthly_budget</code></a><br>
• <a href="src/monthly_budget.py#L118"><code>update_monthly_budget</code></a>
</td>
<td><code>test_register_and_login</code></td>
<td>
• <code>test_expense_save_and_load</code><br>
• <code>test_duplicate_registration</code>
</td>
</tr>
</tbody>
</table>

---
