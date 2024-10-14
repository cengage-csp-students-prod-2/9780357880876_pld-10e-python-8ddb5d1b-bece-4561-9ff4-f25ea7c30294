Declare and initialize the variables:double salary = 1250.00;int numDependents = 2;double stateTax, federalTax, dependentDeduction, totalWithholding, takeHomePay;

Calculate the state withholding tax:stateTax = salary * 0.065;

Calculate the federal withholding tax:federalTax = salary * 0.28;

Calculate the dependent deductions:dependentDeduction = salary * 0.025 * numDependents;

Calculate the total withholding:totalWithholding = stateTax + federalTax + dependentDeduction;

Calculate the take-home pay:takeHomePay = salary - totalWithholding;
