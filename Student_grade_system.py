# ================================================================================
#                     STUDENT GRADE MANAGEMENT SYSTEM
# ================================================================================

# DETAILED PROBLEM STATEMENT:
# ---------------------------
# Create a comprehensive Student Grade Management System that evaluates student
# performance based on multiple criteria including attendance, assignments, and
# exam scores. The system should provide detailed feedback and recommendations
# using various conditional statements (if, if-else, if-elif-else).

# REQUIREMENTS:
# -------------
# 1. Calculate final grade based on:
#    - Attendance (20% weight)
#    - Assignments (30% weight)
#    - Exam Score (50% weight)

# 2. Attendance Rules:
#    - 90% or above: Excellent (full 20 points)
#    - 75-89%: Good (15 points)
#    - 60-74%: Average (10 points)
#    - Below 60%: Poor (5 points)

# 3. Assignment Rules:
#    - All 10 assignments submitted: Full 30 points
#    - 8-9 assignments: 24 points
#    - 6-7 assignments: 18 points
#    - Below 6: Proportional points

# 4. Exam Score (Direct 50% of final grade)

# 5. Final Letter Grade:
#    - A: 90-100
#    - B: 80-89
#    - C: 70-79
#    - D: 60-69
#    - F: Below 60

# 6. Special Conditions:
#    - Perfect attendance (100%) gets 5 bonus points
#    - All assignments + exam >90 = Dean's List
#    - Attendance <50% = Automatic warning
#    - Final grade <60 = Must retake course

# 7. Generate detailed report with recommendations

# ================================================================================
# """

"""
================================================================================
                    STUDENT GRADE MANAGEMENT SYSTEM
================================================================================

DETAILED PROBLEM STATEMENT:
---------------------------
Create a comprehensive Student Grade Management System that evaluates student
performance based on multiple criteria including attendance, assignments, and
exam scores. The system should provide detailed feedback and recommendations
using various conditional statements (if, if-else, if-elif-else).

REQUIREMENTS:
-------------
1. Calculate final grade based on:
   - Attendance (20% weight)
   - Assignments (30% weight)
   - Exam Score (50% weight)

2. Attendance Rules:
   - 90% or above: Excellent (full 20 points)
   - 75-89%: Good (15 points)
   - 60-74%: Average (10 points)
   - Below 60%: Poor (5 points)

3. Assignment Rules:
   - All 10 assignments submitted: Full 30 points
   - 8-9 assignments: 24 points
   - 6-7 assignments: 18 points
   - Below 6: Proportional points

4. Exam Score (Direct 50% of final grade)

5. Final Letter Grade:
   - A: 90-100
   - B: 80-89
   - C: 70-79
   - D: 60-69
   - F: Below 60

6. Special Conditions:
   - Perfect attendance (100%) gets 5 bonus points
   - All assignments + exam >90 = Dean's List
   - Attendance <50% = Automatic warning
   - Final grade <60 = Must retake course

7. Generate detailed report with recommendations

================================================================================
"""

