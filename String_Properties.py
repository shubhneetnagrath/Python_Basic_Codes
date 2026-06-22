a = "Shubhneet"
b = "Nagarth"
#Concatenation of Strings using (+)
print(a+b)
#Output>> ShubhneeetNagrath

#Passing multiple arguments to a function (or argument separation) Using (,)
print(a,b)
#Output>> Shubhneet Nagrath
# Note..>> Using commma does not concatenate the string so arguments different data types can be print together

c = a + b
#this again string concatenation by redefining it into a new varaiable(c)

c = a,b
#this is not argument sepration by comma anymore, instead now a new "tuple" is created

age = 36
#This will produce an error:
txt = "My name is John, I am " + age
print(txt)
#In python two different data types cannot be concatenated usinf (+)

#Instead F- String is used 
age = 36
txt = f"My name is John, I am {age}"
print(txt)
#{age} is a placeholder

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

#{price} is a placeholder
#{price:.2f} is a modifier i.e. (.2f) means till 2 decimal places

txt = f"The price is {20 * 59} dollars"
print(txt)

# Placeholders can also contain mathematical operations