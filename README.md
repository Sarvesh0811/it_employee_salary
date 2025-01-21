# Employee Data Dataset

## Overview

The `employee_data.csv` dataset contains simulated data of employees working in various IT-related positions. This dataset includes details about each employee's gender, years of experience, position, and salary. It was generated using the Python Faker library, providing realistic fake data to reflect real-world distributions and trends in the IT industry, particularly salary variations based on job roles and experience.

## Dataset Description

The dataset contains the following columns:

1. **ID**: A unique identifier for each employee.
2. **Gender**: The gender of the employee. Possible values: `'M'` (Male) or `'F'` (Female).
3. **Experience (Years)**: The number of years of professional experience the employee has, ranging from 0 to 20 years.
4. **Position**: The job title of the employee. Possible values include:
   - IT Manager
   - Software Engineer
   - Network Administrator
   - Systems Administrator
   - Database Administrator (DBA)
   - Web Developer
   - IT Support Specialist
   - Systems Analyst
   - IT Security Analyst
   - DevOps Engineer
   - Cloud Solutions Architect
5. **Salary**: The annual salary of the employee in USD. The salary increases with both the position and years of experience.

### Sample Data

| ID  | Gender | Experience (Years) | Position                | Salary   |
| --- | ------ | ------------------- | ----------------------- | -------- |
| 1   | M      | 5                   | Software Engineer       | 84,000   |
| 2   | F      | 10                  | IT Manager              | 135,000  |
| 3   | M      | 7                   | Network Administrator   | 85,000   |
| 4   | F      | 15                  | Cloud Solutions Architect | 147,000  |
| 5   | M      | 2                   | Web Developer           | 60,000   |

## Applications

This dataset can be utilized for various purposes, such as:

- **Data Analysis**: Analyzing salary trends based on position and years of experience.
- **Machine Learning**: Training models for salary prediction based on employee attributes (experience, position, etc.).
- **Human Resources**: Understanding compensation structures in the IT industry and making data-driven decisions regarding salaries.
- **Education**: Using this dataset as a teaching tool in data science, machine learning, and data analysis courses.

## Usage

You can download and use the dataset for various analyses, visualizations, and machine learning projects. The dataset provides a realistic overview of how experience and job roles influence salaries in the IT sector.
