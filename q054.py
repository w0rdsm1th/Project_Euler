
import csv
from collections import Counter

"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

1: High Card: Highest value card.
2: One Pair: Two cards of the same value.
3: Two Pairs: Two different pairs.

4: Three of a Kind: Three cards of the same value.
5: Straight: All cards are consecutive values.
6: Flush: All cards of the same suit.
7: Full House: Three of a kind and a pair.
8: Four of a Kind: Four cards of the same value.
9: Straight Flush: All cards are consecutive values of same suit.
10: Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below).
But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

"""

"""LEARNINGS
- initially tried too many passes over the hand
- initially wasnt passing back tie breakers
- testing for most frequent/probable to least
"""

# confused by card value "T" (found = 10), so doing some stats of occurrences
# unique_card_vals = set()
# with open("q054_poker.txt", 'r') as f:
#     all_hands = csv.reader(f)
#     for each_hand in all_hands:
#         cards_in_hand = each_hand[0].split(" ")
#         unique_card_vals.update([crd[0] for crd in cards_in_hand])
# print("unique_card_vals: ", unique_card_vals)

"""simplify
single pass: 
    sort descending by card value, count occurrences of value and suit
gather repeated 
"""


def _get_hand_stats(hnd):
    face_card_ordinal_map = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14, }

    # optimisation - create counter as extract card values from hand
    vals = [face_card_ordinal_map.get(crd[0]) if crd[0] in face_card_ordinal_map else int(crd[0]) for crd in hnd]
    suits = [crd[1] for crd in hnd]

    occ_counter = Counter(vals)
    occ_counter_tuples = [(crd_val, occ) for crd_val, occ in occ_counter.items()]

    # sort on number of occurrences, then card value
    occ_counter_tuples = sorted(occ_counter_tuples, key=lambda x: (x[1], x[0]), reverse=True)

    return occ_counter_tuples, len(set(suits))


def _hand_val(hnd):
    hand_stats = _get_hand_stats(hnd)
    if hand_stats[1] == 1:  # flush
        if [_[0] for _ in hand_stats[0]] == list(range(hand_stats[0][0][0],
                                                       hand_stats[0][-1][0] - 1,
                                                       -1)) and len(hand_stats[0]) == 5:
            if hand_stats[0][0][0] == 14:  # royal flush
                return 10, "royal flush"

            # straight flush, N high
            return 9, "straight flush, high card {0}".format(hand_stats[0][0][0]), hand_stats[0]

        else:
            return 6, "flush, high card {0}".format(hand_stats[0][0][0]), hand_stats[0]

    if hand_stats[0][0][1] == 4:
        return 8, "four of a kind of {0}".format(hand_stats[0][0][0]), hand_stats[0]

    if hand_stats[0][0][1] == 3:
        if hand_stats[0][1][1] == 2:
            return 7, "full house, {0} full of {1}".format(hand_stats[0][0][0],
                                                           hand_stats[0][1][0]),\
                   hand_stats[0]
        else:
            return 4, "three of a kind of {0}".format(hand_stats[0][0][0]), hand_stats[0]

    if [_[0] for _ in hand_stats[0]] == list(range(hand_stats[0][0][0],
                                                   hand_stats[0][-1][0] - 1,
                                                   -1)) and len(hand_stats[0]) == 5:
        return 5, "straight, high card {0}".format(hand_stats[0][0][0]), hand_stats[0]

    if hand_stats[0][0][1] == 2:
        if hand_stats[0][1][1] == 2:
            return 3, "two pair, {0} and {1}".format(hand_stats[0][0][0], hand_stats[0][1][0]), hand_stats[0]

        else:
            return 2, "one pair of {0}".format(hand_stats[0][0][0]), hand_stats[0]
    else:
        return 1, "high card, {0}".format(hand_stats[0][0][0]), hand_stats[0]


def poker_win_calculator(p1_hand, p2_hand):
    p1_score, p1_msg, p1_sorted_hand = _hand_val(p1_hand)
    p2_score, p2_msg, p2_sorted_hand = _hand_val(p2_hand)

    if abs(p1_score - p2_score) == 0:

        for p1_crd, p2_crd in zip(p1_sorted_hand, p2_sorted_hand):
            if p1_crd[0] > p2_crd[0]:
                return 1, 0
            elif p1_crd[0] < p2_crd[0]:
                return 0, 1
            else:
                continue

        print("dead lock remains!",
              "p1_hand", p1_hand, p1_msg,
              "p2_hand", p2_hand, p2_msg,
              "\n")

    return p1_score, p2_score


if __name__ == '__main__':
    p1_wins, p2_wins, deadlock_count = 0, 0, 0
    with open("q054_poker.txt", 'r') as f:
        all_hands = csv.reader(f)

        for each_hand in all_hands:
            cards_in_hand = each_hand[0].split(" ")
            p1_hand, p2_hand = cards_in_hand[0:5], cards_in_hand[5:]

            this_hand_score = poker_win_calculator(p1_hand, p2_hand)

            if this_hand_score[0] > this_hand_score[1]:
                p1_wins += 1
            elif this_hand_score[0] < this_hand_score[1]:
                p2_wins += 1
            else:
                deadlock_count += 1

    print("p1 wins: ", p1_wins,
          "p2 wins: ", p2_wins,
          "deadlocks: ", deadlock_count)

