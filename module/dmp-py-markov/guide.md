# Markov Chains
### Python Programming

## Overview
[image](image_overview.jpg)
* Probabilities
* Expectations
* What is weather tomorrow?
* Independence
* Dependence
* Assumptions
* Transition
* Problem
* Solution
* Monte Carlo
* Convergence
* Exercise

## Probabilities
[figure](fig_design_table.jpg)
* Two designs 
* Marketing survey
* .. Which design to push to market?


## Expectations
[graphic](tip_howmuch.jpg)
* Survey of 1000
* .. Interest/person = 1 for yes, 0 for no
* .. Design A - 420 interested
* ... ((420 x 1) + (580 x 0))/ 1000 x 17.45 = 7.24 GBP
* .. Design B - 350 interested
* ... ((350 x 1) + (650 x 0))/ 1000 x 24.23 = 8.48 GBP  

## Probabilities and Expectations
* Given the sale of both
* .. How much would be made on average?
* .. 1000 products
* ... 500 Design A:   		500 x 0.42 = 210 sold
* .... profit:  210 x 17.45 = 3664.5 GBP
* ... 500 Design B:   		500 x 0.35 = 175 sold
* .... profit:  175 x 24.23 = 4240.25 GBP
* Overall - per attempt
* .. (3664.5 + 4240.25)/1000 = 7.90 GBP


## What is weather tomorrow?
[graphic](sunrain.jpg)

## Independence
* Simplify
* .. If it does not rain then it will be sunny
* Suppose
* .. The weather today has no affect on the weather tomorrow
* Probabilities
* .. Sun: 60%
* .. Rain: 40%


## The Independent Future
[graphic](future_questions.jpg)
* Given it is sunny today
* .. what are the chances of rain tomorrow?
* ... 60% sun
* ... 40% rain
* .. What about the day after tomorrow?
* .. 60% sun
* ... 40% rain

## The Far Future
* Probability of rain tomorrow and the day after?
* .. Probability of rain tomorrow  
* ... X  
* .. Probability of rain the day after
* ... 0.4 * 0.4 = 0.16 

## Dependence
* What if the weather tomorrow depends on the weather today?
* .. If it is sunny today
* ... 60% sun tomorrow
* ... 40% rain tomorrow
* .. If it is raining today
* ... 40% sun tomorrow
* ... 60% rain tomorrow

## The Dependent Future
[graphic](future_questions.jpg)
* Given sun today
* .. Tomorrow there is 40% chance of rain
* If tomorrow rains
* .. The day after tomorrow there is 60% chance of rain
* Probability of raining in the next two days
* .. Probability it rains tomorrow  
* ... X  
* Probability it rains the day after given it rains tomorrow
* ... 0.4 * 0.6  = 0.24

## Markov Chains
* A sequence of observations
* .. rain, sun, sun, sun, rain
* .. next depends on the previous
* Probability Notation
* .. P(S|S):       P of sun tomorrow given sun today
* .. P(R|S):       P of rain tomorrow given sun today
* .. P(S|R):       P of sun tomorrow given rain today
* .. P(R|R):       P of rain tomorrow given rain today
* .. P(R|S,R):     P of ain in two days, given sun today and rain tomorrow
* .. P(R|R,R):     P of of rain in two days, given rain today and tomorrow 

## Markov Assumptions
* The first order Markov Chain assumes
* .. Tomorrow only depends on today
* ... not days further in the past
* ... not days in the future

## Example
* Suppose 
* ... today there is 80/20 chance it is going to rain
* What is the chance of raining tomorrow?

## Transition Matrix I
* Formula for the transition matrix
[figure](transition_matrix_1.jpg)


## Transition Matrix II 
* As a matrix equation
[figure](transition_matrix_2.jpg)


## Transition Matrix II 
* Matrix multiplication gives probability
[figure](transition_matrix_3.jpg)


## The Day After Tomorrow? I
* The same formula applies
[figure](day_after_tomorrow_1.jpg)


## The Day After Tomorrow? II
* Probabilities for the day after tomorrow
[figure](day_after_tomorrow_2.jpg)


## One year later? I
* How about 365 days later?
[figure](one_year_later_1.jpg)

## One year later? II
* How do you compute M^365?
* .. use a computer!
[figure](one_year_later_2.jpg)


## Calculating
[code](calculating.py)
* Python + NumPy
* .. Efficient
* Matrix multiplication
* Calculate
* .. Transition X state:   @
* .. Transition ^ 365:   for loop


## Question
* Today is sunny
* .. In the next 365 days
* ... how many days do we expect will be rain?

## Problem
* Not
* .. Will it rain in 365 days time
* Rather
* .. If we count number of raining days in a year
* .. If we repeat this over many many years
* On average:  
* .. How many days in a year will it rain?
* ... ( Ignoring leap years )

## Solution
* Hard way
* .. Pen and paper: solve a geometric series
* Easy way
* .. Use a computer (Python)
* .. Work out whether it will rain for every day of the year
* .. Many times
* .. Compute the averages

## Monte Carlo
[graphic](dice.jpg)
* History
* .. First published by Stanislaw Ulam, 1946
* .. Radiation shielding in nuclear weapons programme
* Use
* .. Estimate expectation values of random variables
* .. Integration
* Methodology
* .. Generate an outcome for an event based on given probabilities
* .. Repeat many number of times
* .. Average = the expectation value

## One Event
* One event 
* .. eg. Counting number of raining days in 365 days
* ... Every day will be either rain or sunny
* ... Every repeat of such event will yield different result

## State
[code](state.py)
* State is a pair 
* .. tuple, list or np.array of length two
* ... probability of sun
* ... probability of rain
* Given today is sunny
* .. P(sun_today) = (1, 0)

## Transition
* Encode transition matrix 
* .. list of list or NumPy array
[code](transition.py)
[image](transition_code_1.jpg)


##  Probability
* NumPy provides matrix multiplication
[code](probability.py)
[image](probability_code_1.jpg)

##  Sample Space
[code](sample_space.py)
* State gives probabilities
* .. outcome is binary: sun or rain
* Pick one based on the probabilities
* To pick with probability 0.4?
* .. Random float from 0 to 1
* .. If less than 0.4,  score positive
* .. otherwise, score negative

##  Sequencing
[code](sequencing.py)

* Repeat for every day
* .. tomorrow becomes today
* Count the number of days it rains
* .. Use a for loop
* Output of every run should be different


## n Events
[code](n_events.py)
* Repeat the one Monte Carlo simulation
* .. n times
* Remember the number of raining days each time
* .. Calculate average after n events
* .. For large n
* .. Average aproximates solution

## Convergence
[graphic](tip_convergence.jpg)
* As n_events increase
* .. The calculated average converges to a stable value
* In theory
* .. average tends to the true solution as n_events tends to infinity
* In practice
* .. average converges after n_events > 10000

##  Exercise
### Markov Chains 

## Exercise Problem
[graphic](qa/qa_exercise.jpg)
* Markov Weather
* .. Change the n_event numbers
* ... Run the script many times, observe variations in the output
* ... Does the size of variations change as you increase n_events?
* .. Do you get a different outcome if you change the probabilities in the transition matrix?
* Markov Stocks
* .. Write a program to predict stock prices using Monte Carlo simulation and Markov Chains
* .. Follow the instructions given in the exercise
* Extra 
* .. Write a script that would automatically check for convergence

## Summary
[slide](overview)

# Thank you
### Markov Chains
