# OrchestraPy Birthday Shopping List Generator

This project generates shopping lists for orchestra leadership based on the birthdays of their group members. The birthdays are adjusted to consider half-birthdays (celebrated in June, July, and August) and then sorted by an "effective month" due to the span of the school year. The project reads from a CSV file containing group members' information and outputs the appropriate shopping lists for each leader.

## Features

- **Birthday Sorting:** Adjusts birthdays to half-birthdays if they fall in June, July, or August and sorts them by an "effective month."
- **Leader Assignment:** Automatically assigns a list of leaders to group members.
- **Shopping List Generation:** Generates shopping lists based on group members' birthday information and their snack preferences.

## Files in the Project

- **`orchestraShoppingMain.py`**  
  The main script that processes the data and generates the shopping lists based on the group's information for the 24-25 school year.

- **`orchestra_shopping_version_two23-24.py`**  
  A version of the script tailored for the 2023-2024 period, with specific adjustments for nature of csv data.

- **`orchestraShopping_version_one23-34.py`**  
  A initial version of the script tailored for the 2023-2024 period, with specific adjustments for nature of csv data and different methodology.

## Getting Started

### Prerequisites

- Python 3.x
- Pandas library (`pip install pandas`)
- NumPy library (`pip install numpy`)

### 24-25 CSV File Structure

Ensure your CSV file (`BdayList24-25.csv`) has the following columns:

- **Your First Name:** First name of the group member.
- **Your Last Name:** Last name of the group member.
- **Your Birthday:** Birthday of the group member (MM/DD/YYYY format).
- **What's your favorite salty snack?:** Favorite salty snack of the group member.
- **What's your favorite sweet snack?:** Favorite sweet snack of the group member.
- **What's your favorite drink?:** Favorite drink of the group member.

### Running the Project

1. Clone this repository to your local machine.
2. Ensure the `BdayList24-25.csv` file is in the same directory as your scripts.
3. Install the required libraries:

   ```bash
   pip install pandas numpy
   ```

4. Run the desired script:

   ```bash
   python orchestraShoppingMain.py
   ```

### Output

The script will print the shopping lists for each leader, detailing the group members' birthdays (or half-birthdays) and their snack preferences based on given month of birthdays.

**Example Output:**

```shell
Joe's shopping list:
   John Doe's Birthday: 01/15
     Snacks: Chips, Chocolate, Soda

   Jane Smith's Actual Birthday (Celebrating Half Birthday): 07/10
     Snacks: Popcorn, Candy, Juice
...
```

## Customization

### Adding Leaders

You can customize the list of leaders by modifying the `leaders_example.csv`


### Modifying Output

If you want to customize the output format, modify the `leader_shopping_list_to_string` function in the script.

## Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

Thanks to everyone who contributed to this project.
