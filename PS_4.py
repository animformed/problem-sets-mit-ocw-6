def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    res = []
    for year in range(years):
        if year == 0:
            t_fund = salary * save * 0.01
            res.append(t_fund)
        if year > 0:
            t_fund = res[year-1] * (1 + 0.01 * growthRate) + salary * save * 0.01
            res.append(t_fund)
    return res
        
def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord
    
def nestEggVariable(salary, save, growthRates):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    res = [0]
    res[0] = salary * save * 0.01
    for i in range(1, len(growthRates)):
        t_fund = res[i-1] * (1 + 0.01 * growthRates[i]) + salary * save * 0.01
        res.append(t_fund)
    return res
    
def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    res = [0]
    res[0] = (savings * (1 + 0.01 * growthRates[0])) - expenses
    for i in range(1, len(growthRates)):
        t_fund = (res[i-1] * (1 + 0.01 * growthRates[i])) - expenses
        res.append(t_fund)
    return res
    
def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print savingsRecord

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    pre_savings = nestEggVariable(salary, save, preRetireGrowthRates)
    savings = pre_savings[-1] 
    
    low = 0
    high = savings + epsilon
    guess = (low + high) * 0.5
    
    p_savings = postRetirement(savings, postRetireGrowthRates, guess)
    ctr = 1
    
    while abs(p_savings[-1]) > epsilon and ctr <= 100:
        print 'low:', low, 'high:', high, 'guess:', guess, 'postSavings:', postRetirement(savings, postRetireGrowthRates, guess)[-1]
        p_savings = postRetirement(savings, postRetireGrowthRates, guess)
        if p_savings[-1] < 0:
            high = guess
        else:
            low = guess
        guess = ((high + low) * 0.5)
        ctr += 1
    print 'Bi method. Num. iterations:', ctr, 'Estimate:', guess
    return guess
        
def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .001
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print expenses
    # Output should have a value close to:
    # 1229.95548986

testFindMaxExpenses()
