# **Pico y Placa Verifier**
                                                                   
## **Project Overview**

The Pico y Placa Verifier is a Python application designed to determine if a vehicle is allowed to circulate on a specific day and time based on the Pico y Placa restrictions of the Quito city. The system verifies the license plate format, calculates the day of the week, and checks for any restrictions based on the last digit of the license plate and the specified time.

## Git Versions
This repository utilizes two branches to manage code development and releases:

- main: Dedicated to stable releases of the code.
- develop: Dedicated to ongoing development and testing activities related to the exercise.

## **Key Features:**


- License Plate Validation: Ensures that the license plate adheres to the correct format, consisting of 6 or 7 characters with the first 3 being letters and the remaining characters being numbers.

- Day of the Week Calculation: Accurately determines the day of the week from the provided date.

- Pico y Placa Rule Enforcement: Implements the Pico y Placa restrictions, prohibiting vehicles with specific last digits from circulating on corresponding days during restricted hours.


## **Pico y Placa Restrictions**

The Pico y Placa system restricts vehicle circulation during the following peak hours:

7:00 AM to 9:30 AM and 4:00 PM to 7:30 PM

Vehicles with license plates ending in the following digits are restricted on their corresponding days:
```
Monday: 1, 2

Tuesday: 3, 4

Wednesday: 5, 6

Thursday: 7, 8

Friday: 9, 0
```
> [!IMPORTANT]
> On Holidays all vehicles are allowed, regardless of their plate number

[Holidays on Quito, Ecuador:](https://www.jezl-auditores.com/index.php/tributario/126-feriados-ecuador-2024)
```
    '01/01'   New Year's Day
    '12/02'   Carnival
    '13/02'   Carnival
    '29/03'   Good Friday
    '03/05'   Labor Day
    '24/05'   Pichincha Battle
    '28/07'   National Holiday
    '29/07'   National Holiday
    '09/08'   First Cry of Independece
    '11/10'   Independence of Guayaquil
    '01/11'   All Souls Day
    '04/11'   Independence of Cuenca
    '06/12'   Foundation of Quito
    '24/12'   Christmas Eve
    '25/12'   Christmas

```
## **Requirements**

Python 3.x

pytest for running tests

## **Installation:**

To install the pytest library, use the following command in your terminal or command prompt:

    pip install pytest

### **Running Tests:**

Once pytest is installed, you can run your test cases using the following command:

    pytest -v


## **Usage**

To use the Pico y Placa Verifier, provide the following information:

License Plate: The vehicle's license plate number.

Date: The date in the format "DD/MM/YYYY".

Time: The time in the format "HH:MM" (24-hour format).


The verifier will then determine if the vehicle is allowed to circulate based on the Pico y Placa rules.
