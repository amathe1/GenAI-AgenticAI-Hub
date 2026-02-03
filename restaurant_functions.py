"""
================================================================================
                    RESTAURANT ORDER MANAGEMENT SYSTEM
================================================================================

DETAILED PROBLEM STATEMENT:
---------------------------
Create a comprehensive Restaurant Order Management System that handles menu
management, order processing, billing, customer management, and reporting.
The system demonstrates ALL function concepts in Python through real-world
restaurant operations.

BUSINESS CONTEXT:
-----------------
A restaurant needs a digital system to:
1. Manage menu items with prices and descriptions
2. Take customer orders with various customizations
3. Calculate bills with taxes, discounts, and tips
4. Process payments and generate receipts
5. Track employee performance and commissions
6. Generate sales reports and analytics
7. Handle special requests and dietary restrictions

REQUIREMENTS - FUNCTION CONCEPTS COVERED:
-----------------------------------------

1. BASIC FUNCTIONS:
   - Define and call simple functions
   - Return values
   - Function documentation (docstrings)

2. FUNCTION ARGUMENTS:
   
   a) POSITIONAL ARGUMENTS:
      - Arguments passed in specific order
      - Example: add_menu_item(name, price, category)
   
   b) KEYWORD ARGUMENTS:
      - Arguments passed by name
      - Example: add_menu_item(price=10.99, name="Burger", category="Main")
   
   c) DEFAULT ARGUMENTS:
      - Arguments with default values
      - Example: calculate_price(amount, tax_rate=0.08, tip_rate=0.15)
   
   d) *args (Variable Positional Arguments):
      - Accept any number of positional arguments
      - Example: calculate_total_cost(*prices)
   
   e) **kwargs (Variable Keyword Arguments):
      - Accept any number of keyword arguments
      - Example: create_custom_order(**toppings)

3. LAMBDA FUNCTIONS:
   - Anonymous one-line functions
   - Use with map(), filter(), sorted()
   - Quick calculations and transformations

4. DECORATORS:
   - Functions that modify other functions
   - @login_required - Check user authentication
   - @time_execution - Measure function execution time
   - @validate_input - Validate function arguments
   - @log_operation - Log function calls

5. PRIVATE FUNCTIONS:
   - Functions prefixed with _ (single underscore)
   - Internal helper functions
   - Not intended for external use

6. NESTED FUNCTIONS:
   - Functions defined inside other functions
   - Closures and encapsulation

7. FUNCTION SCOPE:
   - Local vs Global variables
   - nonlocal keyword

LEARNING OBJECTIVES:
-------------------
By the end of this program, you will understand:
• How to define and call functions effectively
• Difference between positional, keyword, and default arguments
• When to use *args and **kwargs
• How to write and use lambda functions
• How to create and apply decorators
• Best practices for function organization
• Function scope and variable lifetime

================================================================================
"""

import time
from datetime import datetime
from functools import wraps

# ============================================================================
# GLOBAL VARIABLES
# ============================================================================

# Restaurant menu (global data)
MENU = {}
ORDERS = []
CURRENT_USER = None

# ============================================================================
# SECTION 1: BASIC FUNCTIONS
# ============================================================================

def show_section_header(section_number, title):
    """
    Display formatted section header.
    
    This is a BASIC FUNCTION demonstrating:
    - Function definition with def keyword
    - Parameters (section_number, title)
    - Docstring documentation
    - Return statement
    """
    print("\n" + "="*80)
    print(f"SECTION {section_number}: {title}")
    print("="*80)
    return f"Section {section_number} displayed"

def greet_customer():
    """Basic function with no parameters and no return value."""
    print("\n👋 Welcome to Python Restaurant!")
    print("   Your satisfaction is our priority!")

def get_restaurant_name():
    """Basic function with return value but no parameters."""
    return "Python Gourmet Restaurant"

def display_menu_item(name, price):
    """Basic function with parameters and formatted output."""
    print(f"   {name:<30} ${price:>6.2f}")

# ============================================================================
# SECTION 2: POSITIONAL ARGUMENTS
# ============================================================================

def add_menu_item_positional(name, price, category, description):
    """
    Add menu item using POSITIONAL ARGUMENTS.
    
    Positional arguments MUST be passed in the correct order:
    1. name
    2. price
    3. category
    4. description
    
    Order matters! Swapping arguments will cause errors or incorrect data.
    """
    item_id = len(MENU) + 1
    MENU[item_id] = {
        'name': name,
        'price': price,
        'category': category,
        'description': description
    }
    print(f"   ✓ Added: {name} - ${price:.2f} ({category})")
    return item_id

