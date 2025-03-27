# Name: Seth Sorrell
# File Name: student_gpa_tracker.py
# Description: This app accepts student names and GPAs, then determines if they qualify 
# for the Dean's List (GPA >= 3.5) or Honor Roll (GPA >= 3.25). The program continues 
# until 'ZZZ' is entered as a last name.

while True:
    # Get student's last name
    last_name = input("Enter student's last name (ZZZ to quit): ")
    
    # Check if user wants to quit
    if last_name.upper() == "ZZZ":
        print("Program terminated.")
        break
    
    # Get student's first name and GPA
    first_name = input("Enter student's first name: ")
    try:
        gpa = float(input("Enter student's GPA: "))
        
        # Validate GPA is within reasonable range
        if gpa < 0 or gpa > 4.0:
            print("Error: GPA must be between 0.0 and 4.0")
            continue
            
        # Check for Dean's List (GPA >= 3.5)
        if gpa >= 3.5:
            print(f"{first_name} {last_name} has made the Dean's List!")
        # Check for Honor Roll (GPA >= 3.25)
        elif gpa >= 3.25:
            print(f"{first_name} {last_name} has made the Honor Roll!")
        else:
            print(f"{first_name} {last_name} did not qualify for academic honors.")
            
    except ValueError:
        print("Error: Please enter a valid numeric GPA")
        continue

# Test cases:
# 1. Smith, John, 3.8  -> Dean's List
# 2. Jones, Mary, 3.4  -> Honor Roll
# 3. Brown, Tom, 2.9   -> No honors
# 4. Davis, Sarah, 3.6 -> Dean's List
# 5. Wilson, Bob, 3.3  -> Honor Roll