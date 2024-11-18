import os
import time
from datetime import datetime

class TodoList:
    def __init__(self):
        self.tasks = []
        self.excuses = [
            "The dog ate my homework... again!",
            "I'll do it tomorrow (just like I said yesterday)",
            "Waiting for the perfect planetary alignment",
            "My coffee didn't give me enough power",
            "A ninja stole my time!"
        ]

    def add_task(self, task, priority="⭐"):
        date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.tasks.append({
            "task": task,
            "done": False,
            "date": date,
            "priority": priority
        })
        return f"Task added! (Though we both know you'll procrastinate 😉)"

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            return "Wow! You actually completed something! 🎉"
        return "That task? Doesn't exist... just like your excuses? 🤔"

    def view_tasks(self):
        if not self.tasks:
            return "Your list is emptier than my fridge at the end of the month 🌪️"
        
        output = "\n📝 Task List (or dream list... who knows)\n"
        for i, task in enumerate(self.tasks):
            status = "✅" if task["done"] else "❌"
            output += f"{i}. {status} {task['priority']} {task['task']} ({task['date']})\n"
        return output

def main():
    todo = TodoList()
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("🎭 The Most Ridiculously Over-the-Top Todo List 🎭")
        print("\nWhat do you want to do today? (Besides procrastinating?)")
        print("1. 📝 Add task (I promise I'll do it this time)")
        print("2. ✅ Complete task (It's a miracle!)")
        print("3. 👀 View tasks (Prepare to feel guilty)")
        print("4. 🏃 Run from responsibilities (Exit)")
        
        choice = input("\nChoose your destiny (1-4): ")
        
        if choice == "1":
            task = input("\nWhat task would you like to add? (Be honest!): ")
            priority = input("Priority (⭐, ⭐⭐, ⭐⭐⭐): ")
            print("\n" + todo.add_task(task, priority))
            
        elif choice == "2":
            print(todo.view_tasks())
            try:
                index = int(input("\nWhich task did you complete? (number): "))
                print("\n" + todo.complete_task(index))
            except ValueError:
                print("\nThat's not even a number! Bad at math too? 😅")
                
        elif choice == "3":
            print(todo.view_tasks())
            
        elif choice == "4":
            print("\n🎭 Goodbye! Remember: procrastination is an art... and you're Picasso!")
            break
            
        else:
            print("\nSeriously? You can't even choose a number from 1 to 4? 🤦")
        
        input("\nPress Enter to continue (or take a nap, whatever you prefer)...")

if __name__ == "__main__":
    main()