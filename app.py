from flask import Flask, render_template, request
app = Flask(__name__,template_folder='templates',static_folder='static')

meal_plans = {
    "general_health": {
          "vegetarian": {
              "male": {
                "18-30": {
                    "sedentary": {
    "Breakfast": [
        {
            "item": "Vegetable upma with a glass of buttermilk",
            "quantity": "1.5 cups upma + 1 glass (200ml) buttermilk",
            "time": "8:00 AM",
            "calories": 350,
            "protein": 12,
            "carbs": 45,
            "fats": 10
        }
    ],
    "Lunch": [
        {
            "item": "Brown rice + Moong dal + mixed vegetable sabzi",
            "quantity": "1 cup brown rice + 1 cup dal + 1 cup sabzi",
            "time": "1:00 PM",
            "calories": 500,
            "protein": 18,
            "carbs": 65,
            "fats": 12
        }
    ],
    "Snack": [
        {
            "item": "Fruit salad with a handful of walnuts",
            "quantity": "1 bowl fruit salad + 5-6 walnuts",
            "time": "4:30 PM",
            "calories": 250,
            "protein": 5,
            "carbs": 30,
            "fats": 12
        }
    ],
    "Dinner": [
        {
            "item": "Multigrain roti + paneer bhurji + cucumber salad",
            "quantity": "2 rotis + 1/2 cup paneer bhurji + 1 cup salad",
            "time": "8:00 PM",
            "calories": 450,
            "protein": 22,
            "carbs": 40,
            "fats": 18
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Moong dal chilla with mint chutney",
            "quantity": "2 chillas + 2 tbsp chutney",
            "time": "7:30 AM",
            "calories": 400,
            "protein": 20,
            "carbs": 40,
            "fats": 15
        }
    ],
    "Lunch": [
        {
            "item": "pulao with curd",
            "quantity": "1.5 cups pulao + 1/2 cup curd",
            "time": "1:00 PM",
            "calories": 550,
            "protein": 20,
            "carbs": 60,
            "fats": 18
        }
    ],
    "Snack": [
        {
            "item": "Roasted chana + green tea",
            "quantity": "1/2 cup roasted chana + 1 cup green tea",
            "time": "5:00 PM",
            "calories": 200,
            "protein": 10,
            "carbs": 20,
            "fats": 6
        }
    ],
    "Dinner": [
        {
            "item": "Vegetable stir-fry + paneer + brown rice",
            "quantity": "1 cup stir-fry + 100g paneer + 1/2 cup brown rice",
            "time": "8:00 PM",
            "calories": 500,
            "protein": 25,
            "carbs": 35,
            "fats": 20
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Oats smoothie with banana and peanut butter",
            "quantity": "1 glass smoothie (1/2 cup oats + 1 banana + 1 tbsp peanut butter + 1 cup milk)",
            "time": "7:00 AM",
            "calories": 500,
            "protein": 22,
            "carbs": 55,
            "fats": 18
        }
    ],
    "Lunch": [
        {
            "item": "Rajma chawal with salad",
            "quantity": "1 cup rajma + 1 cup brown rice + 1 cup salad",
            "time": "12:30 PM",
            "calories": 600,
            "protein": 22,
            "carbs": 65,
            "fats": 15
        }
    ],
    "Snack": [
        {
            "item": "Fruit chaat with nuts",
            "quantity": "1 cup mixed fruits + 5 almonds",
            "time": "5:00 PM",
            "calories": 250,
            "protein": 7,
            "carbs": 30,
            "fats": 8
        }
    ],
    "Dinner": [
        {
            "item": "Paneer tikka with sautéed veggies",
            "quantity": "150g paneer + 1 cup vegetables",
            "time": "8:00 PM",
            "calories": 550,
            "protein": 30,
            "carbs": 25,
            "fats": 28
        }
    ]
}
                },
                "31-50": {
                   "sedentary": {
    "Breakfast": [
        {
           "item": "Vegetable upma with a glass of buttermilk",
            "quantity": "1.5 cups upma + 1 glass (200ml) buttermilk",
            "time": "8:00 AM",
            "calories": 350,
            "protein": 12,
            "carbs": 45,
            "fats": 10
        }
    ],
    "Lunch": [
        {
            "item": "Phulka with dal and mixed vegetable sabzi",
            "quantity": "2 phulkas + 1 cup dal + 1 cup sabzi",
            "time": "1:00 PM",
            "calories": 550,
            "protein": 20,
            "carbs": 55,
            "fats": 18
        }
    ],
    "Snack": [
        {
            "item": "Roasted chana",
            "quantity": "1/2 cup roasted chana",
            "time": "5:00 PM",
            "calories": 150,
            "protein": 8,
            "carbs": 20,
            "fats": 3
        }
    ],
    "Dinner": [
        {
            "item": "Vegetable khichdi with curd",
            "quantity": "1 cup khichdi + 1/2 cup curd",
            "time": "8:00 PM",
            "calories": 500,
            "protein": 18,
            "carbs": 50,
            "fats": 15
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Vegetable poha with peanuts",
            "quantity": "1 cup poha + 2 tbsp peanuts",
            "time": "7:30 AM",
            "calories": 450,
            "protein": 12,
            "carbs": 55,
            "fats": 16
        }
    ],
    "Lunch": [
        {
            "item": "Brown rice with rajma and cucumber salad",
            "quantity": "1 cup brown rice + 1 cup rajma + 1 cup salad",
            "time": "1:00 PM",
            "calories": 600,
            "protein": 22,
            "carbs": 60,
            "fats": 18
        }
    ],
    "Snack": [
        {
            "item": "Sprouts chaat",
            "quantity": "1 cup sprouts chaat",
            "time": "5:00 PM",
            "calories": 200,
            "protein": 14,
            "carbs": 20,
            "fats": 5
        }
    ],
    "Dinner": [
        {
            "item": "Multigrain roti with paneer bhurji",
            "quantity": "2 rotis + 1 cup paneer bhurji",
            "time": "8:00 PM",
            "calories": 550,
            "protein": 25,
            "carbs": 40,
            "fats": 20
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Masala oats with mixed veggies and buttermilk",
            "quantity": "1 cup oats + 1 cup buttermilk",
            "time": "7:30 AM",
            "calories": 500,
            "protein": 18,
            "carbs": 55,
            "fats": 15
        }
    ],
    "Lunch": [
        {
            "item": "brown rice pulao with mixed vegetables and dal",
            "quantity": "1 cup brown rice pulao + 1 cup dal",
            "time": "1:00 PM",
            "calories": 650,
            "protein": 22,
            "carbs": 60,
            "fats": 20
        }
    ],
    "Snack": [
        {
            "item": "Roasted chana and a fruit",
            "quantity": "1/2 cup roasted chana + 1 apple",
            "time": "5:00 PM",
            "calories": 250,
            "protein": 12,
            "carbs": 30,
            "fats": 5
        }
    ],
    "Dinner": [
        {
            "item": "Paneer tikka with multigrain roti and salad",
            "quantity": "1 cup paneer tikka + 2 rotis + 1 cup salad",
            "time": "8:00 PM",
            "calories": 600,
            "protein": 28,
            "carbs": 35,
            "fats": 22
        }
    ]
}
                },
                "51+": {
                    "sedentary": {
    "Breakfast": [
        {
            "item": "Vegetable poha with green tea",
            "quantity": "1 cup poha + 1 cup green tea",
            "time": "8:00 AM",
            "calories": 350,
            "protein": 8,
            "carbs": 45,
            "fats": 10
        }
    ],
    "Lunch": [
        {
            "item": "Brown rice with mixed vegetable curry and salad",
            "quantity": "1 cup brown rice + 1 cup curry + 1 cup salad",
            "time": "1:00 PM",
            "calories": 550,
            "protein": 18,
            "carbs": 55,
            "fats": 18
        }
    ],
    "Snack": [
        {
            "item": "Handful of walnuts and a small banana",
            "quantity": "7 walnuts + 1 small banana",
            "time": "5:00 PM",
            "calories": 200,
            "protein": 5,
            "carbs": 20,
            "fats": 12
        }
    ],
    "Dinner": [
        {
            "item": "Grilled paneer wrap with whole wheat roti and veggies",
            "quantity": "1 wrap + 1 cup vegetables",
            "time": "8:00 PM",
            "calories": 450,
            "protein": 22,
            "carbs": 30,
            "fats": 15
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Vegetable upma with curd",
            "quantity": "1 cup upma + 1/2 cup curd",
            "time": "7:30 AM",
            "calories": 400,
            "protein": 10,
            "carbs": 50,
            "fats": 12
        }
    ],
    "Lunch": [
        {
            "item": "Multigrain roti with dal and sautéed vegetables",
            "quantity": "2 rotis + 1 cup dal + 1 cup vegetables",
            "time": "12:30 PM",
            "calories": 600,
            "protein": 22,
            "carbs": 50,
            "fats": 18
        }
    ],
    "Snack": [
        {
            "item": "Fruit chaat with mixed seeds",
            "quantity": "1 cup fruit chaat + 1 tbsp mixed seeds",
            "time": "4:30 PM",
            "calories": 250,
            "protein": 6,
            "carbs": 30,
            "fats": 10
        }
    ],
    "Dinner": [
        {
            "item": "Khichdi with curd and salad",
            "quantity": "1.5 cup khichdi + 1/2 cup curd + 1 cup salad",
            "time": "8:00 PM",
            "calories": 500,
            "protein": 18,
            "carbs": 45,
            "fats": 15
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Oats porridge with chopped nuts and banana",
            "quantity": "1 cup oats + 1 tbsp nuts + 1 banana",
            "time": "7:30 AM",
            "calories": 450,
            "protein": 15,
            "carbs": 55,
            "fats": 14
        }
    ],
    "Lunch": [
        {
            "item": "Brown rice with rajma and mixed vegetable salad",
            "quantity": "1 cup brown rice + 1 cup rajma + 1 cup salad",
            "time": "12:30 PM",
            "calories": 650,
            "protein": 25,
            "carbs": 60,
            "fats": 18
        }
    ],
    "Snack": [
        {
            "item": "Greek yogurt with berries",
            "quantity": "1 cup Greek yogurt + 1/2 cup mixed berries",
            "time": "4:30 PM",
            "calories": 250,
            "protein": 12,
            "carbs": 25,
            "fats": 8
        }
    ],
    "Dinner": [
        {
            "item": "pulao with paneer bhurji",
            "quantity": "1 cup  pulao + 1/2 cup paneer bhurji",
            "time": "8:00 PM",
            "calories": 500,
            "protein": 22,
            "carbs": 40,
            "fats": 16
        }
    ]
}
                }
            },
            "female": {
                  "18-30": {
                   "sedentary": {
    "Breakfast": [
        {
            "item": "Vegetable upma with a cup of green tea",
            "quantity": "1 cup upma + 1 cup green tea",
            "time": "8:00 AM",
            "calories": 300,
            "protein": 8,
            "carbs": 40,
            "fats": 10
        }
    ],
    "Lunch": [
        {
            "item": "Chapati with mixed vegetable curry and cucumber salad",
            "quantity": "2 chapatis + 1 cup vegetable curry + 1/2 cup salad",
            "time": "1:00 PM",
            "calories": 450,
            "protein": 15,
            "carbs": 50,
            "fats": 12
        }
    ],
    "Snack": [
        {
            "item": "Handful of roasted chickpeas",
            "quantity": "30 grams roasted chickpeas",
            "time": "5:00 PM",
            "calories": 150,
            "protein": 8,
            "carbs": 18,
            "fats": 5
        }
    ],
    "Dinner": [
        {
            "item": "Moong dal khichdi with sautéed spinach",
            "quantity": "1 cup khichdi + 1/2 cup spinach",
            "time": "8:00 PM",
            "calories": 400,
            "protein": 18,
            "carbs": 45,
            "fats": 8
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Vegetable poha with peanuts and a cup of herbal tea",
            "quantity": "1 cup poha + 1 cup tea",
            "time": "7:30 AM",
            "calories": 350,
            "protein": 9,
            "carbs": 45,
            "fats": 12
        }
    ],
    "Lunch": [
        {
            "item": "Brown rice with rajma curry and mixed salad",
            "quantity": "1 cup rice + 1 cup rajma + 1/2 cup salad",
            "time": "1:00 PM",
            "calories": 500,
            "protein": 18,
            "carbs": 55,
            "fats": 14
        }
    ],
    "Snack": [
        {
            "item": "Greek yogurt with fruits",
            "quantity": "1 small bowl yogurt + 1/2 cup fruits",
            "time": "5:00 PM",
            "calories": 200,
            "protein": 10,
            "carbs": 25,
            "fats": 5
        }
    ],
    "Dinner": [
        {
            "item": "Vegetable-stuffed paratha with curd",
            "quantity": "1 medium paratha + 1/2 cup curd",
            "time": "8:00 PM",
            "calories": 450,
            "protein": 16,
            "carbs": 50,
            "fats": 12
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Paneer sandwich with multigrain bread and a glass of milk",
            "quantity": "2 slices bread + 50g paneer + 1 cup milk",
            "time": "7:00 AM",
            "calories": 450,
            "protein": 20,
            "carbs": 40,
            "fats": 18
        }
    ],
    "Lunch": [
        {
            "item": "brown rice  with chickpeas and vegetables",
            "quantity": "1 cup brown rice + 1/2 cup chickpeas + 1 cup veggies",
            "time": "12:30 PM",
            "calories": 500,
            "protein": 22,
            "carbs": 50,
            "fats": 15
        }
    ],
    "Snack": [
        {
            "item": "Peanut butter with apple slices",
            "quantity": "2 tbsp peanut butter + 1 apple",
            "time": "5:00 PM",
            "calories": 250,
            "protein": 8,
            "carbs": 28,
            "fats": 14
        }
    ],
    "Dinner": [
        {
            "item": "Grilled paneer with  vegetables and brown rice",
            "quantity": "100g paneer + 1/2 cup veggies + 1/2 cup rice",
            "time": "8:00 PM",
            "calories": 450,
            "protein": 25,
            "carbs": 40,
            "fats": 16
        }
    ]
}
            },
                  "31-50": {
                    "sedentary": {
    "Breakfast": [
        {
            "item": "Vegetable upma with a cup of buttermilk",
            "quantity": "1 cup upma + 1 cup buttermilk",
            "time": "7:30 AM",
            "calories": 350,
            "protein": 10,
            "carbs": 45,
            "fats": 10
        }
    ],
    "Lunch": [
        {
            "item": "Brown rice with dal and mixed vegetable sabzi",
            "quantity": "1/2 cup brown rice + 1/2 cup dal + 1 cup sabzi",
            "time": "1:00 PM",
            "calories": 450,
            "protein": 18,
            "carbs": 50,
            "fats": 12
        }
    ],
    "Snack": [
        {
            "item": "Roasted makhana (fox nuts)",
            "quantity": "1 cup",
            "time": "4:30 PM",
            "calories": 100,
            "protein": 4,
            "carbs": 12,
            "fats": 3
        }
    ],
    "Dinner": [
        {
            "item": "Moong dal chilla with mint chutney",
            "quantity": "2 medium chillas + 2 tbsp chutney",
            "time": "8:00 PM",
            "calories": 350,
            "protein": 18,
            "carbs": 30,
            "fats": 12
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Vegetable poha with peanuts and a glass of milk",
            "quantity": "1 cup poha + 1 cup milk",
            "time": "7:30 AM",
            "calories": 400,
            "protein": 15,
            "carbs": 50,
            "fats": 12
        }
    ],
    "Lunch": [
        {
            "item": "Multigrain roti with paneer bhurji and salad",
            "quantity": "2 rotis + 1/2 cup paneer bhurji + 1 cup salad",
            "time": "1:00 PM",
            "calories": 500,
            "protein": 25,
            "carbs": 40,
            "fats": 20
        }
    ],
    "Snack": [
        {
            "item": "Fruit chaat (seasonal fruits)",
            "quantity": "1 bowl",
            "time": "5:00 PM",
            "calories": 150,
            "protein": 2,
            "carbs": 30,
            "fats": 2
        }
    ],
    "Dinner": [
        {
            "item": "Vegetable khichdi with curd",
            "quantity": "1 cup khichdi + 1/2 cup curd",
            "time": "8:00 PM",
            "calories": 400,
            "protein": 15,
            "carbs": 45,
            "fats": 10
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Oats porridge with banana slices and chia seeds",
            "quantity": "1 cup oats + 1 banana + 1 tbsp chia seeds",
            "time": "7:30 AM",
            "calories": 450,
            "protein": 18,
            "carbs": 55,
            "fats": 14
        }
    ],
    "Lunch": [
        {
            "item": "Brown rice with mixed vegetable curry and salad",
            "quantity": "1 cup brown rice + 1 cup vegetable curry + 1 cup salad",
            "time": "1:00 PM",
            "calories": 500,
            "protein": 20,
            "carbs": 55,
            "fats": 15
        }
    ],
    "Snack": [
        {
            "item": "Roasted chickpeas",
            "quantity": "1/2 cup",
            "time": "5:00 PM",
            "calories": 180,
            "protein": 10,
            "carbs": 20,
            "fats": 6
        }
    ],
    "Dinner": [
        {
            "item": "brown rice  and paneer curry",
            "quantity": "1 cup brown rice + 50g paneer cubes",
            "time": "8:00 PM",
            "calories": 450,
            "protein": 20,
            "carbs": 40,
            "fats": 18
        }
    ]
}
            },
            "51+": {
              "sedentary": {
    "Breakfast": [
        {
            "item": "Vegetable poha with peanuts",
            "quantity": "1 cup poha + 1 tbsp peanuts",
            "time": "8:00 AM",
            "calories": 300,
            "protein": 8,
            "carbs": 45,
            "fats": 8
        }
    ],
    "Lunch": [
        {
            "item": "Mixed vegetable khichdi with curd",
            "quantity": "1 cup khichdi + 1/2 cup curd",
            "time": "1:00 PM",
            "calories": 400,
            "protein": 15,
            "carbs": 50,
            "fats": 10
        }
    ],
    "Snack": [
        {
            "item": "1 Apple with almond butter",
            "quantity": "1 medium apple + 1 tbsp almond butter",
            "time": "5:00 PM",
            "calories": 180,
            "protein": 4,
            "carbs": 25,
            "fats": 8
        }
    ],
    "Dinner": [
        {
            "item": "Vegetable soup with whole wheat toast",
            "quantity": "1 bowl soup + 1 slice toast",
            "time": "8:00 PM",
            "calories": 300,
            "protein": 10,
            "carbs": 30,
            "fats": 8
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Oats porridge with nuts and banana",
            "quantity": "1 cup oats + 1/2 banana + 5 almonds",
            "time": "8:00 AM",
            "calories": 350,
            "protein": 10,
            "carbs": 45,
            "fats": 12
        }
    ],
    "Lunch": [
        {
            "item": "Brown rice, dal, and mixed vegetable salad",
            "quantity": "1 cup rice + 1/2 cup dal + 1 cup salad",
            "time": "1:00 PM",
            "calories": 450,
            "protein": 18,
            "carbs": 55,
            "fats": 10
        }
    ],
    "Snack": [
        {
            "item": "Greek yogurt with berries",
            "quantity": "3/4 cup yogurt + 1/4 cup mixed berries",
            "time": "5:00 PM",
            "calories": 150,
            "protein": 8,
            "carbs": 15,
            "fats": 4
        }
    ],
    "Dinner": [
        {
            "item": "vegetable pulao with raita",
            "quantity": "1 cup pulao + 1/2 cup raita",
            "time": "8:00 PM",
            "calories": 350,
            "protein": 12,
            "carbs": 40,
            "fats": 8
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Multigrain toast with Peanut Chutney, Sprouted Moong and a Cucumber",
            "quantity": "2 slices toast + 2 tbsp peanut chutney + 5 cucumber slices + 1 tsp sesame seeds ",
            "time": "7:30 AM",
            "calories": 400,
            "protein": 15,
            "carbs": 36,
            "fats": 21
        }
    ],
    "Lunch": [
        {
            "item": "Chapati with paneer bhurji and cucumber salad",
            "quantity": "2 chapati + 3/4 cup paneer bhurji + 1 cup salad",
            "time": "12:30 PM",
            "calories": 500,
            "protein": 25,
            "carbs": 40,
            "fats": 22
        }
    ],
    "Snack": [
        {
            "item": "Roasted chana and coconut water",
            "quantity": "1/2 cup chana + 1 cup coconut water",
            "time": "5:00 PM",
            "calories": 200,
            "protein": 10,
            "carbs": 20,
            "fats": 6
        }
    ],
    "Dinner": [
        {
            "item": "Vegetable stir fry with tofu",
            "quantity": "1 cup stir fry + 3/4 cup tofu",
            "time": "8:00 PM",
            "calories": 400,
            "protein": 22,
            "carbs": 30,
            "fats": 18
        }
    ]
}
            }
        }
    },
     
    
            "non-vegetarian": {
                 "male": {
                 "18-30": {
                    "sedentary": {
    "Breakfast": [
        {
            "item": "Omelette with vegetables + whole wheat toast",
            "quantity": "2 eggs + 1 cup vegetables + 2 slices toast",
            "time": "8:00 AM",
            "calories": 400,
            "protein": 25,
            "carbs": 30,
            "fats": 18
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken breast + brown rice + mixed greens salad",
            "quantity": "120g chicken + 1 cup brown rice + 1 cup salad",
            "time": "1:00 PM",
            "calories": 550,
            "protein": 40,
            "carbs": 35,
            "fats": 20
        }
    ],
    "Snack": [
        {
            "item": "Greek yogurt with honey",
            "quantity": "150g yogurt + 1 tsp honey",
            "time": "4:30 PM",
            "calories": 150,
            "protein": 10,
            "carbs": 15,
            "fats": 3
        }
    ],
    "Dinner": [
        {
            "item": "Grilled chicken with brown rice and steamed broccoli",
            "quantity": "100g chicken + 1 cup brown rice + 1 cup broccoli",
            "time": "8:00 PM",
            "calories": 500,
            "protein": 35,
            "carbs": 40,
            "fats": 18
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Boiled eggs + Masala Omelette Toast",
            "quantity": "3 boiled eggs + 2 slices whole wheat toast + 1 tbsp butter/ghee + masala omelette (1 egg + veggies)",
            "time": "8:00 AM",
            "calories": 500,
            "protein": 32,
            "carbs": 35,
            "fats": 26
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken wrap with veggies",
            "quantity": "1 wrap with 120g chicken and mixed veggies",
            "time": "1:00 PM",
            "calories": 600,
            "protein": 40,
            "carbs": 45,
            "fats": 20
        }
    ],

    "Snack": [
        {
            "item": "Peanut butter-stuffed dates with almonds",
            "quantity": "3 medium dates + 1tbsp peanut butter + 5 almonds",
            "time": "4:30 PM",
            "calories": 200,
            "protein": 15,
            "carbs": 15,
            "fats": 8
        }
    ],
    "Dinner": [
        {
            "item": "Tandoori Chicken+ Mashed sweet potato + Sauteed beans ",
            "quantity": "1 Chicken leg (120g, skinless) + 1 medium sweet potato + 1 cup beans",
            "time": "8:00 PM",
            "calories": 550,
            "protein": 42,
            "carbs": 35,
            "fats": 18
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Scrambled eggs with spinach + multigrain toast + banana",
            "quantity": "3 eggs + 1 cup spinach + 2 slices toast + 1 banana",
            "time": "7:30 AM",
            "calories": 550,
            "protein": 30,
            "carbs": 45,
            "fats": 22
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken + brown rice + mixed veggies",
            "quantity": "150g chicken + 1 cup brown rice + 1 cup vegetables",
            "time": "1:00 PM",
            "calories": 600,
            "protein": 45,
            "carbs": 40,
            "fats": 20
        }
    ],
    "Snack": [
        {
            "item": "Boiled egg + apple + peanut butter",
            "quantity": "1 egg + 1 medium apple + 1 tbsp peanut butter",
            "time": "4:30 PM",
            "calories": 250,
            "protein": 12,
            "carbs": 22,
            "fats": 12
        }
    ],
    "Dinner": [
        {
            "item": "Grilled chicken with brown rice and steamed broccoli",
            "quantity": "100g chicken + 1 cup brown rice + 1 cup broccoli",
            "time": "8:00 PM",
            "calories": 500,
            "protein": 35,
            "carbs": 40,
            "fats": 18
        }
    ]
}
                },
                "31-50": {
                  "sedentary": {
    "Breakfast": [
        {
            "item": "Boiled eggs + whole wheat toast + orange",
            "quantity": "2 eggs + 2 slices toast + 1 medium orange",
            "time": "8:00 AM",
            "calories": 400,
            "protein": 22,
            "carbs": 35,
            "fats": 18
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken salad with olive oil dressing + brown bread",
            "quantity": "100g chicken + 2 cups salad + 1 tbsp olive oil + 1 slice bread",
            "time": "1:00 PM",
            "calories": 500,
            "protein": 35,
            "carbs": 30,
            "fats": 22
        }
    ],
    "Snack": [
        {
            "item": "Yogurt + walnuts",
            "quantity": "1 cup low-fat yogurt + 5 walnuts",
            "time": "5:00 PM",
            "calories": 200,
            "protein": 10,
            "carbs": 15,
            "fats": 12
        }
    ],
    "Dinner": [
        {
            "item": "Butter Chicken + Roasted vegetables + sweet potato",
            "quantity": "100g chicken thigh (curry cut) + 1 cup veggies + ½ medium sweet potato",
            "time": "8:00 PM",
            "calories": 550,
            "protein": 36,
            "carbs": 40,
            "fats": 20
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Omelette with veggies + multigrain toast + apple",
            "quantity": "2 eggs + ½ cup mixed veggies + 2 slices toast + 1 medium apple",
            "time": "8:00 AM",
            "calories": 450,
            "protein": 25,
            "carbs": 40,
            "fats": 18
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken breast + brown rice + steamed broccoli",
            "quantity": "120g chicken + ¾ cup brown rice + 1 cup broccoli",
            "time": "1:00 PM",
            "calories": 600,
            "protein": 40,
            "carbs": 45,
            "fats": 20
        }
    ],
    "Snack": [
        {
            "item": "Boiled egg + banana",
            "quantity": "1 egg + 1 medium banana",
            "time": "5:00 PM",
            "calories": 200,
            "protein": 9,
            "carbs": 22,
            "fats": 7
        }
    ],
    "Dinner": [
        {
            "item": "Grilled chicken with brown rice and steamed broccoli",
            "quantity": "100g chicken + 1 cup brown rice + 1 cup broccoli",
            "time": "8:00 PM",
            "calories": 500,
            "protein": 35,
            "carbs": 40,
            "fats": 18
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Boiled eggs + whole grain toast + orange juice",
            "quantity": "3 eggs + 2 slices toast + 1 cup juice",
            "time": "7:30 AM",
            "calories": 500,
            "protein": 30,
            "carbs": 35,
            "fats": 25
        }
    ],
    "Lunch": [
        {
            "item": "Chicken breast + millet khichdi + sautéed vegetables",
            "quantity": "150g chicken + 1 cup khichdi + 1 cup vegetables",
            "time": "1:00 PM",
            "calories": 650,
            "protein": 42,
            "carbs": 50,
            "fats": 22
        }
    ],
    "Snack": [
        {
            "item": "Greek yogurt + walnuts",
            "quantity": "1 cup yogurt + 10 walnuts",
            "time": "5:00 PM",
            "calories": 250,
            "protein": 12,
            "carbs": 10,
            "fats": 18
        }
    ],
    "Dinner": [
        {
            "item": "Tandoori Chicken + Mashed sweet potatoes + mixed greens",
            "quantity": "1 Chicken leg (120g, skinless) + 1 medium sweet potato + 1 cup greens",
            "time": "8:00 PM",
            "calories": 550,
            "protein": 42,
            "carbs": 35,
            "fats": 18
        }
    ]
}
                },
                "51+": {
                   "sedentary": {
    "Breakfast": [
        {
            "item": "Oats porridge with skim milk and boiled egg",
            "quantity": "1 cup oats + 1 cup milk + 1 egg",
            "time": "8:00 AM",
            "calories": 320,
            "protein": 18,
            "carbs": 35,
            "fats": 12
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken salad with olive oil dressing",
            "quantity": "100g chicken + 2 cups salad + 1 tbsp olive oil",
            "time": "1:00 PM",
            "calories": 400,
            "protein": 30,
            "carbs": 15,
            "fats": 25
        }
    ],
    "Snack": [
        {
            "item": "Buttermilk + handful of roasted chana",
            "quantity": "1 glass buttermilk + 30g chana",
            "time": "5:00 PM",
            "calories": 180,
            "protein": 9,
            "carbs": 12,
            "fats": 8
        }
    ],
    "Dinner": [
        {
            "item": "Grilled chicken with brown rice and steamed broccoli",
            "quantity": "100g chicken + 1 cup brown rice + 1 cup broccoli",
            "time": "8:00 PM",
            "calories": 500,
            "protein": 35,
            "carbs": 40,
            "fats": 18
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Boiled eggs with whole wheat toast and mixed fruit",
            "quantity": "2 eggs + 2 slices toast + 1/2 cup fruit",
            "time": "8:00 AM",
            "calories": 360,
            "protein": 20,
            "carbs": 30,
            "fats": 16
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken breast with brown rice and stir-fried vegetables",
            "quantity": "100g chicken + 1 cup brown rice + 1 cup veggies",
            "time": "1:00 PM",
            "calories": 500,
            "protein": 35,
            "carbs": 35,
            "fats": 18
        }
    ],
    "Snack": [
        {
            "item": "Low-fat yogurt with walnuts",
            "quantity": "1/2 cup yogurt + 10g walnuts",
            "time": "5:00 PM",
            "calories": 200,
            "protein": 10,
            "carbs": 12,
            "fats": 12
        }
    ],
    "Dinner": [
        {
            "item": "Fish tikka with roti and mixed vegetable soup",
            "quantity": "100g fish + 1 roti + 1 cup soup",
            "time": "7:30 PM",
            "calories": 450,
            "protein": 30,
            "carbs": 30,
            "fats": 18
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Boiled eggs with sautéed spinach and multigrain toast",
            "quantity": "2 eggs + 1 cup spinach + 2 slices toast",
            "time": "8:00 AM",
            "calories": 350,
            "protein": 22,
            "carbs": 28,
            "fats": 16
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken with brown rice and steamed broccoli",
            "quantity": "100g chicken + 1 cup brown rice + 1 cup broccoli",
            "time": "1:00 PM",
            "calories": 500,
            "protein": 35,
            "carbs": 40,
            "fats": 18
        }
    ],
    "Snack": [
        {
            "item": "Greek yogurt with almonds",
            "quantity": "1/2 cup yogurt + 10g almonds",
            "time": "5:00 PM",
            "calories": 200,
            "protein": 12,
            "carbs": 10,
            "fats": 12
        }
    ],
    "Dinner": [
        {
            "item": "Fish curry with chapati and cucumber salad",
            "quantity": "100g fish + 1 chapati + 1/2 cup salad",
            "time": "7:30 PM",
            "calories": 450,
            "protein": 30,
            "carbs": 32,
            "fats": 17
        }
    ]
}
                }
            },
              "female": {   
                 "18-30": {
                   "sedentary": {
    "Breakfast": [
        {
            "item": "Boiled egg with multigrain toast and orange",
            "quantity": "1 egg + 1 toast + 1 orange",
            "time": "8:00 AM",
            "calories": 250,
            "protein": 12,
            "carbs": 28,
            "fats": 9
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken salad with olive oil dressing",
            "quantity": "100g chicken + 1 cup veggies + 1 tsp oil",
            "time": "1:00 PM",
            "calories": 350,
            "protein": 30,
            "carbs": 15,
            "fats": 20
        }
    ],
    "Snack": [
        {
            "item": "Low-fat yogurt with berries",
            "quantity": "1/2 cup yogurt + 1/4 cup berries",
            "time": "4:30 PM",
            "calories": 150,
            "protein": 8,
            "carbs": 18,
            "fats": 4
        }
    ],
    "Dinner": [
        {
            "item": "Egg curry with chapati and cucumber salad",
            "quantity": "1 egg + 1 chapati + 1/2 cup salad",
            "time": "7:30 PM",
            "calories": 300,
            "protein": 16,
            "carbs": 24,
            "fats": 12
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Oats porridge with skim milk and boiled egg",
            "quantity": "1/2 cup oats + 1 cup milk + 1 egg",
            "time": "8:00 AM",
            "calories": 300,
            "protein": 18,
            "carbs": 30,
            "fats": 10
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken with brown rice and sautéed vegetables",
            "quantity": "100g chicken + 1/2 cup brown rice + 1 cup veggies",
            "time": "1:00 PM",
            "calories": 450,
            "protein": 32,
            "carbs": 35,
            "fats": 16
        }
    ],
    "Snack": [
        {
            "item": "Boiled egg with green tea",
            "quantity": "1 egg + 1 cup tea",
            "time": "5:00 PM",
            "calories": 90,
            "protein": 6,
            "carbs": 2,
            "fats": 5
        }
    ],
    "Dinner": [
        {
            "item": "Grilled chicken with brown rice and steamed broccoli",
            "quantity": "100g chicken + 1 cup brown rice + 1 cup broccoli",
            "time": "8:00 PM",
            "calories": 500,
            "protein": 35,
            "carbs": 40,
            "fats": 18
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Scrambled eggs with whole grain toast and a banana",
            "quantity": "2 eggs + 2 slices toast + 1 banana",
            "time": "8:00 AM",
            "calories": 400,
            "protein": 22,
            "carbs": 38,
            "fats": 18
        }
    ],
    "Lunch": [
        {
            "item": "Chicken breast with brown rice and mixed salad",
            "quantity": "120g chicken + 1 cup rice + 1 cup salad",
            "time": "1:00 PM",
            "calories": 500,
            "protein": 35,
            "carbs": 45,
            "fats": 15
        }
    ],
    "Snack": [
        {
            "item": "Greek yogurt with nuts",
            "quantity": "1 cup yogurt + 10 almonds",
            "time": "5:00 PM",
            "calories": 220,
            "protein": 14,
            "carbs": 12,
            "fats": 10
        }
    ],
    "Dinner": [
        {
            "item": "Grilled fish with sweet potato and steamed broccoli",
            "quantity": "100g fish + 1 medium sweet potato + 1 cup broccoli",
            "time": "8:00 PM",
            "calories": 450,
            "protein": 30,
            "carbs": 40,
            "fats": 18
        }
    ]
}
    },
    "31-50": {
       "sedentary": {
    "Breakfast": [
        {
            "item": "Omelette with spinach and 1 slice whole wheat toast",
            "quantity": "2 eggs + 1 slice toast + 1/4 cup spinach",
            "time": "8:00 AM",
            "calories": 300,
            "protein": 18,
            "carbs": 20,
            "fats": 15
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken salad with olive oil dressing",
            "quantity": "80g chicken + 2 cups salad + 1 tbsp olive oil",
            "time": "1:00 PM",
            "calories": 400,
            "protein": 30,
            "carbs": 15,
            "fats": 25
        }
    ],
    "Snack": [
        {
            "item": "Boiled egg and apple",
            "quantity": "1 egg + 1 medium apple",
            "time": "5:00 PM",
            "calories": 160,
            "protein": 7,
            "carbs": 18,
            "fats": 7
        }
    ],
    "Dinner": [
        {
            "item": "Fish stir-fry with mixed vegetables",
            "quantity": "80g fish + 1.5 cups vegetables",
            "time": "8:00 PM",
            "calories": 380,
            "protein": 28,
            "carbs": 20,
            "fats": 18
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Scrambled eggs with mixed vegetables and a slice of multigrain toast",
            "quantity": "2 eggs + 1/2 cup vegetables + 1 toast",
            "time": "8:00 AM",
            "calories": 320,
            "protein": 20,
            "carbs": 22,
            "fats": 18
        }
    ],
    "Lunch": [
        {
            "item": "Chicken curry with brown rice and salad",
            "quantity": "90g chicken + 1 cup rice + 1 cup salad",
            "time": "1:00 PM",
            "calories": 450,
            "protein": 32,
            "carbs": 35,
            "fats": 20
        }
    ],
    "Snack": [
        {
            "item": "Greek yogurt with berries",
            "quantity": "1/2 cup yogurt + 1/4 cup berries",
            "time": "5:00 PM",
            "calories": 180,
            "protein": 10,
            "carbs": 20,
            "fats": 7
        }
    ],
    "Dinner": [
        {
            "item": "Grilled fish with steamed broccoli and sweet potato",
            "quantity": "100g fish + 1 cup broccoli + 1/2 sweet potato",
            "time": "8:00 PM",
            "calories": 420,
            "protein": 30,
            "carbs": 25,
            "fats": 18
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Boiled eggs with multigrain toast and papaya",
            "quantity": "2 eggs + 2 slices toast + 1/2 cup papaya",
            "time": "8:00 AM",
            "calories": 380,
            "protein": 20,
            "carbs": 32,
            "fats": 18
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken with brown rice and sautéed vegetables",
            "quantity": "100g chicken + 1 cup brown rice + 1 cup vegetables",
            "time": "1:00 PM",
            "calories": 520,
            "protein": 35,
            "carbs": 45,
            "fats": 18
        }
    ],
    "Snack": [
        {
            "item": "Boiled egg and fruit smoothie",
            "quantity": "1 egg + 1 cup smoothie",
            "time": "5:00 PM",
            "calories": 230,
            "protein": 14,
            "carbs": 20,
            "fats": 10
        }
    ],
    "Dinner": [
        {
            "item": "Chicken curry with brown rice and salad",
            "quantity": "90g chicken + 1 cup rice + 1 cup salad",
            "time": "1:00 PM",
            "calories": 450,
            "protein": 32,
            "carbs": 35,
            "fats": 20
        }
    ]
}
    },
    "51+": {
       "sedentary": {
    "Breakfast": [
        {
            "item": "Boiled egg with oats and a slice of multigrain toast",
            "quantity": "1 egg + 1/2 cup oats + 1 toast",
            "time": "8:00 AM",
            "calories": 280,
            "protein": 15,
            "carbs": 30,
            "fats": 10
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken salad with olive oil dressing",
            "quantity": "90g chicken + 1.5 cup salad + 1 tsp olive oil",
            "time": "1:00 PM",
            "calories": 350,
            "protein": 28,
            "carbs": 12,
            "fats": 20
        }
    ],
    "Snack": [
        {
            "item": "Low-fat paneer cubes with cucumber sticks",
            "quantity": "40g paneer + 1/2 cup cucumber",
            "time": "5:00 PM",
            "calories": 150,
            "protein": 12,
            "carbs": 5,
            "fats": 9
        }
    ],
    "Dinner": [
        {
            "item": "Fish stew with vegetables",
            "quantity": "80g fish + 1 cup mixed vegetables",
            "time": "7:30 PM",
            "calories": 380,
            "protein": 30,
            "carbs": 15,
            "fats": 18
        }
    ]
},
"moderate": {
    "Breakfast": [
        {
            "item": "Vegetable omelette with multigrain toast and a glass of milk",
            "quantity": "2 eggs + 1 toast + 150 ml milk",
            "time": "8:00 AM",
            "calories": 350,
            "protein": 22,
            "carbs": 28,
            "fats": 18
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken with brown rice and steamed broccoli",
            "quantity": "100g chicken + 3/4 cup brown rice + 1/2 cup broccoli",
            "time": "1:00 PM",
            "calories": 420,
            "protein": 32,
            "carbs": 35,
            "fats": 14
        }
    ],
    "Snack": [
        {
            "item": "Boiled egg and fruit salad",
            "quantity": "1 egg + 1/2 cup seasonal fruits",
            "time": "5:00 PM",
            "calories": 160,
            "protein": 8,
            "carbs": 15,
            "fats": 7
        }
    ],
    "Dinner": [
        {
            "item": "Fish curry with brown rice and sautéed vegetables",
            "quantity": "90g fish + 1/2 cup brown rice + 1 cup vegetables",
            "time": "7:30 PM",
            "calories": 400,
            "protein": 30,
            "carbs": 25,
            "fats": 17
        }
    ]
},
"active": {
    "Breakfast": [
        {
            "item": "Scrambled eggs with spinach, 2 slices whole wheat toast, and a glass of milk",
            "quantity": "2 eggs + 1/2 cup spinach + 2 toast + 150 ml milk",
            "time": "8:00 AM",
            "calories": 420,
            "protein": 28,
            "carbs": 30,
            "fats": 20
        }
    ],
    "Lunch": [
        {
            "item": "Grilled chicken breast, brown rice, mixed vegetables, and a small salad",
            "quantity": "120g chicken + 1 cup brown rice + 1 cup vegetables",
            "time": "1:00 PM",
            "calories": 480,
            "protein": 36,
            "carbs": 38,
            "fats": 16
        }
    ],
    "Snack": [
        {
            "item": "Boiled egg and a banana",
            "quantity": "1 egg + 1 medium banana",
            "time": "5:00 PM",
            "calories": 180,
            "protein": 8,
            "carbs": 22,
            "fats": 6
        }
    ],
    "Dinner": [
        {
            "item": "Baked fish with sweet potato and steamed beans",
            "quantity": "100g fish + 1/2 cup sweet potato + 1 cup beans",
            "time": "7:30 PM",
            "calories": 440,
            "protein": 32,
            "carbs": 28,
            "fats": 18
        }
    ]
}
                }
            }

        } 
    },

    "muscle_gain": {
        "vegetarian": {
            "male": {
                "18-30": {
                    "sedentary": {
                        "breakfast": [
                            {
                                "item": "Oats with Milk and Nuts",
                                "quantity": "1 bowl",
                                "time": "8:00 AM",
                                "calories": 400,
                                "protein": 18,
                                "carbs": 45,
                                "fats": 15
                            }
                        ],
                        
                        "snack": [
                        {
                            "item": "Boiled Moong + Banana",
                            "quantity": "1 small bowl + 1 banana",
                            "time": "11:00 AM",
                            "calories": 200,
                            "protein": 10,
                            "carbs": 30,
                            "fats": 2
                        }
                        ],
                        "lunch": [
                            {
                                "item": "Multigrain Roti",
                                "quantity": "2 medium",
                                "time": "1:00 PM",
                                "calories": 220,
                                "protein": 6,
                                "carbs": 30,
                                "fats": 5
                            },
                            {
                                "item": "Rajma",
                                "quantity": "1 cup",
                                "time": "1:00 PM",
                                "calories": 250,
                                "protein": 12,
                                "carbs": 30,
                                "fats": 6
                            },
                            {
                                "item": "Curd",
                                "quantity": "1 small bowl",
                                "time": "1:00 PM",
                                "calories": 60,
                                "protein": 4,
                                "carbs": 3,
                                "fats": 2
                            }
                        ],
                        "post_workout":[
                             {
                            "item": "Whey Protein in Water + 4 Soaked Almonds",
                            "quantity": "1 scoop + 4 almonds",
                            "time": "6:00 PM (if working out)",
                            "calories": 180,
                            "protein": 25,
                            "carbs": 5,
                            "fats": 4
                        }
                        ],
                        "dinner": [
                            {
                                "item": "Vegetable Dalia",
                                "quantity": "1.5 bowls",
                                "time": "8:00 PM",
                                "calories": 350,
                                "protein": 12,
                                "carbs": 50,
                                "fats": 8
                            },
                            {
                                "item": "Paneer Tikka",
                                "quantity": "100 gm",
                                 "time": "8:00 PM",
                                "calories": 200,
                                "protein": 18,
                                "carbs": 5,
                                "fats": 14
                            }
                        ],                            
                        
                    },

                    "moderate": {
                         "breakfast": [
                                       {
                                        "item": "Paneer Stuffed Paratha with Curd",
                                        "quantity": "2 medium + 1 cup curd",
                                        "time": "8:00 AM",
                                        "calories": 550,
                                        "protein": 25,
                                        "carbs": 55,
                                        "fats": 22
                                        }
                                       ],
    "snack_1": [
        {
            "item": "Peanut Butter on Whole Wheat Bread + Apple",
            "quantity": "2 slices + 1 apple",
            "time": "11:00 AM",
            "calories": 300,
            "protein": 10,
            "carbs": 35,
            "fats": 15
        }
    ],
    "lunch": [
        {
            "item": "Brown Rice + Dal + Mixed Veg + Salad",
            "quantity": "1.5 cups + 1 cup + 1 cup + 1 cup",
            "time": "2:00 PM",
            "calories": 700,
            "protein": 30,
            "carbs": 85,
            "fats": 20
        }
    ],
    "snack_2": [
        {
            "item": "Protein Shake + Handful of Nuts",
            "quantity": "1 scoop + 10 almonds",
            "time": "5:00 PM",
            "calories": 350,
            "protein": 30,
            "carbs": 10,
            "fats": 15
        }
    ],
    "dinner": [
        {
            "item": "brown rice + Soya Chunk Curry + Steamed Broccoli",
            "quantity": "1 cup + 1 cup + 1 cup",
            "time": "8:30 PM",
            "calories": 600,
            "protein": 35,
            "carbs": 50,
            "fats": 18
        }
    ],
    "post_workout": [
        {
            "item": "Banana + Whey Protein Shake",
            "quantity": "1 banana + 1 scoop",
            "time": "After Workout",
            "calories": 300,
            "protein": 27,
            "carbs": 28,
            "fats": 2
        }
    ],                              
                  },
                  
    "active": {
        "Breakfast": [
            {
                "item": "Oats porridge with milk, nuts, and peanut butter",
                "quantity": "1 bowl",
                "time": "8:00 AM",
                "calories": 400,
                "protein": 15,
                "carbs": 45,
                "fats": 18
            },
            {
                "item": "Banana",
                "quantity": "1 medium",
                "time": "8:00 AM",
                "calories": 100,
                "protein": 1,
                "carbs": 27,
                "fats": 0.3
            }
        ],
        "Snack": [
            {
                "item": "Peanut Butter Sandwich (Whole Wheat)",
                "quantity": "2 slices bread + 2 tbsp peanut butter",
                "time": "11:00 AM",
                "calories": 350,
                "protein": 12,
                "carbs": 30,
                "fats": 22
            },
            {
                "item": "Whey protein shake (or plant protein)",
                "quantity": "1 scoop",
                "time": "11:30 AM",
                "calories": 120,
                "protein": 24,
                "carbs": 2,
                "fats": 1.5
            }
        ],
        "Lunch": [
            {
                "item": "Brown rice",
                "quantity": "1 cup cooked",
                "time": "2:00 PM",
                "calories": 215,
                "protein": 5,
                "carbs": 45,
                "fats": 1.5
            },
            {
                "item": "Moong dal tadka",
                "quantity": "1 cup",
                "time": "2:00 PM",
                "calories": 180,
                "protein": 12,
                "carbs": 25,
                "fats": 5
            },
            {
                "item": "Paneer bhurji (made with minimal oil)",
                "quantity": "100 gm",
                "time": "2:00 PM",
                "calories": 250,
                "protein": 16,
                "carbs": 6,
                "fats": 18
            },
            {
                "item": "Cucumber & carrot salad",
                "quantity": "1 bowl",
                "time": "2:00 PM",
                "calories": 40,
                "protein": 1,
                "carbs": 9,
                "fats": 0
            }
        ],
        "Post Workout": [
            {
                "item": "Banana + peanut butter shake",
                "quantity": "1 glass",
                "time": "6:30 PM",
                "calories": 300,
                "protein": 10,
                "carbs": 30,
                "fats": 16
            },
            {
                "item": "Roasted chana",
                "quantity": "1 handful (30 gm)",
                "time": "6:45 PM",
                "calories": 120,
                "protein": 7,
                "carbs": 15,
                "fats": 3
            }
        ],
        "Dinner": [
            {
                "item": "Whole wheat roti",
                "quantity": "2 pieces",
                "time": "9:00 PM",
                "calories": 200,
                "protein": 6,
                "carbs": 36,
                "fats": 4
            },
            {
                "item": "Rajma curry",
                "quantity": "1 cup",
                "time": "9:00 PM",
                "calories": 210,
                "protein": 13,
                "carbs": 30,
                "fats": 4
            },
               {
                "item": "Boiled mixed veggies with olive oil drizzle",
                "quantity": "1 bowl",
                "time": "9:00 PM",
                "calories": 80,
                "protein": 2,
                "carbs": 10,
                "fats": 4
                }
              ]
           }
         },
         
     "31-50":{
     "sedentary":{
        "Breakfast": [
            {
                "item": "Vegetable upma with peanuts",
                "quantity": "1 bowl",
                "time": "8:00 AM",
                "calories": 300,
                "protein": 7,
                "carbs": 40,
                "fats": 10
            },
            {
                "item": "Low-fat milk with soaked almonds",
                "quantity": "1 glass + 6 almonds",
                "time": "8:00 AM",
                "calories": 180,
                "protein": 8,
                "carbs": 12,
                "fats": 10
            }
        ],
        "Snack": [
            {
                "item": "Sprouted moong chaat",
                "quantity": "1 bowl",
                "time": "11:00 AM",
                "calories": 200,
                "protein": 14,
                "carbs": 22,
                "fats": 4
            },
            {
                "item": "Green tea (optional)",
                "quantity": "1 cup",
                "time": "11:15 AM",
                "calories": 5,
                "protein": 0,
                "carbs": 1,
                "fats": 0
            }
        ],
        "Lunch": [
            {
                "item": "Multigrain roti",
                "quantity": "2 pieces",
                "time": "2:00 PM",
                "calories": 200,
                "protein": 6,
                "carbs": 34,
                "fats": 4
            },
            {
                "item": "Mixed dal (toor + moong + masoor)",
                "quantity": "1 cup",
                "time": "2:00 PM",
                "calories": 180,
                "protein": 12,
                "carbs": 22,
                "fats": 4
            },
            {
                "item": "Curd (low-fat)",
                "quantity": "1 small bowl",
                "time": "2:00 PM",
                "calories": 80,
                "protein": 4,
                "carbs": 6,
                "fats": 4
            },
            {
                "item": "Salad (cucumber, beetroot, tomato)",
                "quantity": "1 bowl",
                "time": "2:00 PM",
                "calories": 40,
                "protein": 1,
                "carbs": 9,
                "fats": 0
            }
        ],
        "Post Workout / Evening Snack": [
            {
                "item": "Fruit smoothie with Greek yogurt and flax seeds",
                "quantity": "1 glass",
                "time": "5:30 PM",
                "calories": 250,
                "protein": 10,
                "carbs": 30,
                "fats": 10
            },
            {
                "item": "Roasted peanuts or chana",
                "quantity": "1 handful (30 gm)",
                "time": "5:45 PM",
                "calories": 120,
                "protein": 6,
                "carbs": 8,
                "fats": 9
            }
        ],
        "Dinner": [
            {
                "item": "Paneer tikka (grilled, less oil)",
                "quantity": "100 gm",
                "time": "8:30 PM",
                "calories": 250,
                "protein": 18,
                "carbs": 6,
                "fats": 18
            },
            {
                "item": "Vegetable khichdi (with moong dal)",
                "quantity": "1 bowl",
                "time": "8:30 PM",
                "calories": 220,
                "protein": 10,
                "carbs": 35,
                "fats": 6
            },
            {
                "item": "Steamed broccoli & carrot with lemon and salt",
                "quantity": "1 bowl",
                "time": "8:30 PM",
                "calories": 60,
                "protein": 2,
                "carbs": 10,
                "fats": 2
            }
        ]
    },
    "moderate":{
        "Breakfast": [
            {
                "item": "Oats porridge with milk, banana & chia seeds",
                "quantity": "1 large bowl",
                "time": "8:00 AM",
                "calories": 400,
                "protein": 15,
                "carbs": 50,
                "fats": 14
            },
            {
                "item": "Boiled eggs (optional for ovo-vegetarian)",
                "quantity": "2 whole",
                "time": "8:15 AM",
                "calories": 140,
                "protein": 12,
                "carbs": 1,
                "fats": 10
            }
        ],
        "Snack": [
            {
                "item": "Peanut butter on whole wheat toast",
                "quantity": "2 slices + 1 tbsp",
                "time": "11:00 AM",
                "calories": 280,
                "protein": 10,
                "carbs": 20,
                "fats": 18
            },
            {
                "item": "Buttermilk (chaas)",
                "quantity": "1 glass",
                "time": "11:30 AM",
                "calories": 50,
                "protein": 2,
                "carbs": 5,
                "fats": 2
            }
        ],
        "Lunch": [
            {
                "item": "Brown rice",
                "quantity": "1 cup cooked",
                "time": "2:00 PM",
                "calories": 215,
                "protein": 5,
                "carbs": 45,
                "fats": 2
            },
            {
                "item": "Rajma curry (kidney beans)",
                "quantity": "1 bowl",
                "time": "2:00 PM",
                "calories": 220,
                "protein": 12,
                "carbs": 30,
                "fats": 4
            },
            {
                "item": "Cucumber + Carrot salad with lemon & seeds",
                "quantity": "1 bowl",
                "time": "2:00 PM",
                "calories": 60,
                "protein": 2,
                "carbs": 10,
                "fats": 2
            },
            {
                "item": "Curd (low-fat)",
                "quantity": "1 bowl",
                "time": "2:00 PM",
                "calories": 80,
                "protein": 4,
                "carbs": 6,
                "fats": 4
            }
        ],
        "Post Workout / Evening Snack": [
            {
                "item": "Homemade protein shake (milk + banana + peanut butter + oats)",
                "quantity": "1 large glass",
                "time": "5:30 PM",
                "calories": 400,
                "protein": 20,
                "carbs": 40,
                "fats": 18
            },
            {
                "item": "Roasted chana or protein bar",
                "quantity": "1 handful or 1 bar",
                "time": "5:45 PM",
                "calories": 150,
                "protein": 8,
                "carbs": 10,
                "fats": 6
            }
        ],
        "Dinner": [
            {
                "item": "Paneer bhurji (low-oil)",
                "quantity": "100 gm paneer",
                "time": "8:30 PM",
                "calories": 265,
                "protein": 17,
                "carbs": 6,
                "fats": 20
            },
            {
                "item": "Chapati (multigrain)",
                "quantity": "2 medium",
                "time": "8:30 PM",
                "calories": 200,
                "protein": 6,
                "carbs": 34,
                "fats": 4
            },
            {
                "item": "Steamed vegetables with olive oil drizzle",
                "quantity": "1 bowl",
                "time": "8:30 PM",
                "calories": 80,
                "protein": 2,
                "carbs": 10,
                "fats": 4
            }
        ]
    },
    "active":{
        "Breakfast": [
            {
                "item": "Paneer-stuffed paratha with ghee",
                "quantity": "2 medium with 1 tsp ghee",
                "time": "8:00 AM",
                "calories": 500,
                "protein": 20,
                "carbs": 40,
                "fats": 25
            },
            {
                "item": "Masala chai with low-fat milk",
                "quantity": "1 cup",
                "time": "8:15 AM",
                "calories": 100,
                "protein": 3,
                "carbs": 10,
                "fats": 4
            }
        ],
        "Snack": [
            {
                "item": "Mixed dry fruits (almonds, walnuts, raisins)",
                "quantity": "1 handful (30g)",
                "time": "11:00 AM",
                "calories": 180,
                "protein": 5,
                "carbs": 10,
                "fats": 15
            },
            {
                "item": "Fruit smoothie (banana + curd + seeds)",
                "quantity": "1 glass",
                "time": "11:30 AM",
                "calories": 250,
                "protein": 8,
                "carbs": 35,
                "fats": 6
            }
        ],
        "Lunch": [
            {
                "item": " brown rice",
                "quantity": "1 cup cooked",
                "time": "2:00 PM",
                "calories": 220,
                "protein": 6,
                "carbs": 40,
                "fats": 3
            },
            {
                "item": "Mixed dal tadka",
                "quantity": "1.5 bowls",
                "time": "2:00 PM",
                "calories": 280,
                "protein": 16,
                "carbs": 25,
                "fats": 10
            },
            {
                "item": "Beetroot-carrot salad with seeds & lemon",
                "quantity": "1 bowl",
                "time": "2:00 PM",
                "calories": 70,
                "protein": 2,
                "carbs": 10,
                "fats": 3
            },
            {
                "item": "Buttermilk",
                "quantity": "1 glass",
                "time": "2:15 PM",
                "calories": 50,
                "protein": 2,
                "carbs": 5,
                "fats": 2
            }
        ],
        "Post Workout / Evening Snack": [
            {
                "item": "Homemade protein shake (milk + oats + banana + peanut butter + whey/soya powder)",
                "quantity": "1 tall glass",
                "time": "5:30 PM",
                "calories": 450,
                "protein": 25,
                "carbs": 40,
                "fats": 20
            },
            {
                "item": "Roasted chickpeas or boiled corn",
                "quantity": "1 cup",
                "time": "5:45 PM",
                "calories": 120,
                "protein": 6,
                "carbs": 18,
                "fats": 2
            }
        ],
        "Dinner": [
            {
                "item": "Soyabean curry",
                "quantity": "1 bowl (50g soya chunks)",
                "time": "8:30 PM",
                "calories": 300,
                "protein": 25,
                "carbs": 10,
                "fats": 15
            },
            {
                "item": "Chapati (multigrain)",
                "quantity": "2 medium",
                "time": "8:30 PM",
                "calories": 200,
                "protein": 6,
                "carbs": 34,
                "fats": 4
            },
            {
                "item": "Steamed broccoli, capsicum, carrots with olive oil",
                "quantity": "1 bowl",
                "time": "8:30 PM",
                "calories": 80,
                "protein": 3,
                "carbs": 10,
                "fats": 3
            }
        ]
    },
},
 "51+":{
     "sedentary":{
        "Breakfast": [
            {
                "item": "Moong dal chilla (with paneer filling)",
                "quantity": "2 medium",
                "time": "8:00 AM",
                "calories": 300,
                "protein": 18,
                "carbs": 25,
                "fats": 10
            },
            {
                "item": "Haldi milk (low-fat)",
                "quantity": "1 cup",
                "time": "8:30 AM",
                "calories": 120,
                "protein": 6,
                "carbs": 10,
                "fats": 6
            }
        ],
        "Snack": [
            {
                "item": "Roasted makhana",
                "quantity": "1 cup (30g)",
                "time": "11:00 AM",
                "calories": 100,
                "protein": 3,
                "carbs": 15,
                "fats": 3
            },
            {
                "item": "Guava or apple",
                "quantity": "1 medium",
                "time": "11:30 AM",
                "calories": 70,
                "protein": 1,
                "carbs": 15,
                "fats": 0
            }
        ],
        "Lunch": [
            {
                "item": "Roti (ragi or multigrain)",
                "quantity": "2 medium",
                "time": "1:30 PM",
                "calories": 180,
                "protein": 6,
                "carbs": 30,
                "fats": 3
            },
            {
                "item": "Palak paneer (less oil)",
                "quantity": "1 bowl",
                "time": "1:30 PM",
                "calories": 250,
                "protein": 15,
                "carbs": 10,
                "fats": 15
            },
            {
                "item": "Cucumber & tomato salad",
                "quantity": "1 small bowl",
                "time": "1:30 PM",
                "calories": 50,
                "protein": 1,
                "carbs": 8,
                "fats": 2
            },
            {
                "item": "Lassi (unsweetened)",
                "quantity": "1 glass",
                "time": "2:00 PM",
                "calories": 80,
                "protein": 4,
                "carbs": 6,
                "fats": 4
            }
        ],
        "Evening Snack": [
            {
                "item": "Homemade besan protein ladoo (with jaggery)",
                "quantity": "1 small",
                "time": "5:30 PM",
                "calories": 130,
                "protein": 4,
                "carbs": 10,
                "fats": 8
            },
            {
                "item": "Herbal tea (tulsi/ginger)",
                "quantity": "1 cup",
                "time": "5:45 PM",
                "calories": 15,
                "protein": 0,
                "carbs": 3,
                "fats": 0
            }
        ],
        "Dinner": [
            {
                "item": "Vegetable khichdi (dal + rice + veggies + ghee)",
                "quantity": "1 bowl",
                "time": "7:30 PM",
                "calories": 300,
                "protein": 12,
                "carbs": 35,
                "fats": 10
            },
            {
                "item": "Boiled egg (optional for ovo-vegetarians)",
                "quantity": "1 egg",
                "time": "7:30 PM",
                "calories": 70,
                "protein": 6,
                "carbs": 1,
                "fats": 5
            },
            {
                "item": "Warm water or herbal tea before bed",
                "quantity": "1 glass",
                "time": "9:00 PM",
                "calories": 0,
                "protein": 0,
                "carbs": 0,
                "fats": 0
            }
        ]
    },
    "moderate":{
        "Breakfast": [
            {
                "item": "Vegetable oats upma with peanuts",
                "quantity": "1 medium bowl",
                "time": "8:00 AM",
                "calories": 320,
                "protein": 10,
                "carbs": 35,
                "fats": 12
            },
            {
                "item": "Low-fat milk with soaked almonds (5 pcs)",
                "quantity": "1 glass",
                "time": "8:30 AM",
                "calories": 150,
                "protein": 8,
                "carbs": 12,
                "fats": 8
            }
        ],
        "Snack": [
            {
                "item": "Fruit smoothie (banana + curd + seeds)",
                "quantity": "1 glass",
                "time": "11:00 AM",
                "calories": 200,
                "protein": 6,
                "carbs": 28,
                "fats": 6
            },
            {
                "item": "Roasted chana",
                "quantity": "1 handful (25g)",
                "time": "11:30 AM",
                "calories": 120,
                "protein": 6,
                "carbs": 18,
                "fats": 2
            }
        ],
        "Lunch": [
            {
                "item": "Multigrain roti",
                "quantity": "2 medium",
                "time": "1:30 PM",
                "calories": 180,
                "protein": 6,
                "carbs": 30,
                "fats": 3
            },
            {
                "item": "Rajma curry (low oil)",
                "quantity": "1 bowl",
                "time": "1:30 PM",
                "calories": 230,
                "protein": 12,
                "carbs": 25,
                "fats": 7
            },
            {
                "item": "Beetroot & carrot salad",
                "quantity": "1 small bowl",
                "time": "1:30 PM",
                "calories": 50,
                "protein": 1,
                "carbs": 8,
                "fats": 1
            },
            {
                "item": "Buttermilk (chaas, no salt)",
                "quantity": "1 glass",
                "time": "2:00 PM",
                "calories": 35,
                "protein": 2,
                "carbs": 4,
                "fats": 1
            }
        ],
        "Evening Snack": [
            {
                "item": "Sprouted moong chaat with lemon",
                "quantity": "1 bowl",
                "time": "5:30 PM",
                "calories": 150,
                "protein": 9,
                "carbs": 15,
                "fats": 3
            },
            {
                "item": "Herbal tea or green tea",
                "quantity": "1 cup",
                "time": "6:00 PM",
                "calories": 5,
                "protein": 0,
                "carbs": 1,
                "fats": 0
            }
        ],
        "Dinner": [
            {
                "item": "brown rice khichdi with dal & veggies",
                "quantity": "1 bowl",
                "time": "7:30 PM",
                "calories": 300,
                "protein": 12,
                "carbs": 32,
                "fats": 10
            },
            {
                "item": "Paneer bhurji (low oil)",
                "quantity": "1 small bowl",
                "time": "7:30 PM",
                "calories": 220,
                "protein": 14,
                "carbs": 5,
                "fats": 15
            },
            {
                "item": "Warm haldi milk (low-fat)",
                "quantity": "1 cup",
                "time": "9:00 PM",
                "calories": 120,
                "protein": 6,
                "carbs": 10,
                "fats": 6
            }
        ]
    },
    "active":{
        "Breakfast": [
            {
                "item": "Paneer-stuffed multigrain paratha with ghee",
                "quantity": "2 medium",
                "time": "7:30 AM",
                "calories": 400,
                "protein": 16,
                "carbs": 35,
                "fats": 20
            },
            {
                "item": "Haldi milk (low-fat)",
                "quantity": "1 glass",
                "time": "8:00 AM",
                "calories": 120,
                "protein": 6,
                "carbs": 10,
                "fats": 6
            }
        ],
        "Snack": [
            {
                "item": "Mixed nuts (almonds, walnuts, seeds)",
                "quantity": "1 handful (25g)",
                "time": "10:30 AM",
                "calories": 180,
                "protein": 5,
                "carbs": 6,
                "fats": 16
            },
            {
                "item": "Seasonal fruit (papaya/mango/melon)",
                "quantity": "1 bowl",
                "time": "11:00 AM",
                "calories": 100,
                "protein": 1,
                "carbs": 24,
                "fats": 0
            }
        ],
        "Lunch": [
            {
                "item": "Brown rice + Sambar with vegetables",
                "quantity": "1 bowl rice + 1 bowl sambar",
                "time": "1:30 PM",
                "calories": 400,
                "protein": 14,
                "carbs": 50,
                "fats": 12
            },
            {
                "item": "Cucumber + tomato salad with lemon",
                "quantity": "1 small bowl",
                "time": "1:45 PM",
                "calories": 40,
                "protein": 1,
                "carbs": 6,
                "fats": 1
            },
            {
                "item": "Buttermilk with jeera",
                "quantity": "1 glass",
                "time": "2:00 PM",
                "calories": 35,
                "protein": 2,
                "carbs": 4,
                "fats": 1
            }
        ],
        "Post Workout": [
            {
                "item": "Banana + peanut butter shake (with low-fat milk)",
                "quantity": "1 glass",
                "time": "5:30 PM",
                "calories": 300,
                "protein": 10,
                "carbs": 30,
                "fats": 15
            },
            {
                "item": "Roasted soy chunks",
                "quantity": "1/2 cup",
                "time": "6:00 PM",
                "calories": 150,
                "protein": 15,
                "carbs": 5,
                "fats": 6
            }
        ],
        "Dinner": [
            {
                "item": "Vegetable dal khichdi (moong + veggies)",
                "quantity": "1.5 bowls",
                "time": "7:30 PM",
                "calories": 350,
                "protein": 12,
                "carbs": 40,
                "fats": 10
            },
            {
                "item": "Sauteed tofu with spinach",
                "quantity": "1 small bowl",
                "time": "8:00 PM",
                "calories": 200,
                "protein": 14,
                "carbs": 5,
                "fats": 14
            }
        ]
    },
}
            },
          "female":{
             "18-30":{
                "sedentary":{
                  "Breakfast": [
                     {
                      "item": "Besan chilla with paneer filling",
                      "quantity": "2 medium",
                      "time": "8:00 AM",
                      "calories": 280,
                      "protein": 14,
                      "carbs": 24,
                      "fats": 14
                    },
            {
                "item": "Low-fat milk with soaked almonds",
                "quantity": "1 glass + 5 almonds",
                "time": "8:30 AM",
                "calories": 150,
                "protein": 6,
                "carbs": 10,
                "fats": 9
            }
        ],
        "Snack": [
            {
                "item": "Boiled chana salad with lemon and chaat masala",
                "quantity": "1 small bowl",
                "time": "11:00 AM",
                "calories": 120,
                "protein": 6,
                "carbs": 15,
                "fats": 3
            },
            {
                "item": "Fruit (apple/pear)",
                "quantity": "1 medium",
                "time": "11:30 AM",
                "calories": 90,
                "protein": 0.5,
                "carbs": 20,
                "fats": 0
            }
        ],
        "Lunch": [
            {
                "item": "Chapati with moong dal and mixed sabzi",
                "quantity": "2 chapatis + 1 bowl dal + 1 bowl sabzi",
                "time": "1:30 PM",
                "calories": 400,
                "protein": 14,
                "carbs": 40,
                "fats": 12
            },
            {
                "item": "Curd with jeera powder",
                "quantity": "1 small bowl",
                "time": "2:00 PM",
                "calories": 80,
                "protein": 4,
                "carbs": 6,
                "fats": 3
            }
        ],
        "Post Workout / Evening Snack": [
            {
                "item": "Banana + peanut butter (optional if no workout)",
                "quantity": "1 medium banana + 1 tbsp peanut butter",
                "time": "5:30 PM",
                "calories": 210,
                "protein": 4,
                "carbs": 27,
                "fats": 10
            }
        ],
        "Dinner": [
            {
                "item": "Vegetable pulao with paneer cubes",
                "quantity": "1.5 bowls",
                "time": "7:30 PM",
                "calories": 350,
                "protein": 12,
                "carbs": 35,
                "fats": 14
            },
                  {
                    "item": "Steamed broccoli and carrot salad",
                    "quantity": "1 bowl",
                    "time": "8:00 PM",
                    "calories": 60,
                    "protein": 3,
                    "carbs": 10,
                    "fats": 2
                   }
                ]
            },
             "moderate":{
        "Breakfast": [
            {
                "item": "Oats with milk, chia seeds, and chopped banana",
                "quantity": "1 bowl",
                "time": "8:00 AM",
                "calories": 320,
                "protein": 12,
                "carbs": 42,
                "fats": 10
            },
            {
                "item": "Boiled egg whites or paneer cubes (for veg)",
                "quantity": "3 egg whites or 50g paneer",
                "time": "8:30 AM",
                "calories": 90,
                "protein": 9,
                "carbs": 1,
                "fats": 5
            }
        ],
        "Snack": [
            {
                "item": "Fruit chaat with chia seeds",
                "quantity": "1 medium bowl",
                "time": "11:00 AM",
                "calories": 130,
                "protein": 2,
                "carbs": 26,
                "fats": 3
            }
        ],
        "Lunch": [
            {
                "item": "brown rice with rajma and salad",
                "quantity": "1 bowl rice + 1 bowl rajma + salad",
                "time": "1:30 PM",
                "calories": 450,
                "protein": 16,
                "carbs": 50,
                "fats": 14
            },
            {
                "item": "Buttermilk or chaas",
                "quantity": "1 glass",
                "time": "2:00 PM",
                "calories": 60,
                "protein": 3,
                "carbs": 5,
                "fats": 2
            }
        ],
        "Post Workout / Evening Snack": [
            {
                "item": "Homemade protein smoothie (milk + banana + peanut butter + oats)",
                "quantity": "1 glass",
                "time": "5:30 PM",
                "calories": 280,
                "protein": 10,
                "carbs": 35,
                "fats": 10
            }
        ],
        "Dinner": [
            {
                "item": "Roti with soyabean curry and sautéed greens",
                "quantity": "2 rotis + 1 bowl curry + veggies",
                "time": "7:30 PM",
                "calories": 420,
                "protein": 18,
                "carbs": 36,
                "fats": 14
            },
            {
                "item": "Warm turmeric milk",
                "quantity": "1 cup",
                "time": "9:00 PM",
                "calories": 100,
                "protein": 4,
                "carbs": 6,
                "fats": 5
            }
        ]
    },
          "active":{
        "Breakfast": [
            {
                "item": "Paneer-stuffed multigrain paratha with curd",
                "quantity": "2 parathas + 1 small bowl curd",
                "time": "8:00 AM",
                "calories": 480,
                "protein": 22,
                "carbs": 45,
                "fats": 20
            },
            {
                "item": "Dates and almonds",
                "quantity": "3 dates + 5 almonds",
                "time": "8:30 AM",
                "calories": 120,
                "protein": 3,
                "carbs": 16,
                "fats": 6
            }
        ],
        "Snack": [
            {
                "item": "Sprouts chaat with lemon and chaat masala",
                "quantity": "1 bowl",
                "time": "11:00 AM",
                "calories": 150,
                "protein": 10,
                "carbs": 20,
                "fats": 3
            }
        ],
        "Lunch": [
            {
                "item": "Brown rice, mixed dal, bhindi sabzi, salad",
                "quantity": "1 bowl rice + 1 bowl dal + 1 bowl veggies",
                "time": "1:30 PM",
                "calories": 500,
                "protein": 20,
                "carbs": 55,
                "fats": 15
            },
            {
                "item": "Lassi (low sugar)",
                "quantity": "1 glass",
                "time": "2:15 PM",
                "calories": 120,
                "protein": 5,
                "carbs": 10,
                "fats": 6
            }
        ],
        "Post Workout / Evening Snack": [
            {
                "item": "Protein smoothie (milk + banana + oats + peanut butter + flax seeds)",
                "quantity": "1 tall glass",
                "time": "5:30 PM",
                "calories": 350,
                "protein": 15,
                "carbs": 35,
                "fats": 16
            }
        ],
        "Dinner": [
            {
                "item": "2 phulkas + soyabean curry + mixed veg stir-fry",
                "quantity": "2 phulkas + 1 bowl curry + 1 bowl veggies",
                "time": "8:00 PM",
                "calories": 450,
                "protein": 22,
                "carbs": 40,
                "fats": 15
            },
            {
                "item": "Warm milk with a pinch of haldi",
                "quantity": "1 glass",
                "time": "9:30 PM",
                "calories": 100,
                "protein": 4,
                "carbs": 6,
                "fats": 5
            }
        ]
    },
 },
           "31-50":{
           "sedentary":{
              "Breakfast": [
                {
                "item": "Vegetable upma with peanuts",
                "quantity": "1 medium bowl",
                "time": "8:00 AM",
                "calories": 280,
                "protein": 8,
                "carbs": 35,
                "fats": 10
            },
            {
                "item": "Low-fat milk",
                "quantity": "1 glass",
                "time": "8:30 AM",
                "calories": 100,
                "protein": 6,
                "carbs": 5,
                "fats": 4
            }
        ],
        "Snack": [
            {
                "item": "Roasted chana + walnuts",
                "quantity": "1 handful",
                "time": "11:00 AM",
                "calories": 150,
                "protein": 6,
                "carbs": 12,
                "fats": 9
            }
        ],
        "Lunch": [
            {
                "item": "Multigrain roti, mixed dal, lauki sabzi, cucumber salad",
                "quantity": "2 rotis + 1 bowl dal + 1 bowl sabzi",
                "time": "1:30 PM",
                "calories": 420,
                "protein": 18,
                "carbs": 40,
                "fats": 12
            }
        ],
        "Evening Snack": [
            {
                "item": "Homemade besan chilla with veggies",
                "quantity": "2 medium chillas",
                "time": "5:00 PM",
                "calories": 220,
                "protein": 10,
                "carbs": 20,
                "fats": 8
            }
        ],
        "Dinner": [
            {
                "item": "brown rice pulao with tofu and mixed vegetables",
                "quantity": "1.5 bowls",
                "time": "7:30 PM",
                "calories": 450,
                "protein": 20,
                "carbs": 45,
                "fats": 15
            },
            {
                "item": "Haldi milk (low fat)",
                "quantity": "1 small glass",
                "time": "9:00 PM",
                "calories": 90,
                "protein": 4,
                "carbs": 6,
                "fats": 3
            }
        ]
    },
    "moderate":{
        "Breakfast": [
            {
                "item": "Oats porridge with banana, chia seeds, and almonds",
                "quantity": "1 bowl",
                "time": "8:00 AM",
                "calories": 350,
                "protein": 12,
                "carbs": 45,
                "fats": 12
            },
            {
                "item": "Low-fat milk",
                "quantity": "1 glass",
                "time": "8:30 AM",
                "calories": 100,
                "protein": 6,
                "carbs": 5,
                "fats": 4
            }
        ],
        "Snack": [
            {
                "item": "Boiled chickpeas chaat with lemon and cucumber",
                "quantity": "1 bowl",
                "time": "11:00 AM",
                "calories": 180,
                "protein": 9,
                "carbs": 25,
                "fats": 5
            }
        ],
        "Lunch": [
            {
                "item": "Brown rice, rajma, spinach sabzi, and salad",
                "quantity": "1 cup rice + 1 cup rajma + 1 bowl sabzi",
                "time": "1:30 PM",
                "calories": 500,
                "protein": 20,
                "carbs": 60,
                "fats": 14
            }
        ],
        "Evening Snack": [
            {
                "item": "Paneer sandwich with whole wheat bread",
                "quantity": "2 slices + 50g paneer",
                "time": "5:00 PM",
                "calories": 300,
                "protein": 16,
                "carbs": 30,
                "fats": 10
            }
        ],
        "Dinner": [
            {
                "item": "Moong dal khichdi with veggies + curd",
                "quantity": "1.5 bowls + 1 small bowl curd",
                "time": "7:30 PM",
                "calories": 400,
                "protein": 16,
                "carbs": 40,
                "fats": 12
            },
            {
                "item": "Haldi milk (low fat)",
                "quantity": "1 small glass",
                "time": "9:00 PM",
                "calories": 90,
                "protein": 4,
                "carbs": 6,
                "fats": 3
            }
        ]
    },
       "active":{
        "Breakfast": [
            {
                "item": "Multigrain toast with peanut butter and banana",
                "quantity": "2 slices + 1 tbsp peanut butter + 1 banana",
                "time": "8:00 AM",
                "calories": 400,
                "protein": 13,
                "carbs": 45,
                "fats": 16
            },
            {
                "item": "Low-fat milk with soaked almonds",
                "quantity": "1 glass + 5 almonds",
                "time": "8:30 AM",
                "calories": 150,
                "protein": 7,
                "carbs": 6,
                "fats": 7
            }
        ],
        "Snack": [
            {
                "item": "Sprouts salad with cucumber, onion, and lemon",
                "quantity": "1 bowl",
                "time": "11:00 AM",
                "calories": 200,
                "protein": 12,
                "carbs": 18,
                "fats": 4
            }
        ],
        "Lunch": [
            {
                "item": "brown rice pulao with tofu and mixed vegetables",
                "quantity": "1.5 cups",
                "time": "1:30 PM",
                "calories": 500,
                "protein": 22,
                "carbs": 55,
                "fats": 14
            },
            {
                "item": "Curd",
                "quantity": "1 small bowl",
                "time": "2:00 PM",
                "calories": 60,
                "protein": 3,
                "carbs": 4,
                "fats": 2
            }
        ],
        "Post Workout": [
            {
                "item": "Whey protein shake with water or almond milk",
                "quantity": "1 scoop",
                "time": "5:00 PM (post workout)",
                "calories": 120,
                "protein": 24,
                "carbs": 2,
                "fats": 1
            },
            {
                "item": "Banana or dates",
                "quantity": "1 banana or 3 dates",
                "time": "5:15 PM",
                "calories": 100,
                "protein": 1,
                "carbs": 25,
                "fats": 0
            }
        ],
        "Dinner": [
            {
                "item": "Whole wheat roti + mixed dal + bhindi sabzi",
                "quantity": "2 rotis + 1 cup dal + 1 bowl sabzi",
                "time": "7:30 PM",
                "calories": 500,
                "protein": 20,
                "carbs": 50,
                "fats": 14
            },
            {
                "item": "Golden turmeric milk (low-fat)",
                "quantity": "1 glass",
                "time": "9:00 PM",
                "calories": 100,
                "protein": 5,
                "carbs": 8,
                "fats": 4
            }
        ]
    },
  },
            "51+":{
              "sedentary":{
                "Breakfast": [
            {
                "item": "Vegetable poha with peas and peanuts",
                "quantity": "1 medium bowl",
                "time": "8:00 AM",
                "calories": 300,
                "protein": 7,
                "carbs": 45,
                "fats": 10
            },
            {
                "item": "Low-fat milk with soaked chia seeds",
                "quantity": "1 glass",
                "time": "8:30 AM",
                "calories": 120,
                "protein": 6,
                "carbs": 6,
                "fats": 5
            }
        ],
        "Snack": [
            {
                "item": "Roasted foxnuts (makhana) with turmeric and ghee",
                "quantity": "1 small bowl",
                "time": "11:00 AM",
                "calories": 150,
                "protein": 4,
                "carbs": 18,
                "fats": 6
            }
        ],
        "Lunch": [
            {
                "item": "Multigrain roti + mixed lentil dal + lauki (bottle gourd) sabzi",
                "quantity": "2 rotis + 1 bowl dal + 1 bowl sabzi",
                "time": "1:30 PM",
                "calories": 450,
                "protein": 18,
                "carbs": 42,
                "fats": 12
            },
            {
                "item": "Buttermilk",
                "quantity": "1 glass",
                "time": "2:00 PM",
                "calories": 50,
                "protein": 2,
                "carbs": 3,
                "fats": 2
            }
        ],
        "Evening Snack": [
            {
                "item": "Mixed fruit bowl (papaya, apple, pomegranate)",
                "quantity": "1 cup",
                "time": "5:30 PM",
                "calories": 100,
                "protein": 1,
                "carbs": 22,
                "fats": 0
            }
        ],
        "Dinner": [
            {
                "item": "Khichdi with moong dal and vegetables + ghee",
                "quantity": "1.5 cups",
                "time": "7:30 PM",
                "calories": 400,
                "protein": 12,
                "carbs": 45,
                "fats": 10
            },
            {
                "item": "Golden turmeric milk (low-fat)",
                "quantity": "1 glass",
                "time": "9:00 PM",
                "calories": 100,
                "protein": 5,
                "carbs": 8,
                "fats": 4
            }
        ]
    },
   "moderate":{
        "Breakfast": [
            {
                "item": "Vegetable upma with cashews",
                "quantity": "1 medium bowl",
                "time": "8:00 AM",
                "calories": 350,
                "protein": 9,
                "carbs": 50,
                "fats": 12
            },
            {
                "item": "Low-fat milk with soaked almonds and chia seeds",
                "quantity": "1 glass + 6 almonds",
                "time": "8:30 AM",
                "calories": 180,
                "protein": 8,
                "carbs": 8,
                "fats": 10
            }
        ],
        "Snack": [
            {
                "item": "Paneer slices with black pepper and lemon",
                "quantity": "50g",
                "time": "11:00 AM",
                "calories": 130,
                "protein": 8,
                "carbs": 2,
                "fats": 10
            }
        ],
        "Lunch": [
            {
                "item": "Brown rice + rajma curry + bhindi (okra) sabzi",
                "quantity": "1 bowl rice + 1 bowl curry + 1 bowl sabzi",
                "time": "1:30 PM",
                "calories": 500,
                "protein": 20,
                "carbs": 55,
                "fats": 14
            },
            {
                "item": "Buttermilk with roasted jeera",
                "quantity": "1 glass",
                "time": "2:00 PM",
                "calories": 50,
                "protein": 2,
                "carbs": 3,
                "fats": 2
            }
        ],
        "Evening Snack": [
            {
                "item": "Banana + Peanut butter on multigrain toast",
                "quantity": "1 slice + 1 tsp PB + 1/2 banana",
                "time": "5:30 PM",
                "calories": 180,
                "protein": 5,
                "carbs": 22,
                "fats": 7
            }
        ],
        "Dinner": [
            {
                "item": "brown rice pulao with mixed vegetables + moong dal soup",
                "quantity": "1 bowl pulao + 1 bowl soup",
                "time": "7:30 PM",
                "calories": 450,
                "protein": 15,
                "carbs": 40,
                "fats": 12
            },
            {
                "item": "Warm turmeric almond milk (low-fat)",
                "quantity": "1 glass",
                "time": "9:00 PM",
                "calories": 120,
                "protein": 5,
                "carbs": 8,
                "fats": 6
            }
        ]
    },
           "active":{
        "Breakfast": [
            {
                "item": "Oats porridge with skim milk, flaxseeds, banana, and almonds",
                "quantity": "1 large bowl",
                "time": "7:30 AM",
                "calories": 400,
                "protein": 14,
                "carbs": 50,
                "fats": 15
            },
            {
                "item": "Boiled eggs or tofu scramble",
                "quantity": "2 eggs or 100g tofu",
                "time": "8:00 AM",
                "calories": 150,
                "protein": 12,
                "carbs": 2,
                "fats": 10
            }
        ],
        "Snack": [
            {
                "item": "Homemade protein smoothie with milk, peanut butter, and soaked dates",
                "quantity": "1 glass",
                "time": "11:00 AM",
                "calories": 250,
                "protein": 10,
                "carbs": 20,
                "fats": 12
            }
        ],
        "Lunch": [
            {
                "item": "Multigrain roti + chana curry + spinach sabzi + cucumber salad",
                "quantity": "2 rotis + 1 bowl curry + 1 bowl sabzi",
                "time": "1:30 PM",
                "calories": 550,
                "protein": 20,
                "carbs": 55,
                "fats": 15
            },
            {
                "item": "Buttermilk (jeera flavored)",
                "quantity": "1 glass",
                "time": "2:00 PM",
                "calories": 50,
                "protein": 2,
                "carbs": 4,
                "fats": 2
            }
        ],
        "Post Workout": [
            {
                "item": "Moong chilla with paneer stuffing + coconut water",
                "quantity": "2 chillas + 1 glass coconut water",
                "time": "5:30 PM",
                "calories": 300,
                "protein": 18,
                "carbs": 20,
                "fats": 10
            }
        ],
        "Dinner": [
            {
                "item": "Vegetable dalia or millet khichdi + stir-fried tofu/tempeh",
                "quantity": "1.5 bowls + 75g tofu",
                "time": "8:00 PM",
                "calories": 500,
                "protein": 22,
                "carbs": 45,
                "fats": 15
            },
            {
                "item": "Golden milk with turmeric and a pinch of cinnamon",
                "quantity": "1 glass (low-fat milk)",
                "time": "9:00 PM",
                "calories": 120,
                "protein": 5,
                "carbs": 10,
                "fats": 6
            }
         ]
     },
  }
}
        },  
       "non-vegetarian": {
          "male": {
           "18-30": {
              "sedentary": {
                 "Breakfast": [
            {
                "item": "Boiled eggs with whole wheat toast and a banana",
                "quantity": "3 eggs + 2 toasts + 1 banana",
                "time": "8:00 AM",
                "calories": 450,
                "protein": 25,
                "carbs": 35,
                "fats": 20
            },
            {
                "item": "Low-fat milk or protein shake",
                "quantity": "1 glass",
                "time": "8:30 AM",
                "calories": 150,
                "protein": 10,
                "carbs": 12,
                "fats": 5
            }
        ],
        "Snack": [
            {
                "item": "Handful of almonds + apple",
                "quantity": "10 almonds + 1 medium apple",
                "time": "11:00 AM",
                "calories": 200,
                "protein": 5,
                "carbs": 20,
                "fats": 12
            }
        ],
        "Lunch": [
            {
                "item": "Grilled chicken breast + brown rice + mixed sabzi + curd",
                "quantity": "100g chicken + 1 cup rice + 1 cup sabzi + 1/2 bowl curd",
                "time": "1:30 PM",
                "calories": 600,
                "protein": 35,
                "carbs": 45,
                "fats": 20
            }
        ],
        "Post Workout": [
            {
                "item": "Not applicable – sedentary (can replace with evening snack)",
                "quantity": "-",
                "time": "-",
                "calories": 0,
                "protein": 0,
                "carbs": 0,
                "fats": 0
            },
            {
                "item": "Boiled egg whites + roasted chana",
                "quantity": "3 egg whites + 1 handful chana",
                "time": "5:30 PM",
                "calories": 150,
                "protein": 15,
                "carbs": 10,
                "fats": 5
            }
        ],
        "Dinner": [
            {
                "item": "Chapati + chicken curry + salad + sautéed veggies",
                "quantity": "2 rotis + 100g chicken + 1 bowl salad + 1/2 bowl veggies",
                "time": "8:00 PM",
                "calories": 550,
                "protein": 35,
                "carbs": 35,
                "fats": 20
            },
            {
                "item": "Warm turmeric milk",
                "quantity": "1 glass",
                "time": "9:30 PM",
                "calories": 120,
                "protein": 6,
                "carbs": 10,
                "fats": 6
            }
        ]
    },
   "moderate":{
        "Breakfast": [
            {
                "item": "Oats with low-fat milk, peanut butter, and banana",
                "quantity": "1 cup oats + 1 cup milk + 1 tbsp peanut butter + 1 banana",
                "time": "8:00 AM",
                "calories": 500,
                "protein": 20,
                "carbs": 60,
                "fats": 18
            },
            {
                "item": "Boiled eggs",
                "quantity": "3 whole eggs",
                "time": "8:30 AM",
                "calories": 210,
                "protein": 18,
                "carbs": 1,
                "fats": 15
            }
        ],
        "Snack": [
            {
                "item": "Sprouts chaat + coconut water",
                "quantity": "1 bowl sprouts + 1 glass coconut water",
                "time": "11:00 AM",
                "calories": 250,
                "protein": 12,
                "carbs": 30,
                "fats": 5
            }
        ],
        "Lunch": [
            {
                "item": "Grilled chicken + brown rice + dal + salad",
                "quantity": "150g chicken + 1 cup rice + 1/2 cup dal + salad",
                "time": "1:30 PM",
                "calories": 650,
                "protein": 40,
                "carbs": 50,
                "fats": 20
            }
        ],
        "Post Workout": [
            {
                "item": "Protein shake + banana",
                "quantity": "1 scoop whey + 1 banana",
                "time": "5:30 PM",
                "calories": 300,
                "protein": 25,
                "carbs": 30,
                "fats": 5
            }
        ],
        "Dinner": [
            {
                "item": "Roti + chicken curry + mixed veggies + curd",
                "quantity": "2 rotis + 100g chicken + 1 cup veggies + 1/2 bowl curd",
                "time": "8:00 PM",
                "calories": 600,
                "protein": 35,
                "carbs": 40,
                "fats": 20
            },
            {
                "item": "Almond milk or warm turmeric milk",
                "quantity": "1 glass",
                "time": "9:30 PM",
                "calories": 150,
                "protein": 6,
                "carbs": 10,
                "fats": 8
            }
        ]
    },
    "active": {
        "Breakfast": [
            {
                "item": "Oats porridge with almonds, peanut butter, and chopped dates",
                "quantity": "1 cup oats + 1 tbsp peanut butter + 5 almonds + 3 dates",
                "time": "7:30 AM",
                "calories": 550,
                "protein": 22,
                "carbs": 65,
                "fats": 20
            },
            {
                "item": "Boiled eggs",
                "quantity": "4 whole eggs",
                "time": "8:00 AM",
                "calories": 280,
                "protein": 24,
                "carbs": 1,
                "fats": 20
            }
        ],
        "Snack": [
            {
                "item": "Grilled chicken sandwich (whole wheat) + banana",
                "quantity": "2 slices bread + 100g chicken + 1 banana",
                "time": "11:00 AM",
                "calories": 450,
                "protein": 30,
                "carbs": 45,
                "fats": 15
            }
        ],
        "Lunch": [
            {
                "item": "Chicken curry + brown rice + dal + salad",
                "quantity": "150g chicken + 1 cup brown rice + 1/2 cup dal + salad",
                "time": "1:30 PM",
                "calories": 700,
                "protein": 45,
                "carbs": 50,
                "fats": 25
            }
        ],
        "Post Workout": [
            {
                "item": "Whey protein shake with peanut butter and milk",
                "quantity": "1 scoop whey + 1 tbsp peanut butter + 1 cup milk",
                "time": "6:00 PM",
                "calories": 400,
                "protein": 35,
                "carbs": 20,
                "fats": 18
            },
            {
                "item": "Dates or raisins",
                "quantity": "4–5 pieces",
                "time": "6:15 PM",
                "calories": 100,
                "protein": 1,
                "carbs": 25,
                "fats": 0
            }
        ],
        "Dinner": [
            {
                "item": "Roti + grilled fish or chicken tikka + sautéed vegetables",
                "quantity": "2 rotis + 150g grilled fish/chicken + 1 cup veggies",
                "time": "8:00 PM",
                "calories": 700,
                "protein": 45,
                "carbs": 40,
                "fats": 25
            },
            {
                "item": "Warm milk with turmeric",
                "quantity": "1 glass",
                "time": "9:30 PM",
                "calories": 120,
                "protein": 6,
                "carbs": 10,
                "fats": 5
            }
        ]
    },
},
             "31-50":{
               "sedentary":{
                  "Breakfast": [
            {
                "item": "Vegetable oats upma + 2 boiled eggs",
                "quantity": "1 bowl oats upma + 2 eggs",
                "time": "8:00 AM",
                "calories": 400,
                "protein": 20,
                "carbs": 35,
                "fats": 18
            }
        ],
        "Snack": [
            {
                "item": "Handful of roasted chana + buttermilk",
                "quantity": "1/2 cup chana + 1 glass buttermilk",
                "time": "11:00 AM",
                "calories": 200,
                "protein": 12,
                "carbs": 18,
                "fats": 5
            }
        ],
        "Lunch": [
            {
                "item": "Grilled chicken + phulka + mixed sabzi + salad",
                "quantity": "100g chicken + 2 phulkas + 1 cup sabzi",
                "time": "1:30 PM",
                "calories": 550,
                "protein": 35,
                "carbs": 40,
                "fats": 20
            }
        ],
        "Post Lunch Snack": [
            {
                "item": "Boiled egg whites + fruit (apple or orange)",
                "quantity": "3 egg whites + 1 fruit",
                "time": "4:00 PM",
                "calories": 180,
                "protein": 15,
                "carbs": 15,
                "fats": 4
            }
        ],
        "Dinner": [
            {
                "item": "Fish curry or grilled fish + brown rice + sauteed spinach",
                "quantity": "100g fish + 1 cup rice + 1 cup spinach",
                "time": "7:30 PM",
                "calories": 550,
                "protein": 35,
                "carbs": 45,
                "fats": 20
            },
            {
                "item": "Turmeric milk",
                "quantity": "1 cup milk with haldi",
                "time": "9:00 PM",
                "calories": 120,
                "protein": 6,
                "carbs": 10,
                "fats": 5
            }
        ]
    },
          "moderate":{
             "Breakfast": [
            {
                "item": "Scrambled eggs + multigrain toast + banana",
                "quantity": "3 eggs + 2 slices toast + 1 banana",
                "time": "8:00 AM",
                "calories": 500,
                "protein": 28,
                "carbs": 40,
                "fats": 22
            }
        ],
        "Snack": [
            {
                "item": "Greek yogurt + walnuts + honey",
                "quantity": "1 cup yogurt + 1 tbsp walnuts + 1 tsp honey",
                "time": "11:00 AM",
                "calories": 250,
                "protein": 14,
                "carbs": 20,
                "fats": 12
            }
        ],
        "Lunch": [
            {
                "item": "Grilled chicken breast + jeera rice + rajma + salad",
                "quantity": "120g chicken + 1 cup rice + 1/2 cup rajma + salad",
                "time": "1:30 PM",
                "calories": 600,
                "protein": 40,
                "carbs": 50,
                "fats": 18
            }
        ],
        "Pre-Workout Snack": [
            {
                "item": "Boiled eggs + banana or dates",
                "quantity": "2 eggs + 1 banana or 3 dates",
                "time": "4:30 PM",
                "calories": 250,
                "protein": 13,
                "carbs": 25,
                "fats": 10
            }
        ],
        "Post-Workout": [
            {
                "item": "Whey protein shake with milk + peanuts",
                "quantity": "1 scoop + 1 glass milk + 1 tbsp peanuts",
                "time": "6:30 PM",
                "calories": 350,
                "protein": 30,
                "carbs": 20,
                "fats": 12
            }
        ],
        "Dinner": [
            {
                "item": "Fish tikka or chicken curry + roti + sabzi",
                "quantity": "100g fish/chicken + 2 roti + 1 cup sabzi",
                "time": "8:00 PM",
                "calories": 550,
                "protein": 35,
                "carbs": 45,
                "fats": 18
            }
        ]
    },
    "active":{
        "Breakfast": [
            {
                "item": "Oats with milk, boiled eggs, peanut butter toast",
                "quantity": "1 cup oats + 200ml milk + 3 eggs + 2 slices toast with 1 tbsp peanut butter",
                "time": "8:00 AM",
                "calories": 650,
                "protein": 35,
                "carbs": 55,
                "fats": 25
            }
        ],
        "Snack": [
            {
                "item": "Chicken sandwich + fruit smoothie",
                "quantity": "1 sandwich with 100g chicken + 1 glass smoothie (banana + milk + almonds)",
                "time": "11:00 AM",
                "calories": 450,
                "protein": 30,
                "carbs": 40,
                "fats": 15
            }
        ],
        "Lunch": [
            {
                "item": "Grilled chicken breast + brown rice + dal + sabzi + salad",
                "quantity": "150g chicken + 1 cup rice + 1/2 cup dal + 1 cup sabzi + salad",
                "time": "1:30 PM",
                "calories": 750,
                "protein": 45,
                "carbs": 55,
                "fats": 28
            }
        ],
        "Pre-Workout Snack": [
            {
                "item": "Boiled eggs + banana or peanut chikki",
                "quantity": "2 eggs + 1 banana or 2 pcs chikki",
                "time": "4:30 PM",
                "calories": 300,
                "protein": 14,
                "carbs": 28,
                "fats": 12
            }
        ],
        "Post-Workout": [
            {
                "item": "Whey protein shake with banana + dry fruits",
                "quantity": "1 scoop whey + 1 banana + 4 soaked almonds + 2 dates",
                "time": "6:30 PM",
                "calories": 400,
                "protein": 30,
                "carbs": 30,
                "fats": 12
            }
        ],
        "Dinner": [
            {
                "item": "Fish curry or grilled chicken + 2 rotis + stir-fried vegetables",
                "quantity": "150g fish/chicken + 2 rotis + 1 cup sabzi",
                "time": "8:30 PM",
                "calories": 600,
                "protein": 38,
                "carbs": 45,
                "fats": 20
            }
        ]
    },
             },
            "51+":{
              "sedentary":{
        "Breakfast": [
            {
                "item": "Vegetable oats + 2 boiled eggs + herbal tea",
                "quantity": "1 cup oats with veggies + 2 eggs + 1 cup tea (no sugar)",
                "time": "8:00 AM",
                "calories": 400,
                "protein": 22,
                "carbs": 35,
                "fats": 15
            }
        ],
        "Snack": [
            {
                "item": "Fruit bowl + handful of walnuts",
                "quantity": "1 bowl seasonal fruits + 5-6 walnuts",
                "time": "11:00 AM",
                "calories": 250,
                "protein": 5,
                "carbs": 30,
                "fats": 12
            }
        ],
        "Lunch": [
            {
                "item": "Grilled fish + brown rice + dal + sautéed greens",
                "quantity": "120g fish + 1/2 cup rice + 1/2 cup dal + 1 cup spinach/bhindi",
                "time": "1:30 PM",
                "calories": 600,
                "protein": 38,
                "carbs": 40,
                "fats": 22
            }
        ],
        "Evening Snack": [
            {
                "item": "Boiled egg + roasted chana or 1 slice whole wheat toast",
                "quantity": "1 egg + 1 handful chana or toast",
                "time": "4:30 PM",
                "calories": 200,
                "protein": 12,
                "carbs": 15,
                "fats": 8
            }
        ],
        "Dinner": [
            {
                "item": "Chicken curry + phulka + steamed vegetables",
                "quantity": "120g chicken + 2 phulkas + 1 cup veggies",
                "time": "7:30 PM",
                "calories": 550,
                "protein": 35,
                "carbs": 35,
                "fats": 20
            }
        ],
        "Optional Bedtime": [
            {
                "item": "Haldi milk or curd",
                "quantity": "1/2 cup curd or 1 glass warm turmeric milk (low fat)",
                "time": "9:30 PM",
                "calories": 150,
                "protein": 7,
                "carbs": 10,
                "fats": 7
            }
        ]
    },
    "moderate":{
        "Breakfast": [
            {
                "item": "Boiled eggs + whole wheat toast + milk",
                "quantity": "3 eggs + 2 toasts + 1 glass low-fat milk",
                "time": "8:00 AM",
                "calories": 450,
                "protein": 28,
                "carbs": 30,
                "fats": 20
            }
        ],
        "Snack": [
            {
                "item": "Mixed nuts + banana",
                "quantity": "5 almonds + 5 walnuts + 1 banana",
                "time": "11:00 AM",
                "calories": 300,
                "protein": 6,
                "carbs": 28,
                "fats": 18
            }
        ],
        "Lunch": [
            {
                "item": "Grilled chicken + roti + dal + salad",
                "quantity": "120g chicken + 2 rotis + 1/2 cup dal + 1 bowl salad",
                "time": "1:30 PM",
                "calories": 600,
                "protein": 40,
                "carbs": 35,
                "fats": 18
            }
        ],
        "Pre-Workout Snack": [
            {
                "item": "Boiled egg + black coffee",
                "quantity": "1 egg + 1 cup coffee (no sugar)",
                "time": "5:00 PM",
                "calories": 100,
                "protein": 6,
                "carbs": 1,
                "fats": 6
            }
        ],
        "Dinner": [
            {
                "item": "Chicken curry with brown rice and salad",
            "quantity": "90g chicken + 1 cup rice + 1 cup salad",
            "time": "8:00 PM",
            "calories": 450,
            "protein": 32,
            "carbs": 35,
            "fats": 20
            }
        ],
        "Bedtime": [
            {
                "item": "Turmeric milk or curd",
                "quantity": "1 glass haldi milk (low fat) or 1/2 cup curd",
                "time": "9:30 PM",
                "calories": 150,
                "protein": 8,
                "carbs": 10,
                "fats": 6
            }
        ]
    },
    "active":{
        "Breakfast": [
            {
                "item": "Oats with milk, chopped nuts & 1 boiled egg",
                "quantity": "1 cup oats + 1 cup milk + 5 almonds + 1 egg",
                "time": "7:30 AM",
                "calories": 500,
                "protein": 25,
                "carbs": 45,
                "fats": 20
            }
        ],
        "Mid-Morning Snack": [
            {
                "item": "Greek yogurt + 1 banana",
                "quantity": "1 cup yogurt + 1 banana",
                "time": "10:30 AM",
                "calories": 250,
                "protein": 12,
                "carbs": 25,
                "fats": 8
            }
        ],
        "Lunch": [
            {
                "item": "Grilled chicken breast + brown rice + dal + salad",
                "quantity": "150g chicken + 1 cup rice + 1/2 cup dal + salad",
                "time": "1:30 PM",
                "calories": 700,
                "protein": 45,
                "carbs": 45,
                "fats": 20
            }
        ],
        "Pre-Workout Snack": [
            {
                "item": "Black coffee + boiled egg whites",
                "quantity": "1 cup coffee + 3 egg whites",
                "time": "5:30 PM",
                "calories": 90,
                "protein": 10,
                "carbs": 0,
                "fats": 2
            }
        ],
        "Post-Workout": [
            {
                "item": "Protein shake with skimmed milk",
                "quantity": "1 scoop whey + 1 cup milk",
                "time": "Immediately after workout",
                "calories": 250,
                "protein": 25,
                "carbs": 15,
                "fats": 5
            }
        ],
        "Dinner": [
            {
                "item": "Fish curry + multigrain roti + sautéed vegetables",
                "quantity": "100g fish + 2 rotis + 1 cup vegetables",
                "time": "8:00 PM",
                "calories": 600,
                "protein": 35,
                "carbs": 35,
                "fats": 20
            }
        ],
        "Bedtime": [
            {
                "item": "Low-fat milk with haldi (turmeric)",
                "quantity": "1 glass (200 ml)",
                "time": "10:00 PM",
                "calories": 120,
                "protein": 8,
                "carbs": 10,
                "fats": 4
            }
        ]
    },
}
          },
         
        "female": {
            "18-30": {
                "sedentary":{
                    "breakfast":[ 
                    {
                        "item": "Vegetable omelette + multigrain toast + milk",
                        "quantity": "2 eggs + 2 toast + 1 cup milk",
                        "time": "8:00 AM",
                        "calories": 420,
                        "protein": 24,
                        "carbs": 30,
                        "fats": 20
                    }
                    ],
                    "snack":[
                         {
                        "item": "Boiled egg + banana",
                        "quantity": "1 egg + 1 banana",
                        "time": "11:00 AM",
                        "calories": 160,
                        "protein": 7,
                        "carbs": 18,
                        "fats": 6
                    }
                    ],
                    "lunch":[
                         {
                        "item": "Grilled chicken + brown rice + mixed veggies + curd",
                        "quantity": "100g chicken + 1 cup rice + 1 cup veggies + 1/2 cup curd",
                        "time": "1:30 PM",
                        "calories": 600,
                        "protein": 35,
                        "carbs": 50,
                        "fats": 22
                    }
                    ],
                    "post_workout": [{
                        "item": "Whey protein shake + almonds",
                        "quantity": "1 scoop whey + 6 almonds",
                        "time": "5:00 PM",
                        "calories": 250,
                        "protein": 25,
                        "carbs": 8,
                        "fats": 10
                    }
                    ],
                    "dinner": [
                        {
                        "item": "Egg curry + multigrain roti + sautéed spinach",
                        "quantity": "2 eggs + 2 rotis + 1 cup spinach",
                        "time": "8:00 PM",
                        "calories": 450,
                        "protein": 22,
                        "carbs": 30,
                        "fats": 18
                       }
                    ]
                    },
                "moderate": {
                    "breakfast": [
                        {
                        "item": "Boiled eggs + oats porridge with fruits",
                        "quantity": "3 eggs + 1 cup oats + 1/2 banana",
                        "time": "8:00 AM",
                        "calories": 500,
                        "protein": 30,
                        "carbs": 40,
                        "fats": 20
                    }
                    ],
                    "snack": [
                        {
                        "item": "Greek yogurt + handful of walnuts",
                        "quantity": "1 cup yogurt + 6 walnuts",
                        "time": "11:00 AM",
                        "calories": 250,
                        "protein": 15,
                        "carbs": 12,
                        "fats": 16
                    }
                    ],
                    "lunch": [
                        {
                        "item": "Chicken curry + brown rice + salad + buttermilk",
                        "quantity": "120g chicken + 1 cup rice + 1 bowl salad + 1 glass buttermilk",
                        "time": "1:30 PM",
                        "calories": 650,
                        "protein": 40,
                        "carbs": 50,
                        "fats": 25
                    }
                    ],
                    "post_workout": [
                        {
                        "item": "Whey protein shake + boiled egg",
                        "quantity": "1 scoop whey + 1 egg",
                        "time": "5:00 PM",
                        "calories": 280,
                        "protein": 28,
                        "carbs": 6,
                        "fats": 10
                    }
                    ],
                    "dinner": [
                        {
                        "item": "Fish tikka + multigrain roti + sautéed beans",
                        "quantity": "100g fish + 2 rotis + 1 cup beans",
                        "time": "8:00 PM",
                        "calories": 500,
                        "protein": 35,
                        "carbs": 32,
                        "fats": 18
                    }
                    ]
                },
                "active": {
                    "breakfast": [
                        {
                        "item": "Oats porridge with milk, dry fruits & 2 boiled eggs",
                        "quantity": "1 cup oats + 1 cup milk + 5 almonds + 2 eggs",
                        "time": "8:00 AM",
                        "calories": 550,
                        "protein": 30,
                        "carbs": 45,
                        "fats": 22
                    }
                    ],
                    "snack": [
                        {
                        "item": "Peanut butter toast + banana",
                        "quantity": "2 multigrain toasts + 1 tbsp peanut butter + 1 banana",
                        "time": "11:00 AM",
                        "calories": 350,
                        "protein": 12,
                        "carbs": 40,
                        "fats": 18
                    }
                    ],
                    "lunch": [
                        {
                        "item": "Grilled chicken breast + brown rice + mixed vegetable curry + salad",
                        "quantity": "120g chicken + 1 cup brown rice + 1/2 cup curry + 1 bowl salad",
                        "time": "1:30 PM",
                        "calories": 700,
                        "protein": 45,
                        "carbs": 50,
                        "fats": 25
                    }
                    ],
                    "post_workout": [
                        {
                        "item": "Whey protein shake + boiled eggs",
                        "quantity": "1 scoop whey + 2 eggs",
                        "time": "5:30 PM",
                        "calories": 320,
                        "protein": 35,
                        "carbs": 5,
                        "fats": 12
                    }
                    ],
                    "dinner": [
                        {
                        "item": "chicken curry + brown rice + sautéed spinach",
                        "quantity": "130g chicken + 1/2 cup rice + 1.5 cup spinach(in 1.5 tsp oil)",
                        "time": "8:00 PM",
                        "calories": 550,
                        "protein": 35,
                        "carbs": 38,
                        "fats": 20
                    }
                    ]
                }
            },
            "31-50": {
                "sedentary": {
                    "breakfast": [
                        {
                        "item": "Vegetable omelette + multigrain toast + milk",
                        "quantity": "2 eggs + 2 slices toast + 1 cup toned milk",
                        "time": "8:00 AM",
                        "calories": 420,
                        "protein": 25,
                        "carbs": 30,
                        "fats": 20
                    }
                    ],
                    "snack": [
                        {
                        "item": "Apple slices with peanut butter",
                        "quantity": "1 apple + 1 tbsp peanut butter",
                        "time": "11:00 AM",
                        "calories": 250,
                        "protein": 6,
                        "carbs": 25,
                        "fats": 14
                    }
                    ],
                    "lunch": [
                        {
                        "item": "Grilled chicken breast + dal + brown rice + salad",
                        "quantity": "100g chicken + 1/2 cup dal + 3/4 cup rice + 1 cup salad",
                        "time": "1:30 PM",
                        "calories": 600,
                        "protein": 40,
                        "carbs": 45,
                        "fats": 18
                    }
                    ],
                    "post_workout": [
                        {
                        "item": "Boiled egg whites + buttermilk",
                        "quantity": "3 egg whites + 1 glass buttermilk",
                        "time": "5:30 PM",
                        "calories": 180,
                        "protein": 15,
                        "carbs": 6,
                        "fats": 6
                    }
                    ],
                    "dinner": [
                        {
                        "item": "Fish curry + sautéed vegetables + phulka",
                        "quantity": "80g fish + 1 cup veggies + 2 phulkas",
                        "time": "8:00 PM",
                        "calories": 480,
                        "protein": 32,
                        "carbs": 30,
                        "fats": 18
                    }
                    ]
                },
                "moderate": {
                    "Breakfast": [
                        {
                            "item": "Boiled eggs + poha with veggies + milk",
                            "quantity": "2 boiled eggs + 1 cup poha + 1 glass milk",
                            "time": "7:30 AM",
                            "calories": 520,
                            "protein": 28,
                            "carbs": 45,
                            "fats": 22
                        }
                    ],
                    "Snack": [
                        {
                            "item": "Greek yogurt with honey and walnuts",
                            "quantity": "1/2 cup yogurt + 1 tsp honey + 4 walnuts",
                            "time": "10:30 AM",
                            "calories": 250,
                            "protein": 10,
                            "carbs": 20,
                            "fats": 14
                        }
                    ],
                    "Lunch": [
                        {
                            "item": "Grilled chicken wrap + hummus + cucumber salad",
                            "quantity": "1 whole wheat wrap + 100g chicken + 2 tbsp hummus + 1/2 cup salad",
                            "time": "1:00 PM",
                            "calories": 600,
                            "protein": 38,
                            "carbs": 40,
                            "fats": 20
                        }
                    ],
                    "Post Workout": [
                        {
                            "item": "Banana + boiled eggs",
                            "quantity": "1 medium banana + 2 boiled eggs",
                            "time": "5:00 PM",
                            "calories": 280,
                            "protein": 16,
                            "carbs": 25,
                            "fats": 12
                        }
                    ],
                    "Dinner": [
                        {
                            "item": "Egg curry + brown rice + sautéed beans",
                            "quantity": "2 eggs + 1 cup rice + 1 cup beans",
                            "time": "8:00 PM",
                            "calories": 520,
                            "protein": 28,
                            "carbs": 40,
                            "fats": 18
                        }
                    ]
                },
                "active": {
                    "Breakfast": [
                        {
                            "item": "Oats with milk, chia seeds, almonds + scrambled eggs",
                            "quantity": "1 cup oats + 1 cup milk + 1 tsp chia + 5 almonds + 2 eggs",
                            "time": "7:30 AM",
                            "calories": 580,
                            "protein": 30,
                            "carbs": 45,
                            "fats": 25
                        }
                    ],
                    "Snack": [
                        {
                            "item": "Peanut butter toast + boiled egg",
                            "quantity": "2 slices whole wheat bread + 1 tbsp peanut butter + 1 egg",
                            "time": "10:30 AM",
                            "calories": 300,
                            "protein": 15,
                            "carbs": 25,
                            "fats": 15
                        }
                    ],
                    "Lunch": [
                        {
                            "item": "Grilled chicken breast + brown rice + sautéed veggies",
                            "quantity": "100g chicken + 1 cup brown rice + 1 cup mixed veggies",
                            "time": "1:00 PM",
                            "calories": 650,
                            "protein": 40,
                            "carbs": 50,
                            "fats": 22
                        }
                    ],
                    "Post Workout": [
                        {
                            "item": "Protein smoothie (milk + banana + whey)",
                            "quantity": "1 glass milk + 1 banana + 1 scoop whey",
                            "time": "5:00 PM",
                            "calories": 350,
                            "protein": 30,
                            "carbs": 30,
                            "fats": 10
                        }
                    ],
                    "Dinner": [
                        {
                            "item": "Fish curry + multigrain roti + sautéed vegetables",
                            "quantity": "100g fish + 2 rotis + 1 cup vegetables",
                            "time": "8:00 PM",
                            "calories": 600,
                            "protein": 35,
                            "carbs": 35,
                            "fats": 20
                        }
                    ]
                }
            },
            "51+": {
                "sedentary": {
                    "Breakfast": [
                        {
                            "item": "Vegetable upma + 1 boiled egg",
                            "quantity": "1 cup upma + 1 egg",
                            "time": "8:00 AM",
                            "calories": 350,
                            "protein": 15,
                            "carbs": 40,
                            "fats": 10
                        }
                    ],
                    "Snack": [
                        {
                            "item": "Low-fat curd with flaxseeds",
                            "quantity": "1/2 cup curd + 1 tsp flaxseeds",
                            "time": "11:00 AM",
                            "calories": 150,
                            "protein": 8,
                            "carbs": 10,
                            "fats": 7
                        }
                    ],
                    "Lunch": [
                        {
                            "item": "Grilled chicken breast + brown rice + stir-fried vegetables",
                            "quantity": "80g chicken + 3/4 cup brown rice + 1 cup vegetables",
                            "time": "1:30 PM",
                            "calories": 500,
                            "protein": 30,
                            "carbs": 45,
                            "fats": 18
                        }
                    ],
                    "Post Workout": [
                        {
                            "item": "Boiled egg whites + coconut water (optional post walk)",
                            "quantity": "2 egg whites + 1 glass coconut water",
                            "time": "5:30 PM",
                            "calories": 140,
                            "protein": 12,
                            "carbs": 8,
                            "fats": 3
                        }
                    ],
                    "Dinner": [
                        {
                            "item": "Fish stew + 1 multigrain roti + steamed broccoli",
                            "quantity": "80g fish + 1 roti + 1 cup broccoli",
                            "time": "8:00 PM",
                            "calories": 450,
                            "protein": 28,
                            "carbs": 30,
                            "fats": 15
                        }
                    ]
                },
                "moderate": {
                    "Breakfast": [
                        {
                            "item": "Vegetable poha with paneer + 1 boiled egg",
                            "quantity": "1 cup poha + 50g paneer + 1 egg",
                            "time": "7:30 AM",
                            "calories": 420,
                            "protein": 22,
                            "carbs": 45,
                            "fats": 15
                        }
                    ],
                    "Snack": [
                        {
                            "item": "Greek yogurt with chia seeds",
                            "quantity": "3/4 cup yogurt + 1 tsp chia seeds",
                            "time": "10:30 AM",
                            "calories": 180,
                            "protein": 10,
                            "carbs": 12,
                            "fats": 8
                        }
                    ],
                    "Lunch": [
                        {
                            "item": "Grilled chicken salad + 1 multigrain roti + dal soup",
                            "quantity": "80g chicken + 1 cup salad + 1 roti + 1/2 cup dal soup",
                            "time": "1:00 PM",
                            "calories": 520,
                            "protein": 30,
                            "carbs": 40,
                            "fats": 20
                        }
                    ],
                    "Post Workout": [
                        {
                            "item": "Boiled eggs + banana",
                            "quantity": "2 eggs + 1 banana",
                            "time": "5:00 PM",
                            "calories": 230,
                            "protein": 14,
                            "carbs": 20,
                            "fats": 10
                        }
                    ],
                    "Dinner": [
                        {
                            "item": "Chicken-Cocunut curry + brown rice + sautéed beans",
                            "quantity": "80g chicken breast + 1.5 tsp cocunut milk + 1/2 cup rice + 1 cup beans + 1tsp oil",
                            "time": "7:30 PM",
                            "calories": 500,
                            "protein": 32,
                            "carbs": 35,
                            "fats": 18
                        }
                    ]
                },
                "active": {
                    "Breakfast": [
                        {
                            "item": "Paneer paratha with curd and boiled egg",
                            "quantity": "2 parathas + 1/2 cup curd + 1 egg",
                            "time": "7:30 AM",
                            "calories": 550,
                            "protein": 28,
                            "carbs": 50,
                            "fats": 22
                        }
                    ],
                    "Snack": [
                        {
                            "item": "Fruit smoothie with protein powder",
                            "quantity": "1 glass smoothie (banana, berries, milk, 1 scoop whey)",
                            "time": "10:30 AM",
                            "calories": 300,
                            "protein": 20,
                            "carbs": 30,
                            "fats": 10
                        }
                    ],
                    "Lunch": [
                        {
                            "item": "Grilled chicken breast + brown rice + mixed vegetables",
                            "quantity": "100g chicken + 1/2 cup brown rice + 1 cup veggies",
                            "time": "1:00 PM",
                            "calories": 550,
                            "protein": 35,
                            "carbs": 40,
                            "fats": 20
                        }
                    ],
                    "Post Workout": [
                        {
                            "item": "Boiled eggs + dates",
                            "quantity": "2 eggs + 2 dates",
                            "time": "5:00 PM",
                            "calories": 250,
                            "protein": 14,
                            "carbs": 20,
                            "fats": 12
                        }
                    ],
                    "Dinner": [
                        {
                            "item": "Chicken tikka + brown rice + sautéed spinach",
                            "quantity": "90g chicken breast + 1/2 cup rice + 1 cup spinach ",
                            "time": "8:00 PM",
                            "calories": 530,
                            "protein": 32,
                            "carbs": 35,
                            "fats": 18
                        }
                    ]
                }
            }
        }
    }
},

"weight_loss": {
        "vegetarian": {
            "male": {
                "18-30": {
                    "sedentary": {
                        "Breakfast": [
                                     {
                                    "item": "Vegetable upma with low-fat curd",
                                    "quantity": "1 cup upma + 1/2 cup curd",
                                    "time": "8:00 AM",
                                    "calories": 300,
                                    "protein": 10,
                                    "carbs": 45,
                                    "fats": 8
                                    }
                                    ],
    "Mid-Morning Snack": [
        {
            "item": "Fruit salad with chia seeds",
            "quantity": "1 cup mixed fruits + 1 tsp chia seeds",
            "time": "10:30 AM",
            "calories": 150,
            "protein": 2,
            "carbs": 30,
            "fats": 3
        }
    ],
    "Lunch": [
        {
            "item": "Brown rice, dal, mixed vegetable sabzi, and salad",
            "quantity": "1 cup brown rice + 1/2 cup dal + 1 cup sabzi + salad",
            "time": "1:00 PM",
            "calories": 450,
            "protein": 18,
            "carbs": 55,
            "fats": 12
        }
    ],
    "Evening Snack": [
        {
            "item": "Roasted makhana and green tea",
            "quantity": "1 cup makhana + 1 cup tea",
            "time": "4:30 PM",
            "calories": 120,
            "protein": 4,
            "carbs": 10,
            "fats": 6
        }
    ],
    "Dinner": [
        {
            "item": "Multigrain roti, paneer bhurji, and sautéed spinach",
            "quantity": "2 rotis + 1/2 cup paneer + 1/2 cup spinach",
            "time": "8:00 PM",
            "calories": 400,
            "protein": 22,
            "carbs": 30,
            "fats": 15
        }
    ]
                    },
                "moderate": {
    "Breakfast": [
        {
            "item": "Vegetable poha with peanuts and herbal tea",
            "quantity": "1 cup poha + 1 tsp peanuts + 1 cup herbal tea",
            "time": "8:00 AM",
            "calories": 350,
            "protein": 9,
            "carbs": 50,
            "fats": 10
        }
    ],
    "Mid-Morning Snack": [
        {
            "item": "Apple with 1 tbsp peanut butter",
            "quantity": "1 medium apple + 1 tbsp peanut butter",
            "time": "11:00 AM",
            "calories": 180,
            "protein": 4,
            "carbs": 22,
            "fats": 8
        }
    ],
    "Lunch": [
        {
            "item": "brown rice khichdi with mixed vegetables and cucumber raita",
            "quantity": "1 cup khichdi + 1/2 cup raita",
            "time": "1:30 PM",
            "calories": 450,
            "protein": 16,
            "carbs": 50,
            "fats": 14
        }
    ],
    "Evening Snack": [
        {
            "item": "Buttermilk and roasted chana",
            "quantity": "1 cup buttermilk + 1/4 cup chana",
            "time": "5:00 PM",
            "calories": 140,
            "protein": 7,
            "carbs": 15,
            "fats": 4
        }
    ],
    "Dinner": [
        {
            "item": "Oats cheela with paneer stuffing and sautéed vegetables",
            "quantity": "2 cheelas + 1/2 cup paneer + 1 cup vegetables",
            "time": "8:00 PM",
            "calories": 420,
            "protein": 20,
            "carbs": 35,
            "fats": 16
        }
    ]
},
         "active": {
        "Breakfast": [
                {
                        "item": "Moong dal chilla with green chutney and herbal tea",
                        "quantity": "2 chillas + 2 tbsp chutney + 1 cup herbal tea",
                        "time": "7:30 AM",
                        "calories": 350,
                        "protein": 18,
                        "carbs": 30,
                        "fats": 12
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Greek yogurt with berries and flaxseeds",
                        "quantity": "3/4 cup yogurt + 1/4 cup berries + 1 tsp flaxseeds",
                        "time": "10:30 AM",
                        "calories": 200,
                        "protein": 10,
                        "carbs": 15,
                        "fats": 9
                }
        ],
        "Lunch": [
                {
                        "item": "Brown rice with rajma curry and sautéed spinach",
                        "quantity": "3/4 cup rice + 1 cup rajma + 1 cup spinach",
                        "time": "1:30 PM",
                        "calories": 480,
                        "protein": 20,
                        "carbs": 55,
                        "fats": 14
                }
        ],
        "Pre-Workout Snack": [
                {
                        "item": "Banana with 1 tbsp peanut butter",
                        "quantity": "1 banana + 1 tbsp peanut butter",
                        "time": "4:30 PM",
                        "calories": 200,
                        "protein": 5,
                        "carbs": 25,
                        "fats": 8
                }
        ],
        "Post-Workout Snack": [
                {
                        "item": "Protein smoothie with milk, whey, and dates",
                        "quantity": "1 scoop whey + 1 cup milk + 2 dates",
                        "time": "6:00 PM",
                        "calories": 300,
                        "protein": 25,
                        "carbs": 20,
                        "fats": 10
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled tofu with stir-fried veggies and millet roti",
                        "quantity": "100g tofu + 1 cup veggies + 1 roti",
                        "time": "8:00 PM",
                        "calories": 400,
                        "protein": 25,
                        "carbs": 30,
                        "fats": 15
                   }
                ]
            }
       },
        "31-50": {
          "sedentary": {
              "Breakfast": [
                {
                        "item": "Vegetable upma with green tea",
                        "quantity": "1 cup upma + 1 cup green tea",
                        "time": "7:30 AM",
                        "calories": 300,
                        "protein": 8,
                        "carbs": 35,
                        "fats": 10
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Buttermilk with roasted chana",
                        "quantity": "1 glass buttermilk + 1/4 cup chana",
                        "time": "10:30 AM",
                        "calories": 150,
                        "protein": 8,
                        "carbs": 12,
                        "fats": 5
                }
        ],
        "Lunch": [
                {
                        "item": "Multigrain roti with mixed veg curry and salad",
                        "quantity": "2 rotis + 1 cup curry + 1 cup salad",
                        "time": "1:30 PM",
                        "calories": 400,
                        "protein": 15,
                        "carbs": 40,
                        "fats": 12
                }
        ],
        "Evening Snack": [
                {
                        "item": "Fruit bowl with chia seeds",
                        "quantity": "1 cup fruits + 1 tsp chia seeds",
                        "time": "5:00 PM",
                        "calories": 180,
                        "protein": 3,
                        "carbs": 30,
                        "fats": 5
                }
        ],
        "Dinner": [
                {
                        "item": "brown rice khichdi with steamed broccoli",
                        "quantity": "1 cup khichdi + 1 cup broccoli",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 12,
                        "carbs": 35,
                        "fats": 10
                }
        ]
},
"moderate": {
        "Breakfast": [
                {
                        "item": "Oats porridge with banana and flaxseeds",
                        "quantity": "1 cup oats + 1 banana + 1 tsp flaxseeds",
                        "time": "7:30 AM",
                        "calories": 350,
                        "protein": 10,
                        "carbs": 40,
                        "fats": 12
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Coconut water with a handful of peanuts",
                        "quantity": "1 glass coconut water + 10 peanuts",
                        "time": "10:30 AM",
                        "calories": 170,
                        "protein": 5,
                        "carbs": 10,
                        "fats": 10
                }
        ],
        "Lunch": [
                {
                        "item": "Brown rice with dal, sautéed vegetables, and salad",
                        "quantity": "1 cup rice + 1 cup dal + 1 cup vegetables + 1 cup salad",
                        "time": "1:30 PM",
                        "calories": 450,
                        "protein": 18,
                        "carbs": 45,
                        "fats": 12
                }
        ],
        "Evening Snack": [
                {
                        "item": "Sprouts chaat with lemon",
                        "quantity": "1 cup sprouts + lemon juice",
                        "time": "5:00 PM",
                        "calories": 150,
                        "protein": 12,
                        "carbs": 15,
                        "fats": 4
                }
        ],
        "Dinner": [
                {
                        "item": "Millet roti with palak paneer and carrot sticks",
                        "quantity": "2 rotis + 1/2 cup palak paneer + 1 cup carrots",
                        "time": "8:00 PM",
                        "calories": 400,
                        "protein": 20,
                        "carbs": 35,
                        "fats": 14
                }
        ]
},
"active": {
        "Breakfast": [
                {
                        "item": "Paneer Bhurji Toast",
                        "quantity": "2 slices toast + 1/2 cup paneer bhurji + 1tsp ghee",
                        "time": "7:30 AM",
                        "calories": 400,
                        "protein": 22,
                        "carbs": 30,
                        "fats": 20
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Fruit smoothie with chia seeds",
                        "quantity": "1 glass smoothie (banana, berries, almond milk) + 1 tsp chia seeds",
                        "time": "10:30 AM",
                        "calories": 200,
                        "protein": 6,
                        "carbs": 28,
                        "fats": 8
                }
        ],
        "Lunch": [
                {
                        "item": "brown rice with mixed vegetables and moong dal",
                        "quantity": "1 cup brown rice + 1 cup vegetables + 1 cup dal",
                        "time": "1:30 PM",
                        "calories": 500,
                        "protein": 22,
                        "carbs": 50,
                        "fats": 14
                }
        ],
        "Evening Snack": [
                {
                        "item": "Roasted chickpeas and herbal tea",
                        "quantity": "1/2 cup chickpeas + 1 cup tea",
                        "time": "5:00 PM",
                        "calories": 180,
                        "protein": 10,
                        "carbs": 20,
                        "fats": 6
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled paneer with sautéed greens and soup",
                        "quantity": "100g paneer + 1 cup greens + 1 bowl soup",
                        "time": "8:00 PM",
                        "calories": 450,
                        "protein": 25,
                        "carbs": 20,
                        "fats": 22
                }
        ]
}
                },
                "51+":{
                "sedentary": {
        "Breakfast": [
                {
                        "item": "Oats porridge with flaxseeds and apple",
                        "quantity": "1 cup oats + 1 tsp flaxseeds + 1 apple",
                        "time": "7:30 AM",
                        "calories": 350,
                        "protein": 12,
                        "carbs": 45,
                        "fats": 10
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Buttermilk and a handful of walnuts",
                        "quantity": "1 glass buttermilk + 5 walnuts",
                        "time": "10:30 AM",
                        "calories": 150,
                        "protein": 5,
                        "carbs": 8,
                        "fats": 10
                }
        ],
        "Lunch": [
                {
                        "item": "Brown rice with mixed veg curry and salad",
                        "quantity": "1 cup rice + 1 cup curry + 1 bowl salad",
                        "time": "1:30 PM",
                        "calories": 450,
                        "protein": 14,
                        "carbs": 55,
                        "fats": 14
                }
        ],
        "Evening Snack": [
                {
                        "item": "Green tea and roasted lotus seeds (makhana)",
                        "quantity": "1 cup tea + 1/2 cup makhana",
                        "time": "5:00 PM",
                        "calories": 120,
                        "protein": 4,
                        "carbs": 10,
                        "fats": 6
                }
        ],
        "Dinner": [
                {
                        "item": "Vegetable soup with grilled tofu",
                        "quantity": "1 bowl soup + 100g tofu",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 20,
                        "carbs": 18,
                        "fats": 18
                }
        ]
},
                "moderate": {
        "Breakfast": [
                {
                        "item": "Vegetable poha with peanuts and herbal tea",
                        "quantity": "1.5 cups poha + 1 tsp peanuts + 1 cup tea",
                        "time": "7:30 AM",
                        "calories": 380,
                        "protein": 10,
                        "carbs": 50,
                        "fats": 12
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Coconut water and 1 banana",
                        "quantity": "1 glass coconut water + 1 medium banana",
                        "time": "10:30 AM",
                        "calories": 160,
                        "protein": 2,
                        "carbs": 35,
                        "fats": 1
                }
        ],
        "Lunch": [
                {
                        "item": "Multigrain roti with spinach dal and cucumber salad",
                        "quantity": "2 rotis + 1 cup dal + 1 bowl salad",
                        "time": "1:30 PM",
                        "calories": 450,
                        "protein": 18,
                        "carbs": 40,
                        "fats": 14
                }
        ],
        "Evening Snack": [
                {
                        "item": "Fruit chaat with chaat masala",
                        "quantity": "1 bowl mixed fruits",
                        "time": "5:00 PM",
                        "calories": 130,
                        "protein": 2,
                        "carbs": 28,
                        "fats": 1
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled paneer with sautéed vegetables and soup",
                        "quantity": "100g paneer + 1 cup veggies + 1 bowl soup",
                        "time": "8:00 PM",
                        "calories": 380,
                        "protein": 22,
                        "carbs": 20,
                        "fats": 20
                }
        ]
},
"active": {
        "Breakfast": [
                {
                        "item": "Vegetable oats upma with curd",
                        "quantity": "1.5 cups oats upma + 1/2 cup curd",
                        "time": "7:30 AM",
                        "calories": 400,
                        "protein": 15,
                        "carbs": 50,
                        "fats": 12
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Apple slices with 1 tbsp peanut butter",
                        "quantity": "1 medium apple + 1 tbsp peanut butter",
                        "time": "10:30 AM",
                        "calories": 180,
                        "protein": 4,
                        "carbs": 22,
                        "fats": 9
                }
        ],
        "Lunch": [
                {
                        "item": "Brown rice with rajma and mixed veg salad",
                        "quantity": "1 cup rice + 1 cup rajma + 1 bowl salad",
                        "time": "1:30 PM",
                        "calories": 480,
                        "protein": 20,
                        "carbs": 55,
                        "fats": 14
                }
        ],
        "Evening Snack": [
                {
                        "item": "Roasted chana and buttermilk",
                        "quantity": "1/2 cup chana + 1 glass buttermilk",
                        "time": "5:00 PM",
                        "calories": 150,
                        "protein": 8,
                        "carbs": 15,
                        "fats": 5
                }
        ],
        "Dinner": [
                {
                        "item": "brown rice khichdi with vegetables and mint chutney",
                        "quantity": "1.5 cups khichdi + 1 tbsp chutney",
                        "time": "8:00 PM",
                        "calories": 420,
                        "protein": 18,
                        "carbs": 42,
                        "fats": 14
                }
        ]
}
                }
            },
                "female": {
                    "18-30":{
                "sedentary": {
        "Breakfast": [
                {
                        "item": "Vegetable poha with green tea",
                        "quantity": "1 cup poha + 1 cup green tea (no sugar)",
                        "time": "7:30 AM",
                        "calories": 300,
                        "protein": 6,
                        "carbs": 40,
                        "fats": 10
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Cucumber and carrot sticks with lemon",
                        "quantity": "1 cup mixed sticks",
                        "time": "10:30 AM",
                        "calories": 80,
                        "protein": 2,
                        "carbs": 10,
                        "fats": 3
                }
        ],
        "Lunch": [
                {
                        "item": "Multigrain roti with palak paneer and salad",
                        "quantity": "2 rotis + 1/2 cup palak paneer + 1 bowl salad",
                        "time": "1:30 PM",
                        "calories": 400,
                        "protein": 20,
                        "carbs": 35,
                        "fats": 15
                }
        ],
        "Evening Snack": [
                {
                        "item": "Masala buttermilk with roasted makhana",
                        "quantity": "1 glass buttermilk + 1/2 cup makhana",
                        "time": "5:00 PM",
                        "calories": 130,
                        "protein": 6,
                        "carbs": 10,
                        "fats": 5
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled tofu stir fry with sautéed veggies",
                        "quantity": "100g tofu + 1 cup veggies",
                        "time": "8:00 PM",
                        "calories": 300,
                        "protein": 18,
                        "carbs": 15,
                        "fats": 12
                           }
                       ]
                    },
                    "moderate": {
        "Breakfast": [
                {
                        "item": "Moong dal chilla with mint chutney",
                        "quantity": "2 chillas + 2 tbsp chutney",
                        "time": "7:30 AM",
                        "calories": 350,
                        "protein": 18,
                        "carbs": 30,
                        "fats": 12
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Low-fat yogurt with chia seeds",
                        "quantity": "1/2 cup yogurt + 1 tsp chia seeds",
                        "time": "10:30 AM",
                        "calories": 120,
                        "protein": 8,
                        "carbs": 8,
                        "fats": 5
                }
        ],
        "Lunch": [
                {
                        "item": "Brown rice with rajma and mixed salad",
                        "quantity": "1/2 cup rice + 1/2 cup rajma + 1 bowl salad",
                        "time": "1:30 PM",
                        "calories": 450,
                        "protein": 20,
                        "carbs": 45,
                        "fats": 15
                }
        ],
        "Evening Snack": [
                {
                        "item": "Fruit bowl with nuts",
                        "quantity": "1 cup fruits + 5 almonds",
                        "time": "5:00 PM",
                        "calories": 180,
                        "protein": 5,
                        "carbs": 25,
                        "fats": 7
                }
        ],
        "Dinner": [
                {
                        "item": "brown rice pulao with sautéed vegetables",
                        "quantity": "3/4 cup brown rice + 1 cup vegetables",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 15,
                        "carbs": 35,
                        "fats": 10
                }
        ]
},
"active": {
        "Breakfast": [
                {
                        "item": "Oats porridge with milk, banana & flax seeds",
                        "quantity": "1 cup oats + 1 cup milk + 1 banana + 1 tsp flax seeds",
                        "time": "7:30 AM",
                        "calories": 400,
                        "protein": 18,
                        "carbs": 50,
                        "fats": 12
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Coconut water with roasted chana",
                        "quantity": "1 glass coconut water + 1/4 cup chana",
                        "time": "10:30 AM",
                        "calories": 150,
                        "protein": 6,
                        "carbs": 15,
                        "fats": 5
                }
        ],
        "Lunch": [
                {
                        "item": "Whole wheat roti, paneer bhurji & salad",
                        "quantity": "2 rotis + 3/4 cup paneer bhurji + 1 bowl salad",
                        "time": "1:30 PM",
                        "calories": 450,
                        "protein": 22,
                        "carbs": 35,
                        "fats": 15
                }
        ],
        "Evening Snack": [
                {
                        "item": "Green smoothie (spinach, apple, yogurt)",
                        "quantity": "1 glass smoothie",
                        "time": "5:00 PM",
                        "calories": 200,
                        "protein": 8,
                        "carbs": 25,
                        "fats": 6
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled paneer with sautéed vegetables",
                        "quantity": "100g paneer + 1 cup vegetables",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 25,
                        "carbs": 15,
                        "fats": 20
                }
        ]
}
                },
                "31-50":{
                "sedentary": {
        "Breakfast": [
                {
                        "item": "Vegetable poha with peanuts",
                        "quantity": "1 cup poha + 1 tbsp peanuts",
                        "time": "7:30 AM",
                        "calories": 350,
                        "protein": 9,
                        "carbs": 45,
                        "fats": 12
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Buttermilk",
                        "quantity": "1 glass (200ml)",
                        "time": "10:30 AM",
                        "calories": 80,
                        "protein": 3,
                        "carbs": 8,
                        "fats": 3
                }
        ],
        "Lunch": [
                {
                        "item": "Multigrain roti with palak dal and cucumber salad",
                        "quantity": "2 rotis + 1 cup palak dal + 1 cup salad",
                        "time": "1:30 PM",
                        "calories": 400,
                        "protein": 18,
                        "carbs": 35,
                        "fats": 12
                }
        ],
        "Evening Snack": [
                {
                        "item": "Roasted lotus seeds (makhana)",
                        "quantity": "1 cup",
                        "time": "5:00 PM",
                        "calories": 100,
                        "protein": 4,
                        "carbs": 12,
                        "fats": 4
                }
        ],
        "Dinner": [
                {
                        "item": "brown rice with mixed vegetable curry",
                        "quantity": "3/4 cup cooked brown rice + 1 cup curry",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 12,
                        "carbs": 30,
                        "fats": 15
                }
        ]
},
"moderate": {
        "Breakfast": [
                {
                        "item": "Moong dal chilla with mint chutney",
                        "quantity": "2 medium chillas + 2 tbsp chutney",
                        "time": "7:30 AM",
                        "calories": 350,
                        "protein": 18,
                        "carbs": 30,
                        "fats": 12
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Coconut water with chia seeds",
                        "quantity": "1 glass + 1 tsp chia",
                        "time": "10:30 AM",
                        "calories": 90,
                        "protein": 2,
                        "carbs": 8,
                        "fats": 4
                }
        ],
        "Lunch": [
                {
                        "item": "Brown rice with rajma and salad",
                        "quantity": "3/4 cup rice + 1 cup rajma + 1 cup salad",
                        "time": "1:30 PM",
                        "calories": 420,
                        "protein": 16,
                        "carbs": 45,
                        "fats": 10
                }
        ],
        "Evening Snack": [
                {
                        "item": "Sprouts chaat",
                        "quantity": "1 bowl (mixed sprouts, veggies, lemon)",
                        "time": "5:00 PM",
                        "calories": 130,
                        "protein": 9,
                        "carbs": 15,
                        "fats": 4
                }
        ],
        "Dinner": [
                {
                        "item": "Vegetable stuffed multigrain paratha with curd",
                        "quantity": "1 medium paratha + 1/2 cup curd",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 14,
                        "carbs": 30,
                        "fats": 14
                }
        ]
},
"active": {
        "Breakfast": [
                {
                        "item": "Vegetable upma with peanuts + herbal tea",
                        "quantity": "1 bowl upma + 1 tsp peanuts + 1 cup tea",
                        "time": "7:30 AM",
                        "calories": 400,
                        "protein": 12,
                        "carbs": 50,
                        "fats": 14
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Apple slices with almond butter",
                        "quantity": "1 medium apple + 1 tbsp almond butter",
                        "time": "10:30 AM",
                        "calories": 150,
                        "protein": 3,
                        "carbs": 20,
                        "fats": 7
                }
        ],
        "Lunch": [
                {
                        "item": "Multigrain roti + mixed vegetable sabzi + dal",
                        "quantity": "2 rotis + 1 cup sabzi + 1/2 cup dal",
                        "time": "1:30 PM",
                        "calories": 450,
                        "protein": 20,
                        "carbs": 40,
                        "fats": 14
                }
        ],
        "Evening Snack": [
                {
                        "item": "Protein smoothie with banana and oats",
                        "quantity": "1 glass (banana, oats, almond milk, plant protein)",
                        "time": "5:00 PM",
                        "calories": 200,
                        "protein": 12,
                        "carbs": 20,
                        "fats": 8
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled tofu + stir-fried vegetables + soup",
                        "quantity": "100g tofu + 1 cup vegetables + 1 cup soup",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 25,
                        "carbs": 20,
                        "fats": 16
                }
        ]
}
                },
                "51+":{
                    "sedentary": {
        "Breakfast": [
                {
                        "item": "Oats porridge with chia seeds and berries",
                        "quantity": "1 cup oats + 1 tsp chia seeds + 1/2 cup berries",
                        "time": "7:30 AM",
                        "calories": 350,
                        "protein": 10,
                        "carbs": 40,
                        "fats": 12
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Handful of walnuts",
                        "quantity": "6-8 walnut halves",
                        "time": "10:30 AM",
                        "calories": 120,
                        "protein": 3,
                        "carbs": 4,
                        "fats": 10
                }
        ],
        "Lunch": [
                {
                        "item": "Brown rice + rajma curry + cucumber salad",
                        "quantity": "1/2 cup brown rice + 1 cup rajma + 1 cup salad",
                        "time": "1:30 PM",
                        "calories": 400,
                        "protein": 18,
                        "carbs": 45,
                        "fats": 10
                }
        ],
        "Evening Snack": [
                {
                        "item": "Low-fat yogurt with flaxseeds",
                        "quantity": "1/2 cup yogurt + 1 tsp flaxseeds",
                        "time": "5:00 PM",
                        "calories": 100,
                        "protein": 6,
                        "carbs": 8,
                        "fats": 4
                }
        ],
        "Dinner": [
                {
                        "item": "Vegetable stew with brown rice",
                        "quantity": "1 cup stew + 1/2 cup brown rice",
                        "time": "8:00 PM",
                        "calories": 300,
                        "protein": 15,
                        "carbs": 30,
                        "fats": 10
                }
        ]
},
"moderate": {
        "Breakfast": [
                {
                        "item": "Vegetable upma with a glass of buttermilk",
            "quantity": "1.5 cups upma + 1 glass (200ml) buttermilk",
            "time": "7:30 AM",
            "calories": 350,
            "protein": 12,
            "carbs": 45,
            "fats": 10
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Apple with peanut butter",
                        "quantity": "1 medium apple + 1 tbsp peanut butter",
                        "time": "10:30 AM",
                        "calories": 200,
                        "protein": 4,
                        "carbs": 25,
                        "fats": 9
                }
        ],
        "Lunch": [
                {
                        "item": "Chapati + mixed vegetable curry + dal",
                        "quantity": "2 chapatis + 1 cup sabzi + 1/2 cup dal",
                        "time": "1:30 PM",
                        "calories": 450,
                        "protein": 20,
                        "carbs": 50,
                        "fats": 12
                }
        ],
        "Evening Snack": [
                {
                        "item": "Buttermilk and roasted chana",
                        "quantity": "1 cup buttermilk + 1/4 cup roasted chana",
                        "time": "5:00 PM",
                        "calories": 150,
                        "protein": 8,
                        "carbs": 10,
                        "fats": 5
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled tofu with stir-fried veggies",
                        "quantity": "100g tofu + 1 cup veggies",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 22,
                        "carbs": 20,
                        "fats": 18
                }
        ]
},
"active": {
        "Breakfast": [
                {
                        "item": "Oats porridge with berries and flaxseeds",
                        "quantity": "1 cup oats + 1/2 cup berries + 1 tbsp flaxseeds",
                        "time": "7:30 AM",
                        "calories": 450,
                        "protein": 18,
                        "carbs": 50,
                        "fats": 15
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Greek yogurt with walnuts",
                        "quantity": "1/2 cup Greek yogurt + 5 walnuts",
                        "time": "10:30 AM",
                        "calories": 220,
                        "protein": 12,
                        "carbs": 12,
                        "fats": 14
                }
        ],
        "Lunch": [
                {
                        "item": "brown rice salad with chickpeas and veggies",
                        "quantity": "1 cup brown rice + 1/2 cup chickpeas + veggies",
                        "time": "1:30 PM",
                        "calories": 500,
                        "protein": 20,
                        "carbs": 55,
                        "fats": 16
                }
        ],
        "Evening Snack": [
                {
                        "item": "Carrot sticks with hummus",
                        "quantity": "1 cup carrot sticks + 2 tbsp hummus",
                        "time": "5:00 PM",
                        "calories": 150,
                        "protein": 5,
                        "carbs": 15,
                        "fats": 8
                }
        ],
        "Dinner": [
                {
                        "item": "Palak paneer with multigrain roti",
                        "quantity": "1 cup palak paneer + 2 rotis",
                        "time": "8:00 PM",
                        "calories": 400,
                        "protein": 22,
                        "carbs": 30,
                        "fats": 18
                }
        ]
}
                }
            }
        },
        "non-vegetarian":{
            "male":{
                "18-30":{
                    "sedentary": {
        "Breakfast": [
                {
                        "item": "Scrambled eggs with vegetables",
                        "quantity": "2 eggs + 1 cup mixed vegetables",
                        "time": "7:30 AM",
                        "calories": 350,
                        "protein": 20,
                        "carbs": 15,
                        "fats": 22
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Low-fat yogurt",
                        "quantity": "1 cup low-fat yogurt",
                        "time": "10:30 AM",
                        "calories": 120,
                        "protein": 10,
                        "carbs": 12,
                        "fats": 3
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken with steamed broccoli",
                        "quantity": "120g grilled chicken + 1 cup broccoli",
                        "time": "1:30 PM",
                        "calories": 400,
                        "protein": 35,
                        "carbs": 10,
                        "fats": 18
                }
        ],
        "Evening Snack": [
                {
                        "item": "Cucumber and carrot sticks",
                        "quantity": "1 cup mixed cucumber and carrot sticks",
                        "time": "5:00 PM",
                        "calories": 80,
                        "protein": 2,
                        "carbs": 14,
                        "fats": 0
                }
        ],
        "Dinner": [
                {
                        "item": "Baked fish with sautéed greens",
                        "quantity": "100g baked fish + 1 cup greens",
                        "time": "8:00 PM",
                        "calories": 320,
                        "protein": 28,
                        "carbs": 7,
                        "fats": 16
                }
        ]
},
"moderate": {
        "Breakfast": [
                {
                        "item": "Boiled eggs with multigrain toast",
                        "quantity": "3 eggs + 2 slices multigrain toast",
                        "time": "7:30 AM",
                        "calories": 400,
                        "protein": 25,
                        "carbs": 20,
                        "fats": 22
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Greek yogurt with chia seeds",
                        "quantity": "1/2 cup Greek yogurt + 1 tbsp chia seeds",
                        "time": "10:30 AM",
                        "calories": 180,
                        "protein": 12,
                        "carbs": 10,
                        "fats": 9
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken salad",
                        "quantity": "150g grilled chicken + assorted veggies",
                        "time": "1:30 PM",
                        "calories": 450,
                        "protein": 35,
                        "carbs": 15,
                        "fats": 22
                }
        ],
        "Evening Snack": [
                {
                        "item": "Handful of almonds",
                        "quantity": "10 almonds",
                        "time": "5:00 PM",
                        "calories": 100,
                        "protein": 4,
                        "carbs": 3,
                        "fats": 9
                }
        ],
        "Dinner": [
                {
                        "item": "Fish curry with sautéed spinach",
                        "quantity": "100g fish + 1 cup spinach",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 30,
                        "carbs": 8,
                        "fats": 18
                }
        ]
},
"active": {
        "Breakfast": [
                {
                        "item": "Omelette with spinach and mushrooms",
                        "quantity": "3 eggs + 1 cup spinach + ½ cup mushrooms",
                        "time": "7:30 AM",
                        "calories": 400,
                        "protein": 28,
                        "carbs": 8,
                        "fats": 26
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Greek yogurt with berries",
                        "quantity": "1 cup Greek yogurt + ½ cup berries",
                        "time": "10:30 AM",
                        "calories": 150,
                        "protein": 15,
                        "carbs": 12,
                        "fats": 4
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken breast with brown rice salad",
                        "quantity": "150g chicken + 1 cup brown rice salad",
                        "time": "1:30 PM",
                        "calories": 500,
                        "protein": 40,
                        "carbs": 30,
                        "fats": 20
                }
        ],
        "Evening Snack": [
                {
                        "item": "Boiled eggs and cucumber slices",
                        "quantity": "2 boiled eggs + 1 cup cucumber slices",
                        "time": "5:00 PM",
                        "calories": 200,
                        "protein": 14,
                        "carbs": 5,
                        "fats": 14
                }
        ],
        "Dinner": [
                {
                        "item": "Tandoori fish with mixed greens",
                        "quantity": "120g tandoori fish + 1 cup salad greens",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 32,
                        "carbs": 6,
                        "fats": 18
                }
        ]
}
                },
                "31-50":{
                    "sedentary": {
        "Breakfast": [
                {
                        "item": "Boiled eggs with whole wheat toast",
                        "quantity": "2 boiled eggs + 2 slices whole wheat toast",
                        "time": "8:00 AM",
                        "calories": 350,
                        "protein": 20,
                        "carbs": 25,
                        "fats": 18
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Buttermilk with a handful of walnuts",
                        "quantity": "1 glass buttermilk + 5 walnuts",
                        "time": "11:00 AM",
                        "calories": 150,
                        "protein": 6,
                        "carbs": 10,
                        "fats": 10
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken salad with olive oil dressing",
                        "quantity": "150g chicken + 2 cups mixed greens + 1 tbsp olive oil",
                        "time": "2:00 PM",
                        "calories": 450,
                        "protein": 38,
                        "carbs": 12,
                        "fats": 24
                }
        ],
        "Evening Snack": [
                {
                        "item": "Apple slices with peanut butter",
                        "quantity": "1 apple + 1 tbsp peanut butter",
                        "time": "5:30 PM",
                        "calories": 200,
                        "protein": 4,
                        "carbs": 25,
                        "fats": 10
                }
        ],
        "Dinner": [
                {
                        "item": "Fish curry with sautéed vegetables",
                        "quantity": "100g fish curry + 1 cup sautéed vegetables",
                        "time": "8:30 PM",
                        "calories": 350,
                        "protein": 28,
                        "carbs": 8,
                        "fats": 20
                }
        ]
},
"moderate": {
        "Breakfast": [
                {
                        "item": "Omelette with spinach and mushrooms + 1 multigrain toast",
                        "quantity": "2 eggs + 1/2 cup spinach + 1/2 cup mushrooms + 1 slice toast",
                        "time": "7:30 AM",
                        "calories": 400,
                        "protein": 25,
                        "carbs": 20,
                        "fats": 22
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Low-fat Greek yogurt with chia seeds",
                        "quantity": "1 cup yogurt + 1 tbsp chia seeds",
                        "time": "10:30 AM",
                        "calories": 180,
                        "protein": 12,
                        "carbs": 10,
                        "fats": 8
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken breast with brown rice and steamed broccoli",
                        "quantity": "150g chicken + 1/2 cup brown rice + 1 cup broccoli",
                        "time": "1:30 PM",
                        "calories": 500,
                        "protein": 40,
                        "carbs": 30,
                        "fats": 18
                }
        ],
        "Evening Snack": [
                {
                        "item": "Cucumber sticks with hummus",
                        "quantity": "1 cucumber + 2 tbsp hummus",
                        "time": "5:00 PM",
                        "calories": 150,
                        "protein": 5,
                        "carbs": 12,
                        "fats": 9
                }
        ],
        "Dinner": [
                {
                        "item": "Tandoori fish with sautéed green beans",
                        "quantity": "120g fish + 1 cup green beans",
                        "time": "8:00 PM",
                        "calories": 400,
                        "protein": 35,
                        "carbs": 10,
                        "fats": 20
                }
        ]
},
"active": {
        "Breakfast": [
                {
                        "item": "Scrambled eggs with mixed veggies + 2 multigrain toasts",
                        "quantity": "3 eggs + 1/2 cup mixed vegetables + 2 slices toast",
                        "time": "7:00 AM",
                        "calories": 500,
                        "protein": 30,
                        "carbs": 30,
                        "fats": 28
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Protein smoothie with whey protein, banana, and almond milk",
                        "quantity": "1 scoop whey + 1 banana + 1 cup almond milk",
                        "time": "10:00 AM",
                        "calories": 250,
                        "protein": 20,
                        "carbs": 20,
                        "fats": 8
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken thigh with brown rice and stir-fried vegetables",
                        "quantity": "150g chicken + 1/2 cup brown rice + 1 cup vegetables",
                        "time": "1:00 PM",
                        "calories": 550,
                        "protein": 40,
                        "carbs": 35,
                        "fats": 20
                }
        ],
        "Evening Snack": [
                {
                        "item": "Handful of mixed nuts and a boiled egg",
                        "quantity": "15g nuts + 1 egg",
                        "time": "4:30 PM",
                        "calories": 200,
                        "protein": 10,
                        "carbs": 5,
                        "fats": 16
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled fish with roasted vegetables",
                        "quantity": "150g fish + 1 cup roasted vegetables",
                        "time": "7:30 PM",
                        "calories": 450,
                        "protein": 35,
                        "carbs": 15,
                        "fats": 22
                }
        ]
}
                },
                "51+":{
                    "sedentary": {
        "Breakfast": [
                {
                        "item": "Boiled eggs with whole wheat toast",
                        "quantity": "2 eggs + 1 slice toast",
                        "time": "7:30 AM",
                        "calories": 300,
                        "protein": 18,
                        "carbs": 20,
                        "fats": 15
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Low-fat yogurt with chia seeds",
                        "quantity": "1 cup yogurt + 1 tbsp chia seeds",
                        "time": "10:30 AM",
                        "calories": 150,
                        "protein": 10,
                        "carbs": 12,
                        "fats": 5
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken salad with olive oil dressing",
                        "quantity": "100g chicken + 2 cups salad greens + 1 tbsp olive oil",
                        "time": "1:00 PM",
                        "calories": 400,
                        "protein": 30,
                        "carbs": 10,
                        "fats": 25
                }
        ],
        "Evening Snack": [
                {
                        "item": "Handful of walnuts",
                        "quantity": "20g walnuts",
                        "time": "4:30 PM",
                        "calories": 130,
                        "protein": 4,
                        "carbs": 4,
                        "fats": 12
                }
        ],
        "Dinner": [
                {
                        "item": "Steamed fish with sautéed spinach",
                        "quantity": "120g fish + 1 cup spinach",
                        "time": "7:30 PM",
                        "calories": 350,
                        "protein": 30,
                        "carbs": 8,
                        "fats": 18
                }
        ]
},
"moderate": {
        "Breakfast": [
                {
                        "item": "Omelette with veggies and whole wheat toast",
                        "quantity": "2 eggs + 1/2 cup mixed veggies + 1 slice toast",
                        "time": "7:30 AM",
                        "calories": 350,
                        "protein": 22,
                        "carbs": 25,
                        "fats": 18
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Low-fat paneer cubes",
                        "quantity": "50g paneer",
                        "time": "10:30 AM",
                        "calories": 120,
                        "protein": 12,
                        "carbs": 2,
                        "fats": 8
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken breast with brown rice and mixed veggies",
                        "quantity": "120g chicken + 1/2 cup brown rice + 1 cup veggies",
                        "time": "1:00 PM",
                        "calories": 450,
                        "protein": 35,
                        "carbs": 30,
                        "fats": 20
                }
        ],
        "Evening Snack": [
                {
                        "item": "Apple slices with peanut butter",
                        "quantity": "1 medium apple + 1 tbsp peanut butter",
                        "time": "4:30 PM",
                        "calories": 180,
                        "protein": 4,
                        "carbs": 22,
                        "fats": 8
                }
        ],
        "Dinner": [
                {
                        "item": "Fish curry with multigrain roti",
                        "quantity": "100g fish + 1 roti",
                        "time": "7:30 PM",
                        "calories": 400,
                        "protein": 28,
                        "carbs": 20,
                        "fats": 18
                }
        ]
},
"active": {
        "Breakfast": [
                {
                        "item": "Scrambled eggs with spinach and 2 multigrain toasts",
                        "quantity": "3 eggs + 1/2 cup spinach + 2 slices toast",
                        "time": "7:30 AM",
                        "calories": 450,
                        "protein": 30,
                        "carbs": 30,
                        "fats": 22
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Greek yogurt with chia seeds",
                        "quantity": "1 cup yogurt + 1 tbsp chia seeds",
                        "time": "10:30 AM",
                        "calories": 200,
                        "protein": 18,
                        "carbs": 10,
                        "fats": 8
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken salad with olive oil dressing",
                        "quantity": "150g chicken + 2 cups mixed greens + 1 tbsp olive oil",
                        "time": "1:00 PM",
                        "calories": 500,
                        "protein": 40,
                        "carbs": 15,
                        "fats": 28
                }
        ],
        "Evening Snack": [
                {
                        "item": "Handful of almonds and 1 banana",
                        "quantity": "15 almonds + 1 small banana",
                        "time": "4:30 PM",
                        "calories": 220,
                        "protein": 6,
                        "carbs": 20,
                        "fats": 14
                }
        ],
        "Dinner": [
                {
                        "item": "Baked fish with steamed vegetables",
                        "quantity": "120g fish + 1.5 cups vegetables",
                        "time": "7:30 PM",
                        "calories": 400,
                        "protein": 30,
                        "carbs": 18,
                        "fats": 20
                }
        ]
}
                }
            },
            "female":{
                "18-30":{
                   "sedentary": {
        "Breakfast": [
                {
                        "item": "Boiled eggs with 1 slice multigrain toast",
                        "quantity": "2 eggs + 1 slice toast",
                        "time": "8:00 AM",
                        "calories": 300,
                        "protein": 20,
                        "carbs": 18,
                        "fats": 18
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Low-fat yogurt with berries",
                        "quantity": "3/4 cup yogurt + 1/4 cup berries",
                        "time": "10:30 AM",
                        "calories": 150,
                        "protein": 10,
                        "carbs": 15,
                        "fats": 4
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken wrap with whole wheat tortilla",
                        "quantity": "100g chicken + 1 tortilla + lettuce",
                        "time": "1:30 PM",
                        "calories": 400,
                        "protein": 30,
                        "carbs": 25,
                        "fats": 18
                }
        ],
        "Evening Snack": [
                {
                        "item": "Handful of walnuts",
                        "quantity": "10 halves",
                        "time": "5:00 PM",
                        "calories": 180,
                        "protein": 4,
                        "carbs": 4,
                        "fats": 18
                }
        ],
        "Dinner": [
                {
                        "item": "Stir-fried prawns with vegetables",
                        "quantity": "120g prawns + 1 cup mixed vegetables",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 28,
                        "carbs": 12,
                        "fats": 20
                }
        ]
},
"moderate": {
        "Breakfast": [
                {
                        "item": "Scrambled eggs with spinach and whole wheat toast",
                        "quantity": "2 eggs + 1 cup spinach + 1 toast",
                        "time": "8:00 AM",
                        "calories": 350,
                        "protein": 22,
                        "carbs": 20,
                        "fats": 20
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Greek yogurt with flaxseeds",
                        "quantity": "1 cup yogurt + 1 tbsp flaxseeds",
                        "time": "11:00 AM",
                        "calories": 200,
                        "protein": 15,
                        "carbs": 10,
                        "fats": 10
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled fish with brown rice and salad",
                        "quantity": "120g fish + 1/2 cup brown rice + 1 cup salad",
                        "time": "2:00 PM",
                        "calories": 450,
                        "protein": 35,
                        "carbs": 30,
                        "fats": 18
                }
        ],
        "Evening Snack": [
                {
                        "item": "Roasted chickpeas",
                        "quantity": "1/2 cup",
                        "time": "5:30 PM",
                        "calories": 150,
                        "protein": 8,
                        "carbs": 18,
                        "fats": 5
                }
        ],
        "Dinner": [
                {
                        "item": "Chicken stew with vegetables",
                        "quantity": "100g chicken + 1 cup vegetables",
                        "time": "8:30 PM",
                        "calories": 380,
                        "protein": 30,
                        "carbs": 20,
                        "fats": 18
                }
        ]
},
"active": {
        "Breakfast": [
                {
                        "item": "Masala Egg Bhurji with Butter toast",
                        "quantity": "2 eggs (bhurji style) + 1 tbsp butter + 1 toast + spices",
                        "time": "7:30 AM",
                        "calories": 400,
                        "protein": 24,
                        "carbs": 18,
                        "fats": 25
                }
        ],
        "Mid-Morning Snack": [
                {
                  "item": "Peanut butter-stuffed dates with almonds",
                  "quantity": "3 medium dates + 1tbsp peanut butter + 5 almonds",
                  "time": "4:30 PM",
                  "calories": 200,
                  "protein": 15,
                  "carbs": 15,
                  "fats": 8
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken breast with brown rice and steamed broccoli",
                        "quantity": "120g chicken + 3/4 cup brown rice + 1 cup broccoli",
                        "time": "1:30 PM",
                        "calories": 500,
                        "protein": 40,
                        "carbs": 35,
                        "fats": 15
                }
        ],
        "Evening Snack": [
                {
                        "item": "Boiled corn with lemon and salt",
                        "quantity": "1 medium corn cob",
                        "time": "5:00 PM",
                        "calories": 150,
                        "protein": 5,
                        "carbs": 30,
                        "fats": 2
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled fish with sautéed green beans",
                        "quantity": "120g fish + 1 cup green beans",
                        "time": "8:00 PM",
                        "calories": 380,
                        "protein": 30,
                        "carbs": 12,
                        "fats": 22
                }
        ]
}
                },
                "31-50":{
                    "sedentary": {
        "Breakfast": [
                {
                        "item": "Scrambled eggs with spinach",
                        "quantity": "2 eggs + 1/2 cup spinach",
                        "time": "8:00 AM",
                        "calories": 250,
                        "protein": 18,
                        "carbs": 5,
                        "fats": 18
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Greek yogurt with chia seeds",
                        "quantity": "1/2 cup yogurt + 1 tsp chia seeds",
                        "time": "11:00 AM",
                        "calories": 150,
                        "protein": 10,
                        "carbs": 8,
                        "fats": 6
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken salad with olive oil dressing",
                        "quantity": "100g chicken + 2 cups salad + 1 tbsp olive oil",
                        "time": "2:00 PM",
                        "calories": 400,
                        "protein": 30,
                        "carbs": 10,
                        "fats": 25
                }
        ],
        "Evening Snack": [
                {
                        "item": "Handful of walnuts",
                        "quantity": "7-8 halves",
                        "time": "5:30 PM",
                        "calories": 180,
                        "protein": 5,
                        "carbs": 4,
                        "fats": 16
                }
        ],
        "Dinner": [
                {
                        "item": "Baked fish with mixed vegetables",
                        "quantity": "100g fish + 1 cup vegetables",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 28,
                        "carbs": 10,
                        "fats": 20
                }
        ]
},
"moderate": {
        "Breakfast": [
                {
                        "item": "Boiled eggs and multigrain toast",
                        "quantity": "2 eggs + 1 toast",
                        "time": "7:30 AM",
                        "calories": 300,
                        "protein": 20,
                        "carbs": 15,
                        "fats": 18
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "roasted masala paneer cubes",
                        "quantity": "60g low-fat paneer",
                        "time": "10:30 AM",
                        "calories": 120,
                        "protein": 10,
                        "carbs": 3,
                        "fats": 8
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken wrap with veggies",
                        "quantity": "100g chicken + whole wheat wrap + 1 cup veggies",
                        "time": "1:30 PM",
                        "calories": 450,
                        "protein": 32,
                        "carbs": 30,
                        "fats": 20
                }
        ],
        "Evening Snack": [
                {
                        "item": "Mixed nuts",
                        "quantity": "10-12 nuts",
                        "time": "5:00 PM",
                        "calories": 200,
                        "protein": 6,
                        "carbs": 8,
                        "fats": 18
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled fish with brown rice and broccoli",
                        "quantity": "100g fish + 1/2 cup brown rice + 1 cup broccoli",
                        "time": "8:00 PM",
                        "calories": 400,
                        "protein": 30,
                        "carbs": 25,
                        "fats": 18
                }
        ]
},
"active": {
        "Breakfast": [
                {
                        "item": "Scrambled eggs with spinach and whole wheat toast",
                        "quantity": "2 eggs + 1/2 cup spinach + 1 toast",
                        "time": "7:30 AM",
                        "calories": 350,
                        "protein": 22,
                        "carbs": 18,
                        "fats": 20
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Greek yogurt with chia seeds",
                        "quantity": "1 cup yogurt + 1 tsp chia seeds",
                        "time": "10:30 AM",
                        "calories": 150,
                        "protein": 12,
                        "carbs": 10,
                        "fats": 5
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken salad with vinaigrette dressing",
                        "quantity": "100g chicken + 2 cups salad + 1 tbsp dressing",
                        "time": "1:30 PM",
                        "calories": 400,
                        "protein": 35,
                        "carbs": 20,
                        "fats": 18
                }
        ],
        "Evening Snack": [
                {
                        "item": "Peanut butter on whole wheat cracker",
                        "quantity": "1 cracker + 1 tbsp peanut butter",
                        "time": "5:00 PM",
                        "calories": 180,
                        "protein": 7,
                        "carbs": 12,
                        "fats": 12
                }
        ],
        "Dinner": [
                {
                        "item": "Baked fish with roasted sweet potatoes and green beans",
                        "quantity": "100g fish + 1/2 cup sweet potatoes + 1 cup green beans",
                        "time": "8:00 PM",
                        "calories": 450,
                        "protein": 32,
                        "carbs": 30,
                        "fats": 20
                }
        ]
}
                },
                "51+":{
                    "sedentary": {
        "Breakfast": [
                {
                        "item": "Egg Masala Toast ",
                        "quantity": "1 boiled egg (mashed) + 1 toast + 1 tsp ghee",
                        "time": "8:00 AM",
                        "calories": 300,
                        "protein": 14,
                        "carbs": 18,
                        "fats": 18
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Low-fat yogurt with flaxseeds",
                        "quantity": "1 cup yogurt + 1 tsp flaxseeds",
                        "time": "10:30 AM",
                        "calories": 120,
                        "protein": 10,
                        "carbs": 8,
                        "fats": 4
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken breast with steamed broccoli and brown rice",
                        "quantity": "100g chicken + 1 cup broccoli + 1/2 cup brown rice",
                        "time": "1:30 PM",
                        "calories": 400,
                        "protein": 35,
                        "carbs": 30,
                        "fats": 15
                }
        ],
        "Evening Snack": [
                {
                        "item": "Handful of mixed nuts",
                        "quantity": "15g nuts",
                        "time": "5:00 PM",
                        "calories": 100,
                        "protein": 4,
                        "carbs": 4,
                        "fats": 8
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled fish with sautéed greens",
                        "quantity": "100g fish + 1 cup greens",
                        "time": "8:00 PM",
                        "calories": 350,
                        "protein": 30,
                        "carbs": 10,
                        "fats": 20
                }
        ]
},
"moderate": {
        "Breakfast": [
                {
                        "item": "Scrambled eggs with spinach and multigrain toast",
                        "quantity": "2 eggs + 1/2 cup spinach + 1 toast",
                        "time": "7:30 AM",
                        "calories": 350,
                        "protein": 20,
                        "carbs": 20,
                        "fats": 22
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Greek yogurt with a handful of berries",
                        "quantity": "1 cup yogurt + 1/2 cup berries",
                        "time": "10:30 AM",
                        "calories": 150,
                        "protein": 12,
                        "carbs": 15,
                        "fats": 5
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken salad with olive oil dressing",
                        "quantity": "120g chicken + 2 cups mixed veggies + 1 tbsp olive oil",
                        "time": "1:30 PM",
                        "calories": 450,
                        "protein": 35,
                        "carbs": 18,
                        "fats": 25
                }
        ],
        "Evening Snack": [
                {
                        "item": "Roasted chickpeas",
                        "quantity": "30g roasted chickpeas",
                        "time": "5:30 PM",
                        "calories": 120,
                        "protein": 6,
                        "carbs": 18,
                        "fats": 3
                }
        ],
        "Dinner": [
                {
                        "item": "crilled chicken thighs with brown rice and side salad (lettuce/cucumber) + olive oil (grilling) ",
                        "quantity": "100g chicken thigh + 1/3 cup brown rice + 1 tsp olive oil +50g salad",
                        "time": "8:00 PM",
                        "calories": 450,
                        "protein": 35,
                        "carbs": 20,
                        "fats": 22
                }
        ]
},
"active": {
        "Breakfast": [
                {
                        "item": "Omelette with 2 eggs, tomatoes, and onions + 1 multigrain toast",
                        "quantity": "2 eggs + 1/2 cup vegetables + 1 toast",
                        "time": "7:30 AM",
                        "calories": 380,
                        "protein": 22,
                        "carbs": 20,
                        "fats": 24
                }
        ],
        "Mid-Morning Snack": [
                {
                        "item": "Protein smoothie with banana and peanut butter",
                        "quantity": "1 scoop protein + 1 banana + 1 tbsp peanut butter + water",
                        "time": "10:30 AM",
                        "calories": 250,
                        "protein": 20,
                        "carbs": 18,
                        "fats": 10
                }
        ],
        "Lunch": [
                {
                        "item": "Grilled chicken wrap with vegetables",
                        "quantity": "100g chicken + 1 whole wheat wrap + 1 cup veggies",
                        "time": "1:30 PM",
                        "calories": 450,
                        "protein": 35,
                        "carbs": 30,
                        "fats": 18
                }
        ],
        "Evening Snack": [
                {
                        "item": "Handful of walnuts and almonds",
                        "quantity": "10 almonds + 5 walnuts",
                        "time": "5:30 PM",
                        "calories": 180,
                        "protein": 6,
                        "carbs": 8,
                        "fats": 16
                }
        ],
        "Dinner": [
                {
                        "item": "Grilled chicken with sautéed spinach and brown rice",
                        "quantity": "110g chicken + 1/3 cup cooked brown rice + 1.5 cup spinach",
                        "time": "8:00 PM",
                        "calories": 480,
                        "protein": 35,
                        "carbs": 28,
                        "fats": 22
                }
        ]
}
                }
            }
        }
    },
}
    
