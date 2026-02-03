"""
================================================================================
                    ONLINE BANKING TRANSACTION SYSTEM
================================================================================

DETAILED PROBLEM STATEMENT:
---------------------------
Create a comprehensive Online Banking Transaction System that handles various
banking operations while properly managing errors and exceptions. The system
must ensure data integrity, security, and reliability through robust exception
handling mechanisms.

BUSINESS CONTEXT:
-----------------
A bank's online system processes thousands of transactions daily. Any error
in transaction processing can result in:
- Financial losses
- Customer dissatisfaction
- Data corruption
- Security breaches
- System crashes

Therefore, EVERY operation must have proper error handling to:
1. Catch and handle errors gracefully
2. Maintain data consistency
3. Provide clear error messages to users
4. Log errors for audit trails
5. Ensure resources are properly released
6. Allow operations to continue after errors

REQUIREMENTS - EXCEPTION HANDLING CONCEPTS:
-------------------------------------------

1. try-except BLOCK:
   - Catches and handles exceptions
   - Prevents program crashes
   - Example: try to withdraw money, catch insufficient funds error

2. try-except-else BLOCK:
   - else executes ONLY if NO exception occurred
   - Used for code that should run only on success
   - Example: Update transaction log only if transfer succeeds

3. try-except-finally BLOCK:
   - finally ALWAYS executes (success or failure)
   - Used for cleanup: close files, release locks, save data
   - Example: Always close database connection

4. COMPLETE STRUCTURE (try-except-else-finally):
   - Combines all blocks for comprehensive handling
   - Provides full control over exception flow

5. MULTIPLE except BLOCKS:
   - Catch different exception types separately
   - Provide specific error handling for each type
   - Example: ValueError, TypeError, ZeroDivisionError

6. EXCEPTION HIERARCHY:
   - Catch specific exceptions before general ones
   - Use base Exception class carefully

7. RAISING EXCEPTIONS:
   - raise keyword to trigger exceptions
   - Create custom validation errors
   - Example: raise ValueError("Invalid amount")

8. CUSTOM EXCEPTIONS:
   - Define your own exception classes
   - Better error categorization
   - Example: InsufficientFundsError, AccountFrozenError

REAL-WORLD SCENARIOS COVERED:
-----------------------------
1. Money Transfer - Handle insufficient funds, invalid accounts
2. ATM Withdrawal - Handle network errors, card issues
3. File Operations - Handle missing files, permissions
4. Data Validation - Handle invalid input, format errors
5. Database Operations - Handle connection errors, timeouts
6. API Calls - Handle network failures, timeouts

LEARNING OBJECTIVES:
-------------------
By the end of this program, you will understand:
• When and why to use exception handling
• Difference between try-except, else, and finally
• How to catch specific exception types
• How to create and raise custom exceptions
• Best practices for error handling
• How to maintain code reliability

================================================================================
"""

import time
import random
from datetime import datetime

# ============================================================================
# CUSTOM EXCEPTIONS
# ============================================================================

class InsufficientFundsError(Exception):
    """Raised when account has insufficient balance for transaction."""
    pass

class AccountNotFoundError(Exception):
    """Raised when account number doesn't exist."""
    pass

class AccountFrozenError(Exception):
    """Raised when trying to access a frozen account."""
    pass

class InvalidAmountError(Exception):
    """Raised when transaction amount is invalid."""
    pass

class DailyLimitExceededError(Exception):
    """Raised when daily transaction limit is exceeded."""
    pass

class NetworkError(Exception):
    """Raised when network connection fails."""
    pass

# ============================================================================
# GLOBAL DATA (Simulated Database)
# ============================================================================

ACCOUNTS = {
    "ACC001": {"name": "Alice Johnson", "balance": 5000.00, "frozen": False, "daily_withdrawn": 0},
    "ACC002": {"name": "Bob Smith", "balance": 2500.00, "frozen": False, "daily_withdrawn": 0},
    "ACC003": {"name": "Charlie Brown", "balance": 100.00, "frozen": True, "daily_withdrawn": 0},
    "ACC004": {"name": "David Lee", "balance": 10000.00, "frozen": False, "daily_withdrawn": 0},
}

TRANSACTION_LOG = []
DAILY_WITHDRAWAL_LIMIT = 3000.00

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def show_section_header(section_number, title):
    """Display formatted section header."""
    print("\n" + "="*80)
    print(f"SECTION {section_number}: {title}")
    print("="*80)

def log_transaction(transaction_type, account, amount, status, error=None):
    """Log transaction for audit trail."""
    log_entry = {
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'type': transaction_type,
        'account': account,
        'amount': amount,
        'status': status,
        'error': error
    }
    TRANSACTION_LOG.append(log_entry)

# ============================================================================
# SECTION 1: BASIC try-except
# ============================================================================

