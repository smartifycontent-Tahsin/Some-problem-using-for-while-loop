#level 1
for n in range(1,11):
    print(n)

#level 2
i=10
while i>0:
    print(i)
    i=i-1

#level 3
total = 0
for n in range(5):
    num= int(input("Enter a number: "))
    total = total + num
print(f"The total is {total}")

#level 4
i=2
while i<22:
    print(i)
    i=i+2
    
#level 5
total = 0
even_count = 0
odd_count = 0

for n in range(10):
    num = int(input("Enter a number: "))

    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    total += num
print(f"Even number: {even_count}\nOdd number: {odd_count}\nTotal sum: {total}")