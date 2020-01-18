"""
 Copyright © 2020 Stephan Hagel (sthagel@uw.edu)
 This file is part of my Master of Science project.
 This project is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 This project is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from metal_graph import ADJ

mode = "find"
# TODO: Find a method to switch modes to random_walk

# The genre from which to start the generation
starting_genre = "heavy metal"  # TODO: Find an option to make these genres variable
possible_modes = ["find", "random_walk"]
if mode == "find":
    target_genre = "swobm"
states = {}


def h(s):
    return 0  # TODO: Find a good heuristic

# DISTANCE = {}
# DISTANCE["heavy metal"] = {"hard rock": 100, "progressive metal": 157} ...
# TODO: Find a model for the distances along the edges


class State:
    def __init__(self, name="no name yet"):
        self.name = name

    def __eq__(self, s2):
        return self.name == s2.name

    def __str__(self):
        return self.name

    def __hash__(self):
        return (self.__str__()).__hash__()

    def copy(self):
        # Performs an appropriately deep copy of a state,
        # for use by operators in creating new states.
        news = State()
        news.name = self.name
        return news

    def ith_neighbor_exists(self, i):
        # Tests whether there are enough adjacent genres to go to the i'th.
        return len(ADJ[self.name]) > i

    def move(self, i):
        # Assuming it's legal to transition to the ith neighbor, this does it.
        neighbor = states[ADJ[self.name][i]]
        return neighbor

    def edge_distance(self, s2):
        return 1  # DISTANCE[self.name][s2.name]


def goal_test(s):
    return s.name == target_genre


def goal_message(s):
    return "Target genre found."


class Operator:
    def __init__(self, name, precond, state_transf):
        self.name = name
        self.precond = precond
        self.state_transf = state_transf

    def is_applicable(self, s):
        return self.precond(s)

    def apply(self, s):
        return self.state_transf(s)


def create_all_states():
    for name in ADJ.keys():
        states[name] = State(name)


create_all_states()

CREATE_INITIAL_STATE = lambda: states[starting_genre]

OPERATORS = [Operator("Go to neighboring genre number " + str(i), lambda s, i1=i: s.ith_neighbor_exists(i1),
                      lambda s, i1=i: s.move(i1)) for i in range(6)]

GOAL_TEST = lambda s: goal_test(s)

GOAL_MESSAGE_FUNCTION = lambda s: goal_message(s)
