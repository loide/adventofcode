"""
--- Day 6: Universal Orbit Map ---

You've landed at the Universal Orbit Map facility on Mercury. Because
navigation in space often involves transferring between orbits, the
orbit maps here are useful for finding efficient routes between, for
example, you and Santa. You download a map of the local orbits (your
puzzle input).

Except for the universal Center of Mass (COM), every object in space is
in orbit around exactly one other object. An orbit looks roughly like
this:

                  \
                   \
                    |
                    |
AAA--> o            o <--BBB
                    |
                    |
                   /
                  /

In this diagram, the object BBB is in orbit around AAA. The path that
BBB takes around AAA (drawn with lines) is only partly shown. In the map
data, this orbital relationship is written AAA)BBB, which means "BBB is
in orbit around AAA".

Before you use your map data to plot a course, you need to make sure it
wasn't corrupted during the download. To verify maps, the Universal
Orbit Map facility uses orbit count checksums - the total number of
direct orbits (like the one shown above) and indirect orbits.

Whenever A orbits B and B orbits C, then A indirectly orbits C. This
chain can be any number of objects long: if A orbits B, B orbits C, and
C orbits D, then A indirectly orbits D.

For example, suppose you have the following map:

COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L

Visually, the above map of orbits looks like this:

        G - H       J - K - L
       /           /
COM - B - C - D - E - F
               \
                I
In this visual representation, when two objects are connected by a line,
the one on the right directly orbits the one on the left.

Here, we can count the total number of orbits as follows:

D directly orbits C and indirectly orbits B and COM, a total of 3 orbits.
L directly orbits K and indirectly orbits J, E, D, C, B, and COM, a
total of 7 orbits.
COM orbits nothing.
The total number of direct and indirect orbits in this example is 42.

What is the total number of direct and indirect orbits in your map data?
"""


import os
import sys


def mapping_orbits(FILEPATH):
    orbitmap = {}

    with open(FILEPATH) as f:
        line = f.readline()
        while line:
            left, right = line.strip().split(")")
            # Add key pair: right object orbits around left object
            orbitmap[right] = [left]

            # If the orbit is already in the map, add the indirect orbits to it
            if left in orbitmap:
                orbitmap[right] = orbitmap[right] + orbitmap[left]

            # check if the right object which orbits around left object is
            # already added in the map as a left side
            # if it is true, update the indirect orbits list
            if right in [item for value in orbitmap.values() for item in value]:
                for key, value in orbitmap.items():
                    if right in value:
                        orbitmap[key] = orbitmap[key] + orbitmap[right]
            line = f.readline()

    return orbitmap


def count_total_orbits(m):
    return sum([len(m[item]) for item in m])


def minimum_number_of_orbital_transfers(m):
    # Get the objects list that YOU are orbiting around
    search_queue = m['YOU']

    # Get the objects list that SAN is orbiting around
    santa_queue = m['SAN']

    # Search for the minimum common orbit object between YOU and SAN
    for position, item in enumerate(santa_queue):
        if item in search_queue:
            n_transfers = search_queue.index(item)
            break

    return position + n_transfers


def main():
    FILEPATH = 'input.txt'

    # Check if the file exists
    if not os.path.isfile(FILEPATH):
        print("File path {} does not exist. Exiting...".format(FILEPATH))
        sys.exit()

    # Create orbit map from input file
    orbit_map = mapping_orbits(FILEPATH)
    print("Total orbits:", count_total_orbits(orbit_map))
    n = minimum_number_of_orbital_transfers(orbit_map)
    print("Minimum Number of Orbital Transfers:", n)


if __name__ == "__main__":
    main()
