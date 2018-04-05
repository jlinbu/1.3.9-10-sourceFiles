
 
team_name = 'HellaZach' # Only 10 chars displayed.
strategy_name = 'Betray if not Collude'
strategy_description = 'Betray if they betray'
   
def move(my_history, their_history, my_score, their_score):
    '''Arguements accepted: my_history, their_history are str
    their_score, my_score are int.
    Make my move
    return 'b', 'c'''
    if 'c' in their_history:
        return 'c'
    else:
        return 'b'

def test_move(my_history, their_history, my_score, their_score, result):
    '''
    calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Rturns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
                ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                           str(my_score), str(their_score)])+
                ") returned " + "'" + real_result + "'" +
                " and should have returned '" + result + "'")
        return False
 
if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='',
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='',
              their_history='',
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0,
              their_score=0,
              result='b')