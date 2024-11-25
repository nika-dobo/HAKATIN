
# Sheet1
# შექმენით manual_max() ფუნქცია. ანუ უნდა შექმნათ ისეთი ფუნქცია რომელიც იპოვის მინიმალურ რიცხვს რაიმე list'ში, max() ფუნქციის გამოყენების გარეშე.





def manual_max(numbers):
    max_num = numbers[1]

    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

numbers = [14, 454, 465, 564, 654, 34653, 23234, 23523565, 2635643, 34634, 436346454]

print(manual_max(numbers))
