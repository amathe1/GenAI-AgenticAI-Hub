"""
================================================================================
                    EMPLOYEE MANAGEMENT SYSTEM
================================================================================

DETAILED PROBLEM STATEMENT:
---------------------------
Create a comprehensive Employee Management System for a software company that
manages different types of employees (Full-time, Part-time, Contractors) with
varying salary structures, benefits, and work arrangements. The system must
demonstrate ALL Object-Oriented Programming (OOP) concepts.

BUSINESS CONTEXT:
-----------------
A software company has multiple employee types:

1. FULL-TIME EMPLOYEES:
   - Fixed monthly salary
   - Health insurance
   - Paid time off (PTO)
   - Performance bonuses
   - Retirement benefits

2. PART-TIME EMPLOYEES:
   - Hourly wage
   - Limited benefits
   - No PTO
   - Flexible hours

3. CONTRACTORS:
   - Project-based payment
   - No benefits
   - Fixed contract duration
   - Specialized skills

4. MANAGERS (Special Full-time):
   - Team management bonus
   - Additional responsibilities
   - Leadership allowance

Each employee type requires different:
- Salary calculation methods
- Benefit packages
- Work hour tracking
- Performance evaluation

REQUIREMENTS - OOP CONCEPTS TO DEMONSTRATE:
-------------------------------------------

1. CLASS (Blueprint):
   - Define structure for Employee
   - Attributes: name, id, department, salary
   - Methods: calculate_salary(), get_details()
   - Constructor (__init__)

2. OBJECT (Instance):
   - Create individual employees
   - Each object has unique data
   - Multiple objects from same class

3. ENCAPSULATION:
   - Private attributes (__)
   - Protected attributes (_)
   - Public attributes
   - Getter and Setter methods
   - Data hiding and access control

4. INHERITANCE:
   - Base class (Employee)
   - Derived classes (FullTimeEmployee, PartTimeEmployee, Contractor)
   - Parent-child relationship
   - Code reusability
   - Method overriding
   - super() function

5. ABSTRACTION:
   - Abstract base class (ABC)
   - Abstract methods (@abstractmethod)
   - Force implementation in child classes
   - Hide complex implementation details

6. POLYMORPHISM:
   - Same method name, different implementations
   - Method overriding
   - Dynamic method resolution
   - Duck typing

7. SPECIAL METHODS:
   - __init__ (constructor)
   - __str__ (string representation)
   - __repr__ (official representation)
   - __eq__ (equality comparison)

LEARNING OBJECTIVES:
-------------------
By the end of this program, you will understand:
• How to create classes and objects
• Difference between class and instance attributes
• How inheritance promotes code reuse
• When and how to use abstraction
• How polymorphism enables flexible code
• Encapsulation for data protection
• Real-world OOP design patterns

================================================================================
"""

from abc import ABC, abstractmethod
from datetime import datetime, date

# ============================================================================
# SECTION 1: BASIC CLASS AND OBJECTS
# ============================================================================

def show_section_header(section_number, title):
    """Display formatted section header."""
    print("\n" + "="*80)
    print(f"SECTION {section_number}: {title}")
    print("="*80)

class BasicEmployee:
    """
    Basic Employee class demonstrating CLASS and OBJECT concepts.
    
    CLASS: Blueprint/template for creating objects
    OBJECT: Instance of a class with actual data
    
    Components:
    - Attributes: Variables that hold data (name, employee_id, salary)
    - Methods: Functions that define behavior (get_info, calculate_bonus)
    - Constructor: Special method __init__ to initialize object
    """
    
    # Class attribute (shared by all objects)
    company_name = "TechCorp Solutions"
    employee_count = 0
    
    def __init__(self, name, employee_id, salary):
        """
        Constructor: Initialize object with data.
        
        __init__ is called automatically when object is created.
        'self' refers to the current object instance.
        """
        # Instance attributes (unique to each object)
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
        
        # Increment class variable
        BasicEmployee.employee_count += 1
    
    def get_info(self):
        """Instance method: Returns employee information."""
        return f"Employee: {self.name} (ID: {self.employee_id}), Salary: ${self.salary:,.2f}"
    
    def calculate_bonus(self, percentage):
        """Instance method: Calculate bonus based on salary."""
        bonus = self.salary * (percentage / 100)
        return bonus
    
    @classmethod
    def get_employee_count(cls):
        """Class method: Access class-level data."""
        return cls.employee_count
    
    @staticmethod
    def is_valid_employee_id(emp_id):
        """Static method: Utility function (doesn't need self or cls)."""
        return emp_id.startswith("EMP") and len(emp_id) == 7

