"""
 Copyright © 2020 Stephan Hagel (sthagel@uw.edu)
 This file is part of my Master of Science project.
 This project is free software: you can redistribute it and /gor modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 This project is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <https: /g/www.gnu.org/licenses/>.
"""

ADJ = {}
ADJ["psychodelic rock"] = ["hard rock"]
ADJ["blues rock"] = ["hard rock"]
ADJ["garage rock"] = ["hard rock", "punk rock"]
ADJ["hard rock"] = ["heavy metal", "shock rock"]
ADJ["shock rock"] = ["hard rock", "heavy metal", "glam metal"]
ADJ["heavy metal"] = ["hard rock", "shock rock", "glam metal", "progressive metal", "nwobhm", "traditional doom metal",
                      "post metal", "folk metal", "death metal"]
ADJ["glam metal"] = ["shock rock", "heavy metal", "visual kei"]
ADJ["visual kei"] = ["glam metal", "gothic rock"]
ADJ["gothic rock"] = ["punk rock", "visual kei", "goth metal"]
ADJ["goth metal"] = ["traditional doom metal", "gothic rock", "symphonic metal"]
ADJ["progressive metal"] = ["heavy metal", "neo-classical metal"]
ADJ["nwobhm"] = ["heavy metal", "punk rock", "speed metal"]
ADJ["punk rock"] = ["garage rock", "nwobhm", "original hardcore punk", "gothic rock"]
ADJ["neo-classical metal"] = ["progressive metal", "speed metal"]
ADJ["speed metal"] = ["nwobhm", "thrash metal", "melodic power metal", "us power metal"]
ADJ["traditional doom metal"] = ["heavy metal", "goth metal", "sludge metal", "stoner metal", "death/doom",
                                 "drone metal"]
ADJ["sludge metal"] = ["traditional doom metal", "grunge"]
ADJ["grunge"] = ["sludge metal", "nu metal", "original hardcore punk"]
ADJ["rap metal"] = ["groove metal", "nu metal"]
ADJ["groove metal"] = ["rap metal", "thrash metal", "neue deutsche haerte", "nwoahm"]
ADJ["nu metal"] = ["grunge", "rap metal", "alternative metal", "nwoahm"]
ADJ["neue deutsche haerte"] = ["groove metal", "industrial metal"]
ADJ["alternative metal"] = ["nu metal"]
ADJ["post rock"] = ["post metal"]
ADJ["post metal"] = ["post rock", "heavy metal"]
ADJ["nwoahm"] = ["nu metal", "groove metal", "original hardcore punk"]
ADJ["us power metal"] = ["speed metal"]
ADJ["melodic power metal"] = ["speed metal", "symphonic metal"]
ADJ["symphonic metal"] = ["melodic power metal", "goth metal", "death metal"]  # death metal
ADJ["stoner metal"] = ["traditional doom metal"]
ADJ["death/doom"] = ["traditional doom metal", "death metal", "funeral doom"]  # death metal
ADJ["funeral doom"] = ["death/doom", "dark ambient"]
ADJ["drone metal"] = ["traditional doom metal", "dark ambient"]
ADJ["folk metal"] = ["heavy metal", "oriental metal", "celtic metal", "medieval metal"]
ADJ["oriental metal"] = ["folk metal"]
ADJ["celtic metal"] = ["folk metal"]
ADJ["medieval metal"] = ["folk metal"]
ADJ["dark ambient"] = ["black ambient", "drone metal", "funeral doom"]
ADJ["original hardcore punk"] = ["punk rock", "thrash metal", "crust punk", "fwobm", "nwoahm", "grunge", "metalcore"]
ADJ["crust punk"] = ["original hardcore punk", "grindcore", "blackened crust"]
ADJ["thrash metal"] = ["speed metal", "original hardcore punk", "industrial metal", "crossover thrash", "deaththrash",
                       "south american death metal", "death metal", "groove metal"]
