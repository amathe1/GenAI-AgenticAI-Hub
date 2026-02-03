"""
================================================================================
                    LIBRARY BOOK MANAGEMENT SYSTEM
================================================================================

DETAILED PROBLEM STATEMENT:
---------------------------
Create a Library Book Management System that manages book inventory, processes
student requests, handles book searches, and generates reports. The system
demonstrates the use of for loops, while loops, break, continue, and pass
statements in various real-world scenarios.

REQUIREMENTS:
-------------

1. BOOK INVENTORY MANAGEMENT (for loop):
   - Display all available books in the library
   - Calculate total books and books by category
   - Generate inventory report

2. BOOK SEARCH SYSTEM (for loop with break):
   - Search for a specific book by ISBN
   - Stop searching once book is found (break statement)
   - Display search results

3. OVERDUE BOOK CHECKER (for loop with continue):
   - Check all borrowed books
   - Skip books that are not overdue (continue statement)
   - Display only overdue books

4. STUDENT REQUEST PROCESSOR (while loop):
   - Process multiple student book requests
   - Continue until valid input received
   - Handle invalid requests

5. BOOK ISSUING SYSTEM (while loop with break):
   - Issue books to students
   - Stop when daily limit reached (break statement)
   - Track issued books

6. REPORT GENERATION (for loop with pass):
   - Generate various reports
   - Use pass for placeholder sections not yet implemented
   - Show future implementation plans

LEARNING OBJECTIVES:
-------------------
• for loop: Iterate through collections (lists, dictionaries)
• while loop: Continue until condition is false
• break: Exit loop immediately when condition is met
• continue: Skip current iteration and move to next
• pass: Placeholder for future code (does nothing)

================================================================================
"""

import datetime

