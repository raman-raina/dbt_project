# DBT Project: Superstore Data Transformation

This project demonstrates how to use **dbt (Data Build Tool)** to perform SQL-based data transformations on a local **SQLite database** created from the *Superstore* dataset.

## Dataset

Use the [Superstore.csv](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) dataset from kaggle.

## Database

Use the `main.py` code to create a local SQLite database `superstore.db` from the downloaded CSV file.  
This database will be used by dbt for performing data transformations and joins.

## Path of each file

Each file should be in a specific folder for dbt to function properly.

| File | Description | Path |
|------|--------------|------|
| `dbt_project.yml` | Main dbt configuration file | `C:\Users\your_username\Desktop\dbt_project\dbt_project.yml` |
| `models\my_first_model.sql` | SQL model used for data transformation | `C:\Users\your_username\Desktop\dbt_project\models\my_first_model.sql` |
| `profiles.yml` | Connection configuration file for SQLite | `C:\Users\your_username\.dbt\profiles.yml` |