def demonstrate_basic_class_and_objects():
    """Demonstrate basic class and object creation."""
    
    show_section_header(1, "BASIC CLASS AND OBJECTS")
    print("\nProblem: Create employee records with salary information")
    print("Concept: Class = Blueprint, Object = Instance with actual data")
    print("-"*80)
    
    print("\n📌 CLASS DEFINITION:")
    print("-"*80)
    print("""
    class BasicEmployee:
        company_name = "TechCorp Solutions"  # Class attribute
        
        def __init__(self, name, employee_id, salary):
            self.name = name              # Instance attribute
            self.employee_id = employee_id
            self.salary = salary
        
        def get_info(self):               # Instance method
            return f"Employee: {self.name}..."
    """)
    
    print("\n📌 CREATING OBJECTS (Instances):")
    print("-"*80)
    
    # Create objects (instances of BasicEmployee class)
    emp1 = BasicEmployee("Alice Johnson", "EMP0001", 75000)
    emp2 = BasicEmployee("Bob Smith", "EMP0002", 65000)
    emp3 = BasicEmployee("Charlie Brown", "EMP0003", 80000)
    
    print(f"✓ Created object emp1: {emp1.get_info()}")
    print(f"✓ Created object emp2: {emp2.get_info()}")
    print(f"✓ Created object emp3: {emp3.get_info()}")
    
    # Class attribute (shared by all)
    print(f"\n📌 CLASS ATTRIBUTES (shared by all objects):")
    print("-"*80)
    print(f"Company name: {BasicEmployee.company_name}")
    print(f"Total employees: {BasicEmployee.get_employee_count()}")
    
    # Instance attributes (unique to each object)
    print(f"\n📌 INSTANCE ATTRIBUTES (unique to each object):")
    print("-"*80)
    print(f"emp1.name = {emp1.name}")
    print(f"emp2.name = {emp2.name}")
    print(f"emp3.name = {emp3.name}")
    print(f"emp1.salary = ${emp1.salary:,.2f}")
    print(f"emp2.salary = ${emp2.salary:,.2f}")
    
    # Call instance methods
    print(f"\n📌 CALLING INSTANCE METHODS:")
    print("-"*80)
    bonus1 = emp1.calculate_bonus(10)
    bonus2 = emp2.calculate_bonus(15)
    print(f"{emp1.name}'s bonus (10%): ${bonus1:,.2f}")
    print(f"{emp2.name}'s bonus (15%): ${bonus2:,.2f}")
    
    # Static method
    print(f"\n📌 STATIC METHOD (utility function):")
    print("-"*80)
    test_ids = ["EMP0001", "EMP123", "INVALID"]
    for emp_id in test_ids:
        valid = BasicEmployee.is_valid_employee_id(emp_id)
        status = "✓ Valid" if valid else "✗ Invalid"
        print(f"{emp_id}: {status}")
    
    print("\n✓ Key Points:")
    print("  • Class = Blueprint/Template")
    print("  • Object = Instance with actual data")
    print("  • Each object has unique instance attributes")
    print("  • All objects share class attributes")

# ============================================================================
# SECTION 2: ENCAPSULATION (Data Hiding)
# ============================================================================

class EncapsulatedEmployee:
    """
    Demonstrate ENCAPSULATION concept.
    
    ENCAPSULATION: Bundling data and methods, controlling access
    
    Access Modifiers:
    - Public: accessible anywhere (name, get_info)
    - Protected: single underscore _ (internal use, accessible)
    - Private: double underscore __ (name mangling, not directly accessible)
    """
    
    def __init__(self, name, employee_id, base_salary):
        # Public attribute (accessible anywhere)
        self.name = name
        
        # Protected attribute (convention: internal use)
        self._department = "Engineering"
        
        # Private attribute (name mangling - cannot access directly)
        self.__salary = base_salary
        self.__bank_account = "****-****-1234"
    
    # Getter method for private attribute
    def get_salary(self):
        """Public method to access private salary."""
        return self.__salary
    
    # Setter method for private attribute (with validation)
    def set_salary(self, new_salary):
        """Public method to modify private salary with validation."""
        if new_salary < 0:
            raise ValueError("Salary cannot be negative")
        if new_salary > 500000:
            raise ValueError("Salary exceeds maximum limit")
        
        print(f"  Validating salary change: ${self.__salary:,.2f} → ${new_salary:,.2f}")
        self.__salary = new_salary
        print(f"  ✓ Salary updated successfully")
    
    # Getter for private bank account
    def get_bank_account(self):
        """Return masked bank account."""
        return self.__bank_account
    
    # Property decorator (Pythonic way)
    @property
    def salary(self):
        """Property getter - access like attribute."""
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        """Property setter - with validation."""
        if value < 30000:
            raise ValueError("Salary below minimum wage")
        self.__salary = value
    
    def get_full_info(self):
        """Public method using private data."""
        return f"{self.name} - ${self.__salary:,.2f} - {self._department}"

