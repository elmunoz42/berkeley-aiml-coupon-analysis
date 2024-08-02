# Will a Customer Accept the Coupon?

## Harnessing the Power of BI Analytics: An Exploration using Correlation Matrices and Pandas DataFrame Queries

## 1. Introduction

In the dynamic landscape of today's consumer market, understanding customer behavior is paramount. This project delves into the intriguing question of what influences a driver's decision to accept a coupon delivered to their cell phone while on the road based on geofencing triggers. Is it the type of establishment - a restaurant, a bar, or a coffee house? Does the presence of passengers, the weather, or the time of day sway the decision?

To unravel these complexities, we embark on an exploratory journey through a rich dataset sourced from the [UCI Machine Learning repository, collected via a survey on Amazon Mechanical Turk.](https://archive.ics.uci.edu/dataset/603/in+vehicle+coupon+recommendation) The survey captures a variety of driving scenarios and the driver's decision to accept or reject a coupon under those circumstances.

Our analysis employs a systematic approach, beginning with a comparative study of different coupons using bar plots. This visual exploration aids in discerning patterns and trends across coupon types. We then delve deeper, constructing a correlation matrix for each coupon type to identify potential areas of interest. Finally, we perform targeted comparisons by querying the data, investigating how different combinations of features influence the coupon acceptance ratio.

This project not only aims to distinguish between customers who accepted a driving coupon versus those who did not, but also seeks to provide insights that could inform targeted marketing strategies and enhance customer engagement. The findings from this analysis will be presented in a comprehensive report, highlighting key insights and actionable recommendations.

It is important to note that much more analysis is possible with this dataset. We had to make choices and explore certain scenarios in depth but not others. Specifically, we only looked at the Coffee House, Restaurant(<20) and Bar coupons. With a deeper dive on the Bar coupon.

## 2. Data Overview

The dataset used in this analysis is a rich collection of information detailing various driving scenarios and the driver's decision to accept or reject a coupon under those circumstances. The data, sourced from the UCI Machine Learning Repository, provides a comprehensive view of the factors that might influence a driver's decision to accept a coupon.

The dataset comprises three main categories of attributes:

### User Attributes

These attributes provide demographic information about the users, including their gender, age, marital status, number of children, education, occupation, and annual income. It also includes lifestyle information such as the frequency of visits to bars, coffee houses, and restaurants with an average expense of less than $20 per person.

### Contextual Attributes

These attributes describe the context in which the coupon was offered. They include the driving destination, the geographical location of the user, the coupon venue, and the destination. They also detail the weather conditions, temperature, time of day, and the presence of passengers in the vehicle.

### Coupon Attributes

These attributes provide information about the coupon itself, including the time before it expires.

This diverse set of attributes allows for a comprehensive analysis of the factors influencing a driver's decision to accept a coupon. The subsequent sections will delve into a detailed analysis of these attributes and their impact on coupon acceptance.

## 3. Methodology

Our approach to analyzing this dataset involved several key steps to ensure the data was clean, relevant, and ready for analysis.

### Data Cleaning

The first step in our methodology was data cleaning. This involved:

- **Removing columns with excessive missing data**: Columns with too many missing values can skew the analysis and lead to inaccurate results. We identified such columns and removed them from our dataset.
- **Handling null values**: We also dealt with null values in our dataset. Depending on the nature of the data and the extent of the null values, we either filled them with appropriate values or removed the rows containing these null values.
- **One-hot encoding**: For categorical variables, we used one-hot encoding. This technique transforms a category value into a new column and assigns a 1 or 0 (True/False) value to the column. This method is effective for handling categorical data without imposing an arbitrary order on the categories.

### Data Analysis Methodology

Once the data was cleaned, we moved on to the analysis phase. This involved:

- **Data Exploration**: We began our analysis by exploring the data using bar graphs. This helped us understand the distribution of different variables in our dataset and identify any noticeable trends or patterns.
- **Correlation Matrix**: We used a correlation matrix to understand the relationship between different variables in our dataset. This helped us identify patterns and trends in the data, and guided our subsequent analysis. We leveraged the Seaborn heatmap plots
- **Data Queries**: We performed targeted queries on our pandas dataframe to investigate specific combinations of features and their impact on coupon acceptance.

This systematic approach allowed us to thoroughly explore the dataset and derive meaningful insights from it.

## 4. Analysis

- Present the overall analysis of all the coupons compared to each other.
- Discuss the correlation matrix for the Bar, Inexpensive Restaurant, and Coffee House coupons.
- Deep dive into the bar coupons and specific populations. Discuss how their coupon acceptance ratio differs from other users.

## 5. Findings

- Clearly state the problem for the specific coupon group.
- Present visualizations that demonstrate exploring differences in those who accepted and rejected the coupon.
- Interpret the descriptive and inferential statistics in a concise manner.
- Highlight actionable items in their own section.

## 6. Conclusion and Recommendations

- Summarize the key findings from your analysis.
- Provide recommendations based on your findings.
- Discuss potential next steps or further analyses that could be done.

## 7. References

- Cite any external sources used in your analysis.
  In-Vehicle Coupon Recommendation. (2020). UCI Machine Learning Repository. https://doi.org/10.24432/C5GS4P.
