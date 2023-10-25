lesson_number = int(input("Введите номер урока (от 1 до 10): "))

total_minutes = lesson_number * 45
short = lesson_number // 2
long = lesson_number - short - 1

hours = total_minutes + short * 5 + long * 15
end_hour = 9 + hours // 60
end_minute = hours % 60

print(f"Урок номер {lesson_number} заканчивается в {end_hour}:{end_minute:02}")


