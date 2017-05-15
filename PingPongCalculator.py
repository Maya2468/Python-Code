def convert_in2cm(inches):
    return inches * 2.54

def convert_Ib2kg(pounds):
    return pounds / 2.2

height_in = int(input("Enter your height in inches: "))
weight_Ib = int(input("Enter your weight in pounds: "))

height_cm = convert_in2cm(height_in)
weight_kg = convert_Ib2kg(weight_Ib)

ping_pong_tall = round(height_cm / 4)
ping_pong_heavy = round(weight_kg * 1000 / 2.7)

feet = height_in // 12
inch = height_in % 12

print("At", feet, "feet", inch, "inches tall,and", weight_Ib,
      "pounds",)
print("You measure", ping_ball_tall, "Ping-Pong balls tall, and ")
print("you weigh the same as", ping_pong_heavy, "Ping-Pong balls!")
