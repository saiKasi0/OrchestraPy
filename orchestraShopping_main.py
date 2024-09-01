import pandas as pd
import numpy as np

leaders = np.squeeze(pd.read_csv('leaders.csv').values).tolist()

def sort_birthdays(df):
    df['Birthday'] = df['Birthday'].str[:-5]  # Extract month/day part of the birthday
    df['Birthday'] = pd.to_datetime(df['Birthday'], format='%m/%d')  # Convert to datetime
    df['effective_month'] = df['Birthday'].dt.month  # Extract month
    df['half_bd'] = df['effective_month'].isin([6, 7, 8])  # Check if in June, July, August
    df['effective_month'] = df.apply(lambda row: row['effective_month'] + (-6 if row['effective_month'] > 6 else 6) if row['half_bd'] else row['effective_month'], axis=1)  # Adjust month for half-birthday
    df.sort_values(by=['effective_month'], inplace=True)  # Sort by effective month
    df['Birthday'] = df['Birthday'].dt.strftime('%m/%d')  # Convert back to string format

def print_leaders(leaders, effective_month, df):
    shopping_list  = ""
    pplw_nothing_this_month = "Nothing this month: "
    for leader in leaders:
        leader_df = df[(df['Leadership'] == leader) & (df['effective_month'] == effective_month)]
        leader_shopping_list = leader_shopping_list_to_string(leader_df)
        if (not leader_shopping_list):
            pplw_nothing_this_month += f"{leader}, " 
        shopping_list += f"{leader}'s shopping list:\n" + leader_shopping_list if leader_shopping_list else ""

    return shopping_list + pplw_nothing_this_month + "\nDone by Prabhav Bot 3.0🤖"

def leader_shopping_list_to_string(leader_df):
    leader_shopping_list = ""
    leader_df = leader_df.fillna("Didn't Specify")  # Replace NaN values
    for index, student in leader_df.iterrows():
        leader_shopping_list += f"   {student['First Name'].strip()} {student['Last Name'].strip()}'s {'Actual Birthday (Celebrating Half Birthday)' if student['half_bd'] else 'Birthday'}: {student['Birthday']}\n     Snacks: {student['Salty'].strip()}, {student['Sweet'].strip()}, {student['Drink'].strip()}\n\n"
    return leader_shopping_list if leader_shopping_list else ""

def main():
    df = pd.read_csv("BdayList24-25.csv")
    df.rename(columns={
        "Your First Name": "First Name",
        "Your Last Name": "Last Name",
        "Your Birthday": "Birthday",
        "What's your favorite salty snack?": "Salty",
        "What's your favorite sweet snack?": "Sweet",
        "What's your favorite drink?": "Drink"
    }, inplace=True)
    df.drop_duplicates(subset=["First Name", "Last Name"], keep='last', inplace=True)

    sort_birthdays(df)
    df['Leadership'] = np.tile(leaders, len(df) // len(leaders) + 1)[:len(df)]  # Assign leaders to each row
    print(print_leaders(leaders=leaders, effective_month=9, df=df))

if __name__ == "__main__":
    main()
