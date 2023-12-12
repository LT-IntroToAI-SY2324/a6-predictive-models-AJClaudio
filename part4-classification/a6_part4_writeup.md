# Part 4 - Classification Writeup

After completing `a6_part4.py` answer the following questions

## Questions to answer

1. Comment out the StandardScaler and re-run your test. How accurate is the model? Why is that?

if we take out standardscaler and rerun the test it will lose accuracy going from .85 to .63. this is because the data is not standardized.

2. How accurate is the model with the StandardScaler? Is this model accurate enough for the given use case? Explain.

the StandardScalar is a lot more accurate which is seen when it is .12 more accurate than without the standardscalar, I think this model is accurate enough for the given case.

3. Looking at the predicted and actual results, how did the model do? Was there a pattern to the inputs that the model was incorrect about?

the model did good when being tested predicted and actual results.I didnt seen any patterns toward the inputs.

4. Would a 34 year old Female who makes 56000 a year buy an SUV according to the model? Remember to scale the data before running it through the model.

no