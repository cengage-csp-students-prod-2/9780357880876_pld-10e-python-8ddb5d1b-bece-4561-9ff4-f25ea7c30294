// SuperMarket.cpp - This program creates a report that lists weekly hours worked
// by employees of a supermarket. The report lists total hours for each day of one week.
// Input: Interactive
// Output: Report.

#include <iostream>
#include <string>
using namespace std;

int main()
{
    // Declare variables.
    const string HEAD1 = "WEEKLY HOURS WORKED";
    const string DAY_FOOTER = "              Day Total: ";
    const string SENTINEL = "done"; // Sentinel value to quit

    double hoursWorked = 0;       // Hours worked for current input
    string dayOfWeek;             // Current day of week
    double dailyTotal = 0;        // Total hours for the current day
    double weeklyTotal = 0;       // Weekly total hours
    string prevDay = "";          // Previous day to track day change
    bool notDone = true;          // Loop control

    // Print two blank lines.
    cout << endl << endl;

    // Print heading.
    cout << "\t\t\t\t\t" << HEAD1 << endl;

    // Print two blank lines.
    cout << endl << endl;

    // Read first record
    cout << "Enter day of week or done to quit: ";
    cin >> dayOfWeek;

    if (dayOfWeek == SENTINEL)
        notDone = false;
    else
    {
        cout << "Enter hours worked: ";
        cin >> hoursWorked;
        prevDay = dayOfWeek;
        dailyTotal = hoursWorked;  // Initialize daily total
    }

    while (notDone)
    {
        cout << "Enter day of week or done to quit: ";
        cin >> dayOfWeek;

        if (dayOfWeek == SENTINEL)
        {
            notDone = false;
            // Display total for the last day before quitting
            cout << DAY_FOOTER << dailyTotal << endl;
            weeklyTotal += dailyTotal;  // Add last day's total to weekly total
        }
        else
        {
            cout << "Enter hours worked: ";
            cin >> hoursWorked;

            // Control break: if the day changes, output the previous day's total
            if (dayOfWeek != prevDay)
            {
                cout << DAY_FOOTER << dailyTotal << endl; // Display previous day total
                weeklyTotal += dailyTotal;               // Add to weekly total

                // Reset for new day
                prevDay = dayOfWeek;
                dailyTotal = hoursWorked;
            }
            else
            {
                // Same day, accumulate hours
                dailyTotal += hoursWorked;
            }

            // Display the current entry
            cout << dayOfWeek << ": " << hoursWorked << endl;
        }
    }

    // Display the grand total
    cout << "\nTotal hours worked by all employees for the week: " << weeklyTotal << endl;

    return 0;
} // End of main()