def calculate_bill_positional(subtotal, tax_rate, tip_rate):
    """
    Calculate total bill using POSITIONAL ARGUMENTS.
    
    Arguments must be in order: subtotal, tax_rate, tip_rate
    """
    tax = subtotal * tax_rate
    tip = subtotal * tip_rate
    total = subtotal + tax + tip
    
    print(f"   Subtotal: ${subtotal:.2f}")
    print(f"   Tax ({tax_rate*100}%): ${tax:.2f}")
    print(f"   Tip ({tip_rate*100}%): ${tip:.2f}")
    print(f"   TOTAL: ${total:.2f}")
    
    return total

# ============================================================================
# SECTION 3: KEYWORD ARGUMENTS
# ============================================================================

def add_menu_item_keyword(name, price, category, description, spicy_level=0):
    """
    Add menu item using KEYWORD ARGUMENTS.
    
    Keyword arguments can be passed in ANY order:
    - name="Burger"
    - price=10.99
    - category="Main"
    
    Advantage: More readable, order doesn't matter!
    """
    item_id = len(MENU) + 1
    MENU[item_id] = {
        'name': name,
        'price': price,
        'category': category,
        'description': description,
        'spicy_level': spicy_level
    }
    spicy = "🌶️" * spicy_level if spicy_level > 0 else ""
    print(f"   ✓ Added: {name} - ${price:.2f} {spicy}")
    return item_id

def create_customer_profile(first_name, last_name, email, phone, 
                           vip_status=False, dietary_restrictions=None):
    """
    Create customer profile with MIXED arguments.
    
    Required keyword arguments: first_name, last_name, email, phone
    Optional with defaults: vip_status, dietary_restrictions
    """
    profile = {
        'name': f"{first_name} {last_name}",
        'email': email,
        'phone': phone,
        'vip': vip_status,
        'dietary': dietary_restrictions or []
    }
    
    print(f"   📋 Customer: {profile['name']}")
    print(f"      Email: {email}")
    print(f"      VIP Status: {'Yes ⭐' if vip_status else 'No'}")
    
    return profile

# ============================================================================
# SECTION 4: DEFAULT ARGUMENTS
# ============================================================================

def calculate_price(base_price, tax_rate=0.08, service_charge=0.10, 
                   discount=0.0, tip_rate=0.15):
    """
    Calculate final price with DEFAULT ARGUMENTS.
    
    Default arguments provide fallback values:
    - tax_rate: defaults to 0.08 (8%)
    - service_charge: defaults to 0.10 (10%)
    - discount: defaults to 0.0 (0%)
    - tip_rate: defaults to 0.15 (15%)
    
    Can override any or all defaults when calling.
    """
    print(f"\n   Base Price: ${base_price:.2f}")
    
    # Calculate components
    tax = base_price * tax_rate
    service = base_price * service_charge
    discount_amount = base_price * discount
    subtotal = base_price + tax + service - discount_amount
    tip = subtotal * tip_rate
    total = subtotal + tip
    
    print(f"   Tax ({tax_rate*100}%): ${tax:.2f}")
    print(f"   Service ({service_charge*100}%): ${service:.2f}")
    if discount > 0:
        print(f"   Discount ({discount*100}%): -${discount_amount:.2f}")
    print(f"   Tip ({tip_rate*100}%): ${tip:.2f}")
    print(f"   TOTAL: ${total:.2f}")
    
    return total

def take_order(customer_name, table_number=1, server_name="Default Server",
               priority="normal", special_requests="None"):
    """
    Take customer order with DEFAULT ARGUMENTS.
    
    Only customer_name is required.
    All others have sensible defaults.
    """
    order = {
        'customer': customer_name,
        'table': table_number,
        'server': server_name,
        'priority': priority,
        'special_requests': special_requests,
        'time': datetime.now().strftime("%H:%M:%S")
    }
    
    print(f"\n   📝 ORDER RECEIVED")
    print(f"      Customer: {customer_name}")
    print(f"      Table: {table_number}")
    print(f"      Server: {server_name}")
    print(f"      Priority: {priority.upper()}")
    if special_requests != "None":
        print(f"      Special: {special_requests}")
    
    return order

# ============================================================================
# SECTION 5: *args (VARIABLE POSITIONAL ARGUMENTS)
# ============================================================================

def calculate_total_cost(*prices):
    """
    Calculate total cost using *args (variable positional arguments).
    
    *args allows ANY NUMBER of positional arguments.
    Can pass 1, 5, 10, or 100 prices!
    
    Example:
        calculate_total_cost(10.99)
        calculate_total_cost(10.99, 5.99, 8.99, 12.99)
    """
    print(f"\n   Calculating total for {len(prices)} items:")
    
    total = 0
    for i, price in enumerate(prices, 1):
        print(f"      Item {i}: ${price:.2f}")
        total += price
    
    print(f"   TOTAL: ${total:.2f}")
    return total

