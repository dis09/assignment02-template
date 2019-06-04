## Exercise 1: two-sample t-test with the `youtube` dataset (45 + 35 points)

Consider our `youtube` zip-archived`.csv` data-set of trending Youtube videos and the channels [RT Deutsch](https://www.youtube.com/user/rtdeutsch) and [ZDF](https://www.youtube.com/ZDF). Are there significant differences between the two channels regarding the average views, likes or number of comments per video? To answer this question follow these steps:

1. Preparations and hypotheses

    - Read in the `youtube.zip` dataset and create two arrays that contain the likes for the videos of the channels `'ZDF'` and `'RT Deutsch'`, respectively.
    - In our data-set, how many videos belong to the channel `'ZDF'`? How many belong to `'RT Deutsch'`? Store the results in the variables `n_zdf` (5) and `n_rt` (5).  
    - Calculate the average likes per video for both channels and store the results in the variables `mean_likes_zdf` (5) and `mean_likes_rt` (5).


2. Significant differences between the average likes per video

      - In your *report* answer the following questions (max 1 sentence per question): What is your null hypothesis? What is your alternative hypothesis? Looking at the average likes, what do you think will be the outcome of the test (-> *report*, 15)?
      - Perform a two-sample t-test with the function [`scipy.stats.ttest_ind`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ttest_ind.html) from the `scipy.stats` package. We do not perform a F-test and just assume equal population variances.  
      - Store the result of the test function in a variable with the name `test_likes` (15).


3. Extensions and interpretation

    - Perform the same test for the average number of views per video and the average number of comments per video. Store the test results in the variables `test_views` (5) and `test_comments` (5).
    - In your *report*, analyze the test results for the three tests (max 1-3 short sentence per question). How do you interpret the p-value? Which null hypotheses can be rejected (-> *report*, 20)?

Notes

  - You are free to use the `pandas` library or your own methods for reading in and handling the data.
  - Only use the `./exercises/ex1.py` file to solve the programming part of this exercise.


## Exercise 2: Simulated asymptotic behavior of the sample mean (20 + 30 points)

Look at the code in `./exercises/ex2.py`. Read the code line by line and try to understand how its works. A hint:
  - the function [`numpy.random.normal`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.normal.html) from the `numpy.random` package simulates random values from the [normal distribution](https://de.wikipedia.org/wiki/Normalverteilung).
  - In our case we simulate values from the normal distribution with a population mean of `4` and a population standard deviation of `1`.

Add useful comments that explain each line of code (20). Change the sample sizes in `N` or the number of simulations `S`. What do the final variables `means_deviations` contain? In your report try to answer the following questions (max 1-3 short sentences per question):

  - Why is the empirical sample mean not exactly equal to the true population mean of `4` (10)?
  - What happens to the standard deviation of the sample means if you increase the sample size `n` (10)?
  - Why is it usually better to have a larger sample size `n` when doing statistical analyses, surveys or hypothesis testing (10)?
  - Read about bias ("Erwartungstreue") and consistency ("Konsistenz") of a statistical estimator, e.g. [here](https://stats.stackexchange.com/questions/31036/what-is-the-difference-between-a-consistent-estimator-and-an-unbiased-estimator).
