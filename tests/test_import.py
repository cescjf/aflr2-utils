#!/usr/bin/env python

"""
This file is part of aflr2-utils.

aflr2-utils is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

aflr2-utils is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with aflr2-utils.  If not, see <http://www.gnu.org/licenses/>.
"""

import aflr2utils.geometry as g
import aflr2utils.distributions as d
import aflr2utils.mesh as m
import matplotlib.pyplot as plt

# Importing geometry from file
segs = g.import_geometry("rae2822.seg")

# Dimensioning connectors
n_u0 = 50
n_u1 = 50
n_l0 = 50
n_l1 = 50

# Creating point distribution object
d_upper0 = d.HyperbolicTangent(n_u0, 1.0e-2)
d_upper1 = d.Uniform(n_u1)
d_lower0 = d.HyperbolicTangent(n_l0, 1.0e-2)
d_lower1 = d.Uniform(n_l1)

# Creating connectors
con_upper0 = m.Connector(segs[0], n_u0)
con_upper1 = m.Connector(segs[1], n_u1)
con_lower0 = m.Connector(segs[2], n_l0)
con_lower1 = m.Connector(segs[3], n_l1)

# Creating point distributions on the connector
con_upper0.create_point_distribution(d_upper1)
con_upper1.create_point_distribution(d_upper1)
con_lower0.create_point_distribution(d_lower1)
con_lower1.create_point_distribution(d_lower1)

c_xu = [n.x for n in con_upper0.nodes+con_upper1.nodes]
c_yu = [n.y for n in con_upper0.nodes+con_upper1.nodes]
c_xl = [n.x for n in con_lower0.nodes+con_lower1.nodes]
c_yl = [n.y for n in con_lower0.nodes+con_lower1.nodes]

for i in range(0, 4):
    plt.plot(segs[i].x_data, segs[i].y_data, "-b")
plt.plot(c_xu, c_yu, "o")
plt.plot(c_xl, c_yl, "o")

plt.axis("equal")

plt.show()