def basic_try_except():
    """
    Demonstrate basic try-except block.
    
    CONCEPT: try-except catches exceptions and prevents crashes
    
    Structure:
        try:
            # Code that might raise exception
        except ExceptionType:
            # Handle the exception
    """
    
    show_section_header(1, "BASIC try-except BLOCK")
    print("\nProblem: Divide numbers safely without crashes")
    print("Concept: Catch ZeroDivisionError to prevent program crash")
    print("-"*80)
    
    # Example 1: Division without exception handling (would crash)
    print("\n📌 Example 1: Division with Exception Handling")
    print("-"*80)
    
    numbers = [(10, 2), (15, 3), (20, 0), (25, 5)]
    
    for numerator, denominator in numbers:
        try:
            # Code that might raise exception
            result = numerator / denominator
            print(f"✓ {numerator} / {denominator} = {result}")
        
        except ZeroDivisionError:
            # Handle division by zero
            print(f"✗ Error: Cannot divide {numerator} by zero!")
    
    print("\n✓ Program continues running despite errors!")
    
    # Example 2: Convert string to integer
    print("\n📌 Example 2: Safe Type Conversion")
    print("-"*80)
    
    inputs = ["123", "456", "abc", "789", "xyz"]
    
    for user_input in inputs:
        try:
            number = int(user_input)
            print(f"✓ Converted '{user_input}' to {number}")
        
        except ValueError:
            print(f"✗ Error: '{user_input}' is not a valid number!")
    
    print("\n✓ All inputs processed without crash!")

# ============================================================================
# SECTION 2: MULTIPLE except BLOCKS
# ============================================================================

def multiple_except_blocks():
    """
    Demonstrate multiple except blocks for different exception types.
    
    CONCEPT: Catch different exceptions separately for specific handling
    
    Structure:
        try:
            # Code
        except ExceptionType1:
            # Handle type 1
        except ExceptionType2:
            # Handle type 2
        except ExceptionType3:
            # Handle type 3
    """
    
    show_section_header(2, "MULTIPLE except BLOCKS")
    print("\nProblem: Handle different types of errors specifically")
    print("Concept: Each exception type gets appropriate handling")
    print("-"*80)
    
    print("\n📌 Example: Account Balance Inquiry")
    print("-"*80)
    
    test_cases = [
        ("ACC001", "100"),      # Valid
        ("ACC999", "200"),      # Invalid account
        ("ACC002", "abc"),      # Invalid amount format
        ("ACC001", "0"),        # Zero amount
    ]
    
    for account_id, amount_str in test_cases:
        print(f"\n→ Processing: Account={account_id}, Amount={amount_str}")
        
        try:
            # Step 1: Validate account exists
            if account_id not in ACCOUNTS:
                raise AccountNotFoundError(f"Account {account_id} not found")
            
            # Step 2: Convert amount to float
            amount = float(amount_str)
            
            # Step 3: Validate amount
            if amount <= 0:
                raise InvalidAmountError("Amount must be greater than zero")
            
            # Step 4: Check balance
            account = ACCOUNTS[account_id]
            if amount > account['balance']:
                raise InsufficientFundsError(
                    f"Insufficient funds. Balance: ${account['balance']:.2f}"
                )
            
            print(f"  ✓ Validation successful!")
            print(f"  Account: {account['name']}")
            print(f"  Balance: ${account['balance']:.2f}")
        
        except AccountNotFoundError as e:
            print(f"  ✗ Account Error: {e}")
        
        except ValueError as e:
            print(f"  ✗ Format Error: Invalid amount format '{amount_str}'")
        
        except InvalidAmountError as e:
            print(f"  ✗ Amount Error: {e}")
        
        except InsufficientFundsError as e:
            print(f"  ✗ Balance Error: {e}")
        
        except Exception as e:
            print(f"  ✗ Unexpected Error: {e}")
    
    print("\n✓ Different error types handled appropriately!")

# ============================================================================
# SECTION 3: try-except-else BLOCK
# ============================================================================

