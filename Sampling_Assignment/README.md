# Sampling_Assignment

In this python code, we have used sampling techniques on a credit card fraud detection dataset 
and then applied various ML models on the dataset to find out which Model,sampling technique combination
gives us the best accuracy.


Following 5 sampling Techniques were used:
1. Random Under Sampler (Sampling1)
2. Random Over Sampler (Sampling2)
3. SMOTE (Sampling3)
4. TOMEK links (Sampling4)
5. Near Miss (Sampling5)


The Sample size was calculates using the following formula: n = Z^2(p(1 – p)/m^2) where: 
n = sample size
Z = z-value (for 95% confidence interval, Z = 1.96)
p = proportion of the minority class (taken as 0.5 for a balanced dataset)
m = margin of error (taken as 0.1 for a sample size of 1000)


Following 5 models were applied on the sampled dataset:
1. Logistic Regression (M1)
2. Decision Tree Classifier (M2)
3. Random Forest Classifier (M3)
4. Support Vector Classifier (SVC) (M4)
5. Extra Tree Classifier (M5)


On execution of the code, following results were obtained:
The cells of the table represent accuracy of the applied model using the respective sampling technique.

![Screenshot from 2023-02-19 01-50-04](https://user-images.githubusercontent.com/71625050/219893357-dc43f216-8e2e-4a83-a758-60f7ef440063.png)

As we can see from the table the Maximum Accuracy obtained is of 99.35% on the following combinations:

1. Logistic Regression with Random Over Sampler, Smote and Tomek
2. Random Forest Classifier with Random Over Sampler, Smote and Tomek
3. Support Vector Classifier with Random Over Sampler, Smote and Tomek
4. Extra Tree Classifier with Random Over Sampler, Smote and Tomek




