import math

class HighScoreTable:
    def __init__(self, limit, scores):
        self.limit = limit
        self.scores = scores

    def update(self, player_score):
        compare_scores_list = self.scores

        if len(compare_scores_list) < self.limit:
            self.scores.append(player_score)
            
        else:
            for player in compare_scores_list:
                if player_score['score'] > player['score']:
                    compare_scores_list.append(player_score)
                    break
                else:
                    self.scores = compare_scores_list
        compare_scores_list = sorted(compare_scores_list, key=lambda person: person['score'], reverse=True)
        compare_scores_list = compare_scores_list[0:self.limit]
        self.scores = compare_scores_list
    
    def average_score(self):
        average = 0
        for score in self.scores:
            average += math.ceil(score['score'] / len(self.scores))
        return average
    
    def highest_scorer(self):
        try:
            return self.scores[0]
        # except Exception as error:
        #     return error
        except IndexError:
            return 'there are no high scores in scores'

    def lowest_scorer(self):
        try:
            return self.scores[len(self.scores) - 1]
        except IndexError as error:
            return 'there are no high scores in scores'
    
    def reset(self):
        try:
            list_is_not_empty = self.scores[1]
            self.scores.clear()
        except IndexError:
            return 'unable to reset as there are no high scores'

        



# errors are exceptions
# BaseException
#     Exception

# TypeError   
# SyntaxError
# IndexError


# .catch(error)
#     console.log(error)
#     404


        



