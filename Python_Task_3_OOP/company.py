import enum
from dataclasses import dataclass, field

from employees import Employee, HourlyEmployee, SalariedEmployee


class Domain(enum.Enum):
    TECHNOLOGY = "TECHNOLOGY"
    HEALTHCARE = "HEALTHCARE"
    RETAIL = "RETAIL"


@dataclass
class Company:
    name: str
    domain: Domain
    employees: list[Employee] = field(default_factory=list)

    def hire(self, employee: Employee):
        if employee.company is not None:
            return

        if any(e.emp_id == employee.emp_id for e in self.employees):
            return

        self.employees.append(employee)
        employee.company = self

    def fire(self, employee: Employee):
        for e in self.employees:
            if e.emp_id == employee.emp_id:
                self.employees.remove(e)
                e.company = None
                return

    def raise_pay(self, employee: Employee, amount: int):
        if all(e.emp_id != employee.emp_id for e in self.employees):
            return

        if isinstance(employee, SalariedEmployee):
            employee.salary += amount

        elif isinstance(employee, HourlyEmployee):
            employee.hourly_rate += amount

    def __repr__(self):
        return f"Company({self.name}, {self.domain.name}, Employees: {len(self.employees)})"