def get_age_range(age):
    if age <= 30:
        return "18-30"
    elif age <= 50:
        return "31-50"
    else:
        return "51+"
    
tips = {
    'muscle_gain': {
        'male': {
            '18-30': {
                'sedentary': "Add strength workouts slowly and focus on protein-rich Indian meals like paneer, eggs(if non-vegetarian), dals. Rest is key.",
                'moderate': "Lift progressively, eat calorie-dense meals with chicken(if non-vegetarian), nuts, and oats. Stay hydrated.",
                'active': "Train smart with compound lifts. Prioritize muscle recovery with protein, sleep, and anti-inflammatory foods."
            },
            '31-50': {
                'sedentary': "Begin with bodyweight workouts and protein-rich meals like dal, paneer, and eggs(if non-vegetarian). Sleep well.",
                'moderate': "Focus on consistency in workouts and high-protein Indian meals. Avoid processed food.",
                'active': "Track workouts and macros. Eat clean, lift smart, and don't skip recovery days."
            },
            '51+': {
                'sedentary': "Include walking and light strength work. Eat soft protein foods like boiled eggs(if non-vegetarian) and paneer bhurji.",
                'moderate': "Strength train 2–3x a week and eat well-balanced meals with fish(if non-vegetarian), lentils, and healthy fats.",
                'active': "Balance workouts with rest. Support joints with good fats and protein. Don’t overtrain."
            }
        },
        'female': {
            '18-30': {
                'sedentary': "Start light strength training and include protein like eggs(if non-vegetarian), lentils, and tofu in meals.",
                'moderate': "Lift weights 3–4x/week and eat calorie-rich foods like paneer paratha and smoothies with whey.",
                'active': "Focus on progressive overload and eating every 3–4 hours. Track your protein intake."
            },
            '31-50': {
                'sedentary': "Begin strength-based movement like yoga or Pilates. Add dals, nuts, and paneer for protein.",
                'moderate': "Train consistently and add meals with chicken(if non-vegetarian), fish(if non-vegetarian), or paneer. Keep stress low.",
                'active': "Optimize your recovery. Use whey, eggs(if non-vegetarian), and ghee wisely in your meal plan. Stay active."
            },
            '51+': {
                'sedentary': "Choose joint-friendly strength routines and soft protein foods like dals, eggs(if non-vegetarian), and tofu.",
                'moderate': "Support your workouts with nutrient-dense foods and hydration. Avoid skipping meals.",
                'active': "Lift light but regularly. Ensure calcium, vitamin D, and protein intake is optimal."
            }
        }
    },
    'weight_loss': {
        'male': {
            '18-30': {
                'sedentary': "Start with walking and reduce sugar, fried food. Drink warm water before meals.",
                'moderate': "Combine cardio and strength. Eat high-fiber meals with sprouts, eggs(if non-vegetarian), and salads.",
                'active': "Track intake and macros. Focus on lean protein like chicken(if non-vegetarian) and avoid late-night meals."
            },
            '31-50': {
                'sedentary': "Avoid processed snacks. Begin with morning walks and portion control.",
                'moderate': "Train consistently and increase fiber intake. Watch salt and sugar.",
                'active': "Focus on clean eating. Meal prep to avoid binge eating. Prioritize sleep."
            },
            '51+': {
                'sedentary': "Start walking 5k steps daily. Avoid deep-fried items. Drink plenty of water.",
                'moderate': "Eat smaller, more frequent meals. Include oats, fruits, and dal in your diet.",
                'active': "Continue light workouts. Prioritize vegetables, protein and digestive health."
            }
        },
        'female': {
            '18-30': {
                'sedentary': "Add daily walks and swap sugary drinks with herbal tea. Focus on home-cooked meals.",
                'moderate': "Do bodyweight workouts and eat meals with dal, veggies, and curd.",
                'active': "Eat every 3-4 hours. Cut sugar and focus on complex carbs like brown rice and dal."
            },
            '31-50': {
                'sedentary': "Walk post meals. Replace white carbs with millets. Cut back on fried food.",
                'moderate': "Strength train lightly and stay hydrated. Eat more vegetables.",
                'active': "Maintain routine with clean eating. Track portions. Avoid processed sweets."
            },
            '51+': {
                'sedentary': "Walk 4,000–5,000 steps daily. Include fruits, sabzis, and dal. Avoid outside food.",
                'moderate': "Practice yoga and eat more raw foods. Focus on fiber and light proteins.",
                'active': "Stay active but don’t overtrain. Add flax seeds and soups to support digestion."
            }
        }
    },
    'general_health': {
        'male': {
            '18-30': {
                'sedentary': "Move every hour. Eat fruits and avoid chips and sugary sodas.",
                'moderate': "Exercise 3-4x/week and add nuts, seeds, and veggies to meals.",
                'active': "Eat whole foods, stay hydrated, and sleep 7-8 hours."
            },
            '31-50': {
                'sedentary': "Avoid skipping meals. Add fiber and seasonal fruits daily.",
                'moderate': "Include brisk walks or yoga. Avoid eating out frequently.",
                'active': "Listen to your body and focus on meal balance. Include ghee and buttermilk."
            },
            '51+': {
                'sedentary': "Do simple stretches. Avoid sugary snacks. Eat home-cooked meals.",
                'moderate': "Walk daily and include protein in every meal.",
                'active': "Balance physical work with rest. Keep meals light and consistent."
            }
        },
        'female': {
            '18-30': {
                'sedentary': "Keep active with household tasks. Avoid late-night eating.",
                'moderate': "Include dal, roti, sabzi and curd in every meal. Do yoga 2-3x a week.",
                'active': "Prioritize hydration and nutrient-rich foods. Limit packaged snacks."
            },
            '31-50': {
                'sedentary': "Avoid skipping breakfast. Eat light dinners. Walk after meals.",
                'moderate': "Stay active with dancing, yoga or walking. Eat more whole grains.",
                'active': "Support energy levels with fruit, nuts, and light meals. Maintain routine."
            },
            '51+': {
                'sedentary': "Focus on digestion-friendly foods. Avoid fried food and aerated drinks.",
                'moderate': "Stretch regularly. Eat home-cooked meals with minimal oil.",
                'active': "Stay consistent with workouts. Eat seasonal produce and hydrate well."
            }
        }
    }
}

