from health_plan import HealthPlan

# Initialize the HealthPlan instance
health_plan = HealthPlan()



# Introduction & Contact Information Inquiry

print("This AI-powered tool will guide you through a set of questions to determine what the best solution is for your"
      "specific lifestyle. We recommend completing all questions before viewing your solution, to ensure"
      "that it's personalized to your unique needs.\n")

print(
    "Hey there! I'm Dino, your friendly diet guide. 🦕 I’m going to create the perfect health solution for your "
    "specific needs.")
print("Before we dive into creating your perfect plan, could I get your name, age, gender, and phone number?")
name = input("Name: ")
phone_number = input("Phone number: ")
gender = input("Gender (male/female): ").lower()
age = float(input("Age: "))

health_plan.update_user_data("name", name)
health_plan.update_user_data("age", age)
health_plan.update_user_data("gender", gender)
health_plan.update_user_data("phone_number", phone_number)

# Height/Weight Inquiry
print("Let's Talk About Your Body Metrics!")
print("First off, could you tell me your current height and weight? It helps me calculate things just right! ")
height = float(input("Height(cm): "))
weight = float(input("Weight(kg): "))

health_plan.update_user_data("height", height)
health_plan.update_user_data("weight", weight)

# BMR calculation based on gender
if gender == 'male':
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
elif gender == 'female':
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
else:
    print("Invalid gender input. BMR calculation requires valid gender.")
    bmr = None

if bmr is not None:
    rounded_bmr = round(bmr)
    health_plan.update_user_data("BMR", rounded_bmr)
    health_plan.update_meal_plan_details("maintenance_calories", rounded_bmr)

# Medical Condition Inquiry
print("\nQuick Health Check!")
print("Do you have any medical conditions, allergies, or sensitivities that "
      "a tailor-made diet could help with?")
has_medical_conditions = input("Medical condition (yes/no): ")
if has_medical_conditions == 'yes':
    medical_conditions = input("Please specify them: ")
    health_plan.update_user_data("medical_conditions", medical_conditions)
    health_plan.update_meal_plan_details("medically_tailored", True)
    health_plan.update_meal_plan_details("made_by_registered_dietician", True)


# Expert Opinion Inquiry
if not has_medical_conditions:
    print("Do you prefer expert opinions?")
    print("Do you like to rely on expert opinions for your diet and exercise choices? 🤔")
    expert_opinion = input("(yes/no): ")
    health_plan.update_user_data("expert_opinion", expert_opinion)
    if expert_opinion == "yes":
        health_plan.update_meal_plan_details("made_by_registered_dietician", True)
        health_plan.update_offers("community_access", True)
else:
    health_plan.update_user_data("expert_opinion", "yes")


# Weight Goal Inquiry
print("Your Weight Goal Mission")
print("Are you on a mission to change your weight? 🎯 Whether it's losing or gaining, I'm here to help!")
weight_goal = input("(lose/maintain/gain): ")

health_plan.update_user_data("weight_goal", weight_goal)

if weight_goal == "lose" or weight_goal == "gain":
    weight_change_goal = float(input(f"How many pounds are you trying to {weight_goal}: "))
    health_plan.update_user_data("weight_change_goal", weight_change_goal)
    health_plan.update_meal_plan_details("timeline", "timeline_here")
    health_plan.update_meal_plan_details("guarantee", True)


# Cooking Preference Inquiry
print("Cooking or Prepared Meals? ")
print("In a perfect world, would you prefer to do the cooking yourself or have"
      " everything prepared for you? This helps me figure out the best way to make your meal planning a breeze! 🍳🌬️")

cooking_preference = input("(myself/prepared): ")
health_plan.update_user_data("cooking_preference", cooking_preference)
if cooking_preference == "myself":
    health_plan.update_offers("meal_prep_delivery", False)
    health_plan.update_offers("meal_kit_delivery", True)

# Current Exercise Inquiry

print("Your Exercise Routine")
print("Do you currently engage in regular exercise? 🏋️‍♂️ Please select your activity "
      "level from the dropdown options below.")