def demonstrate_encapsulation():
    """Demonstrate encapsulation and access control."""
    
    show_section_header(2, "ENCAPSULATION (Data Hiding & Access Control)")
    print("\nProblem: Protect sensitive employee data from unauthorized access")
    print("Concept: Control access to data using public/protected/private")
    print("-"*80)
    
    print("\n📌 ACCESS MODIFIERS:")
    print("-"*80)
    print("""
    class EncapsulatedEmployee:
        def __init__(self, name, salary):
            self.name = name              # Public
            self._department = "Eng"      # Protected (convention)
            self.__salary = salary        # Private (name mangling)
    """)
    
    emp = EncapsulatedEmployee("David Lee", "EMP0004", 70000)
    
    print("\n📌 PUBLIC ACCESS (accessible anywhere):")
    print("-"*80)
    print(f"emp.name = {emp.name}")
    emp.name = "David K. Lee"  # Can modify directly
    print(f"Modified name: {emp.name}")
    
    print("\n📌 PROTECTED ACCESS (_attribute):")
    print("-"*80)
    print(f"emp._department = {emp._department}")
    print("Note: Can access but indicates 'internal use'")
    
    print("\n📌 PRIVATE ACCESS (__attribute):")
    print("-"*80)
    print("Attempting direct access: emp.__salary")
    try:
        print(emp.__salary)
    except AttributeError as e:
        print(f"✗ Error: Cannot access private attribute directly")
    
    print("\n✓ Correct way - Use getter method:")
    print(f"emp.get_salary() = ${emp.get_salary():,.2f}")
    
    print("\n📌 SETTER METHOD WITH VALIDATION:")
    print("-"*80)
    
    # Valid salary update
    print("Setting valid salary ($85,000):")
    emp.set_salary(85000)
    print(f"New salary: ${emp.get_salary():,.2f}")
    
    # Invalid salary update
    print("\nAttempting invalid salary (-5000):")
    try:
        emp.set_salary(-5000)
    except ValueError as e:
        print(f"✗ Validation Error: {e}")
    
    print("\n📌 PROPERTY DECORATOR (Pythonic way):")
    print("-"*80)
    print(f"Access like attribute: emp.salary = ${emp.salary:,.2f}")
    
    print("Setting with validation: emp.salary = 90000")
    emp.salary = 90000
    print(f"New value: ${emp.salary:,.2f}")
    
    print("\n✓ Benefits of Encapsulation:")
    print("  • Data validation before modification")
    print("  • Hide sensitive information")
    print("  • Control how data is accessed/modified")
    print("  • Maintain data integrity")

# ============================================================================
# SECTION 3: INHERITANCE (Code Reusability)
# ============================================================================

class Employee:
    """
    BASE CLASS (Parent/Super class) for all employees.
    
    INHERITANCE: Child class inherits attributes and methods from parent
    
    Benefits:
    - Code reusability
    - Hierarchical relationships
    - Extend functionality
    - Override methods
    """
    
    def __init__(self, name, employee_id, department):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.joining_date = datetime.now()
    
    def get_info(self):
        """Base method - can be overridden by child classes."""
        return f"Employee: {self.name} (ID: {self.employee_id})"
    
    def calculate_salary(self):
        """Abstract-like method - should be overridden."""
        raise NotImplementedError("Subclass must implement calculate_salary()")
    
    def get_work_email(self):
        """Common method inherited by all."""
        # firstname.lastname@company.com
        first = self.name.split()[0].lower()
        last = self.name.split()[-1].lower()
        return f"{first}.{last}@techcorp.com"

class FullTimeEmployee(Employee):
    """
    DERIVED CLASS (Child/Sub class) - inherits from Employee.
    
    Adds full-time specific attributes and methods.
    """
    
    def __init__(self, name, employee_id, department, monthly_salary):
        # Call parent constructor
        super().__init__(name, employee_id, department)
        
        # Child-specific attributes
        self.monthly_salary = monthly_salary
        self.pto_days = 20
        self.has_health_insurance = True
    
    def calculate_salary(self):
        """Override parent method - full-time specific implementation."""
        return self.monthly_salary
    
    def get_info(self):
        """Override parent method with more details."""
        base_info = super().get_info()  # Call parent method
        return f"{base_info} - Full-time - ${self.monthly_salary:,.2f}/month"
    
    def take_pto(self, days):
        """Child-specific method."""
        if days <= self.pto_days:
            self.pto_days -= days
            return f"✓ PTO approved: {days} days. Remaining: {self.pto_days}"
        return f"✗ Insufficient PTO days. Available: {self.pto_days}"

