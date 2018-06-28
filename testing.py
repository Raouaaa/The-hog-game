def announce_highest(who, previous_high=0, previous_score=0):
    """Return a commentary function that announces when WHO's score
    increases by more than ever before in the game.

    >>> f0 = announce_highest(1) # Only announce Player 1 score gains
    >>> f1 = f0(11, 0)
    >>> f2 = f1(11, 1)
    1 point! That's the biggest gain yet for Player 1
    >>> f3 = f2(20, 1)
    >>> f4 = f3(5, 20) # Player 1 gets 4 points, then Swine Swap applies
    19 points! That's the biggest gain yet for Player 1
    >>> f5 = f4(20, 40) # Player 0 gets 35 points, then Swine Swap applies
    20 points! That's the biggest gain yet for Player 1
    >>> f6 = f5(20, 55) # Player 1 gets 15 points; not enough for a new high
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    if who ==0 :
        if previous_score> previous_high:
            previous_high=previous_score
            if previous_score>1:
                print(previous_score,'points! Thats the biggest gain yet for Player 1')
                #print('Thats the biggest gain yet for Player 1')
            elif previous_score==1:
                print(previous_score,'point! Thats the biggest gain yet for Player 1')
                print('Thats the biggest gain yet for Player 1')
        else: 
            print('Player 1 gets ',previous_score,'point ; not enough for a new high')
    elif who==1:
        if previous_score> previous_high:
            previous_high=previous_score
            if previous_score>1:
                print(previous_score,'points! Thats the biggest gain yet for Player 2')
                #print('Thats the biggest gain yet for Player 2')
            elif previous_score==1:
                print(previous_score,'point! Thats the biggest gain yet for Player 2')
                #print('Thats the biggest gain yet for Player 2')
        else:
            print('Player 2 gets ',previous_score,'point ; not enough for a new high')
who=0
f0=announce_highest(who,10,1)
