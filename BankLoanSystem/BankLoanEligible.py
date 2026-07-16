cust_age=int(input("Enter the age: "))
if(21<cust_age<60):
    mon_income=float(input("Enter the monthly income: "))
    if(mon_income>=25000):
        cred_score=int(input("Enter the credit score(<=900): "))
        if(700<=cred_score<=900):
            exs_loan_amt=float(input("Enter the existing loan amount: "))
            if(exs_loan_amt<(0.5*mon_income)):
                loan_amt_req=float(input("Enter the loan amount request: "))
                if(loan_amt_req<(20*mon_income)):
                    EMI=((loan_amt_req+(loan_amt_req*0.1))/12)
                    print(f"Loan Approved for this customer with EMI of RS. {EMI:.2f}")
                else:
                    print("Loan Rejected because of Loan amount condition not satisfied")
            else:
                print("Loan Rejected because of existing loan amount condition not satisfied")
        else:
            print("Loan Rejected because of credit score condition not satisfied")
    else:
        print("Loan Rejected because of monthly income condition not satisfied")
else:
    print("Loan Rejected because of age condition not satisfied")