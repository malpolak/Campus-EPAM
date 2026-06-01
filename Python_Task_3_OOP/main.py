from company import Company, Domain
from employees import HourlyEmployee, SalariedEmployee


def print_company_state(company):
    print(company)
    for e in company.employees:
        print(
            f" - {e.name} ({e.emp_id}) | company: {e.company.name if e.company else None}"
        )
    print("-" * 50)


def main():
    tech_company = Company("Tech Corp", Domain.TECHNOLOGY)
    health_company = Company("My Health", Domain.HEALTHCARE)

    john = HourlyEmployee("John", _hourly_rate=25)
    alice = HourlyEmployee("Alice", _hourly_rate=30)

    bob = SalariedEmployee("Bob", _salary=8000)
    kate = SalariedEmployee("Kate", _salary=10000)

    tech_company.hire(john)
    tech_company.hire(alice)
    tech_company.hire(bob)

    health_company.hire(kate)

    print("\nAfter hiring:")
    print_company_state(tech_company)
    print_company_state(health_company)

    emp_ids = [e.emp_id for e in tech_company.employees]
    print("Unique emp_id check (TechCorp):", len(emp_ids) == len(set(emp_ids)))

    print("\nAttempt duplicate hire (John again):")
    tech_company.hire(john)

    print_company_state(tech_company)

    print("\nFiring Alice...")
    tech_company.fire(alice)

    print_company_state(tech_company)

    # verify removal
    print(
        "Alice still in company:",
        any(e.emp_id == alice.emp_id for e in tech_company.employees),
    )

    print("\nEmployee does not exist in this company")
    tech_company.fire(alice)

    print_company_state(tech_company)


if __name__ == "__main__":
    main()
