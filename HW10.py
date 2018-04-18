import ParameterClasses as P
import MarkovModel as MarkovCls
import SupportMarkovModel as SupportMarkov
import scr.SamplePathClasses as PathCls
import scr.FigureSupport as Figs



# QUESTION 1
# create and simulate cohort with treatment
cohort1 = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.ANTICOAG)

simOutputs1 = cohort1.simulate()
#print out discounted total cost and discounted total utility
SupportMarkov.print_outcomes(simOutputs1, 'Anticoagulation:')

# create and simulate cohort with out treatment
cohort2 = MarkovCls.Cohort(
    id=2,
    therapy=P.Therapies.NONE)

simOutputs2 = cohort2.simulate()
#print out discounted total cost and discounted total utility
SupportMarkov.print_outcomes(simOutputs2, 'No treatment:')

# QUESTION 2
#print out  change in the expected discounted cost, the expected discounted utility, and the expected number of strokes
SupportMarkov.print_comparative_outcomes(simOutputs2,simOutputs1)

# QUESTION 3 and 4
#  cost-utility plane and net monetary benefit curve
SupportMarkov.report_CEA_CBA(simOutputs2,simOutputs1)
print("When willingness-to-pay is more than 15000, i will recommend to use the anticoagulation.")

# QUESTION 4