print('''Sedentary Lifestyle: Little or No Exercise | Approximately 20% increase (use these percentages to calculate daily burn with BMR)
Casually Active: Exercise 1-3 Times/Week | Approximately 37.5% increase
Moderately Active: Exercise 4-5 Times/Week | Approximately 46.5% increase
Very Active: Daily Exercise or Intense Exercise 3-4 Times/Week | Approximately 55% increase
Highly Active: Intense Exercise 6-7 Times/Week | Approximately 72.5% increase
Extremely Active: Very Intense Exercise Daily, or Physical Job | Approximately 90% increase''')
activity_level = int(input("(1/2/3/4/5): "))

health_plan.update_user_data("activity_level", activity_level)
health_plan.update_meal_plan_details("daily_burn", "updated_daily_burn_here")
# Update Profile

# Exercise Location Inquiry

exercise_location = "none"
if activity_level == 1:
    print("Starting an Exercise Routine?")
    print("Interested in starting an exercise routine? 💪 Whether it’s a yes, no, I'm all ears!")
    interest_in_exercise = input("(yes/no): ")
    health_plan.update_user_data("interest_in_exercise", interest_in_exercise)
    if interest_in_exercise == "yes":
        print()
        print("Ideal Fitness Habitat")
        print("In the ideal world, would you rather workout at home or in the gym?"
              " Your answer helps me tailor your plan to suit your style!")
        exercise_location = input("(home/gym): ")
    else:
        health_plan.update_offers("online_personal_training", False)
        health_plan.update_offers("workout_videos", False)


elif activity_level >= 2:
    health_plan.update_user_data("interest_in_exercise", "yes")
    print("Your Fitness Habitat")
    print(" I'm curious about your fitness habitat! 🏠🏋️‍♂️🌳"
          " Are you more of a home workout enthusiast or a gym-goer? "
          "Your answer helps me tailor your plan to suit your style!")
    exercise_location = input("(home/gym): ")
    health_plan.update_user_data("exercise_location", exercise_location)


if exercise_location == "gym":
    health_plan.update_offers("online_personal_training", False)
    health_plan.update_offers("in_person_personal_training", True)

# Progress Tracking Inquiry

if has_medical_conditions or activity_level >= 2 or interest_in_exercise or weight_goal == "lose" or weight_goal == "gain":
    print("Tracking Your Progress")
    print("Is it important for you to have precise tracking of your health and progress?"
          " It helps me know if we should focus on super detailed updates or keep it more big picture.")
    tracking_importance = input("(yes/no): ")
    health_plan.update_user_data("tracking_importance", tracking_importance)
    if tracking_importance == "yes":
        health_plan.update_offers("body_measurement", True)
    else:
        health_plan.update_offers("tracking_app", False)

# Stress Level Inquiry
print("Your Daily Stress Level")
print("On a scale from 'totally relaxed' to 'super stressed,' how would you describe your daily lifestyle?")
# Ideally, there would be a slider here, and it would decide based on the halfway point
# whether to offer the meditation or not
stress_level = input("(relaxed/stressed): ")
if stress_level == "stressed":
    health_plan.update_offers("therapy_sessions", True)
health_plan.update_user_data("stress_level", stress_level)

# Email List Subscription Inquiry
print("Join Our Exclusive Club!")
print("How about joining our exclusive club? 💌 Get free recipes, tips and tricks for living your healthiest life, "
      "straight to your inbox. Interested?")
email_list = input("(yes/no): ")
if email_list == "yes":
    pass
    # Get Email
    health_plan.update_offers("email_list", True)
health_plan.update_user_data("email_list", email_list)
print()

# Final Step

running = True
while running:
    print("What do you want to see?")
    print("1 for user_data")
    print("2 for offer")
    print("3 for meal plan details")
    print("4 to quit")
    answer = int(input("(1/2/3/4): "))
    if answer == 4:
        running = False
    elif answer == 1:
        health_plan.display_user_data()
    elif answer == 2:
        health_plan.display_plan()
    else:
        health_plan.display_meal_plan_details()
