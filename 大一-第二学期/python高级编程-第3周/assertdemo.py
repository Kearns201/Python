def KelvinToFahrenheit(Temperature):
    temp = 0
    try:
        assert (Temperature >= 0), 'Colder than the absolute zero！'
        temp = ((Temperature - 273) * 1.8) + 32 / 0
    except (AssertionError, ZeroDivisionError) as arg:
        print("出现了问题", arg)
    else:
        print("一切正常")
    return temp


print(KelvinToFahrenheit(273))
print(KelvinToFahrenheit(-5))
