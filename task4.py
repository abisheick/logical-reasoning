# Unit - 4: Logical Reasoning
# Rule-Based Expert System using Backward Chaining
# Student Academic Guidance

# -----------------------------
# FACTS ABOUT THE STUDENT
# -----------------------------

facts = {
    "GoodAttendance",
    "HighMarks",
    "CompletedProjects",
    "GoodCommunication"
}


# -----------------------------
# RULES
# -----------------------------
# Each rule has:
# conclusion : conditions required to prove it

rules = {
    "GoodAcademicPerformance": [
        "HighMarks",
        "GoodAttendance"
    ],

    "NeedsExtraPractice": [
        "LowMarks"
    ],

    "EligibleForPlacement": [
        "GoodAcademicPerformance",
        "CompletedProjects",
        "GoodCommunication"
    ],

    "ReadyForInterview": [
        "EligibleForPlacement",
        "GoodCommunication"
    ]
}


# -----------------------------
# BACKWARD CHAINING
# -----------------------------

def backward_chaining(goal, depth=0):
    indent = "  " * depth

    print(indent + "Trying to prove:", goal)

    # Step 1: Check whether the goal is already a fact
    if goal in facts:
        print(indent + "Fact found:", goal)
        return True

    # Step 2: Check whether a rule can prove the goal
    if goal not in rules:
        print(indent + "No rule found for:", goal)
        return False

    # Step 3: Try to prove all conditions of the rule
    conditions = rules[goal]

    print(indent + "Rule found for", goal)
    print(indent + "Required conditions:", conditions)

    for condition in conditions:
        print(indent + "Checking condition:", condition)

        if not backward_chaining(condition, depth + 1):
            print(indent + "Condition failed:", condition)
            return False

    # If all conditions are true
    print(indent + "All conditions satisfied for:", goal)
    return True


# -----------------------------
# SELECT GOAL
# -----------------------------

goal = "EligibleForPlacement"

print("========================================")
print(" STUDENT ACADEMIC GUIDANCE SYSTEM")
print("========================================")

print("\nFacts about the student:")
for fact in facts:
    print("-", fact)

print("\nRules:")
for conclusion, conditions in rules.items():
    print(conclusion, "<-", " AND ".join(conditions))

print("\n----------------------------------------")
print("BACKWARD CHAINING REASONING")
print("----------------------------------------")

result = backward_chaining(goal)

print("\n----------------------------------------")
print("FINAL CONCLUSION")
print("----------------------------------------")

if result:
    print("Goal:", goal)
    print("Conclusion: Student is eligible for placement.")
else:
    print("Goal:", goal)
    print("Conclusion: Student is NOT eligible for placement.")