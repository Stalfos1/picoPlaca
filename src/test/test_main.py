import pytest
import datetime
from src.main import day_date, pico_placa_detector, is_vehicle_allowed, plate_verificator

@pytest.mark.parametrize(
    "date,day",
    [
        ('29/2/2008','Friday'),
        ('11/1/2024','Thursday'),
        ('1/1/0900','Friday'),
        ('23/9/0020','Wednesday'),
        ('22/5/0001','Tuesday'),
        ('18/4/2016','Monday')
    ]
)
def test_day_date(date,day):
    assert day_date(date)==day
    
@pytest.mark.parametrize(
    "date,expected_exception",
    [
        ('32/1/0900', ValueError),
        ('22/6/-0020', ValueError),
        ('5/3/0000', ValueError),
        ('13/15/2020', ValueError)
    ]
)
def test_negative_day_date(date, expected_exception):
    with pytest.raises(expected_exception):
        day_date(date)
    


@pytest.mark.parametrize(
     "plate,date,time,result",
    [
        ("pbx1023", "10/09/2024", datetime.time(8, 30), False),
        ("abc1234", "12/12/2023", datetime.time(16, 45),False),
        ("xyz5678", "01/01/2025", datetime.time(23, 59),True),
        ("pqr9876", "05/07/2024", datetime.time(10, 15),True),
        ("uvw7654", "09/03/2024", datetime.time(0, 0),True),
        ("def3210", "18/10/2024", datetime.time(17, 30),False)
    ]
)   
def test_pico_placa_detector(plate,date,time,result):
    assert pico_placa_detector(plate,date,time)==result
    
    
@pytest.mark.parametrize(
    "plate, result",
    [
        ("ABC123", True),
        ("DEF7890", True), 
        ("123ABC", False), 
        ("ABCD", False),  
        ("ABCDEFGHI", False), 
        ("ABC12345", False),  
        ("123ABCX", False), 
        ("@ABC", False),
        ("2154ABC", False)  
    ]
)
def test_plate_verificator(plate, result):
    assert plate_verificator(plate) == result