def try_except_else_block():
    """
    Demonstrate try-except-else block.
    
    CONCEPT: else block executes ONLY if NO exception occurred
    
    Structure:
        try:
            # Code that might raise exception
        except ExceptionType:
            # Handle exception
        else:
            # Executes ONLY if try succeeds (no exception)
            # Used for code that depends on try succeeding
    """
    
    show_section_header(3, "try-except-else BLOCK")
    print("\nProblem: Execute success actions only when no errors occur")
    print("Concept: else block runs ONLY if try block succeeds")
    print("-"*80)
    
    print("\n📌 Example: Money Transfer with Success Notification")
    print("-"*80)
    
    transfers = [
        ("ACC001", "ACC002", 500.00),   # Valid transfer
        ("ACC002", "ACC001", 5000.00),  # Insufficient funds
        ("ACC999", "ACC001", 100.00),   # Invalid account
    ]
    
    for from_acc, to_acc, amount in transfers:
        print(f"\n→ Transfer ${amount:.2f}: {from_acc} → {to_acc}")
        
        try:
            # Validate source account
            if from_acc not in ACCOUNTS:
                raise AccountNotFoundError(f"Source account {from_acc} not found")
            
            # Validate destination account
            if to_acc not in ACCOUNTS:
                raise AccountNotFoundError(f"Destination account {to_acc} not found")
            
            # Check balance
            if ACCOUNTS[from_acc]['balance'] < amount:
                raise InsufficientFundsError(
                    f"Insufficient funds in {from_acc}. "
                    f"Balance: ${ACCOUNTS[from_acc]['balance']:.2f}"
                )
            
            # Perform transfer
            ACCOUNTS[from_acc]['balance'] -= amount
            ACCOUNTS[to_acc]['balance'] += amount
            
            print(f"  ✓ Transfer successful!")
        
        except AccountNotFoundError as e:
            print(f"  ✗ Error: {e}")
            log_transaction("TRANSFER", from_acc, amount, "FAILED", str(e))
        
        except InsufficientFundsError as e:
            print(f"  ✗ Error: {e}")
            log_transaction("TRANSFER", from_acc, amount, "FAILED", str(e))
        
        else:
            # This runs ONLY if transfer succeeded (no exception)
            print(f"  ✓ Notification sent to both parties")
            print(f"  ✓ Transaction logged")
            print(f"  ✓ New balance {from_acc}: ${ACCOUNTS[from_acc]['balance']:.2f}")
            print(f"  ✓ New balance {to_acc}: ${ACCOUNTS[to_acc]['balance']:.2f}")
            log_transaction("TRANSFER", from_acc, amount, "SUCCESS")
    
    print("\n✓ else block executed only for successful transfers!")

# ============================================================================
# SECTION 4: try-except-finally BLOCK
# ============================================================================

def try_except_finally_block():
    """
    Demonstrate try-except-finally block.
    
    CONCEPT: finally block ALWAYS executes (success or failure)
    
    Structure:
        try:
            # Code that might raise exception
        except ExceptionType:
            # Handle exception
        finally:
            # ALWAYS executes (cleanup code)
            # Used for: closing files, releasing resources, saving data
    """
    
    show_section_header(4, "try-except-finally BLOCK")
    print("\nProblem: Ensure cleanup happens regardless of success/failure")
    print("Concept: finally ALWAYS executes - perfect for cleanup")
    print("-"*80)
    
    print("\n📌 Example 1: File Operations with Guaranteed Cleanup")
    print("-"*80)
    
    # Simulate file operations
    filenames = ["transaction_log.txt", "nonexistent.txt"]
    
    for filename in filenames:
        print(f"\n→ Processing file: {filename}")
        file = None
        
        try:
            # Try to open file
            print(f"  → Opening {filename}...")
            
            if filename == "nonexistent.txt":
                raise FileNotFoundError(f"File {filename} not found")
            
            # Simulate file operations
            print(f"  → Reading {filename}...")
            print(f"  ✓ File processed successfully")
            file = "opened"  # Simulate file handle
        
        except FileNotFoundError as e:
            print(f"  ✗ Error: {e}")
        
        finally:
            # This ALWAYS executes
            if file:
                print(f"  → Closing {filename} (cleanup)")
            print(f"  ✓ Cleanup completed for {filename}")
    
    print("\n📌 Example 2: Database Connection with Guaranteed Closure")
    print("-"*80)
    
    operations = [
        ("Connect and query successfully", False),
        ("Connect but query fails", True)
    ]
    
    for operation, should_fail in operations:
        print(f"\n→ {operation}")
        connection = None
        
        try:
            # Simulate database connection
            print(f"  → Opening database connection...")
            connection = "CONNECTED"
            
            print(f"  → Executing query...")
            
            if should_fail:
                raise NetworkError("Database connection lost")
            
            print(f"  ✓ Query executed successfully")
        
        except NetworkError as e:
            print(f"  ✗ Error: {e}")
        
        finally:
            # ALWAYS close connection (even if error occurred)
            if connection:
                print(f"  → Closing database connection (cleanup)")
            print(f"  ✓ Connection cleanup completed")
    
    print("\n✓ finally block ensured cleanup in ALL cases!")

# ============================================================================
# SECTION 5: COMPLETE STRUCTURE (try-except-else-finally)
# ============================================================================