def combine_orders(*order_ids):
    """
    Combine multiple orders using *args.
    
    Can combine any number of orders!
    """
    print(f"\n   Combining {len(order_ids)} orders:")
    for order_id in order_ids:
        print(f"      - Order #{order_id}")
    
    combined_id = f"COMBINED-{'-'.join(map(str, order_ids))}"
    print(f"   New Combined Order ID: {combined_id}")
    return combined_id

def find_maximum_price(*prices):
    """
    Find maximum price from any number of items using *args.
    """
    if not prices:
        return 0
    
    max_price = max(prices)
    min_price = min(prices)
    avg_price = sum(prices) / len(prices)
    
    print(f"\n   Price Analysis ({len(prices)} items):")
    print(f"      Maximum: ${max_price:.2f}")
    print(f"      Minimum: ${min_price:.2f}")
    print(f"      Average: ${avg_price:.2f}")
    
    return max_price

# ============================================================================
# SECTION 6: **kwargs (VARIABLE KEYWORD ARGUMENTS)
# ============================================================================

def create_custom_pizza(**toppings):
    """
    Create custom pizza using **kwargs (variable keyword arguments).
    
    **kwargs allows ANY NUMBER of keyword arguments.
    Can pass any combination of toppings!
    
    Example:
        create_custom_pizza(cheese="mozzarella", sauce="tomato", 
                          pepperoni=True, mushrooms=True)
    """
    print(f"\n   🍕 CUSTOM PIZZA ORDER:")
    print(f"      Base Price: $10.00")
    
    base_price = 10.00
    topping_price = 1.50
    total_toppings = len(toppings)
    
    print(f"      Customizations ({total_toppings}):")
    for topping, value in toppings.items():
        print(f"         + {topping.replace('_', ' ').title()}: {value}")
    
    total = base_price + (total_toppings * topping_price)
    print(f"      TOTAL: ${total:.2f}")
    
    return total

def generate_receipt(**details):
    """
    Generate detailed receipt using **kwargs.
    
    Accepts any number of receipt details as keyword arguments.
    """
    print(f"\n   {'='*50}")
    print(f"   {'RECEIPT':^50}")
    print(f"   {'='*50}")
    
    for key, value in details.items():
        label = key.replace('_', ' ').title()
        print(f"   {label:<30} {value}")
    
    print(f"   {'='*50}")
    return details

def configure_restaurant_settings(**settings):
    """
    Configure restaurant settings using **kwargs.
    
    Can set any number of configuration options dynamically.
    """
    print(f"\n   ⚙️ RESTAURANT SETTINGS:")
    
    for setting, value in settings.items():
        print(f"      {setting.replace('_', ' ').title()}: {value}")
    
    return settings

# ============================================================================
# SECTION 7: COMBINING *args AND **kwargs
# ============================================================================

