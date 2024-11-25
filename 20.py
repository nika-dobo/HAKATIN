# 20)შექმენით calculator ფუნქცია რომელსაც ექნება ყველა მათემატიკური მოქმედება მაგალითად:+,-,*,/. ფუნქციას გადაეცით 3 არგუმენტი. პირველი იქნება პირველი რიცხვი, მეორე მეორე რიცხვი და მესამე მათემატიკური ოპერაციის ოპერატორი (+,-...).



num1 =  int(input("enter first number:"))
num2 =  int(input("enter second number:"))

moqmedeba = input("enter matematikuri moqmedeba(-,+,*,/,)")


if moqmedeba == "-":
    print(num1 - num2)

elif moqmedeba == "+":
    print(num1 + num2)

elif moqmedeba == "*":
    print(num1 * num2)

elif moqmedeba == "/":
    print(num1 / num2)
    