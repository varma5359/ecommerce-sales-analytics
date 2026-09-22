'''
What is Data Cleaning?
-----------------------
Think of it like washing vegetables before cooking:

Validation = looking at vegetables, spotting the dirty ones

Cleaning = actually washing them

We will:
---------
Remove duplicate orders

Handle missing values

Remove invalid rows (bad quantity, price, discount)

Convert dates properly

Add new helpful columns

'''


# ============================================================
# src/data_cleaning.py
# Cleans the data after validation.
# Always works on a COPY - never touches the original.
# ============================================================

import pandas as pd

from config import (
    MIN_QUANTITY,
    MIN_UNIT_PRICE,
    MIN_DISCOUNT,
    MAX_DISCOUNT,
)


# ------------------------------------------------------------
# STEP 1: Make a safe copy of the data
# ------------------------------------------------------------
def make_copy(df):
    """
    Returns a copy of the DataFrame.
    We work on the copy - original stays safe.
    """
    if df is None:
        return None

    return df.copy()


# ------------------------------------------------------------
# STEP 2: Remove duplicate orders
# ------------------------------------------------------------
def remove_duplicates(df):
    """
    Removes rows with duplicate order_id.
    Keeps the first one, drops the rest.
    """
    if df is None or "order_id" not in df.columns:
        return df

    before = len(df)
    df = df.drop_duplicates(subset=["order_id"], keep="first")
    after = len(df)

    removed = before - after
    if removed > 0:
        print(f"Removed {removed} duplicate order(s).")

    return df


# ------------------------------------------------------------
# STEP 3: Fill missing categorical values
# ------------------------------------------------------------
def fill_missing_text(df):
    """
    For text columns (like category, region),
    replace missing values with 'Unknown'.
    """
    if df is None:
        return df

    text_columns = ["category", "region", "product_name"]

    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")

    return df


# ------------------------------------------------------------
# STEP 4: Remove rows with missing critical values
# ------------------------------------------------------------
def remove_missing_critical(df):
    """
    Rows missing order_id, customer_id, order_date, or sales
    cannot be used. Remove them.
    """
    if df is None:
        return df

    critical_columns = ["order_id", "customer_id", "order_date", "sales"]

    # Keep only columns that actually exist in df
    columns_to_check = [c for c in critical_columns if c in df.columns]

    before = len(df)
    df = df.dropna(subset=columns_to_check)
    after = len(df)

    removed = before - after
    if removed > 0:
        print(f"Removed {removed} row(s) with missing critical values.")

    return df


# ------------------------------------------------------------
# STEP 5: Fix data types (numbers and dates)
# ------------------------------------------------------------
def fix_data_types(df):
    """
    Make sure numbers are numbers and dates are dates.
    """
    if df is None:
        return df

    # Convert to numbers (bad values become NaN)
    numeric_columns = ["quantity", "unit_price", "discount", "sales"]
    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Convert order_date to datetime
    if "order_date" in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    return df


# ------------------------------------------------------------
# STEP 6: Remove invalid rows
# ------------------------------------------------------------
def remove_invalid_rows(df):
    """
    Removes rows with:
    - quantity less than minimum
    - unit_price less than minimum
    - discount outside allowed range
    - invalid date
    """
    if df is None:
        return df

    before = len(df)

    # Invalid quantity
    if "quantity" in df.columns:
        df = df[df["quantity"] >= MIN_QUANTITY]

    # Invalid price
    if "unit_price" in df.columns:
        df = df[df["unit_price"] >= MIN_UNIT_PRICE]

    # Invalid discount
    if "discount" in df.columns:
        df = df[(df["discount"] >= MIN_DISCOUNT) & (df["discount"] <= MAX_DISCOUNT)]

    # Invalid date
    if "order_date" in df.columns:
        df = df[df["order_date"].notna()]

    after = len(df)
    removed = before - after

    if removed > 0:
        print(f"Removed {removed} invalid row(s).")

    return df


# ------------------------------------------------------------
# STEP 7: Add helpful new columns
# ------------------------------------------------------------
def add_new_columns(df):
    """
    Adds calculated columns:
    - gross_sales       = quantity * unit_price
    - discount_amount   = gross_sales * discount / 100
    - net_sales         = gross_sales - discount_amount
    - order_year        = year from order_date
    - order_month       = month from order_date
    - order_month_name  = month name (Jan, Feb, ...)
    """
    if df is None or df.empty:
        return df

    # Gross sales (before discount)
    if "quantity" in df.columns and "unit_price" in df.columns:
        df["gross_sales"] = df["quantity"] * df["unit_price"]

    # Discount amount
    if "gross_sales" in df.columns and "discount" in df.columns:
        df["discount_amount"] = df["gross_sales"] * df["discount"] / 100

    # Net sales (after discount)
    if "gross_sales" in df.columns and "discount_amount" in df.columns:
        df["net_sales"] = df["gross_sales"] - df["discount_amount"]

    # Date parts
    if "order_date" in df.columns:
        df["order_year"] = df["order_date"].dt.year
        df["order_month"] = df["order_date"].dt.month
        df["order_month_name"] = df["order_date"].dt.strftime("%b")

    return df


# ------------------------------------------------------------
# MASTER FUNCTION: Clean the data (runs all steps)
# ------------------------------------------------------------
def clean_data(df, verbose=True):
    """
    Runs all cleaning steps in order.
    Returns the cleaned DataFrame.
    """
    if df is None:
        if verbose:
            print("No data to clean.")
        return None

    if verbose:
        print("=" * 50)
        print("CLEANING DATA")
        print("=" * 50)
        print("Rows before cleaning:", len(df))

    # Step 1: Copy
    df = make_copy(df)

    # Step 2: Remove duplicates
    df = remove_duplicates(df)

    # Step 3: Fill missing text values
    df = fill_missing_text(df)

    # Step 4: Remove rows with missing critical values
    df = remove_missing_critical(df)

    # Step 5: Fix data types
    df = fix_data_types(df)

    # Step 6: Remove invalid rows
    df = remove_invalid_rows(df)

    # Step 7: Add new columns
    df = add_new_columns(df)

    # Reset index
    df = df.reset_index(drop=True)

    if verbose:
        print()
        print("Rows after cleaning:", len(df))
        print("Cleaning finished.")
        print("=" * 50)

    return df


# ------------------------------------------------------------
# TEST BLOCK
# Run: python -m src.data_cleaning
# ------------------------------------------------------------
if __name__ == "__main__":
    from src.data_loader import load_default_data

    print("Loading data...")
    raw = load_default_data()

    if raw is not None:
        print()
        print("Columns BEFORE cleaning:")
        print(list(raw.columns))
        print()

        cleaned = clean_data(raw)

        print()
        print("Columns AFTER cleaning:")
        print(list(cleaned.columns))
        print()

        print("First 5 rows of cleaned data:")
        print(cleaned.head().to_string())
    else:
        print("Could not load data.")