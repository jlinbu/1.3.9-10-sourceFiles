####
# Each team's file must define four tokens:
#     team_name: Orthinger
#     strategy_name: Collude until betray 5
#     strategy_description: Always collude, until they betray five times.
#     move: A function that returns 'c' or 'b'
####

team_name = 'Orthinger'
strategy_name = 'Collude until betray 5'
strategy_description = 'Always collude, until the other betrays 5 times.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]/
    
    Returns 'c' or 'b' for collude or betray.
    ''' 
    betraycount=0
    for move in their_history:
        if betraycount == 5:
            return 'b'
        elif move=='b':
            betraycount=betraycount+1
            return 'c'
        if move == 'c':
            return 'c'
            