def complete_exception_structure():
    """
    Demonstrate complete exception handling structure.
    
    CONCEPT: Combine all blocks for comprehensive control
    
    Structure:
        try:
            # Code that might raise exception
        except ExceptionType:
            # Handle exception
        else:
            # Runs ONLY if no exception (success actions)
        finally:
            # ALWAYS runs (cleanup)
    
    Execution Flow:
    - If NO exception: try → else → finally
    - If exception: try → except → finally
    """
    
    show_section_header(5, "COMPLETE STRUCTURE (try-except-else-finally)")
    print("\nProblem: Comprehensive transaction processing with full control")
    print("Concept: All blocks working together")
    print("-"*80)
    
    print("\n📌 Example: ATM Withdrawal with Complete Error Handling")
    print("-"*80)
    
    withdrawals = [
        ("ACC001", 1000.00),   # Success
        ("ACC002", 5000.00),   # Insufficient funds
        ("ACC003", 500.00),    # Frozen account
        ("ACC004", 3500.00),   # Exceeds daily limit
    ]
    
    for account_id, amount in withdrawals:
        print(f"\n{'='*70}")
        print(f"→ ATM WITHDRAWAL: {account_id} - ${amount:.2f}")
        print(f"{'='*70}")
        
        atm_session = None
        transaction_id = None
        
        try:
            # Step 1: Start ATM session
            print(f"  [TRY] Starting ATM session...")
            atm_session = f"SESSION-{random.randint(1000, 9999)}"
            print(f"  [TRY] Session ID: {atm_session}")
            
            # Step 2: Validate account
            print(f"  [TRY] Validating account {account_id}...")
            if account_id not in ACCOUNTS:
                raise AccountNotFoundError(f"Account {account_id} not found")
            
            account = ACCOUNTS[account_id]
            
            # Step 3: Check if account is frozen
            if account['frozen']:
                raise AccountFrozenError(
                    f"Account {account_id} is frozen. Contact bank."
                )
            
            # Step 4: Validate amount
            if amount <= 0:
                raise InvalidAmountError("Withdrawal amount must be positive")
            
            # Step 5: Check balance
            if amount > account['balance']:
                raise InsufficientFundsError(
                    f"Insufficient funds. Balance: ${account['balance']:.2f}, "
                    f"Requested: ${amount:.2f}"
                )
            
            # Step 6: Check daily limit
            if account['daily_withdrawn'] + amount > DAILY_WITHDRAWAL_LIMIT:
                remaining = DAILY_WITHDRAWAL_LIMIT - account['daily_withdrawn']
                raise DailyLimitExceededError(
                    f"Daily limit exceeded. Remaining limit: ${remaining:.2f}"
                )
            
            # Step 7: Process withdrawal
            print(f"  [TRY] Processing withdrawal...")
            account['balance'] -= amount
            account['daily_withdrawn'] += amount
            transaction_id = f"TXN-{random.randint(10000, 99999)}"
            
            print(f"  [TRY] ✓ Withdrawal successful!")
        
        except AccountNotFoundError as e:
            print(f"  [EXCEPT] ✗ Account Error: {e}")
            log_transaction("WITHDRAWAL", account_id, amount, "FAILED", str(e))
        
        except AccountFrozenError as e:
            print(f"  [EXCEPT] ✗ Security Error: {e}")
            log_transaction("WITHDRAWAL", account_id, amount, "BLOCKED", str(e))
        
        except InvalidAmountError as e:
            print(f"  [EXCEPT] ✗ Validation Error: {e}")
            log_transaction("WITHDRAWAL", account_id, amount, "INVALID", str(e))
        
        except InsufficientFundsError as e:
            print(f"  [EXCEPT] ✗ Balance Error: {e}")
            log_transaction("WITHDRAWAL", account_id, amount, "INSUFFICIENT", str(e))
        
        except DailyLimitExceededError as e:
            print(f"  [EXCEPT] ✗ Limit Error: {e}")
            log_transaction("WITHDRAWAL", account_id, amount, "LIMIT_EXCEEDED", str(e))
        
        else:
            # Executes ONLY if withdrawal succeeded
            print(f"\n  [ELSE] SUCCESS ACTIONS:")
            print(f"  [ELSE] → Dispensing cash: ${amount:.2f}")
            print(f"  [ELSE] → Printing receipt (Transaction: {transaction_id})")
            print(f"  [ELSE] → Sending SMS notification")
            print(f"  [ELSE] → New balance: ${account['balance']:.2f}")
            print(f"  [ELSE] → Daily withdrawn: ${account['daily_withdrawn']:.2f}")
            log_transaction("WITHDRAWAL", account_id, amount, "SUCCESS")
        
        finally:
            # ALWAYS executes (cleanup)
            print(f"\n  [FINALLY] CLEANUP:")
            if atm_session:
                print(f"  [FINALLY] → Closing ATM session {atm_session}")
            print(f"  [FINALLY] → Releasing card")
            print(f"  [FINALLY] → Clearing screen")
            print(f"  [FINALLY] ✓ ATM ready for next customer")
    
    print("\n" + "="*80)
    print("✓ Complete structure provides full control over exception flow!")
    print("✓ Try → Except → Else → Finally executed in proper order!")

# ============================================================================
# SECTION 6: RAISING EXCEPTIONS
# ============================================================================

