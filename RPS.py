# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)

    win_play = { 
      "R":"P",
      "P":"S",
      "S":"R"
    }

    counter_play = { 
      "R":"P",
      "P":"S",
      "S":"R"
    }

   if (len(opponent_history)>1) and (len(my_history)>1):
     if ((opponent_history[-3]!="") and (opponent_history[-2]!="") and (opponent_history[-1]!="")):
       if(opponent_history[-3]=="R") and (opponent_history[-2]=="P")and(opponent_history[-1]=="S") and (my_history[-3]!="") and(my_history[-2]!="") and (my_history[-1]!="") and (my_history[-3]=="R") and     
       (my_history[-2]=="S") and (my_history[-1]=="P")):
         values_view = counter_set.values()
         value_iterator = iter(values_view)
         first_value = next(value_iterator)
         guess = first_value
       elif ((opponent_history[-3]=="S") and(opponent_history[-2]=="R") and (opponent_history[-1]=="P") and(my_history[-3]!="") and(my_history[-2]!="") and (my_history[-1]!="") and (my_history[-3]=="R") and 
       (my_history[-2]=="P") and (my_history[-1]=="S")):
         guess = counter_set["R"]
       elif ((opponent_history[-3]=="R") and (opponent_history[-2]=="S") and (opponent_history[-1]=="P") and (my_history[-3]!="") and(my_history[-2]!="") and (my_history[-1]!="") and (my_history[-3]=="S") and    
       (my_history[-2]=="P") and (my_history[-1]=="R")):
        guess = counter_set["S"]
       elif (winning_set[my_history[-1]]==prev_play):
        guess = winning_set[prev_play]
       else:
        if not prev_play:
          prev_play = 'R'
        opponent_history.append(prev_play)

        last_three = "".join(opponent_history[-3:])
        if len(last_three) == 3:
          play_order[0][last_three] += 1

        posible_plays = [
            prev_play + "R" + "R",
            prev_play + "R" + "P",
            prev_play + "R" + "S",
            prev_play + "P" + "R",
            prev_play + "P" + "P",
            prev_play + "P" + "S",
            prev_play + "S" + "R",
            prev_play + "S" + "P",
            prev_play + "S" + "S",
        ]

        int_order = { k: play_order[0][k] for k in posible_plays if k in play_order[0] }

        prediction = max(int_order, key=int_order.get)[-1:]

        response = {'P': 'S', 'R': 'P', 'S': 'R'}
        guess = response[prediction]

      
               
      else:
        guess = "P"
      my_history.append(guess)
    return guess