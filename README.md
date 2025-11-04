[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/38izMa6v)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21095552)


**desription**
  
  -The Command-Line GPA Calculator is a lightweight, interactive tool designed to help students monitor and improve their academic performance directly from the terminal. It provides an efficient way to input, calculate, and analyze grades across multiple semesters without relying on web-based tools or spreadsheets..

**Requirements**
  
  -language= python
  
  -platform= visual studio code
  
  -storage	Local file (JSON/CSV) for the sentimental archivist
  
  -Error Handling	Politely refuses invalid grades and negative credits
  
**purpose**

  -to give a interactive way to calculate GPA with varying grades.

  -A way to see your GPA with humorous comments.
  
**Usage Examples**
  
  -When run, the program prompts the user for the number of classes (minimum 5), collects grade inputs, calculates the overall GPA, and analyzes either the first or second half of the semester. It also lets users input a goal GPA and suggests ways to improve individual grades to meet that goal.

**Configuration & Testing**

  -No external configuration is needed; all inputs are entered via prompts. To test, simply run the script and follow the prompts—try entering valid/invalid grades, and different goal GPAs to see how the program responds.

**decision tree**
  
  -START
│
├── Display welcome message ("Greetings, noble scholar...")
│
├── Ask: "Would you like to load a previous GPA record?"  
│     │
│     ├── YES → Load file → Display loaded data summary  
│     │          │
│     │          └── Proceed to "Add New Semester?"  
│     │
│     └── NO → Start fresh GPA record  
│
├── Ask: "Would you like to add a new semester?"  
│     │
│     ├── NO → Go to "View or Save Results"  
│     │
│     └── YES → Begin semester entry  
│           │
│           ├── Ask: "Enter course name"  
│           ├── Ask: "Enter credit hours"  
│           ├── Ask: "Enter letter grade (A–F)"  
│           │
│           ├── Validate grade input  
│           │     ├── If INVALID → Show error message and re-prompt  
│           │     └── If VALID → Continue  
│           │
│           ├── Ask: "Add another course?"  
│           │     ├── YES → Repeat course entry  
│           │     └── NO → Calculate semester GPA  
│           │
│           ├── Display verbose GPA result  
│           │     ("Your semester GPA stands tall at 3.72!")  
│           │
│           ├── Add semester GPA to cumulative total  
│           │
│           └── Ask: "Add another semester?"  
│                 ├── YES → Loop back to semester entry  
│                 └── NO → Proceed  
│
├── Display cumulative GPA  
│
├── Ask: "Would you like to set a target GPA?"  
│     │
│     ├── NO → Proceed to Save  
│     └── YES →  
│           ├── Ask: "Enter desired target GPA"  
│           ├── Calculate required future GPA  
│           └── Display verbose prediction  
│               ("You must achieve an average of 3.88 next term.  
│                 Time to unleash your inner scholar!")  
│
├── Ask: "Would you like to save your GPA data to file?"  
│     │
│     ├── NO → End session with farewell message  
│     └── YES → Save file → Confirm success  
│
└── END ("Farewell, academic adventurer! May your grades ever rise.")



