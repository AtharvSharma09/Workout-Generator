import random

class UserInput:
    """Class to collect and validate user input for workout planning."""
    
    def __init__(self, current_weight: float, height: float, goal_weight: float):
        """Initialize UserInput with basic physical attributes.
        
        Args:
            current_weight (float): User's current weight in kg.
            height (float): User's height in meters.
            goal_weight (float): User's goal weight in kg.
        """
        self.current_weight = current_weight
        self.height = height
        self.goal_weight = goal_weight
        self.user_data = {
            "cw": current_weight,
            "height": height,
            "gw": goal_weight,
            "intensity": "",
            "level": "",
            "days": "",
            "time": "",
            "cals": "",
            "user_ex": ""
        }

    def get_intensity(self) -> tuple[dict, int]:
        """Prompt user for workout intensity level and validate input.
        
        Returns:
            tuple: Dictionary of intensity options and selected intensity value.
        """
        intensity_list = {"Casual(1)": 1, "Average(2)": 2, "Hardcore(3)": 3}
        print("-----------------------------------")
        print("Intensities: ", end="")
        print(" | ".join(intensity_list.keys()))
        
        while True:
            try:
                intensity_input = int(input("Enter the level of intensity you want (1, 2, 3): "))
                if intensity_input not in [1, 2, 3]:
                    print("Please enter 1, 2, or 3!")
                else:
                    self.user_data["intensity"] = intensity_input
                    return intensity_list, intensity_input
            except ValueError:
                print("Please enter a valid number!")

    def get_level(self) -> tuple[dict, int]:
        """Prompt user for fitness level and validate input.
        
        Returns:
            tuple: Dictionary of level options and selected level value.
        """
        level_list = {"Beginner(1)": 1, "Intermediate(2)": 2, "Advanced(3)": 3}
        print("-----------------------------------")
        print("Levels: ", end="")
        print(" | ".join(level_list.keys()))
        
        while True:
            try:
                level_input = int(input("Enter the level you are (1, 2, 3): "))
                if level_input not in [1, 2, 3]:
                    print("Please enter 1, 2, or 3!")
                else:
                    self.user_data["level"] = level_input
                    return level_list, level_input
            except ValueError:
                print("Please enter a valid number!")

    def get_days(self) -> int:
        """Prompt user for number of workout days per week and validate input.
        
        Returns:
            int: Number of workout days.
        """
        print("-----------------------------------")
        while True:
            try:
                days_input = int(input("Enter the number of days you want to workout in a week (1-7): "))
                if days_input < 1 or days_input > 7:
                    print("Please enter a number between 1 and 7!")
                else:
                    self.user_data["days"] = days_input
                    return days_input
            except ValueError:
                print("Please enter a valid number!")

    def get_time(self) -> int:
        """Prompt user for workout time per session and validate input.
        
        Returns:
            int: Workout time in minutes.
        """
        print("-----------------------------------")
        while True:
            try:
                time_input = int(input("Enter the time you can allocate to workouts (minutes): "))
                if time_input <= 0:
                    print("Please enter a positive number!")
                else:
                    self.user_data["time"] = time_input
                    return time_input
            except ValueError:
                print("Please enter a valid number!")

    def get_cals(self) -> int:
        """Prompt user for average daily calorie intake and validate input.
        
        Returns:
            int: Calorie intake.
        """
        print("-----------------------------------")
        while True:
            try:
                cal_input = int(input("Enter the amount of calories you consume on average: "))
                if cal_input <= 0:
                    print("Please enter a positive number!")
                else:
                    self.user_data["cals"] = cal_input
                    return cal_input
            except ValueError:
                print("Please enter a valid number!")

