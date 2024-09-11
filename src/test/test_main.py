import pytest
import datetime
from src.main import day_date, pico_placa_detector, is_vehicle_allowed

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
     "date,day",
    [
        ('32/1/0900','Thursday'),
        ('22/6/-0020','Thursday')
    ]
)    
def test_negative_day_date(date,day):
    assert not day_date(date)==day
    


@pytest.mark.parametrize(
     "plate,date,time,result",
    [
        ("pbx1023", "10/09/2024", datetime.time(8, 30), False),
        ("abc1234", "12/12/2023", datetime.time(15, 45),True),
        ("xyz5678", "01/01/2025", datetime.time(23, 59),True),
        ("pqr9876", "05/07/2024", datetime.time(10, 15),True),
        ("uvw7654", "09/03/2024", datetime.time(0, 0),True),
        ("def3210", "22/10/2024", datetime.time(17, 30),True)
    ]
)   
def test_pico_placa_detector(plate,date,time,result):
    assert pico_placa_detector(plate,date,time)==result