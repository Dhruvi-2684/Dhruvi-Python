import pandas as pd
import datetime

# Initialize an empty attendance DataFrame
attendance_df = pd.DataFrame()

# Add students to the DataFrame
def add_students(student_list):
    global attendance_df
    attendance_df = pd.DataFrame(index=student_list)
    print("Students added!")

# Mark attendance for today
def mark_attendance():
    global attendance_df
    today = datetime.date.today().isoformat()
    print(f"\nMarking attendance for {today}")
    attendance_df[today] = 'A'  # Default Absent

    for student in attendance_df.index:
        status = input(f"Is {student} present? (y/n): ").strip().lower()
        if status == 'y':
            attendance_df.at[student, today] = 'P'

# View the current attendance sheet
def view_attendance():
    global attendance_df
    print("\nCurrent Attendance:")
    print(attendance_df)

# Save attendance to a CSV file
def save_attendance(filename="attendance.csv"):
    global attendance_df
    attendance_df.to_csv(filename)
    print(f"Attendance saved to {filename}")

# Load attendance from a CSV file
def load_attendance(filename="attendance.csv"):
    global attendance_df
    attendance_df = pd.read_csv(filename, index_col=0)
    print(f"Attendance loaded from {filename}")

# Menu
def main():
    while True:
        print("\n--- Classroom Attendance System ---")
        print("1. Add Students")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Save Attendance")
        print("5. Load Attendance")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == '1':
            students = input("Enter student names (comma-separated): ").split(",")
            students = [s.strip() for s in students]
            add_students(students)
        elif choice == '2':
            mark_attendance()
        elif choice == '3':
            view_attendance()
        elif choice == '4':
            save_attendance()
        elif choice == '5':
            load_attendance()
        elif choice == '6':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again!")

# Run the program
if __name__ == "__main__":
    main()