def raising_exceptions():
    """
    Demonstrate raising exceptions with raise keyword.
    
    CONCEPT: Trigger exceptions intentionally for validation
    
    Syntax:
        raise ExceptionType("Error message")
    
    Use cases:
    - Input validation
    - Business rule enforcement
    - Error propagation
    """
    
    show_section_header(6, "RAISING EXCEPTIONS")
    print("\nProblem: Validate inputs and enforce business rules")
    print("Concept: Use 'raise' to trigger exceptions")
    print("-"*80)
    
    def validate_transfer(from_acc, to_acc, amount):
        """Validate transfer with multiple checks - raises exceptions."""
        
        # Check 1: Validate amount
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        
        if amount <= 0:
            raise InvalidAmountError("Amount must be greater than zero")
        
        if amount > 50000:
            raise InvalidAmountError("Amount exceeds maximum transfer limit ($50,000)")
        
        # Check 2: Validate accounts
        if from_acc not in ACCOUNTS:
            raise AccountNotFoundError(f"Source account {from_acc} not found")
        
        if to_acc not in ACCOUNTS:
            raise AccountNotFoundError(f"Destination account {to_acc} not found")
        
        # Check 3: Same account check
        if from_acc == to_acc:
            raise InvalidAmountError("Cannot transfer to same account")
        
        # Check 4: Frozen account check
        if ACCOUNTS[from_acc]['frozen']:
            raise AccountFrozenError(f"Source account {from_acc} is frozen")
        
        if ACCOUNTS[to_acc]['frozen']:
            raise AccountFrozenError(f"Destination account {to_acc} is frozen")
        
        # Check 5: Balance check
        if ACCOUNTS[from_acc]['balance'] < amount:
            raise InsufficientFundsError(
                f"Insufficient funds in {from_acc}. "
                f"Available: ${ACCOUNTS[from_acc]['balance']:.2f}"
            )
        
        return True
    
    print("\n📌 Example: Transfer Validation")
    print("-"*80)
    
    test_transfers = [
        ("ACC001", "ACC002", 1000.00),      # Valid
        ("ACC001", "ACC002", "invalid"),    # TypeError
        ("ACC001", "ACC002", -500.00),      # Negative amount
        ("ACC001", "ACC001", 100.00),       # Same account
        ("ACC999", "ACC002", 100.00),       # Invalid account
        ("ACC001", "ACC003", 100.00),       # Frozen account
        ("ACC002", "ACC001", 10000.00),     # Insufficient funds
        ("ACC001", "ACC002", 60000.00),     # Exceeds limit
    ]
    
    for from_acc, to_acc, amount in test_transfers:
        print(f"\n→ Validating: {from_acc} → {to_acc}, Amount: {amount}")
        
        try:
            validate_transfer(from_acc, to_acc, amount)
            print(f"  ✓ Validation passed!")
        
        except TypeError as e:
            print(f"  ✗ Type Error: {e}")
        
        except InvalidAmountError as e:
            print(f"  ✗ Amount Error: {e}")
        
        except AccountNotFoundError as e:
            print(f"  ✗ Account Error: {e}")
        
        except AccountFrozenError as e:
            print(f"  ✗ Security Error: {e}")
        
        except InsufficientFundsError as e:
            print(f"  ✗ Balance Error: {e}")
    
    print("\n✓ Raising exceptions allows validation at any point!")

# ============================================================================
# SECTION 7: CUSTOM EXCEPTIONS
# ============================================================================

