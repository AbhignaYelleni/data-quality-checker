import pandas as pd

def validate_columns(df, required_columns):
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        print(f"Missing columns: {', '.join(missing_columns)}")
    else:
        print("All required columns are present.")

def validate_dtypes(df, required_columns):
    for col, dtype in required_columns.items():
        if not pd.api.types.is_dtype_equal(df[col].dtype, dtype):
            print(f"Column '{col}' has incorrect dtype. Expected {dtype}, got {df[col].dtype}.")
        else:
            print(f"Column '{col}' has correct dtype.")
