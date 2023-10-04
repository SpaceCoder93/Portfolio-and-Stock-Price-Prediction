        lam_fun = lambda title: vader.polarity_scores(title)['compound']