def custom_exceptions_demo():
    """
    Demonstrate custom exception classes.
    
    CONCEPT: Create your own exception types
    
    Benefits:
    - Better error categorization
    - More meaningful error messages
    - Easier to catch specific errors
    """
    
    show_section_header(7, "CUSTOM EXCEPTIONS")
    print("\nProblem: Create specific exception types for banking operations")
    print("Concept: Define custom exception classes")
    print("-"*80)
    
    print("\n📌 Custom Exception Classes Defined:")
    print("-"*80)
    print("""
    class InsufficientFundsError(Exception):
        \"\"\"Raised when account has insufficient balance.\"\"\"
        pass
    
    class AccountNotFoundError(Exception):
        \"\"\"Raised when account doesn't exist.\"\"\"
        pass
    
    class AccountFrozenError(Exception):
        \"\"\"Raised when account is frozen.\"\"\"
        pass
    
    class InvalidAmountError(Exception):
        \"\"\"Raised when amount is invalid.\"\"\"
        pass
    
    class DailyLimitExceededError(Exception):
        \"\"\"Raised when daily limit is exceeded.\"\"\"
        pass
    """)
    
    print("\n📌 Example: Using Custom Exceptions")
    print("-"*80)
    
    def process_transaction(account_id, transaction_type, amount):
        """Process transaction using custom exceptions."""
        
        if account_id not in ACCOUNTS:
            raise AccountNotFoundError(
                f"Account {account_id} does not exist in our system"
            )
        
        account = ACCOUNTS[account_id]
        
        if account['frozen']:
            raise AccountFrozenError(
                f"Account {account_id} is frozen. "
                f"Please contact customer service at 1-800-BANK"
            )
        
        if amount <= 0:
            raise InvalidAmountError(
                f"Transaction amount must be positive. Received: ${amount}"
            )
        
        if transaction_type == "withdrawal":
            if amount > account['balance']:
                raise InsufficientFundsError(
                    f"Cannot withdraw ${amount:.2f}. "
                    f"Current balance: ${account['balance']:.2f}. "
                    f"Shortfall: ${amount - account['balance']:.2f}"
                )
        
        return True
    
    transactions = [
        ("ACC001", "withdrawal", 100.00),    # Success
        ("ACC999", "withdrawal", 50.00),     # Account not found
        ("ACC003", "withdrawal", 50.00),     # Frozen
        ("ACC001", "withdrawal", -50.00),    # Invalid amount
        ("ACC002", "withdrawal", 10000.00),  # Insufficient
    ]
    
    for account, trans_type, amount in transactions:
        print(f"\n→ Transaction: {trans_type.upper()} from {account} - ${amount:.2f}")
        
        try:
            process_transaction(account, trans_type, amount)
            print(f"  ✓ Transaction approved!")
        
        except AccountNotFoundError as e:
            print(f"  ✗ ACCOUNT ERROR: {e}")
            print(f"     Action: Please verify account number")
        
        except AccountFrozenError as e:
            print(f"  ✗ SECURITY ALERT: {e}")
            print(f"     Action: Contact customer service")
        
        except InvalidAmountError as e:
            print(f"  ✗ INPUT ERROR: {e}")
            print(f"     Action: Enter valid amount")
        
        except InsufficientFundsError as e:
            print(f"  ✗ BALANCE ERROR: {e}")
            print(f"     Action: Deposit funds or reduce amount")
    
    print("\n✓ Custom exceptions provide clear, specific error information!")

# ============================================================================
# SECTION 8: PRACTICAL APPLICATION
# ============================================================================

def practical_application():
    """
    Comprehensive real-world example using all concepts.
    
    Demonstrates:
    - Multiple exception types
    - try-except-else-finally
    - Custom exceptions
    - Error logging
    - Resource cleanup
    """
    
    show_section_header(8, "PRACTICAL APPLICATION - COMPLETE TRANSACTION")
    print("\nProblem: Process complex multi-step transaction safely")
    print("Concept: All exception handling techniques combined")
    print("-"*80)
    
    def process_payment_with_invoice(from_account, to_account, amount, 
                                     invoice_number):
        """
        Process payment with comprehensive error handling.
        
        Steps:
        1. Validate all inputs
        2. Check account statuses
        3. Create invoice file
        4. Process payment
        5. Update invoice
        6. Send notifications
        7. Cleanup resources
        """
        
        print(f"\n{'='*70}")
        print(f"PROCESSING PAYMENT")
        print(f"{'='*70}")
        print(f"From: {from_account}")
        print(f"To: {to_account}")
        print(f"Amount: ${amount:.2f}")
        print(f"Invoice: {invoice_number}")
        print(f"{'='*70}")
        
        invoice_file = None
        payment_processed = False
        
        try:
            # Step 1: Validate inputs
            print(f"\n[STEP 1] Validating inputs...")
            if not all([from_account, to_account, amount, invoice_number]):
                raise ValueError("All fields are required")
            
            if amount <= 0:
                raise InvalidAmountError("Payment amount must be positive")
            
            print(f"  ✓ Inputs validated")
            
            # Step 2: Check accounts
            print(f"\n[STEP 2] Checking accounts...")
            if from_account not in ACCOUNTS:
                raise AccountNotFoundError(f"Payer account {from_account} not found")
            
            if to_account not in ACCOUNTS:
                raise AccountNotFoundError(f"Payee account {to_account} not found")
            
            payer = ACCOUNTS[from_account]
            payee = ACCOUNTS[to_account]
            
            if payer['frozen']:
                raise AccountFrozenError(f"Payer account {from_account} is frozen")
            
            if payer['balance'] < amount:
                raise InsufficientFundsError(
                    f"Insufficient funds. Required: ${amount:.2f}, "
                    f"Available: ${payer['balance']:.2f}"
                )
            
            print(f"  ✓ Accounts verified")
            
            # Step 3: Create invoice file
            print(f"\n[STEP 3] Creating invoice...")
            invoice_file = f"invoice_{invoice_number}.txt"
            print(f"  ✓ Invoice file created: {invoice_file}")
            
            # Step 4: Process payment
            print(f"\n[STEP 4] Processing payment...")
            time.sleep(0.1)  # Simulate processing
            payer['balance'] -= amount
            payee['balance'] += amount
            payment_processed = True
            print(f"  ✓ Payment processed successfully")
            
            # Step 5: Update invoice
            print(f"\n[STEP 5] Updating invoice...")
            print(f"  ✓ Invoice updated with payment details")
        
        except ValueError as e:
            print(f"\n✗ INPUT ERROR: {e}")
            return False
        
        except InvalidAmountError as e:
            print(f"\n✗ AMOUNT ERROR: {e}")
            return False
        
        except AccountNotFoundError as e:
            print(f"\n✗ ACCOUNT ERROR: {e}")
            return False
        
        except AccountFrozenError as e:
            print(f"\n✗ SECURITY ERROR: {e}")
            return False
        
        except InsufficientFundsError as e:
            print(f"\n✗ BALANCE ERROR: {e}")
            return False
        
        except Exception as e:
            print(f"\n✗ UNEXPECTED ERROR: {e}")
            # Rollback if payment was processed
            if payment_processed:
                print(f"\n[ROLLBACK] Reversing payment...")
                payer['balance'] += amount
                payee['balance'] -= amount
                print(f"  ✓ Payment reversed")
            return False
        
        else:
            # Execute only if payment succeeded
            print(f"\n[SUCCESS] Payment completed successfully!")
            print(f"\n[NOTIFICATIONS]:")
            print(f"  → Email sent to {payer['name']}")
            print(f"  → Email sent to {payee['name']}")
            print(f"  → SMS confirmation sent")
            
            print(f"\n[BALANCES]:")
            print(f"  {from_account}: ${payer['balance']:.2f}")
            print(f"  {to_account}: ${payee['balance']:.2f}")
            
            return True
        
        finally:
            # Always execute cleanup
            print(f"\n[CLEANUP]:")
            if invoice_file:
                print(f"  → Saving invoice file: {invoice_file}")
            print(f"  → Logging transaction")
            print(f"  → Releasing resources")
            print(f"  ✓ Cleanup completed")
    
    # Test cases
    print("\n📌 Test Case 1: Successful Payment")
    process_payment_with_invoice("ACC001", "ACC002", 500.00, "INV-001")
    
    print("\n\n📌 Test Case 2: Insufficient Funds")
    process_payment_with_invoice("ACC002", "ACC001", 10000.00, "INV-002")
    
    print("\n\n📌 Test Case 3: Frozen Account")
    process_payment_with_invoice("ACC003", "ACC001", 50.00, "INV-003")
    
    print("\n" + "="*80)
    print("✓ Practical application demonstrates robust error handling!")

