import pandas as pd
import numpy as np

def calculate_concordance(df):
    """
    Calculate the concordance index for survival analysis.

    Parameters:
        df (pd.DataFrame): A DataFrame containing columns 'time_of_death' and 'risk'.

    Returns:
        float: The concordance index.
    """
    concordant_pairs = 0
    discordant_pairs = 0
    tied_pairs = 0

    # Sort the dataframe by 'time_of_death' to make comparison easier
    df = df.sort_values(by="time_of_death").reset_index(drop=True)
    n = len(df)

    # Iterate over all pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            time_i = df.loc[i, "time_of_death"]
            time_j = df.loc[j, "time_of_death"]
            risk_i = df.loc[i, "risk"]
            risk_j = df.loc[j, "risk"]

            if time_i != time_j:  # Only compare pairs with different survival times
                if (time_i < time_j and risk_i > risk_j) or (time_i > time_j and risk_i < risk_j):
                    concordant_pairs += 1
                elif (time_i < time_j and risk_i < risk_j) or (time_i > time_j and risk_i > risk_j):
                    discordant_pairs += 1
            else:
                # If survival times are tied, check for risk ties
                if risk_i == risk_j:
                    tied_pairs += 1

    total_pairs = concordant_pairs + discordant_pairs + tied_pairs
    concordance_index = concordant_pairs / total_pairs if total_pairs > 0 else np.nan

    return concordance_index

if __name__ == "__main__":
    # Sample input data
    data = {
        "ID": [1, 2, 3, 4, 5],
        "time_of_death": [1, 3, 4, 6, 9],
        "risk": [6, 3, 5, 2, 4]
    }
    df = pd.DataFrame(data)

    # Calculate concordance index
    concordance_index = calculate_concordance(df)
    print(f"Concordance Index: {concordance_index:.4f}")

