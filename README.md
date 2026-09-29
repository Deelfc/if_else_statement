# Football Club Checker

Simple Python script using `if / else` and the `in` operator. Takes a club name via `input()`, checks membership in a tuple of clubs, and prints whether it's a "bigger" or "smaller" club. Demonstrates tuples, membership checking, and basic conditional logic.

## Code

\`\`\`python
import random

club = ("Real Madrid", "Liverpool", "Man utd", "Barcelona", "Bayern", "Mancity", "Arsenal")

football_club = input("Enter your club name: ")

if football_club in club:
    print("You are a bigger club")
else:
    print("You are a smaller club")
\`\`\`

## Example Run

\`\`\`
Enter your club name: Arsenal
You are a bigger club
\`\`\`

\`\`\`
Enter your club name: Chelsea
You are a smaller club
\`\`\`

## Notes

- The check is case-sensitive: `"arsenal"` (lowercase) won't match `"Arsenal"`.
- The `random` import is currently unused in this version.
