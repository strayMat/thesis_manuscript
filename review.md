# Before thesis

## Pete's review, general comments

- p.51, chapter prediction: 
  - Even with over 3M national cases, I wonder whether this method is handicapped by the rareness of most specific sequences of data occurrences. Do you use the dimension-reduction methods from SVD-PPMI for this transformer model as well?
  - In my experience, it's often helpful to include a prediction gap between the end of the observation period and the beginning of the follow-up. Because of the uncertain timing of recorded observations, without such a gap, there is risk of leaking data from the outcomes to the predictors. 

## Florence

- chap 2: "étude en cours" 
- chap3: A noter qu’il est dit qu’en santé, les évènements sont rares (et donc que les modèles parcimonieux sont plus adaptés), ce qui n’est pas toujours le ca

- Contraste causal, et donc la question des censures informatives ? 

- Pourquoi le biais de temps immortel est-il qualifié de biais subtil ?

- For continuous outcomes, risk difference is a natural estimand