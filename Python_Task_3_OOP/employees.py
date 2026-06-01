from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from typing import ClassVar, Optional


@dataclass
class Employee(ABC):
    name: str
    emp_id: str = field(init=False)
    _company: Optional["Company"] = field(default=None, init=False)

    # class-level attribute
    _last_assigned_id: ClassVar[int] = 0

    def __post_init__(self):
        Employee._last_assigned_id += 1
        self.emp_id = f"E{Employee._last_assigned_id}"

    # property for company
    @property
    def company(self):
        return self._company

    @company.setter
    def company(self, company):
        self._company = company

    @abstractmethod
    def calculate_payment(self):
        pass

    def leave_company(self):
        if self.company is None:
            print("Employee is not currently employed by any company.")
            return

        self.company.fire(self)


@dataclass
class HourlyEmployee(Employee):
    _hourly_rate: int

    def __post_init__(self):
        super().__post_init__()
        self.hourly_rate = self._hourly_rate

    @property
    def hourly_rate(self):
        return self._hourly_rate

    @hourly_rate.setter
    def hourly_rate(self, rate):
        if rate < 0:
            raise ValueError("Hourly rate cannot be negative")
        self._hourly_rate = rate

    def calculate_payment(self):
        return self.hourly_rate * 40


@dataclass
class SalariedEmployee(Employee):
    _salary: int

    def __post_init__(self):
        super().__post_init__()
        self.salary = self._salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value

    def calculate_payment(self):
        return self.salary / 4