ADJ["industrial metal"] = ["thrash metal", "neue deutsche haerte"]
ADJ["crossover thrash"] = ["thrash metal", "metalcore"]
ADJ["deaththrash"] = ["thrash metal", "death metal"]
ADJ["metalcore"] = ["crossover thrash", "mathcore", "deathcore", "original hardcore punk"]
ADJ["mathcore"] = ["metalcore", "grindcore"]
ADJ["fwobm"] = ["original hardcore punk", "viking metal", "swobm", "black ambient", "us black metal",
                "canadian black metal", "greek black metal", "symphonic black metal", "black/death", "death metal"]
ADJ["viking metal"] = ["fwobm"]
ADJ["black ambient"] = ["dark ambient", "fwobm"]
ADJ["symphonic black metal"] = ["fwobm"]
ADJ["black/death"] = ["death metal", "fwobm"]
ADJ["us black metal"] = ["fwobm", "swobm"]
ADJ["canadian black metal"] = ["fwobm", "swobm"]
ADJ["greek black metal"] = ["fwobm", "swobm"]
ADJ["grindcore"] = ["mathcore", "crust punk", "deathgrind"]
ADJ["deathgrind"] = ["grindcore", "death metal"]
ADJ["brutal death"] = ["death metal"]
ADJ["death metal"] = ["symphonic metal", "death/doom", "heavy metal", "thrash metal", "fwobm", "deathgrind",
                      "black/death", "tech death", "brutal death", "deathcore", "death n roll", "swedish death metal",
                      "south american death metal"]
ADJ["south american death metal"] = ["thrash metal", "death metal"]
ADJ["death n roll"] = ["death metal"]
ADJ["deathcore"] = ["metalcore", "death metal"]
ADJ["swedish death metal"] = ["death metal", "melodic death"]
ADJ["melodic death"] = ["swedish death metal", "trance metal"]
ADJ["trance metal"] = ["melodic death"]
ADJ["tech death"] = ["death metal", "djent"]
ADJ["djent"] = ["tech death"]
ADJ["blackened crust"] = ["crust punk", "swobm"]
ADJ["swobm"] = ["depressive black metal", "blackened crust", "unblack metal", "us black metal", "canadian black metal",
                "greek black metal"]
ADJ["unblack metal"] = ["swobm"]
ADJ["depressive black metal"] = ["swobm"]
ADJ["avant-garde metal"] = []


# DISTANCE = {}
# DISTANCE['Brest'] = {'Rennes':244}
# DISTANCE['Rennes'] = {'Caen':176,'Paris':348,'Brest':244,'Nantes':107}
# DISTANCE['Caen'] = {'Calais':120,'Paris':241,'Rennes':176}
# DISTANCE['Calais'] = {'Nancy':534,'Paris':297,'Caen':120}
# DISTANCE['Nancy'] = {'Strasbourg':145,'Dijon':201,'Paris':372,'Calais':534}
# DISTANCE['Strasbourg'] = {'Dijon':335,'Nancy':145}
# DISTANCE['Dijon'] = {'Strasbourg':335,'Lyon':192,'Paris':313,'Nancy':201}
# DISTANCE['Lyon'] = {'Grenoble':104,'Avignon':216,'Limoges':389,'Dijon':192}
# DISTANCE['Grenoble'] = {'Avignon':227,'Lyon':104}
# DISTANCE['Avignon'] = {'Grenoble':227,'Marseille':99,'Montpellier':212,'Lyon':216}
# DISTANCE['Marseille'] = {'Nice':188,'Avignon':99}
# DISTANCE['Nice'] = {'Marseille':188}
# DISTANCE['Montpellier'] = {'Avignon':212,'Toulouse':240}
# DISTANCE['Toulouse'] = {'Montpellier':240,'Bordeaux':253,'Limoges':313}
# DISTANCE['Bordeaux'] = {'Limoges':220,'Toulouse':253,'Nantes':329}
# DISTANCE['Limoges'] = {'Lyon':389,'Toulouse':313,'Bordeaux':220,'Nantes':329,'Paris':396}
# DISTANCE['Nantes'] = {'Limoges':329,'Bordeaux':329,'Rennes':107}
# DISTANCE['Paris'] = {'Calais':297,'Nancy':372,'Dijon':313,'Limoges':396,'Rennes':348,'Caen':241}
