class HealthPlan:
    def __init__(self):
        self.user_data = {
            "name": None,
            "age": None,
            "gender": None,
            "phone_number": None,
            "height": None,
            "weight": None,
            "BMR": None,
            "medical_conditions": None,
            "expert_opinion": None,
            "weight_goal": None,
            "weight_change_goal": None,
            "cooking_preference": None,
            "activity_level": None,
            "exercise_location": None,
            "interest_in_exercise": None,
            "tracking_importance": None,
            "stress_level": None,
            "email_list": None
        }
        self.offers = {
            "workout_videos": True,  # Initially Default offers
            "online_personal_training": True,
            "in_person_personal_training": False,
            "tracking_app": True,
            "diet_plan": True,
            "meal_prep_delivery": True,
            "meal_kit_delivery": False,
            "community_access": False,
            "supplements": True,
            "therapy_sessions": False,
            "body_measurement": False,
            "email_list": False,
        }
        self.meal_plan_details = {
            "daily_burn": None,
            "medically_tailored": False,
            "made_by_registered_dietician": False,
            "guarantee": False,
            "timeline": None,
        }

    def update_user_data(self, key, value):
        self.user_data[key] = value
        # self.update_offers()

    def update_meal_plan_details(self, key, value):
        self.meal_plan_details[key] = value

    def update_offers(self, key, value):
        self.offers[key] = value

    def get_current_plan(self):
        # Return the current plan based on user data and offers
        plan = {}
        for offer, included in self.offers.items():
            if included:
                plan[offer] = "Included"
            else:
                plan[offer] = "Not Included"
        return plan

    def display_plan(self):
        plan = self.get_current_plan()
        for offer, status in plan.items():
            print(f"{offer}: {status}")

    def display_meal_plan_details(self):
        print("Meal Plan Details:")
        for key, value in self.meal_plan_details.items():
            formatted_key = key.replace('_', ' ').capitalize()
            if value is None:
                display_value = "Not specified"
            elif isinstance(value, bool):
                display_value = "Yes" if value else "No"
            else:
                display_value = value

            print(f"- {formatted_key}: {display_value}")

    def display_user_data(self):
        print("User Data:")
        for key, value in self.user_data.items():
            formatted_key = key.replace('_', ' ').capitalize()
            display_value = value if value is not None else "Not specified"
            print(f"- {formatted_key}: {display_value}")
