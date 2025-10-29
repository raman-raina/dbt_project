# ELT Project: Superstore Dataset

This project demonstrates a complete ELT (Extract, Load, Transform) pipeline on the *Superstore* dataset.

## Pipeline

1. **Extract**

The *Superstore* dataset is extracted from **AWS S3** using **Snowflake**. This is done by creating a *STAGE* in an SQL worksheet in Snowflake.

2. **Load**

The dataset is then loaded into Snowflake by using *COPY INTO*. Hence, the dataset is now stored in Snowflake as a table.

3. **Transform**

SQL-based data transformantion is applied on the stored dataset using **dbt (data build tool)**.

## Dataset

Use the [Superstore.csv](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) dataset from kaggle.

## Database

Use the `main.py` code to create a local SQLite database `superstore.db` from the downloaded CSV file.  
This database will be used by dbt for performing data transformations and joins.

## Path of each file

Each file should be in a specific folder for dbt to function properly.

| File | Description | Path |
|------|--------------|------|
| `dbt_project.yml` | Main dbt configuration file | `C:\Users\your_username\Desktop\dbt_project\` |
| `models\my_first_model.sql` | SQL model used for data transformation | `C:\Users\your_username\Desktop\dbt_project\models\` |
| `profiles.yml` | Connection configuration file for SQLite | `C:\Users\your_username\.dbt\` |
