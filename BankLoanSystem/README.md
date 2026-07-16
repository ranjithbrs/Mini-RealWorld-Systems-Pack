# 🏦 Bank Loan Eligibility System

## 📌 Aim
To design a Python program that checks whether a customer is eligible for a loan based on age, income, credit score, existing loans, and requested loan amount. If eligible, the system calculates the EMI (Equated Monthly Installment).

---

## 📝 Problem Statement
A bank wants to automate its loan approval process. The system should:
- Validate customer details (age, income, credit score).
- Check existing loan burden.
- Ensure requested loan amount is within limits.
- Approve or reject with clear reasons.
- If approved, calculate EMI with 10% interest for 1 year.

---

## ⚙️ Algorithm
1. Input customer age.  
   - If not between 21 and 60 → Reject.  
2. Input monthly income.  
   - If < ₹25,000 → Reject.  
3. Input credit score (≤ 900).  
   - If < 700 → Reject.  
4. Input existing loan amount.  
   - If ≥ 50% of monthly income → Reject.  
5. Input requested loan amount.  
   - If ≥ 20 × monthly income → Reject.  
6. If all conditions pass → Approve loan.  
   - Calculate EMI:  



\[
EMI = \frac{\text{Loan Amount} + (\text{Loan Amount} \times 0.10)}{12}
\]



7. Print approval with EMI or rejection with reason.

---

## ❓ Practice Questions
1. What happens if age = 21 or 60?  
2. Why is the credit score threshold set at 700?  
3. What is the maximum loan amount for a customer earning ₹40,000/month?  
4. How does the program handle existing loans equal to exactly 50% of income?  
5. What formula is used to calculate EMI?

---

## 💻 Sample Input / Output

### ✅ Case 1: Approved
Enter the age: 30
Enter the monthly income: 40000
Enter the credit score(<=900): 750
Enter the existing loan amount: 10000
Enter the loan amount request: 500000

**Output:**
Loan Approved for this customer with EMI of RS. 45833.33

---

### ❌ Case 2: Rejected (Credit Score)
Enter the age: 30
Enter the monthly income: 40000
Enter the credit score(<=900): 650

**Output:**
Loan Rejected because of credit score condition not satisfied

---

## ✅ Result
The program successfully validates customer details and calculates EMI for approved loans, while giving clear rejection reasons for failed conditions.

---

## 🚀 Future Enhancements
- Add GUI for user‑friendly input.  
- Store customer records in a database.  
- Allow multiple repayment periods (1 year, 5 years, etc.).  