def main():
    print("="*80)
    print(" "*25 + "LIBRARY BOOK MANAGEMENT SYSTEM")
    print("="*80)
    
    # ========================================================================
    # SAMPLE DATA - Library Book Inventory
    # ========================================================================
    
    books = [
        {"isbn": "ISBN001", "title": "Python Programming", "category": "Programming", 
         "author": "John Smith", "copies": 5, "available": 3},
        {"isbn": "ISBN002", "title": "Data Structures", "category": "Programming", 
         "author": "Jane Doe", "copies": 4, "available": 2},
        {"isbn": "ISBN003", "title": "Machine Learning", "category": "AI", 
         "author": "Alice Johnson", "copies": 3, "available": 0},
        {"isbn": "ISBN004", "title": "Web Development", "category": "Programming", 
         "author": "Bob Wilson", "copies": 6, "available": 4},
        {"isbn": "ISBN005", "title": "Database Design", "category": "Database", 
         "author": "Charlie Brown", "copies": 4, "available": 4},
        {"isbn": "ISBN006", "title": "Network Security", "category": "Security", 
         "author": "David Lee", "copies": 2, "available": 1},
        {"isbn": "ISBN007", "title": "Cloud Computing", "category": "Cloud", 
         "author": "Eve Garcia", "copies": 3, "available": 2},
        {"isbn": "ISBN008", "title": "Mobile Apps", "category": "Programming", 
         "author": "Frank Martinez", "copies": 5, "available": 5},
    ]
    
    borrowed_books = [
        {"isbn": "ISBN001", "student": "Alice", "due_date": "2025-01-05", "days_overdue": 6},
        {"isbn": "ISBN002", "student": "Bob", "due_date": "2025-01-15", "days_overdue": 0},
        {"isbn": "ISBN003", "student": "Charlie", "due_date": "2025-01-08", "days_overdue": 3},
        {"isbn": "ISBN004", "student": "David", "due_date": "2025-01-20", "days_overdue": 0},
        {"isbn": "ISBN001", "student": "Eve", "due_date": "2025-01-03", "days_overdue": 8},
        {"isbn": "ISBN006", "student": "Frank", "due_date": "2025-01-10", "days_overdue": 1},
    ]
    
    # ========================================================================
    # SECTION 1: BOOK INVENTORY DISPLAY (for loop)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 1: BOOK INVENTORY DISPLAY (for loop)")
    print("="*80)
    print("\nProblem: Display all books in the library inventory")
    print("Concept: Use for loop to iterate through list of books")
    print("\nCode Example:")
    print("    for book in books:")
    print("        print(book['title'])")
    print("\n" + "-"*80)
    
    print("\n📚 COMPLETE LIBRARY INVENTORY:")
    print("-"*80)
    print(f"{'ISBN':<12} {'Title':<25} {'Category':<15} {'Available':<10} {'Total':<8}")
    print("-"*80)
    
    total_books = 0
    total_available = 0
    
    # FOR LOOP: Iterate through each book in the inventory
    for book in books:
        print(f"{book['isbn']:<12} {book['title']:<25} {book['category']:<15} "
              f"{book['available']:<10} {book['copies']:<8}")
        total_books += book['copies']
        total_available += book['available']
    
    print("-"*80)
    print(f"{'TOTAL:':<52} {total_available:<10} {total_books:<8}")
    
    print(f"\n✓ For loop completed: Displayed {len(books)} books")
    print(f"✓ Total books in library: {total_books}")
    print(f"✓ Books available for borrowing: {total_available}")
    
    # ========================================================================
    # SECTION 2: CATEGORY-WISE BOOK COUNT (for loop)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 2: CATEGORY-WISE BOOK COUNT (for loop)")
    print("="*80)
    print("\nProblem: Count books in each category")
    print("Concept: Use for loop to group and count items")
    print("\nCode Example:")
    print("    for book in books:")
    print("        if book['category'] not in categories:")
    print("            categories[book['category']] = 0")
    print("        categories[book['category']] += 1")
    print("\n" + "-"*80)
    
    categories = {}
    
    # FOR LOOP: Count books by category
    for book in books:
        category = book['category']
        if category not in categories:
            categories[category] = 0
        categories[category] += book['copies']
    
    print("\n📊 BOOKS BY CATEGORY:")
    print("-"*80)
    for category, count in categories.items():
        print(f"{category:<20}: {count:>3} books")
    print("-"*80)
    
    print(f"\n✓ For loop completed: Analyzed {len(categories)} categories")
    
    # ========================================================================
    # SECTION 3: BOOK SEARCH WITH BREAK
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 3: BOOK SEARCH SYSTEM (for loop with break)")
    print("="*80)
    print("\nProblem: Search for a specific book by ISBN and stop when found")
    print("Concept: Use break to exit loop immediately when condition is met")
    print("\nCode Example:")
    print("    for book in books:")
    print("        if book['isbn'] == search_isbn:")
    print("            print('Book found!')")
    print("            break  # Exit loop immediately")
    print("\n" + "-"*80)
    
    search_isbn = "ISBN004"
    print(f"\n🔍 SEARCHING FOR BOOK: {search_isbn}")
    print("-"*80)
    
    found = False
    search_count = 0
    
    # FOR LOOP with BREAK: Search and stop when found
    for book in books:
        search_count += 1
        print(f"Checking {book['isbn']}... ", end="")
        
        if book['isbn'] == search_isbn:
            print("✓ FOUND!")
            print("\n📖 BOOK DETAILS:")
            print(f"   Title: {book['title']}")
            print(f"   Author: {book['author']}")
            print(f"   Category: {book['category']}")
            print(f"   Available: {book['available']}/{book['copies']}")
            found = True
            break  # BREAK: Exit loop immediately when book is found
        else:
            print("Not a match")
    
    print(f"\n✓ Break statement executed after checking {search_count} book(s)")
    print(f"✓ Saved {len(books) - search_count} unnecessary comparisons!")
    
    if not found:
        print("✗ Book not found in inventory")
    
    # ========================================================================
    # SECTION 4: SEARCH FOR NON-EXISTENT BOOK (break not executed)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 4: SEARCH FOR NON-EXISTENT BOOK (break not executed)")
    print("="*80)
    print("\nProblem: Demonstrate loop completing without break")
    print("Concept: Break only executes when condition is met")
    print("\n" + "-"*80)
    
    search_isbn = "ISBN999"
    print(f"\n🔍 SEARCHING FOR BOOK: {search_isbn}")
    print("-"*80)
    
    found = False
    search_count = 0
    
    for book in books:
        search_count += 1
        print(f"Checking {book['isbn']}... Not a match")
        
        if book['isbn'] == search_isbn:
            found = True
            break
    
    print(f"\n✓ Loop completed all {search_count} iterations (break never executed)")
    print("✗ Book not found - searched entire inventory")
    
    # ========================================================================
    # SECTION 5: OVERDUE BOOKS CHECKER (for loop with continue)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 5: OVERDUE BOOKS CHECKER (for loop with continue)")
    print("="*80)
    print("\nProblem: Display only overdue books, skip books returned on time")
    print("Concept: Use continue to skip current iteration and move to next")
    print("\nCode Example:")
    print("    for book in borrowed_books:")
    print("        if book['days_overdue'] == 0:")
    print("            continue  # Skip this book, move to next")
    print("        print('Overdue:', book['title'])")
    print("\n" + "-"*80)
    
    print("\n⚠️  OVERDUE BOOKS REPORT:")
    print("-"*80)
    print(f"{'ISBN':<12} {'Student':<15} {'Due Date':<15} {'Days Overdue':<15}")
    print("-"*80)
    
    overdue_count = 0
    skipped_count = 0
    
    # FOR LOOP with CONTINUE: Skip non-overdue books
    for borrowed in borrowed_books:
        # CONTINUE: Skip books that are not overdue
        if borrowed['days_overdue'] == 0:
            skipped_count += 1
            print(f"{borrowed['isbn']:<12} {borrowed['student']:<15} "
                  f"{borrowed['due_date']:<15} {'On Time (Skipped)':<15}")
            continue  # Skip to next iteration
        
        # This code only runs for overdue books
        overdue_count += 1
        print(f"{borrowed['isbn']:<12} {borrowed['student']:<15} "
              f"{borrowed['due_date']:<15} {borrowed['days_overdue']} days ⚠️")
    
    print("-"*80)
    print(f"\n✓ Continue statement executed {skipped_count} times")
    print(f"✓ Found {overdue_count} overdue books")
    print(f"✓ Skipped {skipped_count} books that were on time")
    
    # ========================================================================
    # SECTION 6: FINE CALCULATION (for loop with continue)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 6: FINE CALCULATION (for loop with continue)")
    print("="*80)
    print("\nProblem: Calculate fines, skip students with no fine")
    print("Concept: Use continue to skip zero-fine calculations")
    print("\n" + "-"*80)
    
    print("\n💰 FINE CALCULATION REPORT:")
    print("-"*80)
    print(f"{'Student':<15} {'Days Overdue':<15} {'Fine Amount':<15}")
    print("-"*80)
    
    total_fines = 0
    fine_per_day = 5  # $5 per day
    
    for borrowed in borrowed_books:
        # CONTINUE: Skip if no fine
        if borrowed['days_overdue'] == 0:
            print(f"{borrowed['student']:<15} {'0 (Skipped)':<15} {'$0.00':<15}")
            continue
        
        fine = borrowed['days_overdue'] * fine_per_day
        total_fines += fine
        print(f"{borrowed['student']:<15} {borrowed['days_overdue']:<15} ${fine}.00")
    
    print("-"*80)
    print(f"{'TOTAL FINES:':<30} ${total_fines}.00")
    print(f"\n✓ Continue skipped students with no fines")
    
    # ========================================================================
    # SECTION 7: STUDENT REQUEST PROCESSOR (while loop)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 7: STUDENT REQUEST PROCESSOR (while loop)")
    print("="*80)
    print("\nProblem: Keep asking for valid input until received")
    print("Concept: Use while loop to repeat until condition is met")
    print("\nCode Example:")
    print("    valid_input = False")
    print("    while not valid_input:")
    print("        response = input('Enter (yes/no): ')")
    print("        if response in ['yes', 'no']:")
    print("            valid_input = True")
    print("\n" + "-"*80)
    
    print("\n📝 SIMULATED STUDENT REQUEST PROCESSING:")
    print("-"*80)
    
    # Simulated user inputs (in real scenario, use input())
    simulated_inputs = ["maybe", "dunno", "YES", "yes"]
    input_index = 0
    
    valid_input = False
    attempt_count = 0
    
    print("Question: Do you want to borrow a book? (yes/no)")
    
    # WHILE LOOP: Continue until valid input
    while not valid_input:
        attempt_count += 1
        
        # Simulating user input
        user_input = simulated_inputs[input_index]
        input_index += 1
        print(f"Attempt {attempt_count}: User entered '{user_input}'")
        
        # Convert to lowercase for comparison
        user_input = user_input.lower()
        
        if user_input in ['yes', 'no']:
            valid_input = True
            print(f"✓ Valid input received: '{user_input}'")
        else:
            print("✗ Invalid input! Please enter 'yes' or 'no'")
    
    print(f"\n✓ While loop executed {attempt_count} times until valid input")
    print(f"✓ Loop condition became False, so loop stopped")
    
    # ========================================================================
    # SECTION 8: BOOK ISSUING WITH DAILY LIMIT (while loop with break)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 8: BOOK ISSUING SYSTEM (while loop with break)")
    print("="*80)
    print("\nProblem: Issue books until daily limit reached")
    print("Concept: Use break to exit while loop when limit reached")
    print("\nCode Example:")
    print("    issued_today = 0")
    print("    while True:")
    print("        if issued_today >= daily_limit:")
    print("            break  # Exit loop when limit reached")
    print("        issue_book()")
    print("        issued_today += 1")
    print("\n" + "-"*80)
    
    print("\n📚 BOOK ISSUING SIMULATION:")
    print("-"*80)
    
    daily_limit = 5
    issued_today = 0
    students_waiting = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
    
    print(f"Daily book issue limit: {daily_limit}")
    print(f"Students in queue: {len(students_waiting)}")
    print()
    
    student_index = 0
    
    # WHILE LOOP with BREAK: Issue books until limit
    while True:
        # Check if daily limit reached
        if issued_today >= daily_limit:
            print(f"\n⚠️  DAILY LIMIT REACHED!")
            print(f"✓ Break statement executed")
            break  # BREAK: Exit loop when limit reached
        
        # Check if more students waiting
        if student_index >= len(students_waiting):
            print(f"\n✓ No more students in queue")
            break
        
        # Issue book to next student
        issued_today += 1
        student = students_waiting[student_index]
        print(f"{issued_today}. Book issued to {student}")
        student_index += 1
    
    remaining_students = len(students_waiting) - student_index
    
    print(f"\n✓ Books issued today: {issued_today}")
    print(f"✓ Students remaining in queue: {remaining_students}")
    print(f"✓ While loop with break prevented over-issuing")
    
    # ========================================================================
    # SECTION 9: COUNTDOWN EXAMPLE (while loop)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 9: LIBRARY CLOSING COUNTDOWN (while loop)")
    print("="*80)
    print("\nProblem: Count down until library closes")
    print("Concept: while loop with decrementing counter")
    print("\nCode Example:")
    print("    minutes = 5")
    print("    while minutes > 0:")
    print("        print(f'{minutes} minutes remaining')")
    print("        minutes -= 1")
    print("\n" + "-"*80)
    
    print("\n⏰ LIBRARY CLOSING IN:")
    print("-"*80)
    
    minutes = 5
    
    # WHILE LOOP: Count down
    while minutes > 0:
        print(f"⏰ {minutes} minute(s) remaining until closing")
        minutes -= 1
    
    print("🔒 Library is now CLOSED")
    print(f"\n✓ While loop ran while minutes > 0")
    print(f"✓ When minutes became 0, condition was False, loop stopped")
    
    # ========================================================================
    # SECTION 10: FUTURE FEATURES WITH PASS
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 10: FUTURE FEATURES (pass statement)")
    print("="*80)
    print("\nProblem: Define placeholders for features to be implemented later")
    print("Concept: Use pass as a null operation placeholder")
    print("\nCode Example:")
    print("    def send_email_reminder():")
    print("        pass  # TODO: Implement email functionality")
    print("\n" + "-"*80)
    
    print("\n🚧 FEATURES UNDER DEVELOPMENT:")
    print("-"*80)
    
    features = [
        "Email Reminder System",
        "SMS Notification Service",
        "Book Recommendation Engine",
        "Digital Library Integration",
        "Mobile App Sync"
    ]
    
    # FOR LOOP with PASS: Show planned features
    for i, feature in enumerate(features, 1):
        print(f"{i}. {feature}")
        
        # PASS: Placeholder for future implementation
        if feature == "Email Reminder System":
            pass  # TODO: Implement email system
        elif feature == "SMS Notification Service":
            pass  # TODO: Implement SMS service
        elif feature == "Book Recommendation Engine":
            pass  # TODO: Implement ML recommendation
        elif feature == "Digital Library Integration":
            pass  # TODO: Implement API integration
        else:
            pass  # TODO: Implement other features
    
    print("\n✓ Pass statement allows code to run without implementation")
    print("✓ Useful for planning and incremental development")
    
    # ========================================================================
    # SECTION 11: EMPTY FUNCTION WITH PASS
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 11: PLACEHOLDER FUNCTIONS (pass statement)")
    print("="*80)
    print("\nProblem: Define function structure without implementation")
    print("Concept: pass prevents syntax errors in empty code blocks")
    print("\nCode Example:")
    print("    def future_function():")
    print("        pass  # Will be implemented later")
    print("\n" + "-"*80)
    
    # Define placeholder functions with PASS
    def send_overdue_email(student, book):
        # TODO: Implement email sending logic
        pass
    
    def generate_monthly_report():
        # TODO: Implement report generation
        pass
    
    def backup_database():
        # TODO: Implement database backup
        pass
    
    print("\n📋 PLACEHOLDER FUNCTIONS DEFINED:")
    print("-"*80)
    print("1. send_overdue_email() - Using pass statement")
    print("2. generate_monthly_report() - Using pass statement")
    print("3. backup_database() - Using pass statement")
    
    # Call placeholder functions (they do nothing but don't cause errors)
    send_overdue_email("Alice", "Python Programming")
    generate_monthly_report()
    backup_database()
    
    print("\n✓ Functions called successfully (did nothing due to pass)")
    print("✓ No errors even though functions are empty")
    print("✓ Pass allows incremental development")
    
    # ========================================================================
    # SECTION 12: COMBINING ALL CONCEPTS
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 12: ADVANCED - COMBINING ALL CONCEPTS")
    print("="*80)
    print("\nProblem: Process book requests with all loop control statements")
    print("Concept: for + while + break + continue + pass together")
    print("\n" + "-"*80)
    
    print("\n🔄 COMPREHENSIVE BOOK REQUEST PROCESSING:")
    print("-"*80)
    
    book_requests = [
        {"student": "Alice", "isbn": "ISBN001", "priority": "high"},
        {"student": "Bob", "isbn": "ISBN999", "priority": "low"},  # Invalid ISBN
        {"student": "Charlie", "isbn": "ISBN003", "priority": "medium"},
        {"student": "David", "isbn": "ISBN004", "priority": "high"},
        {"student": "Eve", "isbn": "ISBN002", "priority": "low"},
    ]
    
    max_requests = 3
    processed = 0
    
    print(f"Processing maximum {max_requests} high-priority requests:\n")
    
    # FOR LOOP through requests
    for request in book_requests:
        student = request['student']
        isbn = request['isbn']
        priority = request['priority']
        
        print(f"Processing request from {student} for {isbn} (Priority: {priority})")
        
        # CONTINUE: Skip low priority requests
        if priority == "low":
            print(f"  → Skipped (low priority) - continue statement\n")
            continue
        
        # Check if ISBN exists (using nested for loop)
        book_found = False
        for book in books:
            if book['isbn'] == isbn:
                book_found = True
                break  # BREAK: Stop searching when found
        
        if not book_found:
            print(f"  → Invalid ISBN - Book not in system\n")
            continue  # Skip to next request
        
        # Check availability
        if priority == "medium":
            # PASS: Medium priority processing not implemented yet
            print(f"  → Medium priority processing (placeholder) - pass statement")
            pass  # TODO: Implement medium priority logic
            print(f"  → Skipped for now\n")
            continue
        
        # Process high priority
        processed += 1
        print(f"  ✓ Request approved and processed (high priority)\n")
        
        # BREAK: Stop after processing max requests
        if processed >= max_requests:
            print(f"⚠️  Maximum daily requests ({max_requests}) reached!")
            print(f"✓ Break statement executed to exit loop")
            break
    
    print(f"\n{'='*80}")
    print("SUMMARY:")
    print(f"{'='*80}")
    print(f"✓ Used for loop to iterate through requests")
    print(f"✓ Used continue to skip low priority and invalid requests")
    print(f"✓ Used pass as placeholder for medium priority logic")
    print(f"✓ Used break to stop after reaching daily limit")
    print(f"✓ Processed {processed} high-priority requests")
    
    # ========================================================================
    # FINAL SUMMARY
    # ========================================================================
    print("\n" + "="*80)
    print("CONCEPT SUMMARY")
    print("="*80)
    
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                         LOOP CONTROL STATEMENTS                            ║
╠════════════════════════════════════════════════════════════════════════════╣
║                                                                            ║
║  1. FOR LOOP:                                                              ║
║     • Used to iterate through sequences (lists, strings, ranges)          ║
║     • Example: for book in books:                                         ║
║     • Best for: Known number of iterations                                ║
║                                                                            ║
║  2. WHILE LOOP:                                                            ║
║     • Continues while condition is True                                   ║
║     • Example: while minutes > 0:                                         ║
║     • Best for: Unknown number of iterations, user input validation       ║
║                                                                            ║
║  3. BREAK STATEMENT:                                                       ║
║     • Immediately exits the loop                                          ║
║     • Example: if found: break                                            ║
║     • Best for: Early exit when condition met, search operations          ║
║                                                                            ║
║  4. CONTINUE STATEMENT:                                                    ║
║     • Skips rest of current iteration, moves to next                      ║
║     • Example: if skip_condition: continue                                ║
║     • Best for: Filtering, skipping invalid data                          ║
║                                                                            ║
║  5. PASS STATEMENT:                                                        ║
║     • Does nothing (null operation)                                       ║
║     • Example: def future_function(): pass                                ║
║     • Best for: Placeholders, empty functions/classes                     ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)
    
    print("\n" + "="*80)
    print("PROGRAM COMPLETED SUCCESSFULLY!")
    print("="*80)
    print("\n✅ All loop control concepts demonstrated")
    print("✅ Real-world library management scenarios shown")
    print("✅ 12 comprehensive sections covered")
    print("\n" + "="*80)

if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════════════════╗
    ║                                                                        ║
    ║           LIBRARY BOOK MANAGEMENT SYSTEM                               ║
    ║           Demonstrating Loop Control Statements                        ║
    ║                                                                        ║
    ║  This program demonstrates:                                            ║
    ║  • for loops - Iterate through collections                             ║
    ║  • while loops - Continue until condition false                        ║
    ║  • break - Exit loop immediately                                       ║
    ║  • continue - Skip current iteration                                   ║
    ║  • pass - Placeholder statement                                        ║
    ║                                                                        ║
    ╚════════════════════════════════════════════════════════════════════════╝
    """)
    
    main()
    
    print("\n\n💡 KEY TAKEAWAYS:")
    print("="*80)
    print("1. Use FOR when you know how many times to iterate")
    print("2. Use WHILE when condition-based iteration is needed")
    print("3. Use BREAK to exit loops early (saves processing time)")
    print("4. Use CONTINUE to skip unwanted iterations (filtering)")
    print("5. Use PASS as placeholder during development")
    print("="*80)