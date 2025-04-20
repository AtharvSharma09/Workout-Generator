# Personalised Workout Routine Generator
A Python-based command-line application that generates personalized weekly workout routines based on user input, including fitness level, workout intensity, available time, and physical measurements.
## Features

User Input Collection: Gathers user details such as current weight, height, goal weight, fitness level, workout intensity, weekly workout days, session duration, and calorie intake.
Unit Conversion: Supports input in kg/feet, pounds/meters, or kg/meters with automatic conversion to kg and meters.
Customized Workouts: Generates tailored routines with exercises suited to Beginner, Intermediate, or Advanced fitness levels.
Time Management: Adjusts exercise durations to fit the user's specified workout time per session.
Randomized Routines: Creates varied daily workout plans for the specified number of days (1-7) with random exercise selection and durations.
Input Validation: Ensures all inputs are valid numbers within acceptable ranges.

## Requirements

Python 3.x
Standard library: random

## How to Run

Clone or download the repository.

Navigate to the project directory.

### Run the script:
python workout_generator.py


### Follow the prompts to:

Enter weight, height, and goal weight with preferred units (kg/feet, pound/m, kg/m).
Select workout intensity (Casual, Average, Hardcore).
Choose fitness level (Beginner, Intermediate, Advanced).
Specify number of workout days per week (1-7).
Enter workout session duration in minutes.
Provide average daily calorie intake.
View the generated weekly workout routine.



## Gameplay

Fitness Levels and Exercises:
Beginner: Bodyweight Squats, Push Ups, Treadmill Walking, Plank Hold, etc.
Intermediate: Barbell Back Squats, Bench Press, Pull Ups, Mountain Climbers, etc.
Advanced: Barbell Deadlifts, Clean and Press, Box Jumps, Pistol Squats, etc.


## Workout Structure:
Routines are generated for the specified number of days (e.g., Monday to Wednesday for 3 days).
Each day includes 1 or more exercises with durations adjusted to fit the user’s available time.
Exercise durations vary based on session length (e.g., 1-5 min for short sessions, 2-15 min for longer ones).


Output: Displays a weekly plan with exercises and their durations for each workout day.

## File Structure

workout_generator.py: Main script containing UserInput and Workout classes, along with the main logic.

## Example

Enter your weight: 70

Enter your height: 1.75

Enter your goal weight: 65

Enter your measure unit, kg/feet(1), pound/m(2), kg/m(3): 3

Intensities: Casual(1) | Average(2) | Hardcore(3)

Enter the level of intensity you want (1, 2, 3): 2

Levels: Beginner(1) | Intermediate(2) | Advanced(3)

Enter the level you are (1, 2, 3): 2

Enter the number of days you want to workout in a week (1-7): 3

Enter the time you can allocate to workouts (minutes): 30

Enter the amount of calories you consume on average: 2000

Monday:

Barbell Back Squats: 7 min

Pull Ups: 6 min

Mountain Climbers: 5 min

Tuesday:

Bench Press: 8 min

Kettlebell Swings: 7 min

Wednesday:

Romanian Deadlifts: 6 min

Jump Squats: 5 min

Cable Chest Flys: 4 min

## Contributing
Contributions are welcome! Feel free to fork the repository, submit issues, or create pull requests to add features like new exercises, improved time allocation algorithms, or a graphical interface.
## License
This project is open-source and available under the MIT License.

## Contact
For questions, suggestions, or issues, please:

Open an issue on GitHub.

Contact Atharv Sharma at atharvsharmatgu@gmail.com.

This project showcases Python skills, including object-oriented programming, randomization, and game logic. It was built as a fun and educational exercise to simulate a popular card game. Enjoy playing, and may the cards be in your favor!