class PartTimeEmployee(Employee):
    """Derived class for part-time employees."""
    
    def __init__(self, name, employee_id, department, hourly_rate):
        super().__init__(name, employee_id, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = 0
    
    def calculate_salary(self):
        """Override - calculate based on hours worked."""
        return self.hourly_rate * self.hours_worked
    
    def get_info(self):
        """Override with part-time specific info."""
        base_info = super().get_info()
        return f"{base_info} - Part-time - ${self.hourly_rate:.2f}/hour"
    
    def log_hours(self, hours):
        """Child-specific method."""
        self.hours_worked += hours
        return f"✓ Logged {hours} hours. Total: {self.hours_worked}"

class Contractor(Employee):
    """Derived class for contractors."""
    
    def __init__(self, name, employee_id, department, project_fee, duration_months):
        super().__init__(name, employee_id, department)
        self.project_fee = project_fee
        self.duration_months = duration_months
    
    def calculate_salary(self):
        """Override - monthly project fee."""
        return self.project_fee / self.duration_months
    
    def get_info(self):
        """Override with contractor specific info."""
        base_info = super().get_info()
        return f"{base_info} - Contractor - ${self.project_fee:,.2f}/{self.duration_months}mo"

def demonstrate_inheritance():
    """Demonstrate inheritance and code reusability."""
    
    show_section_header(3, "INHERITANCE (Code Reusability)")
    print("\nProblem: Create different employee types without duplicating code")
    print("Concept: Child classes inherit from parent, add specific features")
    print("-"*80)
    
    print("\n📌 INHERITANCE HIERARCHY:")
    print("-"*80)
    print("""
                        Employee (Base Class)
                              |
            +-----------------+-----------------+
            |                 |                 |
      FullTimeEmployee   PartTimeEmployee   Contractor
       (Derived)          (Derived)         (Derived)
    """)
    
    print("\n📌 CREATING DIFFERENT EMPLOYEE TYPES:")
    print("-"*80)
    
    # Create different types of employees
    ft_emp = FullTimeEmployee("Emma Wilson", "EMP0005", "Engineering", 8000)
    pt_emp = PartTimeEmployee("Frank Miller", "EMP0006", "Support", 35)
    contractor = Contractor("Grace Lee", "CON0001", "Consulting", 120000, 12)
    
    print(f"✓ Full-time: {ft_emp.get_info()}")
    print(f"✓ Part-time: {pt_emp.get_info()}")
    print(f"✓ Contractor: {contractor.get_info()}")
    
    print("\n📌 INHERITED METHODS (from parent Employee):")
    print("-"*80)
    print(f"Full-time email: {ft_emp.get_work_email()}")
    print(f"Part-time email: {pt_emp.get_work_email()}")
    print(f"Contractor email: {contractor.get_work_email()}")
    
    print("\n📌 OVERRIDDEN METHODS (different implementation per type):")
    print("-"*80)
    print(f"Full-time salary: ${ft_emp.calculate_salary():,.2f}")
    
    pt_emp.log_hours(40)
    print(f"Part-time salary: ${pt_emp.calculate_salary():,.2f} (40 hours)")
    
    print(f"Contractor monthly: ${contractor.calculate_salary():,.2f}")
    
    print("\n📌 CHILD-SPECIFIC METHODS:")
    print("-"*80)
    print(ft_emp.take_pto(5))
    print(pt_emp.log_hours(20))
    
    print("\n📌 USING super() to call parent methods:")
    print("-"*80)
    print("""
    class FullTimeEmployee(Employee):
        def get_info(self):
            base_info = super().get_info()  # Call parent method
            return f"{base_info} - Full-time..."
    """)
    
    print("\n✓ Benefits of Inheritance:")
    print("  • Reuse common code from parent")
    print("  • Add specific features in child")
    print("  • Override methods for custom behavior")
    print("  • Maintain hierarchical relationships")

# ============================================================================
# SECTION 4: ABSTRACTION (Hide Implementation Details)
# ============================================================================

class AbstractEmployee(ABC):
    """
    ABSTRACT BASE CLASS using ABC (Abstract Base Class).
    
    ABSTRACTION: Hide complex implementation, show only essential features
    
    - Cannot create objects of abstract class directly
    - Forces child classes to implement abstract methods
    - Ensures consistent interface across all employee types
    """
    
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    @abstractmethod
    def calculate_salary(self):
        """Abstract method - MUST be implemented by child classes."""
        pass
    
    @abstractmethod
    def calculate_benefits(self):
        """Abstract method - MUST be implemented by child classes."""
        pass
    
    # Concrete method (has implementation)
    def display_info(self):
        """Non-abstract method - inherited as-is."""
        print(f"Employee: {self.name} (ID: {self.employee_id})")

class AbstractFullTime(AbstractEmployee):
    """Concrete class implementing abstract methods."""
    
    def __init__(self, name, employee_id, base_salary):
        super().__init__(name, employee_id)
        self.base_salary = base_salary
    
    def calculate_salary(self):
        """Implementation of abstract method."""
        return self.base_salary + self.calculate_benefits()
    
    def calculate_benefits(self):
        """Implementation of abstract method."""
        health_insurance = 500
        retirement = self.base_salary * 0.05
        return health_insurance + retirement

class AbstractPartTime(AbstractEmployee):
    """Concrete class with different implementation."""
    
    def __init__(self, name, employee_id, hourly_rate, hours):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours = hours
    
    def calculate_salary(self):
        """Different implementation of same method."""
        return self.hourly_rate * self.hours
    
    def calculate_benefits(self):
        """Different implementation - limited benefits."""
        return 0  # Part-time gets no benefits

def demonstrate_abstraction():
    """Demonstrate abstraction using ABC."""
    
    show_section_header(4, "ABSTRACTION (Hide Implementation Details)")
    print("\nProblem: Ensure all employee types implement required methods")
    print("Concept: Abstract class forces child classes to implement methods")
    print("-"*80)
    
    print("\n📌 ABSTRACT CLASS DEFINITION:")
    print("-"*80)
    print("""
    from abc import ABC, abstractmethod
    
    class AbstractEmployee(ABC):
        @abstractmethod
        def calculate_salary(self):
            pass  # Must be implemented by child
        
        @abstractmethod
        def calculate_benefits(self):
            pass  # Must be implemented by child
    """)
    
    print("\n📌 CANNOT CREATE OBJECT OF ABSTRACT CLASS:")
    print("-"*80)
    print("Attempting: emp = AbstractEmployee('John', 'EMP001')")
    try:
        emp = AbstractEmployee("John", "EMP001")
    except TypeError as e:
        print(f"✗ Error: {e}")
        print("  Cannot instantiate abstract class!")
    
    print("\n📌 CONCRETE CLASSES (implementing abstract methods):")
    print("-"*80)
    
    ft = AbstractFullTime("Helen Smith", "EMP0007", 7000)
    pt = AbstractPartTime("Ian Brown", "EMP0008", 30, 80)
    
    print(f"✓ Created full-time employee: {ft.name}")
    print(f"✓ Created part-time employee: {pt.name}")
    
    print("\n📌 CALLING ABSTRACT METHODS (implemented in child):")
    print("-"*80)
    
    print(f"\nFull-time ({ft.name}):")
    ft.display_info()
    print(f"  Base Salary: ${ft.base_salary:,.2f}")
    print(f"  Benefits: ${ft.calculate_benefits():,.2f}")
    print(f"  Total Salary: ${ft.calculate_salary():,.2f}")
    
    print(f"\nPart-time ({pt.name}):")
    pt.display_info()
    print(f"  Hourly Rate: ${pt.hourly_rate:.2f}")
    print(f"  Hours: {pt.hours}")
    print(f"  Benefits: ${pt.calculate_benefits():,.2f}")
    print(f"  Total Salary: ${pt.calculate_salary():,.2f}")
    
    print("\n✓ Benefits of Abstraction:")
    print("  • Forces consistent interface")
    print("  • Prevents incomplete implementations")
    print("  • Hides complex details")
    print("  • Ensures all child classes have required methods")

# ============================================================================
# SECTION 5: POLYMORPHISM (Many Forms)
# ============================================================================

def demonstrate_polymorphism():
    """
    Demonstrate POLYMORPHISM.
    
    POLYMORPHISM: Same interface, different implementations
    
    Types:
    1. Method Overriding: Same method name in parent and child
    2. Duck Typing: "If it walks like a duck and quacks like a duck..."
    """
    
    show_section_header(5, "POLYMORPHISM (Many Forms)")
    print("\nProblem: Process different employee types uniformly")
    print("Concept: Same method name, different behaviors based on object type")
    print("-"*80)
    
    print("\n📌 POLYMORPHISM DEFINITION:")
    print("-"*80)
    print("""
    Same method name 'calculate_salary()' in different classes:
    - FullTimeEmployee.calculate_salary() → monthly salary
    - PartTimeEmployee.calculate_salary() → hourly * hours
    - Contractor.calculate_salary() → project fee / months
    
    Same interface, different implementation!
    """)
    
    # Create different employee types
    employees = [
        FullTimeEmployee("Julia Roberts", "EMP0009", "Marketing", 9000),
        PartTimeEmployee("Kevin Brown", "EMP0010", "Support", 40),
        Contractor("Laura White", "CON0002", "Design", 90000, 6),
        FullTimeEmployee("Mike Johnson", "EMP0011", "Sales", 7500),
    ]
    
    # Set hours for part-time
    employees[1].hours_worked = 100
    
    print("\n📌 POLYMORPHIC BEHAVIOR (same method, different results):")
    print("-"*80)
    
    total_payroll = 0
    
    for emp in employees:
        # Same method call, different behavior based on object type
        salary = emp.calculate_salary()
        total_payroll += salary
        
        print(f"\n{emp.get_info()}")
        print(f"  Salary: ${salary:,.2f}")
        print(f"  Email: {emp.get_work_email()}")
    
    print(f"\n{'='*80}")
    print(f"Total Monthly Payroll: ${total_payroll:,.2f}")
    print(f"{'='*80}")
    
    print("\n📌 PROCESS EMPLOYEES UNIFORMLY (polymorphism in action):")
    print("-"*80)
    
    def process_payroll(employee_list):
        """
        This function works with ANY employee type!
        Demonstrates polymorphism - doesn't need to know specific type.
        """
        print("\nProcessing payroll for all employees...")
        for emp in employee_list:
            print(f"  Paying {emp.name}: ${emp.calculate_salary():,.2f}")
    
    process_payroll(employees)
    
    print("\n📌 DUCK TYPING (Pythonic polymorphism):")
    print("-"*80)
    print("""
    "If it walks like a duck and quacks like a duck, it's a duck"
    
    Python doesn't check type - just checks if method exists!
    Any object with calculate_salary() method will work.
    """)
    
    def print_salary(emp):
        """Works with any object that has calculate_salary method."""
        try:
            salary = emp.calculate_salary()
            print(f"{emp.name}: ${salary:,.2f}")
        except AttributeError:
            print(f"Object doesn't have calculate_salary method")
    
    print("\nCalling with different types:")
    for emp in employees[:2]:
        print_salary(emp)
    
    print("\n✓ Benefits of Polymorphism:")
    print("  • Write flexible, reusable code")
    print("  • Process different types uniformly")
    print("  • Easy to add new types without changing existing code")
    print("  • Dynamic method resolution at runtime")

# ============================================================================
# SECTION 6: SPECIAL METHODS (Magic Methods)
# ============================================================================

class SmartEmployee:
    """Demonstrate special/magic methods."""
    
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def __str__(self):
        """String representation for print()."""
        return f"{self.name} (ID: {self.employee_id}) - ${self.salary:,.2f}"
    
    def __repr__(self):
        """Official representation for debugging."""
        return f"SmartEmployee('{self.name}', '{self.employee_id}', {self.salary})"
    
    def __eq__(self, other):
        """Equality comparison with ==."""
        if not isinstance(other, SmartEmployee):
            return False
        return self.employee_id == other.employee_id
    
    def __lt__(self, other):
        """Less than comparison for sorting."""
        return self.salary < other.salary
    
    def __add__(self, other):
        """Addition operator + (combine salaries)."""
        if isinstance(other, SmartEmployee):
            return self.salary + other.salary
        return self.salary + other

def demonstrate_special_methods():
    """Demonstrate magic/special methods."""
    
    show_section_header(6, "SPECIAL METHODS (Magic Methods)")
    print("\nProblem: Make objects behave naturally with operators and functions")
    print("Concept: Special methods define how objects behave with built-ins")
    print("-"*80)
    
    print("\n📌 SPECIAL METHODS:")
    print("-"*80)
    print("""
    __init__    : Constructor
    __str__     : String representation (for print)
    __repr__    : Official representation (for debugging)
    __eq__      : Equality (==)
    __lt__      : Less than (<)
    __add__     : Addition (+)
    __len__     : Length (len())
    """)
    
    emp1 = SmartEmployee("Nancy Davis", "EMP0012", 85000)
    emp2 = SmartEmployee("Oscar Martinez", "EMP0013", 72000)
    emp3 = SmartEmployee("Nancy Davis", "EMP0012", 85000)  # Same as emp1
    
    print("\n📌 __str__ (used by print()):")
    print("-"*80)
    print(f"print(emp1): {emp1}")
    print(f"print(emp2): {emp2}")
    
    print("\n📌 __repr__ (used in console/debugging):")
    print("-"*80)
    print(f"repr(emp1): {repr(emp1)}")
    
    print("\n📌 __eq__ (equality comparison ==):")
    print("-"*80)
    print(f"emp1 == emp2: {emp1 == emp2}")
    print(f"emp1 == emp3: {emp1 == emp3}")
    
    print("\n📌 __lt__ (comparison for sorting):")
    print("-"*80)
    employees = [emp1, emp2, SmartEmployee("Paula Brown", "EMP0014", 95000)]
    print("Before sorting:", [e.name for e in employees])
    
    employees.sort()  # Uses __lt__ for comparison
    print("After sorting by salary:", [f"{e.name} (${e.salary:,})" for e in employees])
    
    print("\n📌 __add__ (addition operator +):")
    print("-"*80)
    total = emp1 + emp2
    print(f"{emp1.name}'s salary + {emp2.name}'s salary = ${total:,.2f}")
    
    print("\n✓ Special methods enable:")
    print("  • Natural object behavior")
    print("  • Operator overloading")
    print("  • Integration with built-in functions")

# ============================================================================
# SECTION 7: COMPREHENSIVE EXAMPLE
# ============================================================================

class Manager(FullTimeEmployee):
    """Manager class - demonstrates multi-level inheritance."""
    
    def __init__(self, name, employee_id, department, monthly_salary, team_size):
        super().__init__(name, employee_id, department, monthly_salary)
        self.team_size = team_size
        self.team_members = []
    
    def calculate_salary(self):
        """Override - add management bonus."""
        base_salary = super().calculate_salary()
        management_bonus = self.team_size * 500  # $500 per team member
        return base_salary + management_bonus
    
    def add_team_member(self, employee):
        """Manager-specific method."""
        self.team_members.append(employee)
        return f"✓ Added {employee.name} to team"
    
    def get_info(self):
        """Override with manager info."""
        base_info = super().get_info()
        return f"{base_info} - MANAGER (Team: {self.team_size})"

def demonstrate_comprehensive_example():
    """Complete real-world example using all OOP concepts."""
    
    show_section_header(7, "COMPREHENSIVE EXAMPLE - ALL CONCEPTS TOGETHER")
    print("\nProblem: Build complete employee management system")
    print("Concepts: Class, Object, Inheritance, Polymorphism, Abstraction, Encapsulation")
    print("-"*80)
    
    print("\n📌 CREATING COMPANY STRUCTURE:")
    print("-"*80)
    
    # Create manager
    manager = Manager("Rachel Green", "MGR0001", "Engineering", 12000, 5)
    
    # Create team members
    team = [
        FullTimeEmployee("Ross Geller", "EMP0015", "Engineering", 8500),
        FullTimeEmployee("Monica Geller", "EMP0016", "Engineering", 8000),
        PartTimeEmployee("Phoebe Buffay", "EMP0017", "Support", 45),
        Contractor("Joey Tribbiani", "CON0003", "Testing", 60000, 6),
    ]
    
    # Build team
    print("\nBuilding team:")
    for emp in team:
        print(f"  {manager.add_team_member(emp)}")
    
    # Add hours for part-time
    team[2].hours_worked = 80
    
    print("\n📌 TEAM ROSTER (POLYMORPHISM - different types, same interface):")
    print("-"*80)
    
    all_employees = [manager] + team
    
    print(f"\n{'Name':<20} {'Type':<15} {'Monthly Salary':<15} {'Email'}")
    print("-"*80)
    
    for emp in all_employees:
        emp_type = emp.__class__.__name__
        salary = emp.calculate_salary()
        email = emp.get_work_email()
        print(f"{emp.name:<20} {emp_type:<15} ${salary:>12,.2f}  {email}")
    
    print("\n📌 MANAGER DETAILS (INHERITANCE - Manager extends FullTimeEmployee):")
    print("-"*80)
    base_salary = manager.monthly_salary
    total_salary = manager.calculate_salary()
    bonus = total_salary - base_salary
    
    print(f"Manager: {manager.name}")
    print(f"Base Salary: ${base_salary:,.2f}")
    print(f"Management Bonus: ${bonus:,.2f}")
    print(f"Total Salary: ${total_salary:,.2f}")
    print(f"Team Size: {manager.team_size}")
    
    print("\n📌 PAYROLL PROCESSING (POLYMORPHISM in action):")
    print("-"*80)
    
    def generate_payroll_report(employees):
        """Process any employee type - polymorphism!"""
        total = 0
        print("\nMonthly Payroll Report:")
        print(f"{'Employee':<25} {'Amount':>15}")
        print("-"*42)
        
        for emp in employees:
            salary = emp.calculate_salary()
            total += salary
            print(f"{emp.name:<25} ${salary:>13,.2f}")
        
        print("-"*42)
        print(f"{'TOTAL PAYROLL:':<25} ${total:>13,.2f}")
        print("="*42)
        return total
    
    total_payroll = generate_payroll_report(all_employees)
    
    print("\n📌 ENCAPSULATION EXAMPLE:")
    print("-"*80)
    
    secure_emp = EncapsulatedEmployee("Chandler Bing", "EMP0018", 9000)
    print(f"Public access - Name: {secure_emp.name}")
    print(f"Using getter - Salary: ${secure_emp.get_salary():,.2f}")
    print(f"Private data protected: {secure_emp.get_bank_account()}")
    
    print("\n" + "="*80)
    print("✓ COMPREHENSIVE EXAMPLE DEMONSTRATES:")
    print("="*80)
    print("""
    ✓ CLASSES & OBJECTS: Created Manager, FullTime, PartTime, Contractor
    ✓ INHERITANCE: Manager extends FullTimeEmployee extends Employee
    ✓ POLYMORPHISM: Same method (calculate_salary) different behaviors
    ✓ ENCAPSULATION: Protected salary data with getter/setter
    ✓ ABSTRACTION: Abstract base class ensures interface consistency
    ✓ CODE REUSE: Common functionality in base classes
    ✓ FLEXIBILITY: Easy to add new employee types
    """)

# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Main program demonstrating all OOP concepts."""
    
    print("="*80)
    print(" "*20 + "EMPLOYEE MANAGEMENT SYSTEM")
    print(" "*15 + "Complete Object-Oriented Programming Demo")
    print("="*80)
    
    # Run all demonstrations
    demonstrate_basic_class_and_objects()
    demonstrate_encapsulation()
    demonstrate_inheritance()
    demonstrate_abstraction()
    demonstrate_polymorphism()
    demonstrate_special_methods()
    demonstrate_comprehensive_example()
    
    # Final Summary
    print("\n" + "="*80)
    print("OOP CONCEPTS SUMMARY")
    print("="*80)
    
    summary = """
╔════════════════════════════════════════════════════════════════════════════╗
║                     OBJECT-ORIENTED PROGRAMMING CONCEPTS                   ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  1. CLASS (Blueprint)                                                      ║
║     • Template for creating objects                                       ║
║     • Defines attributes (data) and methods (behavior)                    ║
║     • Example: class Employee: ...                                        ║
║                                                                            ║
║  2. OBJECT (Instance)                                                      ║
║     • Actual instance created from class                                  ║
║     • Has real data                                                       ║
║     • Example: emp = Employee("John", "EMP001", 50000)                    ║
║                                                                            ║
║  3. ENCAPSULATION (Data Hiding)                                            ║
║     • Bundle data and methods together                                    ║
║     • Control access: public, protected (_), private (__)                 ║
║     • Use getters/setters for validation                                  ║
║                                                                            ║
║  4. INHERITANCE (Code Reuse)                                               ║
║     • Child class inherits from parent                                    ║
║     • Reuse common code                                                   ║
║     • Override methods for custom behavior                                ║
║     • Example: class Manager(Employee): ...                               ║
║                                                                            ║
║  5. ABSTRACTION (Hide Complexity)                                          ║
║     • Abstract base class (ABC)                                           ║
║     • Abstract methods (@abstractmethod)                                  ║
║     • Force child classes to implement methods                            ║
║                                                                            ║
║  6. POLYMORPHISM (Many Forms)                                              ║
║     • Same method name, different implementations                         ║
║     • Method overriding                                                   ║
║     • Process different types uniformly                                   ║
║                                                                            ║
║  BENEFITS OF OOP:                                                          ║
║  ───────────────────────────────────────────────────────────────────────  ║
║  • Code Reusability (inheritance)                                         ║
║  • Modularity (organized in classes)                                      ║
║  • Flexibility (polymorphism)                                             ║
║  • Security (encapsulation)                                               ║
║  • Maintainability (easier to update)                                     ║
║  • Scalability (easy to extend)                                           ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """
    print(summary)
    
    print("\n" + "="*80)
    print("PROGRAM COMPLETED SUCCESSFULLY!")
    print("="*80)
    
    print("\n✅ Covered 7 comprehensive sections")
    print("✅ Demonstrated all OOP pillars")
    print("✅ Real-world employee management scenarios")
    
    print("\n🎯 KEY TAKEAWAYS:")
    print("   1. Class = Blueprint, Object = Instance")
    print("   2. Encapsulation = Data protection")
    print("   3. Inheritance = Code reuse")
    print("   4. Abstraction = Hide complexity")
    print("   5. Polymorphism = Flexible code")
    print("   6. Use super() to access parent methods")
    print("   7. Abstract classes ensure consistent interface")
    print("   8. Special methods for natural object behavior")
    print("   9. OOP enables scalable, maintainable code")
    print("   10. Real-world design: base classes + specific children")
    
    print("\n" + "="*80)

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║              EMPLOYEE MANAGEMENT SYSTEM                                    ║
║              Complete OOP Demonstration                                    ║
║                                                                            ║
║  This program demonstrates ALL OOP concepts:                               ║
║                                                                            ║
║  ✓ Classes & Objects       ✓ Encapsulation (Public/Private)               ║
║  ✓ Inheritance             ✓ Abstraction (ABC)                            ║
║  ✓ Polymorphism            ✓ Special Methods                              ║
║                                                                            ║
║  Total: 40+ examples in real employee management context!                 ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)
    
    main()
    
    print("\n\n💡 QUICK REFERENCE:")
    print("="*80)
    print("• Class:         class Employee: ...")
    print("• Object:        emp = Employee('John', 'EMP001', 50000)")
    print("• Inheritance:   class Manager(Employee): ...")
    print("• Encapsulation: self.__private, self._protected, self.public")
    print("• Abstraction:   from abc import ABC, abstractmethod")
    print("• Polymorphism:  Same method, different behavior per class")
    print("• super():       super().__init__(...) - call parent method")
    print("="*80)