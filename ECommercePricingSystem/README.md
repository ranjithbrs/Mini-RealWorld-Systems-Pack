# 🛒 E‑Commerce Dynamic Pricing System

## 📌 Aim
To design a Python program that dynamically calculates the final price of a product based on customer type, time of purchase, festival season, and customer rating. The system applies discounts, surcharges, and validations to simulate real‑world e‑commerce pricing.

---

## 📝 Problem Statement
An e‑commerce platform wants to adjust product prices based on customer loyalty, purchase timing, and seasonal offers. The system should:
- Apply discounts for premium and new customers.
- Add surcharges for night purchases and festival seasons.
- Validate customer rating (0–5).
- Provide best deal messages if total discount ≥ 15%.

---

## ⚙️ Algorithm
1. Input base price.  
2. Input customer type (regular, premium, new).  
   - Premium → 15% discount.  
   - New → 5% discount.  
3. Input time of purchase.  
   - Night → +10% surcharge.  
4. Input festival season (yes/no).  
   - Yes → +20% surcharge.  
5. Input customer rating (0–5).  
   - If rating ≥ 4.7 → extra 5% discount.  
   - Else if rating outside 0–5 → print error message.  
6. Calculate final price.  
7. Print final price and deal message:  
   - If total discount ≥ 15% → “Best deal for you”.  
   - Else → “Standard pricing applied”.

---

## ❓ Practice Questions
1. What happens if customer type = regular?  
2. Why is a surcharge added for night purchases?  
3. What is the effect of festival season on pricing?  
4. How does the program handle invalid ratings (e.g., 6)?  
5. When does the system print “Best deal for you”?

---

## 💻 Sample Input / Output

### ✅ Case 1: Premium Customer, Festival Season
Enter the base price: 2000
Enter the customer type(regular, premium, new): premium
Enter the time of purchase(morning, afternoon, night): night
Enter the festival season(yes, no): yes
Enter the rating(<=5.0): 4.8

**Output:**
Final_price: ₹2131.80
Best deal for you

---

### ❌ Case 2: Invalid Rating
Enter the base price: 1500
Enter the customer type(regular, premium, new): new
Enter the time of purchase(morning, afternoon, night): morning
Enter the festival season(yes, no): no
Enter the rating(<=5.0): 6

**Output:**
Rating should be between 0 and 5
Standard pricing applied

---

## ✅ Result
The program successfully adjusts product prices based on customer type, purchase timing, festival season, and rating, while validating inputs and providing clear deal messages.

---

## 🚀 Future Enhancements
- Add coupon code integration.  
- Store customer purchase history in a database.  
- Extend logic for multiple products in a cart.  
- Build a GUI or web interface for user‑friendly interaction.  