def student_grade_system():
    print("="*80)
    print(" "*20 + "STUDENT GRADE MANAGEMENT SYSTEM")
    print("="*80)
    
    # ========================================================================
    # STUDENT DATA INPUT
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 1: STUDENT INFORMATION")
    print("="*80)
    
    student_name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    
    print(f"\nProcessing grades for: {student_name} (ID: {student_id})")
    
    # ========================================================================
    # ATTENDANCE EVALUATION (Using if-elif-else)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 2: ATTENDANCE EVALUATION")
    print("="*80)
    print("\nAttendance Weight: 20% of final grade")
    print("-" * 50)
    
    total_classes = int(input("Enter total classes conducted: "))
    classes_attended = int(input("Enter classes attended: "))
    
    # Calculate attendance percentage
    attendance_percentage = (classes_attended / total_classes) * 100
    
    print(f"\nAttendance: {classes_attended}/{total_classes} classes")
    print(f"Attendance Percentage: {attendance_percentage:.2f}%")
    
    # if-elif-else for attendance evaluation
    if attendance_percentage >= 90:
        attendance_points = 20
        attendance_grade = "Excellent"
        attendance_comment = "Outstanding attendance! Keep it up!"
    elif attendance_percentage >= 75:
        attendance_points = 15
        attendance_grade = "Good"
        attendance_comment = "Good attendance. Try to improve further."
    elif attendance_percentage >= 60:
        attendance_points = 10
        attendance_grade = "Average"
        attendance_comment = "Attendance needs improvement. Be more regular."
    else:
        attendance_points = 5
        attendance_grade = "Poor"
        attendance_comment = "Critical! Very low attendance. Immediate improvement needed."
    
    print(f"\nAttendance Grade: {attendance_grade}")
    print(f"Points Earned: {attendance_points}/20")
    print(f"Comment: {attendance_comment}")
    
    # ========================================================================
    # PERFECT ATTENDANCE BONUS (Using simple if)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 3: PERFECT ATTENDANCE BONUS CHECK")
    print("="*80)
    
    bonus_points = 0
    
    # Simple if statement for bonus
    if attendance_percentage == 100:
        bonus_points = 5
        print("🎉 BONUS AWARDED!")
        print(f"Perfect attendance achieved! +{bonus_points} bonus points")
        print("Congratulations on your dedication!")
    
    if attendance_percentage < 100:
        print("No bonus this time. Achieve 100% attendance for 5 bonus points!")
    
    # ========================================================================
    # ASSIGNMENT EVALUATION (Using if-elif-else)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 4: ASSIGNMENT EVALUATION")
    print("="*80)
    print("\nAssignment Weight: 30% of final grade")
    print("-" * 50)
    
    total_assignments = 10
    assignments_submitted = int(input("Enter number of assignments submitted (out of 10): "))
    
    print(f"\nAssignments Submitted: {assignments_submitted}/{total_assignments}")
    
    # if-elif-else for assignment evaluation
    if assignments_submitted >= 10:
        assignment_points = 30
        assignment_grade = "Excellent"
        assignment_comment = "All assignments completed! Perfect score!"
    elif assignments_submitted >= 8:
        assignment_points = 24
        assignment_grade = "Very Good"
        assignment_comment = "Almost all assignments done. Great effort!"
    elif assignments_submitted >= 6:
        assignment_points = 18
        assignment_grade = "Good"
        assignment_comment = "Decent submission rate. Submit remaining assignments."
    else:
        # Proportional points for less than 6 assignments
        assignment_points = (assignments_submitted / total_assignments) * 30
        assignment_grade = "Needs Improvement"
        assignment_comment = "Low submission rate. Focus on completing assignments!"
    
    print(f"\nAssignment Grade: {assignment_grade}")
    print(f"Points Earned: {assignment_points}/30")
    print(f"Comment: {assignment_comment}")
    
    # ========================================================================
    # EXAM SCORE EVALUATION (Using if-else)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 5: EXAM SCORE EVALUATION")
    print("="*80)
    print("\nExam Weight: 50% of final grade")
    print("-" * 50)
    
    exam_score = float(input("Enter exam score (0-100): "))
    
    # Calculate exam points (50% weight)
    exam_points = (exam_score / 100) * 50
    
    print(f"\nExam Score: {exam_score}/100")
    print(f"Points Earned: {exam_points}/50")
    
    # if-else for exam performance
    if exam_score >= 80:
        exam_comment = "Excellent exam performance!"
    else:
        exam_comment = "Work harder for better exam results."
    
    print(f"Comment: {exam_comment}")
    
    # ========================================================================
    # FINAL GRADE CALCULATION
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 6: FINAL GRADE CALCULATION")
    print("="*80)
    
    # Calculate total points
    total_points = attendance_points + assignment_points + exam_points + bonus_points
    
    # Cap at 100 if bonus points push it over
    if total_points > 100:
        total_points = 100
    
    print("\nGrade Breakdown:")
    print("-" * 50)
    print(f"Attendance Points:    {attendance_points:>6.2f}/20")
    print(f"Assignment Points:    {assignment_points:>6.2f}/30")
    print(f"Exam Points:          {exam_points:>6.2f}/50")
    if bonus_points > 0:
        print(f"Bonus Points:         {bonus_points:>6}/5")
    print("-" * 50)
    print(f"TOTAL POINTS:         {total_points:>6.2f}/100")
    
    # ========================================================================
    # LETTER GRADE ASSIGNMENT (Using if-elif-else)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 7: LETTER GRADE ASSIGNMENT")
    print("="*80)
    
    # if-elif-else chain for letter grade
    if total_points >= 90:
        letter_grade = "A"
        grade_description = "Excellent"
        gpa = 4.0
    elif total_points >= 80:
        letter_grade = "B"
        grade_description = "Very Good"
        gpa = 3.0
    elif total_points >= 70:
        letter_grade = "C"
        grade_description = "Good"
        gpa = 2.0
    elif total_points >= 60:
        letter_grade = "D"
        grade_description = "Satisfactory"
        gpa = 1.0
    else:
        letter_grade = "F"
        grade_description = "Fail"
        gpa = 0.0
    
    print(f"\nFinal Grade: {letter_grade} ({grade_description})")
    print(f"Percentage: {total_points:.2f}%")
    print(f"GPA: {gpa}")
    
    # ========================================================================
    # SPECIAL RECOGNITIONS & WARNINGS (Using if statements)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 8: SPECIAL RECOGNITIONS & WARNINGS")
    print("="*80)
    
    # Dean's List check (simple if)
    if assignments_submitted == 10 and exam_score > 90:
        print("\n🏆 DEAN'S LIST RECOGNITION!")
        print("Outstanding performance in both assignments and exam!")
        print("You are eligible for the Dean's List this semester.")
    
    # Attendance warning (simple if)
    if attendance_percentage < 50:
        print("\n⚠️  CRITICAL ATTENDANCE WARNING!")
        print("Your attendance is below 50%.")
        print("You may be debarred from taking the exam.")
        print("Please contact the academic advisor immediately.")
    
    # Must retake course (simple if)
    if total_points < 60:
        print("\n❌ COURSE FAILED - MUST RETAKE")
        print("Your final grade is below passing (60%).")
        print("You must retake this course next semester.")
        print("Schedule a meeting with your advisor for counseling.")
    
    # Honor Roll (simple if)
    if total_points >= 85 and attendance_percentage >= 90:
        print("\n⭐ HONOR ROLL STUDENT")
        print("Congratulations! You qualify for the Honor Roll.")
        print("Excellent academic performance and attendance!")
    
    # ========================================================================
    # PERFORMANCE ANALYSIS (Using nested if-else)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 9: PERFORMANCE ANALYSIS & RECOMMENDATIONS")
    print("="*80)
    
    print("\n📊 Detailed Analysis:")
    print("-" * 50)
    
    # Analyze strongest area
    if attendance_points >= assignment_points and attendance_points >= exam_points:
        print("✓ Strongest Area: ATTENDANCE")
        print("  Your attendance is your best strength!")
    elif assignment_points >= exam_points:
        print("✓ Strongest Area: ASSIGNMENTS")
        print("  You excel at completing assignments!")
    else:
        print("✓ Strongest Area: EXAM PERFORMANCE")
        print("  You perform best in exams!")
    
    # Analyze weakest area
    print("\n⚠ Areas for Improvement:")
    if attendance_points < 15:
        print("  • Attendance needs significant improvement")
        print("    Recommendation: Attend all classes regularly")
    
    if assignment_points < 20:
        print("  • Assignment completion rate is low")
        print("    Recommendation: Submit all assignments on time")
    
    if exam_points < 35:
        print("  • Exam performance needs improvement")
        print("    Recommendation: Study regularly and seek help if needed")
    
    # Overall performance category (using nested if-else)
    print("\n📈 Overall Performance Category:")
    if total_points >= 90:
        print("  OUTSTANDING PERFORMER")
        if attendance_percentage == 100:
            print("  With perfect attendance - You're a role model!")
        else:
            print("  Aim for perfect attendance to be even better!")
    elif total_points >= 75:
        print("  GOOD PERFORMER")
        if exam_score < 80:
            print("  Focus on improving exam scores to reach excellence!")
        else:
            print("  You're on the right track. Keep pushing!")
    else:
        print("  NEEDS IMPROVEMENT")
        if attendance_percentage < 70:
            print("  Priority: Improve attendance immediately!")
        elif assignment_points < 18:
            print("  Priority: Complete all assignments!")
        else:
            print("  Priority: Strengthen exam preparation!")
    
    # ========================================================================
    # SEMESTER STATUS (Using if-elif-else)
    # ========================================================================
    print("\n" + "="*80)
    print("SECTION 10: SEMESTER STATUS")
    print("="*80)
    
    if total_points >= 60:
        semester_status = "PASSED"
        print(f"\n✅ Semester Status: {semester_status}")
        
        if total_points >= 90:
            print("   Next Semester: Eligible for advanced courses")
        elif total_points >= 75:
            print("   Next Semester: Eligible for regular courses")
        else:
            print("   Next Semester: Eligible but consider extra preparation")
    else:
        semester_status = "FAILED"
        print(f"\n❌ Semester Status: {semester_status}")
        print("   Next Semester: Must retake this course")
        print("   Additional: Mandatory counseling session required")
    
    # ========================================================================
    # FINAL SUMMARY REPORT
    # ========================================================================
    print("\n" + "="*80)
    print("FINAL SUMMARY REPORT")
    print("="*80)
    
    print(f"""
╔════════════════════════════════════════════════════════════════════════════╗
║                          GRADE REPORT SUMMARY                              ║
╠════════════════════════════════════════════════════════════════════════════╣
║ Student Name:     {student_name:<56} ║
║ Student ID:       {student_id:<56} ║
╠════════════════════════════════════════════════════════════════════════════╣
║ Attendance:       {attendance_percentage:>5.1f}%  ({attendance_grade:<15})  Points: {attendance_points:>4.1f}/20    ║
║ Assignments:      {assignments_submitted:>2}/10  ({assignment_grade:<15})  Points: {assignment_points:>4.1f}/30    ║
║ Exam Score:       {exam_score:>5.1f}% ({exam_comment:<15})  Points: {exam_points:>4.1f}/50    ║
║ Bonus Points:                                           {bonus_points:>4}/5     ║
╠════════════════════════════════════════════════════════════════════════════╣
║ FINAL GRADE:      {letter_grade:^10} ({total_points:>5.2f}%)                                  ║
║ GPA:              {gpa:^10}                                                 ║
║ Status:           {semester_status:^10}                                            ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)
    
    # ========================================================================
    # ACTION ITEMS (Using multiple if statements)
    # ========================================================================
    print("\n" + "="*80)
    print("REQUIRED ACTION ITEMS")
    print("="*80)
    
    action_count = 0
    
    if attendance_percentage < 75:
        action_count += 1
        print(f"\n{action_count}. ATTENDANCE ACTION:")
        print("   - Meet with academic advisor")
        print("   - Provide medical certificates if applicable")
        print("   - Commit to 100% attendance going forward")
    
    if assignments_submitted < 8:
        action_count += 1
        print(f"\n{action_count}. ASSIGNMENT ACTION:")
        print("   - Submit all pending assignments within 1 week")
        print("   - Meet with course instructor for makeup work")
        print("   - Create assignment submission schedule")
    
    if exam_score < 70:
        action_count += 1
        print(f"\n{action_count}. EXAM PREPARATION ACTION:")
        print("   - Attend tutoring sessions")
        print("   - Join study groups")
        print("   - Review and practice regularly")
    
    if total_points < 60:
        action_count += 1
        print(f"\n{action_count}. MANDATORY ACTION:")
        print("   - Schedule counseling session")
        print("   - Develop improvement plan")
        print("   - Register for course retake")
    
    if action_count == 0:
        print("\n✅ No action items required - Excellent work!")
        print("   Continue your outstanding performance!")
    
    # ========================================================================
    # MOTIVATIONAL MESSAGE (Using if-elif-else)
    # ========================================================================
    print("\n" + "="*80)
    print("MOTIVATIONAL MESSAGE")
    print("="*80)
    
    if total_points >= 90:
        message = """
        🌟 OUTSTANDING ACHIEVEMENT! 🌟
        
        You have demonstrated exceptional dedication and excellence.
        Your hard work has paid off magnificently!
        Keep up this outstanding performance!
        
        "Success is not final, failure is not fatal: 
         It is the courage to continue that counts." - Winston Churchill
        """
    elif total_points >= 75:
        message = """
        👏 GREAT JOB! 👏
        
        You're performing well and showing strong commitment.
        With a little more effort, you can reach excellence!
        Keep pushing forward!
        
        "The only way to do great work is to love what you do." - Steve Jobs
        """
    elif total_points >= 60:
        message = """
        💪 YOU PASSED! 💪
        
        You've made it through, but there's room for improvement.
        Focus on your weak areas and aim higher next time.
        You have the potential - unlock it!
        
        "It does not matter how slowly you go as long as you do not stop." - Confucius
        """
    else:
        message = """
        🔄 DON'T GIVE UP! 🔄
        
        This is a setback, not the end.
        Learn from this experience and come back stronger.
        Success is built on failures turned into lessons.
        
        "Success is not final, failure is not fatal." - Winston Churchill
        You CAN and you WILL succeed!
        """
    
    print(message)
    
    print("\n" + "="*80)
    print("END OF GRADE REPORT")
    print("="*80)
    
    return {
        'name': student_name,
        'id': student_id,
        'final_grade': letter_grade,
        'percentage': total_points,
        'gpa': gpa,
        'status': semester_status
    }

# ============================================================================
# MAIN PROGRAM EXECUTION
# ============================================================================

if __name__ == "__main__":
    print("""
    ╔════════════════════════════════════════════════════════════════════════╗
    ║                                                                        ║
    ║              WELCOME TO STUDENT GRADE MANAGEMENT SYSTEM                ║
    ║                                                                        ║
    ║  This program demonstrates the use of:                                 ║
    ║  • Simple if statements                                                ║
    ║  • if-else statements                                                  ║
    ║  • if-elif-else statements (multiple conditions)                       ║
    ║  • Nested if-else statements                                           ║
    ║                                                                        ║
    ║  The program evaluates student performance across multiple             ║
    ║  parameters and provides comprehensive feedback.                       ║
    ║                                                                        ║
    ╚════════════════════════════════════════════════════════════════════════╝
    """)
    
    # Run the grade system
    result = student_grade_system()
    
    print("\n\n" + "="*80)
    print("THANK YOU FOR USING THE STUDENT GRADE MANAGEMENT SYSTEM")
    print("="*80)
    print(f"\nQuick Summary for {result['name']}:")
    print(f"  Final Grade: {result['final_grade']} ({result['percentage']:.2f}%)")
    print(f"  GPA: {result['gpa']}")
    print(f"  Status: {result['status']}")
    print("\n" + "="*80)
    print("Program completed successfully!")
    print("="*80)