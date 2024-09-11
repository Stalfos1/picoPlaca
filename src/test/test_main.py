import pytest
from src.main import day_date

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