# Dummy data for blog posts (replace with a real database or content management system)
blog_posts_data = {
    'understanding-macronutrients': {
        'title': 'Understanding Your Macronutrients',
        'date': 'July 1, 2024',
        'excerpt': 'Dive deep into the world of proteins, carbs, and fats. Learn how balancing these essential macronutrients can optimize your energy, performance, and weight management goals.',
        'image': '{{ url_for("static", filename="images/macros.png") }}', # Example image path
        'keywords': 'macronutrients, proteins, carbohydrates, fats, nutrition, healthy eating'
    },
    'hydration-for-weight-loss': {
        'title': 'The Benefits of Hydration for Weight Loss',
        'date': 'June 25, 2024',
        'excerpt': 'Water is crucial for overall health, but did you know it plays a significant role in your weight loss journey? Discover how proper hydration can boost metabolism and reduce cravings.',
        'image': '{{ url_for("static", filename="images/hydration.png") }}', # Example image path
        'keywords': 'hydration, water, weight loss, metabolism, healthy habits'
    },
    'healthy-breakfast-ideas': {
        'title': 'Quick & Healthy Breakfast Ideas for Busy Mornings',
        'date': 'June 18, 2024',
        'excerpt': 'Don\'t skip the most important meal of the day! We\'ve compiled a list of nutritious and easy-to-prepare breakfast options that fit even the busiest schedules.',
        'image': '{{ url_for("static", filename="images/breakfast.png") }}', # Example image path
        'keywords': 'healthy breakfast, quick meals, breakfast ideas, healthy recipes'
    }
}


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/menu')
def menu():
    return render_template("menu.html")

