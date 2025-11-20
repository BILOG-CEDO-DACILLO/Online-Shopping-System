# ------------------------------------------
# GEAR INDEXING CALCULATOR
# Computes:
# - Pitch Diameter (PD)
# - Number of Teeth
# - Worm Gear Division (hk = holes/turn)
# - Recommended Index Plate, Circle, and Holes
# Based on input: Outside Diameter (OD) and Module (M)
# ------------------------------------------

from fractions import Fraction

# Available index plates and circles (standard)
index_plates = {
    1: [15, 16, 17, 18, 19, 20],
    2: [21, 23, 27, 29, 31, 33],
    3: [37, 39, 41, 43, 47, 49]
}

print("\n=== GEAR CUTTING INDEX CALCULATOR ===\n")

# ---- USER INPUT ----
OD = float(input("Enter Outside Diameter (OD): "))
M = float(input("Enter Module (M): "))

# ---- COMPUTATIONS BASED ON YOUR FORMULAS ----
PD = OD - 2 * M
N = PD / M                   # number of teeth
N = int(N)                   # must be whole number

worm_ratio = 40             # Standard dividing head ratio (40:1)
hk = Fraction(worm_ratio, N)    # holes per turn (fraction)

# ---- SELECT INDEX PLATE AND CIRCLE ----
selected_plate = None
selected_circle = None

for plate_no, circles in index_plates.items():
    for circle in circles:
        # check if denominator divides the circle
        needed_holes = hk.denominator
        if circle % needed_holes == 0:
            selected_plate = plate_no
            selected_circle = circle
            break
    if selected_plate:
        break

# ---- PRINT RESULTS ----
print("\n--- RESULTS ---")
print(f"Pitch Diameter (PD): {PD}")
print(f"Number of Teeth (N): {N}")
print(f"Worm Gear Division (hk): {hk} turn per tooth")

if selected_plate:
    print(f"\nRecommended Index Plate: Plate No. {selected_plate}")
    print(f"Index Circle to Use: {selected_circle} holes")
    holes_to_move = selected_circle // hk.denominator
    print(f"Holes to Move Per Tooth: {holes_to_move}")
else:
    print("\n No matching index plate/circle found for this gear.")