# ============================================================================
# SECTION 9: BEST PRACTICES
# ============================================================================

def best_practices():
    """Demonstrate exception handling best practices."""
    
    show_section_header(9, "EXCEPTION HANDLING BEST PRACTICES")
    print("\nKey principles for effective exception handling")
    print("-"*80)
    
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                    EXCEPTION HANDLING BEST PRACTICES                       ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  1. CATCH SPECIFIC EXCEPTIONS FIRST                                        ║
║     ✓ except ValueError:        # Specific                                ║
║     ✓ except TypeError:         # Specific                                ║
║     ✓ except Exception:         # General (last)                          ║
║                                                                            ║
║     ✗ Don't catch Exception first - hides specific errors                 ║
║                                                                            ║
║  2. USE ELSE FOR SUCCESS LOGIC                                             ║
║     ✓ Put success-dependent code in else block                            ║
║     ✗ Don't put it in try - makes error handling unclear                  ║
║                                                                            ║
║  3. USE FINALLY FOR CLEANUP                                                ║
║     ✓ Close files, connections, release resources                         ║
║     ✓ Always runs regardless of success/failure                           ║
║                                                                            ║
║  4. CREATE CUSTOM EXCEPTIONS                                               ║
║     ✓ Makes error handling more specific                                  ║
║     ✓ Provides better error messages                                      ║
║     ✓ Easier to maintain                                                  ║
║                                                                            ║
║  5. DON'T CATCH EVERYTHING                                                 ║
║     ✗ except: (bare except)                                               ║
║     ✓ except Exception as e: (at minimum)                                 ║
║                                                                            ║
║  6. INCLUDE ERROR MESSAGES                                                 ║
║     ✓ raise ValueError("Amount must be positive")                         ║
║     ✗ raise ValueError()  # No context                                    ║
║                                                                            ║
║  7. LOG ERRORS                                                             ║
║     ✓ Keep audit trail for debugging                                      ║
║     ✓ Include timestamp, user, operation                                  ║
║                                                                            ║
║  8. DON'T SILENCE ERRORS                                                   ║
║     ✗ except: pass  # Silent failure - very bad!                          ║
║     ✓ Always handle or log                                                ║
║                                                                            ║
║  9. USE CONTEXT MANAGERS (with statement)                                  ║
║     ✓ with open('file') as f:                                             ║
║       Automatically handles cleanup                                        ║
║                                                                            ║
║  10. FAIL FAST                                                             ║
║      ✓ Validate inputs early                                              ║
║      ✓ Raise exceptions immediately on invalid data                       ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)

# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Main program demonstrating all exception handling concepts."""
    
    print("="*80)
    print(" "*20 + "ONLINE BANKING TRANSACTION SYSTEM")
    print(" "*15 + "Comprehensive Exception Handling Demo")
    print("="*80)
    
    # Run all sections
    basic_try_except()
    
    multiple_except_blocks()
    
    try_except_else_block()
    
    try_except_finally_block()
    
    complete_exception_structure()
    
    raising_exceptions()
    
    custom_exceptions_demo()
    
    practical_application()
    
    best_practices()
    
    # Final Summary
    print("\n" + "="*80)
    print("COMPREHENSIVE SUMMARY")
    print("="*80)
    
    summary = """
╔════════════════════════════════════════════════════════════════════════════╗
║                   EXCEPTION HANDLING CONCEPTS COVERED                      ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  1. try-except BLOCK                                                       ║
║     • Catches exceptions to prevent crashes                               ║
║     • Basic error handling                                                ║
║                                                                            ║
║  2. MULTIPLE except BLOCKS                                                 ║
║     • Handle different exception types separately                         ║
║     • Specific error handling                                             ║
║                                                                            ║
║  3. try-except-else BLOCK                                                  ║
║     • else runs ONLY if no exception                                      ║
║     • For success-dependent code                                          ║
║                                                                            ║
║  4. try-except-finally BLOCK                                               ║
║     • finally ALWAYS runs                                                 ║
║     • Perfect for cleanup (close files, connections)                      ║
║                                                                            ║
║  5. COMPLETE STRUCTURE                                                     ║
║     • try-except-else-finally together                                    ║
║     • Full control over exception flow                                    ║
║                                                                            ║
║  6. RAISING EXCEPTIONS                                                     ║
║     • raise keyword to trigger exceptions                                 ║
║     • Input validation and business rules                                 ║
║                                                                            ║
║  7. CUSTOM EXCEPTIONS                                                      ║
║     • Define your own exception classes                                   ║
║     • Better error categorization                                         ║
║                                                                            ║
║  EXECUTION FLOW:                                                           ║
║  ─────────────────────────────────────────────────────────────────────    ║
║  If NO exception:    try → else → finally                                 ║
║  If exception:       try → except → finally                               ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """
    print(summary)
    
    print("\n" + "="*80)
    print("PROGRAM COMPLETED SUCCESSFULLY!")
    print("="*80)
    
    print("\n✅ Covered 9 comprehensive sections")
    print("✅ Demonstrated 30+ exception handling examples")
    print("✅ Showed real-world banking scenarios")
    
    print("\n🎯 KEY TAKEAWAYS:")
    print("   1. Always use try-except to handle potential errors")
    print("   2. Catch specific exceptions before general ones")
    print("   3. Use else for success-only code")
    print("   4. Use finally for cleanup (ALWAYS runs)")
    print("   5. Create custom exceptions for better clarity")
    print("   6. Never silence exceptions with empty except")
    print("   7. Include meaningful error messages")
    print("   8. Log errors for debugging and audit")
    print("   9. Validate inputs early (fail fast)")
    print("   10. Exception handling = Robust, reliable code")
    
    print("\n📊 TRANSACTION LOG SUMMARY:")
    print("-"*80)
    print(f"Total transactions logged: {len(TRANSACTION_LOG)}")
    
    success_count = sum(1 for t in TRANSACTION_LOG if t['status'] == 'SUCCESS')
    failed_count = len(TRANSACTION_LOG) - success_count
    
    print(f"Successful: {success_count}")
    print(f"Failed: {failed_count}")
    
    print("\n" + "="*80)

if __name__ == "__main__":
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║              ONLINE BANKING TRANSACTION SYSTEM                             ║
║              Exception Handling Comprehensive Demo                         ║
║                                                                            ║
║  This program demonstrates ALL exception handling concepts:                ║
║                                                                            ║
║  ✓ try-except          ✓ Multiple except blocks                           ║
║  ✓ try-except-else     ✓ try-except-finally                               ║
║  ✓ Complete structure  ✓ Raising exceptions                               ║
║  ✓ Custom exceptions   ✓ Best practices                                   ║
║                                                                            ║
║  Total: 30+ examples in real banking context!                             ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)
    
    main()
    
    print("\n\n💡 QUICK REFERENCE:")
    print("="*80)
    print("• Basic:     try: code  except Exception: handle")
    print("• Multiple:  except ValueError: ... except TypeError: ...")
    print("• With else: try: code  except: handle  else: success_code")
    print("• Cleanup:   try: code  except: handle  finally: cleanup")
    print("• Complete:  try: code  except: handle  else: success  finally: cleanup")
    print("• Raise:     raise ValueError('Error message')")
    print("• Custom:    class MyError(Exception): pass")
    print("="*80)