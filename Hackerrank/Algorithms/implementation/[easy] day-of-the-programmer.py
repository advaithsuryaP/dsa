'''
@Link: https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
@Difficulty: Easy

Problem: Marie invented a Time Machine and wants to test it by time-traveling to visit Russia on the Day of the Programmer (the 256th day of the year) 
during a year in the inclusive range from 1700 to 2700. From 1700 to 1917, the Julian calendar was used. Since 1919, the Gregorian calendar is used.
The transition from the Julian to Gregorian calendar happened in 1918, when the next day after January 31st was February 14th. This means that in 1918, 
February 14th was the 32nd day of the year in Russia.

In both calendars, February is the only month with a variable amount of days; it has 29 days in a leap year, and 28 days in a common year. 
In the Julian calendar, leap years are divisible by 4; in the Gregorian calendar, leap years are either of the following:
- Divisible by 400.
- Divisible by 4 and not divisible by 100.
Given a year, determine the date of the 256th day of that year according to the official Russian calendar during that year. 
Then print it in the format dd.mm.yyyy, where dd is the two-digit day, mm is the two-digit month, and yyyy is the year.
For example, the given 2017. Your function should return 13.09.2017.

Example:
Input: 2017
Output: 13.09.2017
'''

def dayOfProgrammer(year):
    if year == 1918:
        return f"26.09.{year}"
    
    if(year <= 1917):
        if year % 4 == 0:
            return f"12.09.{year}" 
        else:
            return f"13.09.{year}"
            
    if year % 400 == 0 or (year % 4 == 0 and year% 100 != 0):
        return f"12.09.{year}"
    return f"13.09.{year}"

print(dayOfProgrammer(2017)) # 13.09.2017
print(dayOfProgrammer(2016)) # 12.09.2016
print(dayOfProgrammer(2018)) # 13.09.2018   
print(dayOfProgrammer(1800)) # 12.09.1800
print(dayOfProgrammer(1918)) # 26.09.1918

'''
Solution

# 📌 Day of the Programmer

## Problem essence

* Find the **256th day of the year** in Russia for a given year `1700–2700`.
* Output format: **`dd.mm.yyyy`**
* The trick is **calendar rules**, not date math.

---

## 🗓️ Calendar systems involved

### 1️⃣ **Julian calendar (1700–1917)**

* Leap year if:

  ```
  year % 4 == 0
  ```
* February:

  * 29 days in leap years
  * 28 days otherwise

### 2️⃣ **Transition year (1918)**

* Russia skipped **13 days in February**
* Feb 14 was the **32nd day of the year**
* Result:

  ```
  26.09.1918
  ```
* **Hard-coded special case**

### 3️⃣ **Gregorian calendar (1919–2700)**

* Leap year if:

  ```
  year % 400 == 0
  OR
  year % 4 == 0 and year % 100 != 0
  ```

---

## 📍 Why September always?

Days from **Jan → Aug**:

* Non-leap year: **243 days**
* Leap year: **244 days**

So:

* `256 − 243 = 13` → **13 September**
* `256 − 244 = 12` → **12 September**

✔️ Holds for **both Julian and Gregorian calendars**

---

## 🧠 Final logic

| Case                           | Output       |
| ------------------------------ | ------------ |
| `year == 1918`                 | `26.09.1918` |
| Leap year (Julian / Gregorian) | `12.09.yyyy` |
| Non-leap year                  | `13.09.yyyy` |

---

## 🧩 Final Python solution (correct & clean)

```python
def dayOfProgrammer(year):
    if year == 1918:
        return f"26.09.{year}"

    if year <= 1917:  # Julian calendar
        return f"12.09.{year}" if year % 4 == 0 else f"13.09.{year}"

    # Gregorian calendar
    leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
    return f"12.09.{year}" if leap else f"13.09.{year}"
```

---

## ⚠️ Gotcha you just hit (worth remembering)

* Python f-strings use:

  ```
  f"{variable}"
  ```
* NOT:

  ```
  ${variable}   # ← JavaScript / TypeScript only
  ```

---

## 🎯 Why this is an “Easy” problem

* No loops
* No arrays
* No date libraries
* Just **calendar classification + constant answers**

If you can spot the **1918 exception**, you win.

---

If you want, next we can:

* convert this to **TypeScript**
* add **unit tests**
* or jump straight into the **next HackerRank / NeetCode problem**

Just say the word 🚀

'''