class Workout:
    """Class to generate a personalized workout routine based on user input."""
    
    def __init__(self, level_of_user: int, time_of_user: int, days_of_user: int):
        """Initialize Workout with user-specific parameters.
        
        Args:
            level_of_user (int): User's fitness level (1=Beginner, 2=Intermediate, 3=Advanced).
            time_of_user (int): Time available per workout session in minutes.
            days_of_user (int): Number of workout days per week.
        """
        self.level_of_user = level_of_user
        self.time_of_user = time_of_user
        self.days_of_user = days_of_user
        self.days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        
        # Exercise lists for different fitness levels
        self.beginner_ex = (
            "Bodyweight Squats", "Push Ups", "Dumbbell Shoulder Press", "Seated Chest Press Machine",
            "Treadmill Walking", "Seated Row Machine", "Lat Pulldown Machine", "Stationary Bike",
            "Dumbbell Bicep Curls", "Dumbbell Tricep Extensions", "Leg Press Machine",
            "Seated Leg Curl Machine", "Standing Calf Raises", "Cable Rope Face Pulls",
            "Plank Hold", "Dead Bug Core Exercise", "Glute Bridges", "Dumbbell Lateral Raises",
            "Assisted Pull-Ups", "Stretching Routine"
        )
        self.intermediate_ex = (
            "Barbell Back Squats", "Bench Press", "Romanian Deadlifts", "Bent-Over Barbell Rows",
            "Pull Ups", "Overhead Barbell Press", "Incline Dumbbell Chest Press", "Kettlebell Swings",
            "Jump Squats", "Bulgarian Split Squats", "Farmer's Carries", "Dumbbell Chest Fly",
            "Mountain Climbers", "Hanging Leg Raises", "Landmine Twists", "Cable Chest Flys",
            "Barbell Bicep Curls", "Skull Crushers", "Battle Ropes", "Plank to Push-up"
        )
        self.advanced_ex = (
            "Barbell Deadlifts", "Clean and Press", "Snatch Grip Deadlifts", "Weighted Pull Ups",
            "Weighted Dips", "Box Jumps", "Barbell Hip Thrusts", "Front Squats", "Turkish Get Ups",
            "Handstand Push Ups", "Barbell Overhead Squats", "One Arm Dumbbell Snatch",
            "Sled Pushes or Pulls", "Kettlebell Clean & Press", "Barbell Rollouts", "Ring Dips",
            "Wall Balls", "Renegade Rows", "Pistol Squats", "CrossFit WODs"
        )
        
        # Select exercise list based on user level
        self.user_ex = (
            self.beginner_ex if level_of_user == 1 else
            self.intermediate_ex if level_of_user == 2 else
            self.advanced_ex
        )

    def generate_routine(self) -> None:
        """Generate and print a weekly workout routine based on user preferences."""
        for day in range(self.days_of_user):
            print("-----------------------------------")
            print(f"{self.days[day]}:")
            day_routine = {}
            no_of_ex = random.randint(1, min(20, len(self.user_ex)))  # Limit to available exercises
            
            # Assign random exercises and durations based on available time
            for _ in range(no_of_ex):
                random_ex = random.choice(self.user_ex)
                random_time = self._get_random_time()
                day_routine[random_ex] = random_time
            
            # Adjust total time to match user's available time
            total_time = sum(day_routine.values())
            if total_time > self.time_of_user:
                self._reduce_time(day_routine)
            elif total_time < self.time_of_user:
                self._increase_time(day_routine)
            
            # Print the day's routine
            for exercise, time in day_routine.items():
                print(f"{exercise}: {time} min")

    def _get_random_time(self) -> int:
        """Determine random exercise duration based on available workout time.
        
        Returns:
            int: Duration in minutes.
        """
        if self.time_of_user <= 15:
            return random.randint(1, 5)
        elif self.time_of_user <= 30:
            return random.randint(2, 7)
        elif self.time_of_user <= 60:
            return random.randint(2, 10)
        else:
            return random.randint(2, 15)

    def _reduce_time(self, day_routine: dict) -> None:
        """Reduce total workout time to fit within user's available time.
        
        Args:
            day_routine (dict): Dictionary of exercises and their durations.
        """
        while sum(day_routine.values()) > self.time_of_user:
            ex_to_reduce = random.choice(list(day_routine.keys()))
            day_routine[ex_to_reduce] -= 1
            if day_routine[ex_to_reduce] <= 0:
                del day_routine[ex_to_reduce]

    def _increase_time(self, day_routine: dict) -> None:
        """Increase total workout time to match user's available time.
        
        Args:
            day_routine (dict): Dictionary of exercises and their durations.
        """
        while sum(day_routine.values()) < self.time_of_user and day_routine:
            ex_to_increase = random.choice(list(day_routine.keys()))
            day_routine[ex_to_increase] += 1

def get_user_measurements() -> tuple[float, float, float]:
    """Collect and convert user's weight, height, and goal weight.
    
    Returns:
        tuple: Current weight, height, and goal weight in kg and meters.
    """
    print("-----------------------------------")
    while True:
        try:
            cw_input = float(input("Enter your weight: "))
            height_input = float(input("Enter your height: "))
            gw_input = float(input("Enter your goal weight: "))
            if cw_input <= 0 or height_input <= 0 or gw_input <= 0:
                print("Please enter positive values!")
                continue
            
            unit = int(input("Enter your measure unit, kg/feet(1), pound/m(2), kg/m(3): "))
            if unit not in [1, 2, 3]:
                print("Please enter 1, 2, or 3!")
                continue
            
            if unit == 1:  # kg/feet
                height_input *= 0.3048  # Convert feet to meters
            elif unit == 2:  # pound/m
                cw_input /= 2.205  # Convert pounds to kg
                gw_input /= 2.205
            # unit == 3 (kg/m) requires no conversion
            
            return cw_input, height_input, gw_input
        except ValueError:
            print("Please enter valid numbers!")

def main():
    """Main function to run the workout generator."""
    # Collect measurements
    current_weight, height, goal_weight = get_user_measurements()
    
    # Initialize user input and collect preferences
    user = UserInput(current_weight, height, goal_weight)
    user.get_intensity()
    user.get_level()
    days = user.get_days()
    time = user.get_time()
    user.get_cals()
    
    # Generate workout routine
    workout = Workout(level_of_user=user.user_data["level"], time_of_user=user.user_data["time"], days_of_user=days)
    workout.generate_routine()

if __name__ == "__main__":
    main()