def process_order(customer_name, *items, **options):
    """
    Process order with COMBINED *args and **kwargs.
    
    Parameters:
    - customer_name: Required positional argument
    - *items: Any number of menu items
    - **options: Any number of order options
    
    Example:
        process_order("John", "Burger", "Fries", "Coke",
                     delivery=True, priority="high", tip=5.00)
    """
    print(f"\n   📋 PROCESSING ORDER FOR: {customer_name}")
    
    print(f"\n   Items Ordered ({len(items)}):")
    for i, item in enumerate(items, 1):
        print(f"      {i}. {item}")
    
    if options:
        print(f"\n   Order Options:")
        for key, value in options.items():
            print(f"      {key.replace('_', ' ').title()}: {value}")
    
    order_summary = {
        'customer': customer_name,
        'items': items,
        'options': options,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return order_summary

def create_combo_meal(combo_name, *items, discount=0.10, **extras):
    """
    Create combo meal with ALL argument types.
    
    - combo_name: Required positional
    - *items: Variable items in combo
    - discount: Default argument
    - **extras: Variable extra options
    """
    print(f"\n   🍔 COMBO MEAL: {combo_name}")
    print(f"   Includes:")
    
    base_price = 0
    for item in items:
        item_price = 5.99  # Simplified pricing
        base_price += item_price
        print(f"      + {item} (${item_price:.2f})")
    
    discount_amount = base_price * discount
    final_price = base_price - discount_amount
    
    print(f"\n   Base Price: ${base_price:.2f}")
    print(f"   Combo Discount ({discount*100}%): -${discount_amount:.2f}")
    
    if extras:
        print(f"   Extras:")
        for extra, price in extras.items():
            print(f"      + {extra}: ${price:.2f}")
            final_price += price
    
    print(f"   FINAL PRICE: ${final_price:.2f}")
    
    return final_price

# ============================================================================
# SECTION 8: LAMBDA FUNCTIONS
# ============================================================================

def demonstrate_lambda_functions():
    """
    Demonstrate LAMBDA FUNCTIONS (anonymous one-line functions).
    
    Lambda syntax: lambda arguments: expression
    
    Use cases:
    - Quick calculations
    - Inline functions for map(), filter(), sorted()
    - Callback functions
    """
    print("\n   LAMBDA FUNCTION EXAMPLES:")
    print("   " + "-"*60)
    
    # Example 1: Simple lambda
    print("\n   1. SIMPLE LAMBDA - Add tip to price")
    add_tip = lambda price: price * 1.15
    price = 25.00
    with_tip = add_tip(price)
    print(f"      Price: ${price:.2f} → With tip: ${with_tip:.2f}")
    
    # Example 2: Lambda with multiple arguments
    print("\n   2. LAMBDA WITH MULTIPLE ARGUMENTS - Calculate total")
    calculate_total = lambda price, tax, tip: price + (price * tax) + (price * tip)
    total = calculate_total(30.00, 0.08, 0.15)
    print(f"      Total with tax and tip: ${total:.2f}")
    
    # Example 3: Lambda with map()
    print("\n   3. LAMBDA WITH MAP - Apply discount to all prices")
    prices = [10.99, 15.99, 8.99, 12.99, 20.99]
    discounted = list(map(lambda x: x * 0.90, prices))
    print(f"      Original:   {[f'${p:.2f}' for p in prices]}")
    print(f"      Discounted: {[f'${p:.2f}' for p in discounted]}")
    
    # Example 4: Lambda with filter()
    print("\n   4. LAMBDA WITH FILTER - Find expensive items")
    expensive_items = list(filter(lambda x: x > 15.00, prices))
    print(f"      All prices: {[f'${p:.2f}' for p in prices]}")
    print(f"      Expensive (>$15): {[f'${p:.2f}' for p in expensive_items]}")
    
    # Example 5: Lambda with sorted()
    print("\n   5. LAMBDA WITH SORTED - Sort menu items")
    menu_items = [
        {'name': 'Burger', 'price': 12.99, 'rating': 4.5},
        {'name': 'Pizza', 'price': 15.99, 'rating': 4.8},
        {'name': 'Salad', 'price': 8.99, 'rating': 4.2},
        {'name': 'Pasta', 'price': 13.99, 'rating': 4.6}
    ]
    
    # Sort by price
    by_price = sorted(menu_items, key=lambda x: x['price'])
    print(f"      Sorted by price (low to high):")
    for item in by_price:
        print(f"         {item['name']:<15} ${item['price']:.2f}")
    
    # Sort by rating
    by_rating = sorted(menu_items, key=lambda x: x['rating'], reverse=True)
    print(f"\n      Sorted by rating (high to low):")
    for item in by_rating:
        print(f"         {item['name']:<15} ⭐{item['rating']}")
    
    # Example 6: Lambda for conditional logic
    print("\n   6. LAMBDA WITH CONDITIONAL - Apply VIP discount")
    apply_vip_discount = lambda price, is_vip: price * 0.80 if is_vip else price
    regular_price = apply_vip_discount(50.00, False)
    vip_price = apply_vip_discount(50.00, True)
    print(f"      Regular customer: ${regular_price:.2f}")
    print(f"      VIP customer: ${vip_price:.2f}")

# ============================================================================
# SECTION 9: DECORATORS
# ============================================================================

def login_required(func):
    """
    DECORATOR: Check if user is logged in before executing function.
    
    Decorators are functions that modify other functions.
    They add functionality without changing the original function.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        global CURRENT_USER
        if CURRENT_USER is None:
            print(f"\n   ❌ ACCESS DENIED: Please login first!")
            print(f"      Function '{func.__name__}' requires authentication.")
            return None
        
        print(f"\n   ✓ Authenticated as: {CURRENT_USER}")
        return func(*args, **kwargs)
    
    return wrapper

def time_execution(func):
    """
    DECORATOR: Measure and display function execution time.
    
    Useful for performance monitoring and optimization.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        
        print(f"\n   ⏱️  Executing '{func.__name__}'...")
        result = func(*args, **kwargs)
        
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        print(f"   ⏱️  Execution time: {execution_time:.2f} ms")
        
        return result
    
    return wrapper

def validate_price(func):
    """
    DECORATOR: Validate price arguments before processing.
    
    Ensures data integrity and prevents errors.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check if 'price' argument exists and is valid
        if 'price' in kwargs:
            price = kwargs['price']
            if price < 0:
                print(f"\n   ❌ VALIDATION ERROR: Price cannot be negative!")
                print(f"      Received: ${price:.2f}")
                return None
            if price > 1000:
                print(f"\n   ⚠️  WARNING: Unusually high price: ${price:.2f}")
        
        print(f"\n   ✓ Validation passed for '{func.__name__}'")
        return func(*args, **kwargs)
    
    return wrapper

def log_operation(func):
    """
    DECORATOR: Log function calls with timestamp.
    
    Useful for debugging and audit trails.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n   📝 LOG [{timestamp}]: {func.__name__} called")
        
        if args:
            print(f"      Arguments: {args}")
        if kwargs:
            print(f"      Keyword Arguments: {kwargs}")
        
        result = func(*args, **kwargs)
        
        print(f"   📝 LOG: {func.__name__} completed")
        
        return result
    
    return wrapper

# Decorated functions

@login_required
def view_order_history(customer_id):
    """Function that requires login (decorated)."""
    print(f"\n   📋 ORDER HISTORY for Customer #{customer_id}")
    print(f"      Order #1: $25.99 - 2024-01-10")
    print(f"      Order #2: $35.50 - 2024-01-09")
    print(f"      Order #3: $18.75 - 2024-01-08")
    return "History retrieved"

@time_execution
def prepare_complex_order():
    """Function with execution time measurement (decorated)."""
    print(f"   Preparing gourmet meal...")
    time.sleep(0.1)  # Simulate cooking time
    print(f"   Adding special sauce...")
    time.sleep(0.05)
    print(f"   Plating...")
    time.sleep(0.03)
    print(f"   ✓ Order ready!")
    return "Order completed"

@validate_price
def add_premium_item(name, price, category):
    """Function with price validation (decorated)."""
    print(f"   ✓ Added premium item: {name} - ${price:.2f}")
    return {'name': name, 'price': price, 'category': category}

@log_operation
@time_execution
def process_payment(amount, payment_method):
    """Function with multiple decorators (stacked)."""
    print(f"\n   💳 Processing ${amount:.2f} via {payment_method}")
    time.sleep(0.05)  # Simulate payment processing
    print(f"   ✓ Payment successful!")
    return f"Payment of ${amount:.2f} processed"

# ============================================================================
# SECTION 10: PRIVATE FUNCTIONS (Helper Functions)
# ============================================================================

def _calculate_tax(amount, rate=0.08):
    """
    PRIVATE FUNCTION: Calculate tax (internal use only).
    
    Private functions start with _ (single underscore).
    Convention: Not intended for external use.
    Used as helper functions within modules.
    """
    return amount * rate

def _calculate_tip(amount, rate=0.15):
    """PRIVATE FUNCTION: Calculate tip (internal use only)."""
    return amount * rate

def _format_currency(amount):
    """PRIVATE FUNCTION: Format amount as currency (internal use only)."""
    return f"${amount:,.2f}"

def _validate_order_items(items):
    """PRIVATE FUNCTION: Validate order items (internal use only)."""
    if not items:
        return False, "No items in order"
    if len(items) > 20:
        return False, "Too many items (max 20)"
    return True, "Valid"

# Public function that uses private functions
def generate_final_bill(subtotal, include_tax=True, include_tip=True):
    """
    PUBLIC FUNCTION: Generate final bill using private helper functions.
    
    This demonstrates how public functions use private helpers internally.
    """
    print(f"\n   💵 GENERATING FINAL BILL:")
    print(f"   " + "-"*60)
    
    # Use private helper functions
    print(f"   Subtotal:     {_format_currency(subtotal)}")
    
    total = subtotal
    
    if include_tax:
        tax = _calculate_tax(subtotal)
        total += tax
        print(f"   Tax (8%):     {_format_currency(tax)}")
    
    if include_tip:
        tip = _calculate_tip(subtotal)
        total += tip
        print(f"   Tip (15%):    {_format_currency(tip)}")
    
    print(f"   " + "-"*60)
    print(f"   TOTAL:        {_format_currency(total)}")
    
    return total

# ============================================================================
# SECTION 11: NESTED FUNCTIONS & CLOSURES
# ============================================================================

def create_discount_calculator(default_discount):
    """
    NESTED FUNCTION & CLOSURE demonstration.
    
    Returns a function that "remembers" the default_discount value.
    This is called a closure.
    """
    print(f"\n   Creating discount calculator with {default_discount*100}% default")
    
    def calculate_discount(price, custom_discount=None):
        """Nested function that uses outer function's variable."""
        discount = custom_discount if custom_discount is not None else default_discount
        discount_amount = price * discount
        final_price = price - discount_amount
        
        print(f"   Original: ${price:.2f} - Discount: {discount*100}% "
              f"= Final: ${final_price:.2f}")
        
        return final_price
    
    return calculate_discount

def create_order_counter():
    """
    CLOSURE: Create order counter with private state.
    
    Demonstrates encapsulation using nested functions.
    """
    count = 0  # Private variable
    
    def increment_and_get():
        """Nested function that modifies outer variable."""
        nonlocal count  # Access outer function's variable
        count += 1
        return count
    
    def get_count():
        """Nested function to get current count."""
        return count
    
    def reset():
        """Nested function to reset counter."""
        nonlocal count
        count = 0
        return count
    
    # Return multiple nested functions
    return increment_and_get, get_count, reset

# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Main program demonstrating all function concepts."""
    
    global CURRENT_USER
    
    print("="*80)
    print(" "*20 + "RESTAURANT ORDER MANAGEMENT SYSTEM")
    print(" "*18 + "Comprehensive Function Demonstration")
    print("="*80)
    
    # ========================================================================
    # SECTION 1: BASIC FUNCTIONS
    # ========================================================================
    
    show_section_header(1, "BASIC FUNCTIONS")
    print("\nProblem: Create simple reusable functions")
    print("Concepts: def keyword, parameters, return values, docstrings")
    print("-"*80)
    
    greet_customer()
    restaurant_name = get_restaurant_name()
    print(f"\n   Restaurant: {restaurant_name}")
    
    print(f"\n   Sample Menu Item:")
    display_menu_item("Gourmet Burger", 12.99)
    
    # ========================================================================
    # SECTION 2: POSITIONAL ARGUMENTS
    # ========================================================================
    
    show_section_header(2, "POSITIONAL ARGUMENTS")
    print("\nProblem: Add menu items with arguments in specific order")
    print("Concept: Arguments must be passed in exact order")
    print("-"*80)
    
    print("\n   Adding menu items (positional arguments):")
    add_menu_item_positional("Classic Burger", 12.99, "Main Course", 
                            "Juicy beef patty with fresh vegetables")
    add_menu_item_positional("Caesar Salad", 8.99, "Appetizer",
                            "Crisp romaine with Caesar dressing")
    
    print("\n   Calculating bill (positional arguments):")
    calculate_bill_positional(50.00, 0.08, 0.15)
    
    # ========================================================================
    # SECTION 3: KEYWORD ARGUMENTS
    # ========================================================================
    
    show_section_header(3, "KEYWORD ARGUMENTS")
    print("\nProblem: Pass arguments by name for better readability")
    print("Concept: Arguments can be passed in any order using names")
    print("-"*80)
    
    print("\n   Adding items with keyword arguments (any order):")
    add_menu_item_keyword(
        price=15.99,
        name="Spicy Pizza",
        description="Wood-fired pizza with jalapeños",
        category="Main Course",
        spicy_level=3
    )
    
    print("\n   Creating customer profile:")
    create_customer_profile(
        email="john.doe@email.com",
        last_name="Doe",
        first_name="John",
        phone="555-1234",
        vip_status=True
    )
    
    # ========================================================================
    # SECTION 4: DEFAULT ARGUMENTS
    # ========================================================================
    
    show_section_header(4, "DEFAULT ARGUMENTS")
    print("\nProblem: Provide default values for optional parameters")
    print("Concept: Parameters with default values can be omitted")
    print("-"*80)
    
    print("\n   Example 1: Using all defaults")
    calculate_price(100.00)
    
    print("\n   Example 2: Override some defaults")
    calculate_price(100.00, tax_rate=0.10, tip_rate=0.20)
    
    print("\n   Example 3: VIP customer (with discount)")
    calculate_price(100.00, discount=0.20, tip_rate=0.10)
    
    print("\n   Taking orders with defaults:")
    take_order("Alice Smith")
    take_order("Bob Johnson", table_number=5, priority="urgent",
              special_requests="No onions, extra cheese")
    
    # ========================================================================
    # SECTION 5: *args (VARIABLE POSITIONAL ARGUMENTS)
    # ========================================================================
    
    show_section_header(5, "*args - VARIABLE POSITIONAL ARGUMENTS")
    print("\nProblem: Accept any number of positional arguments")
    print("Concept: *args allows unlimited positional parameters")
    print("-"*80)
    
    print("\n   Example 1: Calculate total (2 items)")
    calculate_total_cost(10.99, 15.99)
    
    print("\n   Example 2: Calculate total (5 items)")
    calculate_total_cost(10.99, 15.99, 8.99, 12.99, 20.99)
    
    print("\n   Example 3: Combine orders")
    combine_orders(101, 102, 103)
    
    print("\n   Example 4: Find maximum price")
    find_maximum_price(10.99, 25.99, 8.99, 15.99, 30.99, 12.99)
    
    # ========================================================================
    # SECTION 6: **kwargs (VARIABLE KEYWORD ARGUMENTS)
    # ========================================================================
    
    show_section_header(6, "**kwargs - VARIABLE KEYWORD ARGUMENTS")
    print("\nProblem: Accept any number of keyword arguments")
    print("Concept: **kwargs allows unlimited named parameters")
    print("-"*80)
    
    print("\n   Example 1: Create custom pizza")
    create_custom_pizza(
        cheese="mozzarella",
        sauce="marinara",
        pepperoni=True,
        mushrooms=True,
        olives=True,
        bell_peppers=True
    )
    
    print("\n   Example 2: Generate receipt")
    generate_receipt(
        order_id="ORD-12345",
        customer_name="Alice Johnson",
        date="2025-01-11",
        payment_method="Credit Card",
        server="John Smith",
        table="5"
    )
    
    print("\n   Example 3: Configure settings")
    configure_restaurant_settings(
        opening_time="10:00 AM",
        closing_time="11:00 PM",
        max_capacity=50,
        delivery_radius="5 miles",
        accepts_reservations=True
    )
    
    # ========================================================================
    # SECTION 7: COMBINING *args AND **kwargs
    # ========================================================================
    
    show_section_header(7, "COMBINING *args AND **kwargs")
    print("\nProblem: Create flexible functions accepting any arguments")
    print("Concept: Use both *args and **kwargs together")
    print("-"*80)
    
    print("\n   Example 1: Process order with multiple items and options")
    process_order(
        "John Smith",
        "Burger", "Fries", "Coke", "Ice Cream",
        delivery=True,
        address="123 Main St",
        priority="high",
        tip=5.00,
        utensils=True
    )
    
    print("\n   Example 2: Create combo meal")
    create_combo_meal(
        "Family Feast",
        "Pizza", "Pasta", "Salad", "Garlic Bread",
        discount=0.15,
        extra_cheese=2.00,
        extra_sauce=1.00,
        delivery=3.00
    )
    
    # ========================================================================
    # SECTION 8: LAMBDA FUNCTIONS
    # ========================================================================
    
    show_section_header(8, "LAMBDA FUNCTIONS")
    print("\nProblem: Create quick inline functions")
    print("Concept: Anonymous one-line functions")
    print("Syntax: lambda arguments: expression")
    print("-"*80)
    
    demonstrate_lambda_functions()
    
    # ========================================================================
    # SECTION 9: DECORATORS
    # ========================================================================
    
    show_section_header(9, "DECORATORS")
    print("\nProblem: Add functionality to existing functions")
    print("Concept: Functions that modify other functions")
    print("Syntax: @decorator_name above function definition")
    print("-"*80)
    
    print("\n   Example 1: Login Required Decorator")
    print("   Attempting to view order history without login:")
    view_order_history(12345)
    
    print("\n   Logging in...")
    CURRENT_USER = "alice@restaurant.com"
    print(f"   ✓ Logged in as: {CURRENT_USER}")
    
    print("\n   Attempting again after login:")
    view_order_history(12345)
    
    print("\n\n   Example 2: Time Execution Decorator")
    prepare_complex_order()
    
    print("\n\n   Example 3: Validate Price Decorator")
    add_premium_item("Lobster Thermidor", 45.99, "Premium")
    
    print("\n   Trying invalid price:")
    add_premium_item("Invalid Item", -10.00, "Test")
    
    print("\n\n   Example 4: Multiple Decorators (Stacked)")
    process_payment(125.50, "Credit Card")
    
    # ========================================================================
    # SECTION 10: PRIVATE FUNCTIONS
    # ========================================================================
    
    show_section_header(10, "PRIVATE FUNCTIONS (HELPER FUNCTIONS)")
    print("\nProblem: Create internal helper functions")
    print("Concept: Functions prefixed with _ are private by convention")
    print("Usage: Used internally, not meant for external calls")
    print("-"*80)
    
    print("\n   Public function using private helpers:")
    generate_final_bill(75.00, include_tax=True, include_tip=True)
    
    print("\n   Note: Private functions _calculate_tax(), _calculate_tip(),")
    print("         and _format_currency() were used internally")
    
    # ========================================================================
    # SECTION 11: NESTED FUNCTIONS & CLOSURES
    # ========================================================================
    
    show_section_header(11, "NESTED FUNCTIONS & CLOSURES")
    print("\nProblem: Create functions with private state")
    print("Concept: Functions inside functions that 'remember' values")
    print("-"*80)
    
    print("\n   Example 1: Discount Calculator (Closure)")
    vip_calculator = create_discount_calculator(0.20)  # 20% discount
    regular_calculator = create_discount_calculator(0.10)  # 10% discount
    
    print("\n   VIP Calculator (20% default):")
    vip_calculator(100.00)
    vip_calculator(100.00, custom_discount=0.25)
    
    print("\n   Regular Calculator (10% default):")
    regular_calculator(100.00)
    
    print("\n\n   Example 2: Order Counter (Encapsulation)")
    increment, get_count, reset = create_order_counter()
    
    print(f"   Order #{increment()}")
    print(f"   Order #{increment()}")
    print(f"   Order #{increment()}")
    print(f"   Current count: {get_count()}")
    print(f"   Resetting counter...")
    reset()
    print(f"   Count after reset: {get_count()}")
    
    # ========================================================================
    # FINAL SUMMARY
    # ========================================================================
    
    print("\n" + "="*80)
    print("COMPREHENSIVE SUMMARY")
    print("="*80)
    
    summary = """
╔════════════════════════════════════════════════════════════════════════════╗
║                    ALL FUNCTION CONCEPTS COVERED                           ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  1. BASIC FUNCTIONS                                                        ║
║     • Function definition with def                                         ║
║     • Parameters and return values                                         ║
║     • Docstrings for documentation                                         ║
║                                                                            ║
║  2. POSITIONAL ARGUMENTS                                                   ║
║     • Arguments passed in specific order                                   ║
║     • Order matters!                                                       ║
║     • Example: func(arg1, arg2, arg3)                                      ║
║                                                                            ║
║  3. KEYWORD ARGUMENTS                                                      ║
║     • Arguments passed by name                                             ║
║     • Order doesn't matter                                                 ║
║     • Example: func(name="value", price=10.99)                             ║
║                                                                            ║
║  4. DEFAULT ARGUMENTS                                                      ║
║     • Parameters with default values                                       ║
║     • Optional parameters                                                  ║
║     • Example: def func(required, optional=default)                        ║
║                                                                            ║
║  5. *args (VARIABLE POSITIONAL)                                            ║
║     • Accept any number of positional arguments                            ║
║     • Creates tuple of arguments                                           ║
║     • Example: def func(*args)                                             ║
║                                                                            ║
║  6. **kwargs (VARIABLE KEYWORD)                                            ║
║     • Accept any number of keyword arguments                               ║
║     • Creates dictionary of arguments                                      ║
║     • Example: def func(**kwargs)                                          ║
║                                                                            ║
║  7. COMBINING ARGUMENT TYPES                                               ║
║     • Order: positional, *args, defaults, **kwargs                         ║
║     • Example: def func(pos, *args, default=val, **kwargs)                 ║
║                                                                            ║
║  8. LAMBDA FUNCTIONS                                                       ║
║     • Anonymous one-line functions                                         ║
║     • Syntax: lambda args: expression                                      ║
║     • Use with map(), filter(), sorted()                                   ║
║                                                                            ║
║  9. DECORATORS                                                             ║
║     • Functions that modify other functions                                ║
║     • Syntax: @decorator above function                                    ║
║     • Can be stacked for multiple effects                                  ║
║                                                                            ║
║  10. PRIVATE FUNCTIONS                                                     ║
║      • Prefix with _ for internal use                                      ║
║      • Convention, not enforced                                            ║
║      • Helper functions within modules                                     ║
║                                                                            ║
║  11. NESTED FUNCTIONS & CLOSURES                                           ║
║      • Functions inside functions                                          ║
║      • Closures "remember" outer variables                                 ║
║      • Encapsulation and data hiding                                       ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """
    print(summary)
    
    print("\n" + "="*80)
    print("PROGRAM COMPLETED SUCCESSFULLY!")
    print("="*80)
    
    print("\n✅ Covered 11 comprehensive sections")
    print("✅ Demonstrated 40+ function examples")
    print("✅ Showed real-world restaurant scenarios")
    
    print("\n🎯 KEY PRINCIPLES:")
    print("   1. Functions promote code reusability")
    print("   2. Use descriptive function names")
    print("   3. Write docstrings for documentation")
    print("   4. Use default arguments for flexibility")
    print("   5. *args and **kwargs for variable arguments")
    print("   6. Lambda for simple, one-time operations")
    print("   7. Decorators for cross-cutting concerns")
    print("   8. Private functions (_func) for internal helpers")
    print("   9. Closures for encapsulation")
    print("   10. One function = One clear purpose")
    
    print("\n" + "="*80)

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║              RESTAURANT ORDER MANAGEMENT SYSTEM                            ║
║              Comprehensive Function Demonstration                          ║
║                                                                            ║
║  This program demonstrates ALL function concepts:                          ║
║                                                                            ║
║  ✓ Basic Functions              ✓ Positional Arguments                    ║
║  ✓ Keyword Arguments             ✓ Default Arguments                       ║
║  ✓ *args (Variable Positional)   ✓ **kwargs (Variable Keyword)            ║
║  ✓ Lambda Functions              ✓ Decorators                              ║
║  ✓ Private Functions             ✓ Nested Functions & Closures            ║
║                                                                            ║
║  Total: 40+ function examples in real-world context!                      ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)
    
    main()
    
    print("\n\n💡 QUICK REFERENCE:")
    print("="*80)
    print("• Basic:      def func(arg1, arg2): return result")
    print("• Positional: func(val1, val2)  # Order matters")
    print("• Keyword:    func(name=val, price=10)  # Order doesn't matter")
    print("• Default:    def func(arg, opt=default):")
    print("• *args:      def func(*args):  # Any number of positional")
    print("• **kwargs:   def func(**kwargs):  # Any number of keyword")
    print("• Lambda:     lambda x: x * 2")
    print("• Decorator:  @decorator above function")
    print("• Private:    def _helper():  # Internal use")
    print("="*80)