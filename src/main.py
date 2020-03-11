"""
 Copyright © 2020 Stephan Hagel (sthagel@uw.edu)
 This file is part of the g.bims project.
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

import algorithms


def rungbims():
    """This is an encapsulation of some setup before running
    g.bims, plus running it and then printing some stats."""
    initial_state = algorithms.graph.CREATE_INITIAL_STATE()
    print("Initial genre:")
    print(initial_state)
    global count, backlinks, max_open_length, solution_path
    count = 0
    backlinks = {}
    max_open_length = 0

    walk_path = algorithms.random_walk(initial_state, 100, 0.5)
    for genre in walk_path:
        print(genre.__str__())

    # This is where the fun begins
    solution_path = algorithms.a_star_search(initial_state)

    # If this code is reached, a solution has been found.
    # TODO: Use the solution to create the playlist instead of just printing it
    print(str(count) + " states expanded.")
    print('max_open_length = ' + str(max_open_length))

    for state in solution_path:
        print(state)


if __name__ == '__main__':
    rungbims()