@app.route('/get-plan')
def get_plan():
    return render_template("get-plan.html")

@app.route('/faq')
def faq():
    return render_template("faq.html")

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/privacy-policy')
def privacy_policy():
    return render_template('privacy.html')

@app.route('/terms-of-service')  # Must match the URL in browser
def terms_of_service():  # This name must match url_for()
    return render_template('terms.html')

@app.route('/blog')
def blog():
    # Pass all blog posts data to the blog.html template
    # In a real app, you might paginate this or fetch from a DB
    return render_template('blog.html', all_posts=blog_posts_data.values())
@app.route('/blog/<string:slug>')
def blog_post(slug):
    post = blog_posts_data.get(slug)
    if post:
        return render_template('blog_post.html', post=post)
    else:
        # Handle 404 or redirect if post not found
        return "Post not found", 404


@app.route('/result', methods=['POST'])
def result(): 
    print("Form Data:", request.form)

    global meal_plans
    goal = request.form.get('goal').lower().replace(" ", "_")
    age = int(request.form.get('age'))
    gender = request.form.get('gender').lower()
    preference = request.form.get('preference').lower()
    activity = request.form.get('activity').lower()
 

    age = get_age_range(age)

    GOALS = ['general_health', 'weight_loss', 'muscle_gain']
    PREFERENCES = ['vegetarian', 'non-vegetarian', 'jain']
    GENDERS = ['male', 'female']

    if goal not in GOALS:
        return f"Invalid goal: {goal}. Available GOALS: {GOALS}"
    if preference not in PREFERENCES:
        return f"Invalid preference: {preference}. Available PREFERENCES: {PREFERENCES}"
    if gender not in GENDERS:
        return f"Invalid gender: {gender}. Available GENDERS: {GENDERS}"

    # Debug printing
    print("GOAL:", goal)
    print("Available GOALS:", list(meal_plans.keys()))

    if goal in meal_plans:
        print("PREFERENCE:", preference)
        print("Available PREFERENCES:", list(meal_plans[goal].keys()))

        if preference in meal_plans[goal]:
            print("GENDER:", gender)
            print("Available GENDERS:", list(meal_plans[goal][preference].keys()))

            if gender in meal_plans[goal][preference]:
                print("AGE RANGE:", age)
                print("Available AGE RANGES:", list(meal_plans[goal][preference][gender].keys()))

                if age in meal_plans[goal][preference][gender]:
                    print("ACTIVITY:", activity)
                    print("Available ACTIVITY LEVELS:", list(meal_plans[goal][preference][gender][age].keys()))

    try:
        age_input = request.form.get('age')
        age = int(age_input)  # This will fail if the input is '18-30'
        age = get_age_range(age)
    except ValueError:
        # If age is already a string range like '18-30', just use it
        age = age_input
 
    try:
        level1 = meal_plans[goal]
        level2 = level1[preference]
        level3 = level2[gender]
        level4 = level3[age]
        meal_plan_result = level4[activity]
    except KeyError as e:
        print(f"KeyError occurred: {e}")
        meal_plan_result = {
            "breakfast": "No meal plan found for this combination.",
            "lunch": "Please try a different set of inputs.",
            "dinner": "Sorry!",
        }

    try:
        healthy_tip = tips[goal][gender][age][activity]
    except KeyError:
        healthy_tip = "Stay healthy, stay consistent, and trust the process!"

    return render_template(
        "result.html",
        meal_plans=meal_plan_result,
        goal=goal,
        age=age,
        gender=gender,
        preference=preference,
        activity=activity,
        healthy_tip=healthy_tip
    )

@app.route('/order', methods=['POST'])
def order():
    meal_time = request.form.get('meal_time')
    item = request.form.get('item')
    quantity = request.form.get('quantity')
    calories = request.form.get('calories')
    protein = request.form.get('protein')
    carbs = request.form.get('carbs')
    fats = request.form.get('fats')

    return render_template(
        'order_form.html',
        meal_time=meal_time,
        item=item,
        quantity=quantity,
        calories=calories,
        protein=protein,
        carbs=carbs,
        fats=fats
    )

@app.route('/confirm_order', methods=['POST'])
def confirm_order():
    # Save or print the order
    order_info = dict(request.form)

    # TODO: store in database or Google Sheet

    return render_template('success.html', order=order_info)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=10000)