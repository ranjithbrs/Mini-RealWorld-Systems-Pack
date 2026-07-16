# 🚖 Travel Cab Fare System

## 📌 Aim
To design a Python program that calculates the final cab fare based on distance, time of day, and customer rating. The system applies surcharges during peak hours and discounts for high ratings, while validating inputs.

---

## 📝 Problem Statement
A cab service wants to automate its fare calculation. The system should:
- Calculate base fare using distance.
- Add surcharge during peak hours.
- Apply discount for high ratings.
- Validate rating input (0–5).
- Print final fare with clear messages.

---

## ⚙️ Algorithm
1. Input distance in kilometers.  
2. Input time of day (peak/non‑peak).  
   - Peak → add 25% surcharge.  
   - Non‑peak → no surcharge.  
   - Invalid → print error.  
3. Input rating (0–5).  
   - If rating > 4.5 → apply 10% discount.  
   - Else → no discount.  
   - If rating outside 0–5 → print error.  
4. Calculate final price:  
   - Base price = ₹50 + (₹10 × distance).  
   - Apply surcharge/discount as per conditions.  
5. Print final price.

---

## ❓ Practice Questions
1. What happens if the time of day is entered incorrectly?  
2. Why is a surcharge added during peak hours?  
3. How does the program handle ratings outside the range 0–5?  
4. What is the formula for base price calculation?  
5. When does the system apply a 10% discount?

---

## 💻 Sample Input / Output

### ✅ Case 1: Peak Hours, High Rating
Enter the distance in km: 10
Enter the time of day(Peek, Non-peek): peek
Enter the rating (for out of 5): 4.8

**Output:**
Final price: ₹162.50

---

### ❌ Case 2: Invalid Rating
Enter the distance in km: 5
Enter the time of day(Peek, Non-peek): non-peek
Enter the rating (for out of 5): 6

**Output:**
rating should be between 0 and 5
Final price: ₹100.00

---

## ✅ Result
The program successfully calculates cab fare based on distance, time of day, and rating, while validating inputs and applying discounts or surcharges.

---

## 🚀 Future Enhancements
- Add different cab types (mini, sedan, SUV) with variable base fares.  
- Integrate surge pricing based on demand.  
- Store trip records in a database.  
- Build a GUI or mobile app interface for user‑friendly booking.